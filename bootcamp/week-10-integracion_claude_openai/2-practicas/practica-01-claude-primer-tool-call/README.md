# Práctica 01 — Claude: Primer Tool Call

## 🎯 Objetivo

Conectar un cliente Python al Library Server (semana 07), hacer una sola llamada
a la API de Anthropic con tools disponibles y detectar el bloque `tool_use` en la respuesta.

---

## Requisitos previos

- Library Server (semana 07) corriendo o disponible como script
- API key de Anthropic en `.env`
- Python 3.13+ con `uv`

## Configuración inicial

```bash
# Desde esta carpeta
uv sync
cp .env.example .env
# Edita .env y añade tu ANTHROPIC_API_KEY
```

---

## Paso 1 — Inicializar el cliente Anthropic

Abre `starter/src/client.py`. Esta práctica tiene código comentado que irás descomentando
paso a paso.

Descomenta la sección **PASO 1** en el archivo:

```python
# import os
# from dotenv import load_dotenv
# from anthropic import Anthropic
#
# load_dotenv()
# ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
# client = Anthropic(api_key=ANTHROPIC_API_KEY)
# print("✓ Cliente Anthropic inicializado")
```

Ejecuta:

```bash
uv run python src/client.py
```

Deberías ver: `✓ Cliente Anthropic inicializado`

---

## Paso 2 — Conectar al MCP Server y listar tools

Descomenta la sección **PASO 2**. Verás cómo conectar via `stdio_client` y llamar a `list_tools()`:

```python
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
#
# SERVER_SCRIPT = os.getenv("SERVER_SCRIPT", "../../../week-07-...")
#
# async def list_server_tools() -> None:
#     params = StdioServerParameters(command="python", args=[SERVER_SCRIPT])
#     async with stdio_client(params) as (stdio, write):
#         async with ClientSession(stdio, write) as session:
#             await session.initialize()
#             result = await session.list_tools()
#             for tool in result.tools:
#                 print(f"  - {tool.name}: {tool.description}")
```

Ejecuta y verifica que aparezcan las tools del Library Server.

---

## Paso 3 — Convertir tools al formato Anthropic

Descomenta la sección **PASO 3** para ver la conversión `inputSchema` → `input_schema`:

```python
# def convert_tools_for_anthropic(tools) -> list[dict]:
#     return [
#         {
#             "name": t.name,
#             "description": t.description or "",
#             "input_schema": t.inputSchema,   # clave crítica: input_schema
#         }
#         for t in tools
#     ]
```

---

## Paso 4 — Hacer la primera llamada con tools

Descomenta **PASO 4**. Esta es la llamada principal a la API:

```python
# response = client.messages.create(
#     model=MODEL,
#     max_tokens=1024,
#     tools=anthropic_tools,
#     messages=[{"role": "user", "content": USER_PROMPT}],
# )
# print(f"stop_reason: {response.stop_reason}")
# print(f"blocks recibidos: {len(response.content)}")
```

---

## Paso 5 — Inspeccionar el bloque tool_use

Descomenta **PASO 5** para extraer los datos del `ToolUseBlock`:

```python
# for block in response.content:
#     if block.type == "tool_use":
#         print(f"  tool: {block.name}")
#         print(f"  id:   {block.id}")
#         print(f"  args: {block.input}")
```

---

## ✅ Verificación final

Al ejecutar `uv run python src/client.py`, la salida debe mostrar:

```
✓ Cliente Anthropic inicializado
Tools disponibles: search_books, add_book, get_book, update_book, delete_book, enrich_book, search_openlibrary
stop_reason: tool_use
  tool: search_books
  id:   toolu_01...
  args: {'query': '...'}
```

---

## 🧩 Reto extra

Modifica `USER_PROMPT` para que Claude pida un libro específico y observa qué tool y qué argumentos elige el modelo.
