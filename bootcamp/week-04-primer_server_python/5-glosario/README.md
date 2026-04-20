# Glosario — Semana 04: Primer MCP Server en Python

Términos clave de esta semana, ordenados alfabéticamente.

---

### @asynccontextmanager

Decorador de `contextlib` que convierte una función generadora asíncrona en un context manager.
Se usa para implementar el patrón `lifespan` en FastMCP. Requiere exactamente un `yield`.

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(server):
    db = await connect()    # startup
    yield {"db": db}        # disponible en tools
    await db.close()        # shutdown
```

---

### @mcp.tool()

Decorador de FastMCP que registra una función Python asíncrona como un Tool MCP.
Genera automáticamente el JSON Schema del input a partir de los type hints de la función
y extrae la descripción del tool desde el docstring.

```python
@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b
```

---

### asyncio

Librería estándar de Python para programación asíncrona con el patrón `async/await`.
FastMCP usa asyncio internamente; no necesitas llamar a `asyncio.run()` directamente —
`mcp.run()` lo maneja.

---

### Context

Objeto especial de FastMCP que se puede declarar como parámetro `ctx: Context` en cualquier tool.
No forma parte del JSON Schema del tool (FastMCP lo inyecta automáticamente). Proporciona:
- `await ctx.info(msg)` / `ctx.debug()` / `ctx.warning()` — enviar logs al cliente LLM
- `ctx.request_context.lifespan_context` — acceder al dict del lifespan

---

### docstring

Cadena de texto al inicio de una función Python que describe su propósito.
FastMCP extrae el docstring para usarlo como `description` del tool en el JSON Schema.
La sección `Args:` describe cada parámetro y también aparece en el schema.

---

### FastMCP

Clase principal del SDK de Python para MCP. API de alto nivel que abstrae el protocolo JSON-RPC,
la generación de schemas y el transport loop. Se instancia con `mcp = FastMCP("name")`.

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("my-server")
```

---

### JSON Schema

Estándar JSON para describir la estructura de datos JSON. MCP lo usa para especificar los inputs
de los tools: nombres de parámetros, tipos, descripciones y cuáles son requeridos.
FastMCP genera el JSON Schema automáticamente a partir de los type hints de Python.

---

### lifespan

Patrón de FastMCP para inicializar y limpiar recursos al arranque y apagado del servidor.
Se implementa como una función `async` decorada con `@asynccontextmanager`.
El dict que se pasa con `yield` queda disponible en todos los tools vía `ctx.request_context.lifespan_context`.

---

### MCP Inspector

Herramienta web oficial para probar MCP Servers de forma interactiva.
Permite explorar tools disponibles, ejecutar tools con parámetros, ver notificaciones y
el historial de requests JSON-RPC. Se ejecuta con `npx @modelcontextprotocol/inspector`.

---

### mcp.run()

Método de FastMCP que inicia el servidor MCP con transport stdio.
Lee mensajes JSON-RPC de `stdin`, los procesa y escribe respuestas a `stdout`.
Ejecuta hasta que `stdin` se cierra.

```python
if __name__ == "__main__":
    mcp.run()   # Inicia el loop stdio
```

---

### Optional / str | None

Forma de indicar que un parámetro puede ser `None` (omitido).
- `Optional[str]` — estilo antiguo (typing)
- `str | None` — estilo moderno (Python 3.10+, preferido en este bootcamp)

El parámetro no aparece en `required` del JSON Schema.

---

### pyproject.toml

Archivo estándar de configuración para proyectos Python (PEP 621).
Define el nombre, versión, versión de Python requerida, dependencias y sistema de build.
En este bootcamp se usa con `hatchling` como build backend y `uv` como gestor de dependencias.

---

### StdioServerTransport

Transport del protocolo MCP que usa `stdin`/`stdout` para comunicación.
Es el transport por defecto en FastMCP (`mcp.run()`). El servidor lee de `stdin` y escribe a `stdout`.
Los logs del desarrollador deben ir a `stderr` para no contaminar el canal del protocolo.

---

### type hint

Anotación de tipo en Python que indica el tipo esperado de una variable, parámetro o valor de retorno.
FastMCP usa los type hints para generar automáticamente el JSON Schema de los tools.

```python
def greet(name: str, times: int = 1) -> str:  # ← type hints
    return name * times
```

---

### uv

Gestor de paquetes y entornos virtuales de Python moderno (Astral). Reemplaza a `pip` y `venv`.
En este bootcamp se usa exclusivamente `uv`. Comandos clave:
- `uv add pkg==1.0.0` — agregar dependencia con versión exacta
- `uv sync --frozen` — instalar exactamente lo del lockfile
- `uv run python src/server.py` — ejecutar en el entorno virtual

---

### uv.lock

Archivo generado automáticamente por `uv` que registra las versiones exactas de todas las
dependencias (directas y transitivas) junto con sus hashes de integridad. Garantiza builds
reproducibles. Se debe commitear al repositorio. Nunca se edita a mano.

Archivo de configuración estándar de proyectos Python moderno

### stdio transport

Transport MCP que comunica client y server por stdin/stdout del proceso

### type hint

Anotación de tipo en Python que FastMCP usa para generar el JSON Schema del tool

### uv

Gestor de paquetes y entornos Python ultrarrápido (reemplaza pip/venv)

### uv run

Comando para ejecutar scripts Python en el entorno virtual gestionado por uv

### uv sync

Comando de uv para instalar dependencias exactas del pyproject.toml

---

[← Volver al README de la semana](../README.md)
