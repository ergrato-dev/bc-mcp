---
applyTo: "**/*.py"
---

# Convenciones Python para bc-mcp

## Versión y sintaxis

- Python 3.13+ obligatorio
- Type hints en todas las funciones y métodos
- `async/await` para todas las operaciones I/O
- Unions con `|` en lugar de `Union[]`
- Genéricos nativos: `list[str]`, `dict[str, int]` (no `List`, `Dict`)

## MCP SDK (`mcp`)

- Usar `FastMCP` para servidores sencillos; `Server` de bajo nivel solo cuando se requiera control explícito del protocolo
- Decoradores: `@mcp.tool()`, `@mcp.resource()`, `@mcp.prompt()`
- Nombres de tools y resources: `snake_case` (ej. `search_files`, `get_weather`)
- URIs de resources: estilo `scheme://path` (ej. `db://users`, `file://docs/readme`)
- Docstrings en inglés para tools y resources — el LLM los usa para entender qué hace cada primitivo

```python
# ✅ CORRECTO
@mcp.tool()
async def search_files(pattern: str, directory: str = ".") -> list[str]:
    """Search files matching the given glob pattern."""
    return [str(p) for p in Path(directory).rglob(pattern)]

# ❌ INCORRECTO — sin type hints, sin async, sin docstring
@mcp.tool()
def search_files(pattern, directory="."):
    return [str(p) for p in Path(directory).rglob(pattern)]
```

## Validación de inputs

- Usar Pydantic `BaseModel` para estructuras de datos complejas
- Validar y sanitizar parámetros antes de usarlos en queries SQL o comandos del sistema
- Nunca interpolar directamente strings de usuario en queries SQL

```python
# ✅ CORRECTO — query parametrizada
rows = await db.fetch_all(
    "SELECT * FROM items WHERE name ILIKE :q LIMIT :limit",
    {"q": f"%{query}%", "limit": limit},
)

# ❌ INCORRECTO — inyección SQL
rows = await db.fetch_all(f"SELECT * FROM items WHERE name LIKE '%{query}%'")
```

## Gestión de paquetes

- Usar `uv` exclusivamente (nunca `pip` directamente en producción)
- Versiones **siempre exactas** en `pyproject.toml`, sin `^`, `~`, `>=` ni `*`

```toml
# ✅ CORRECTO
[project]
dependencies = [
    "mcp==1.6.0",
    "httpx==0.28.1",
    "pydantic==2.11.3",
]

# ❌ INCORRECTO
dependencies = [
    "mcp>=1.0",
    "httpx^0.28",
]
```

## Estructura de server

```python
# server.py — punto de entrada estándar
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("nombre-del-server")

# Importar tools, resources y prompts desde sus módulos
from tools.search import search_files        # noqa: E402, F401
from resources.database import db_schema     # noqa: E402, F401
from prompts.templates import analyze_code   # noqa: E402, F401

if __name__ == "__main__":
    mcp.run()
```

## Testing

- Framework: `pytest` + `pytest-asyncio`
- Usar `mcp.shared.memory.create_connected_server_and_client_session` para tests de integración
- Un archivo de test por módulo: `tests/test_tools.py`, `tests/test_resources.py`

```python
@pytest.mark.asyncio
async def test_search_files_tool():
    async with create_connected_server_and_client_session(server) as (_, client):
        result = await client.call_tool("search_files", {"pattern": "*.py"})
        assert isinstance(result.content[0].text, str)
```
