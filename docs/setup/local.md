# Setup Local — Sin Docker

> ⚠️ **Este método no es el oficial del bootcamp.**
> Úsalo solo si no puedes instalar Docker en tu equipo.
> Los comandos y rutas asumen Linux/macOS. En Windows se recomienda WSL2.

---

## Requisitos Previos

### Para semanas Python (01–04, 06–08, 10–12)

| Herramienta | Versión | Instalación |
|-------------|---------|-------------|
| Python | **3.13+** | [python.org](https://www.python.org/downloads/) o `pyenv` |
| uv | **0.6+** | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Git | 2.x | [git-scm.com](https://git-scm.com/) |

### Para semanas TypeScript (05–07, 09–12)

| Herramienta | Versión | Instalación |
|-------------|---------|-------------|
| Node.js | **22+** | [nodejs.org](https://nodejs.org/) o `nvm` |
| pnpm | **9+** | `corepack enable && corepack prepare pnpm@9.15.4 --activate` |
| Git | 2.x | [git-scm.com](https://git-scm.com/) |

---

## Verificar Instalación

```bash
# Python
python3 --version        # Python 3.13.x
uv --version             # uv 0.6.x

# Node.js / TypeScript
node --version           # v22.x.x
pnpm --version           # 9.x.x
```

---

## Clonar el Repositorio

```bash
git clone https://github.com/ergrato-dev/bc-mcp.git
cd bc-mcp
```

---

## Setup para Proyectos Python

### 1. Navegar al proyecto

```bash
cd bootcamp/week-04-primer_server_python/3-proyecto/starter/python-server
```

### 2. Crear entorno virtual con uv

```bash
# uv crea automáticamente el .venv en el directorio
uv sync
```

### 3. Activar el entorno virtual (opcional con uv)

```bash
# Con uv run no necesitas activar manualmente
# Pero si prefieres activar:
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
```

### 4. Copiar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus valores
```

### 5. Ejecutar el servidor MCP

```bash
# Con uv run (recomendado — no requiere activar .venv)
uv run python src/server.py

# O con el entorno activado
python src/server.py
```

### 6. Ejecutar tests

```bash
uv run pytest tests/ -v
```

### 7. Agregar dependencias

```bash
# Siempre con versión exacta
uv add mcp==1.6.0
uv add httpx==0.28.1
```

---

## Setup para Proyectos TypeScript

### 1. Navegar al proyecto

```bash
cd bootcamp/week-05-primer_server_typescript/3-proyecto/starter/ts-server
```

### 2. Instalar dependencias

```bash
pnpm install --frozen-lockfile
```

### 3. Copiar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus valores
```

### 4. Compilar TypeScript

```bash
pnpm build
```

### 5. Ejecutar el servidor MCP

```bash
# Ejecutar el build compilado
node dist/index.js

# O en modo desarrollo (con tsx, si está configurado)
pnpm dev
```

### 6. Ejecutar tests

```bash
pnpm test
```

### 7. Agregar dependencias

```bash
# Siempre con versión exacta
pnpm add @modelcontextprotocol/sdk@1.10.2
pnpm add zod@3.24.2
```

---

## Bases de Datos Locales (Semanas 07+)

Si el proyecto usa SQLite:

```bash
# SQLite viene incluido con Python 3.x
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"

# En Node.js, se usa better-sqlite3 o similar (incluido en package.json)
```

Si el proyecto usa PostgreSQL:

```bash
# Instalar PostgreSQL localmente
sudo apt install postgresql          # Ubuntu/Debian
brew install postgresql@17           # macOS

# O usar solo Docker para la BD (híbrido recomendado)
docker run -d \
  --name bc-mcp-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 \
  postgres:17-alpine
```

---

## Configurar MCP Inspector sin Docker

```bash
# Instalar MCP Inspector globalmente con pnpm
pnpm add -g @modelcontextprotocol/inspector@0.9.0

# Ejecutar Inspector apuntando a tu server Python
npx @modelcontextprotocol/inspector uv run python src/server.py

# Apuntando a tu server TypeScript compilado
npx @modelcontextprotocol/inspector node dist/index.js
```

Abrir el navegador en `http://localhost:5173`

---

## Variables de Entorno

```bash
# Crear .env desde el template
cp .env.example .env

# Editar con tu editor
code .env
nano .env
```

Nunca commitees el archivo `.env` — está en `.gitignore`.

---

## Solución de Problemas Frecuentes

### Python no encontrado o versión incorrecta

```bash
# Ver todas las versiones disponibles con pyenv
pyenv versions

# Instalar Python 3.13
pyenv install 3.13.3
pyenv local 3.13.3

# Verificar
python3 --version
```

### `uv: command not found`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env   # o reiniciar la terminal
```

### `pnpm: command not found`

```bash
# Activar corepack (incluido con Node.js 22)
corepack enable
corepack prepare pnpm@9.15.4 --activate
```

### Error de versión de Node.js

```bash
# Instalar nvm y cambiar versión
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install 22
nvm use 22
node --version  # v22.x.x
```

### `ModuleNotFoundError` al ejecutar server Python

```bash
# Asegurarse de ejecutar con uv run (usa el .venv correcto)
uv run python src/server.py

# O verificar que el .venv esté activado
which python   # debe apuntar a .venv/bin/python
```

### Puerto 5173 ocupado (MCP Inspector)

```bash
# Cambiar el puerto del inspector
npx @modelcontextprotocol/inspector --port 5174 uv run python src/server.py
```

---

## Diferencias Clave vs Docker

| Aspecto | Docker ✅ | Local ⚠️ |
|---------|-----------|---------|
| Reproducibilidad | Idéntica en todos los equipos | Depende de las versiones instaladas |
| Aislamiento | Completo | Puede haber conflictos con otras versiones |
| Setup inicial | 1 comando | Varios pasos manuales |
| Compatibilidad SO | Linux, macOS, Windows | Puede requerir ajustes en Windows |
| Bases de datos | Incluidas en compose | Requieren instalación o contenedor aparte |
| Recomendado | ✅ Sí | Solo como fallback |

---

[← Setup con Docker](docker.md) · [← Índice de setup](README.md)
