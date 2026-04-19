---
description: "Genera un MCP Server completo y funcional en Python o TypeScript con la estructura de carpetas estándar del bootcamp."
mode: "agent"
---

Crea un MCP Server completo siguiendo las convenciones del bootcamp bc-mcp.

## Información necesaria

Si no se especificó en la solicitud, pregunta:

1. **Lenguaje**: Python o TypeScript
2. **Nombre del server** en `kebab-case` (ej. `weather-server`, `file-search-server`)
3. **Propósito**: descripción breve de qué hace el server
4. **Primitivos a incluir**: Tools / Resources / Prompts (puede ser cualquier combinación)
5. **Integración**: ¿DB SQLite, API externa, file system?
6. **Transport**: `stdio` (default) o `http+SSE`
7. **¿Incluir Docker?**: sí/no

## Python — estructura a generar

```
{server-name}/
├── pyproject.toml
├── uv.lock              # vacío/placeholder — el estudiante ejecuta uv sync
├── README.md
├── .env.example
├── src/
│   ├── server.py        # punto de entrada con FastMCP
│   ├── config.py        # variables de entorno con pydantic-settings
│   ├── tools/
│   │   ├── __init__.py
│   │   └── {tool_name}.py
│   ├── resources/       # si se pidió
│   │   ├── __init__.py
│   │   └── {resource_name}.py
│   ├── prompts/         # si se pidió
│   │   ├── __init__.py
│   │   └── {prompt_name}.py
│   └── utils/
│       ├── __init__.py
│       └── db.py        # solo si usa DB
└── tests/
    ├── conftest.py
    └── test_tools.py
```

### server.py base (Python)

```python
"""MCP Server: {server-name}"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{server-name}")

# Register tools
from tools.{tool_name} import {tool_name}  # noqa: E402, F401

if __name__ == "__main__":
    mcp.run()
```

### pyproject.toml (Python)

```toml
[project]
name = "{server-name}"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "mcp==1.6.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## TypeScript — estructura a generar

```
{server-name}/
├── package.json
├── pnpm-lock.yaml       # vacío/placeholder — el estudiante ejecuta pnpm install
├── tsconfig.json
├── README.md
├── .env.example
├── src/
│   ├── index.ts         # punto de entrada
│   ├── config.ts        # variables de entorno
│   ├── tools/
│   │   └── {toolName}.ts
│   ├── resources/       # si se pidió
│   │   └── {resourceName}.ts
│   └── prompts/         # si se pidió
│       └── {promptName}.ts
└── tests/
    └── tools.test.ts
```

### package.json (TypeScript)

```json
{
  "name": "{server-name}",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsx src/index.ts",
    "test": "vitest"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "1.10.2",
    "zod": "3.24.2"
  },
  "devDependencies": {
    "typescript": "5.8.3",
    "tsx": "4.19.3",
    "vitest": "3.1.2",
    "@types/node": "22.14.1"
  }
}
```

## Reglas de generación

- Todos los tools deben tener docstrings/JSDoc descriptivos (el LLM los usa)
- Validar todos los inputs con Pydantic (Python) o Zod (TypeScript)
- Queries SQL siempre parametrizadas
- Variables sensibles en `.env`, nunca hardcodeadas
- El `README.md` del server debe incluir: descripción, instalación, uso, lista de tools/resources/prompts disponibles

## Si se pide Docker

Generar adicionalmente:

- `Dockerfile.python` o `Dockerfile.node` según el lenguaje
- `docker-compose.yml` si incluye DB u otros servicios
- `.env.example` completo con todas las variables

## Validación final

Verificar que:

1. El server arranca sin errores (`uv run python src/server.py` o `pnpm start`)
2. Los tools tienen schemas Zod/Pydantic completos
3. No hay secrets hardcodeados
4. El README documenta todos los primitivos disponibles
