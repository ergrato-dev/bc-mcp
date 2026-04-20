# Práctica 02 — Agentic Loop Completo con Claude

## 🎯 Objetivo

Implementar el bucle `while` completo: Claude llama tools, recibe resultados y genera
una respuesta final cuando `stop_reason == "end_turn"`. Verás el historial de mensajes
crecer en cada iteración.

---

## Requisitos previos

- Completada la Práctica 01
- Library Server (semana 07) disponible

## Configuración inicial

```bash
uv sync
cp .env.example .env
# Edita .env con tu ANTHROPIC_API_KEY
```

---

## Paso 1 — Imports y configuración

Descomenta **PASO 1** en `starter/src/agent.py`:

```python
# import os, asyncio, json
# from dotenv import load_dotenv
# from anthropic import Anthropic
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
# ...
# load_dotenv()
# client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
```

---

## Paso 2 — Conectar al server y convertir tools

Descomenta **PASO 2**: conexión al Library Server y conversión a formato Anthropic.

Verifica que la lista de tools se imprime correctamente.

---

## Paso 3 — Despachador de tool calls

Descomenta **PASO 3**: la función `dispatch_tool_calls` que ejecuta cada `tool_use` block
vía MCP y construye los bloques `tool_result`.

```python
# async def dispatch_tool_calls(response, session) -> list[dict]:
#     ...
#     for block in response.content:
#         if block.type == "tool_use":
#             result = await session.call_tool(block.name, block.input)
#             tool_results.append({
#                 "type": "tool_result",
#                 "tool_use_id": block.id,
#                 "content": result.content[0].text if result.content else "",
#             })
#     return tool_results
```

---

## Paso 4 — El agentic loop

Descomenta **PASO 4**: el bucle `while` con condición de salida y acumulación de mensajes:

```python
# while iteration < MAX_ITERATIONS:
#     response = client.messages.create(...)
#
#     if response.stop_reason == "end_turn":
#         return final_text
#
#     if response.stop_reason == "tool_use":
#         tool_results = await dispatch_tool_calls(response, session)
#         messages.append({"role": "assistant", "content": response.content})
#         messages.append({"role": "user", "content": tool_results})
```

---

## Paso 5 — Observar el historial

Descomenta **PASO 5**: logging del historial para ver cómo crece en cada iteración.

```python
# print(f"[Iteración {iteration}] mensajes en historial: {len(messages)}")
```

---

## ✅ Verificación final

Con el prompt `"Busca libros de Python, añade uno nuevo llamado 'MCP en Python' y confirma que quedó guardado"`, la salida debería mostrar:

```
Iteración 1 — stop_reason: tool_use (search_books)
Iteración 2 — stop_reason: tool_use (add_book)
Iteración 3 — stop_reason: tool_use (search_books)
Iteración 4 — stop_reason: end_turn

Respuesta final: He encontrado los libros de Python...
Historial final: 9 mensajes
```

---

## 🧩 Reto extra

Añade un contador que muestre cuántas tools se llamaron en total durante el loop.
