# Setup con Docker — Método Oficial

> Este es el método **recomendado y oficial** del bootcamp.
> Garantiza un entorno idéntico para todos los estudiantes, independientemente del sistema operativo.

---

## Requisitos Previos

| Herramienta | Versión mínima | Instalación |
|-------------|---------------|-------------|
| Docker Engine / Docker Desktop | 27+ | [docs.docker.com/get-docker](https://docs.docker.com/get-docker/) |
| Docker Compose | 2.x (plugin v2) | Incluido en Docker Desktop; en Linux: `apt install docker-compose-plugin` |
| Git | 2.x | [git-scm.com](https://git-scm.com/) |
| VS Code | Reciente | [code.visualstudio.com](https://code.visualstudio.com/) (opcional pero recomendado) |

### Verificar instalación

```bash
docker --version
# Docker version 27.x.x, build ...

docker compose version
# Docker Compose version v2.x.x

git --version
# git version 2.x.x
```

---

## Clonar el Repositorio

```bash
git clone https://github.com/ergrato-dev/bc-mcp.git
cd bc-mcp
```

---

## Estructura de un Proyecto Semanal con Docker

Cada semana tiene su propio `docker-compose.yml` (a partir de la semana 04).
La estructura estándar es:

```
bootcamp/week-XX-tema/3-proyecto/starter/
├── docker-compose.yml    # Orquesta los servicios del proyecto
├── Dockerfile.python     # Imagen del MCP Server Python (semanas 04–12)
├── Dockerfile.node       # Imagen del MCP Server TypeScript (semanas 05–12)
├── .env.example          # Variables de entorno requeridas (template)
├── .env                  # Tu configuración local (en .gitignore)
├── python-server/        # Código fuente Python
│   ├── pyproject.toml
│   └── src/
│       └── server.py
└── ts-server/            # Código fuente TypeScript
    ├── package.json
    └── src/
        └── index.ts
```

---

## Flujo de Trabajo Semanal

### 1. Navegar a la semana

```bash
cd bootcamp/week-04-primer_server_python/3-proyecto/starter
```

### 2. Copiar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus API keys si la semana las requiere
```

### 3. Levantar el entorno

```bash
# Construir imágenes y levantar todos los servicios
docker compose up --build

# O en background
docker compose up --build -d
```

### 4. Ver logs

```bash
# Todos los servicios
docker compose logs -f

# Solo un servicio específico
docker compose logs -f python-server
docker compose logs -f ts-server
```

### 5. Ejecutar comandos dentro del contenedor

```bash
# Acceder a la shell del server Python
docker compose exec python-server bash

# Ejecutar un script Python puntual
docker compose exec python-server uv run python scripts/test_client.py

# Acceder a la shell del server TypeScript
docker compose exec ts-server sh

# Ejecutar tests Python
docker compose exec python-server uv run pytest tests/ -v

# Ejecutar tests TypeScript
docker compose exec ts-server pnpm test
```

### 6. Detener el entorno

```bash
# Detener sin borrar datos
docker compose down

# Detener y borrar volúmenes (BD, caché, etc.)
docker compose down -v
```

---

## Ejemplo: `docker-compose.yml` Estándar

```yaml
# docker-compose.yml — template estándar del bootcamp
services:
  python-server:
    build:
      context: ./python-server
      dockerfile: ../Dockerfile.python
    env_file: .env
    stdin_open: true
    tty: true
    volumes:
      - ./python-server:/app

  ts-server:
    build:
      context: ./ts-server
      dockerfile: ../Dockerfile.node
    env_file: .env
    stdin_open: true
    tty: true
    volumes:
      - ./ts-server:/app
```

---

## Ejemplo: `Dockerfile.python` Estándar

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

RUN pip install --no-cache-dir uv==0.6.14

WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen

COPY . .

CMD ["uv", "run", "python", "src/server.py"]
```

---

## Ejemplo: `Dockerfile.node` Estándar

```dockerfile
FROM node:22-slim

RUN corepack enable && corepack prepare pnpm@9.15.4 --activate

WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

CMD ["node", "dist/index.js"]
```

---

## Solución de Problemas Frecuentes

### `docker compose` no reconocido (Linux)

```bash
# Instalar el plugin de Compose v2
sudo apt-get install docker-compose-plugin

# Verificar
docker compose version
```

### Puerto ya en uso

```bash
# Ver qué proceso usa el puerto 3000
sudo lsof -i :3000

# Cambiar el puerto en docker-compose.yml o detener el proceso
```

### Permisos denegados en Linux (Docker sin sudo)

```bash
# Agregar tu usuario al grupo docker
sudo usermod -aG docker $USER

# Cerrar sesión y volver a entrar, luego verificar
docker ps
```

### Imagen no se actualiza con mis cambios

```bash
# Forzar rebuild sin caché
docker compose build --no-cache
docker compose up
```

### Volumen con datos corruptos

```bash
# Borrar todo y empezar de cero
docker compose down -v
docker compose up --build
```

---

[← Índice de setup](README.md) · [Setup local →](local.md)
