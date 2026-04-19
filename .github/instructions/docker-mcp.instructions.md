---
applyTo: "**/Dockerfile*, **/docker-compose*.yml, **/docker-compose*.yaml"
---

# Convenciones Docker para bc-mcp

## Principios generales

- Docker es el entorno de desarrollo oficial — NO instalar Python ni Node.js localmente
- Usar `docker compose` (v2) para orquestar servicios multi-contenedor
- Un `Dockerfile` por lenguaje: `Dockerfile.python` y `Dockerfile.node`
- Archivos `.env` para variables de entorno; nunca hardcodear secrets en Dockerfiles

## Dockerfile Python (uv)

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

RUN pip install --no-cache-dir uv==0.6.14

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

COPY . .

CMD ["uv", "run", "python", "src/server.py"]
```

- Usar `uv sync --frozen` para reproducibilidad exacta
- Separar `COPY pyproject.toml uv.lock*` del `COPY . .` para aprovechar el cache de capas
- Usar `python:3.13-slim` (no `alpine` — mejor compatibilidad con dependencias compiladas)

## Dockerfile Node.js (pnpm)

```dockerfile
FROM node:22-slim

RUN corepack enable && corepack prepare pnpm@10.8.1 --activate

WORKDIR /app

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile --prod

COPY . .
RUN pnpm build

CMD ["node", "dist/index.js"]
```

- Usar `pnpm install --frozen-lockfile` para reproducibilidad exacta
- Separar `COPY package.json pnpm-lock.yaml` del `COPY . .` para cache de capas
- `pnpm build` compila TypeScript a `dist/` antes de iniciar el servidor

## docker-compose.yml — estructura estándar

```yaml
services:
  python-server:
    build:
      context: ./python-server
      dockerfile: Dockerfile.python
    env_file: .env
    volumes:
      - ./python-server/src:/app/src # hot-reload en desarrollo
    stdin_open: true
    tty: true

  ts-server:
    build:
      context: ./ts-server
      dockerfile: Dockerfile.node
    env_file: .env
    volumes:
      - ./ts-server/src:/app/src # hot-reload en desarrollo

  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## .env.example — template obligatorio

Cada proyecto debe tener `.env.example` con todas las variables documentadas:

```bash
# Base de datos
POSTGRES_DB=mcp_db
POSTGRES_USER=mcp_user
POSTGRES_PASSWORD=change_me_in_production

# APIs externas (si aplica)
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# MCP Server config
MCP_SERVER_NAME=my-server
MCP_SERVER_VERSION=1.0.0
```

## .gitignore — entradas obligatorias para proyectos Docker

```gitignore
.env
**/solution/
**/__pycache__/
**/*.pyc
**/node_modules/
**/dist/
**/.venv/
```

## Comandos de referencia

```bash
# Construir y levantar todos los servicios
docker compose up --build

# Levantar en background
docker compose up -d

# Ver logs de un servicio específico
docker compose logs -f python-server

# Ejecutar shell en un contenedor
docker compose exec python-server bash
docker compose exec ts-server sh

# Detener y limpiar contenedores
docker compose down

# Limpiar también volúmenes (⚠️ borra datos de BD)
docker compose down -v
```
