# Práctica 04 — Multi-Server: Orquestación de N servidores

## 🎯 Objetivo

Conectar un agente Claude a **dos MCP servers simultáneamente**: el Library Server
(semana 07) y un Calculator Server local. Implementar el registro unificado de tools
y el routing basado en el mapa `tool_name → session`.

---

## Requisitos previos

- Completadas Prácticas 01, 02 y 03
- API key de Anthropic en `.env`

## Configuración inicial

```bash
uv sync
cp .env.example .env
# Edita .env con tu ANTHROPIC_API_KEY
```

---

## Paso 1 — Imports y dos configuraciones de server

Descomenta **PASO 1** en `starter/src/multi_agent.py`. Verás dos configuraciones:
una para el Library Server y otra para el Calculator Server incluido en `starter/servers/`.

---

## Paso 2 — Conectar a múltiples servers con AsyncExitStack

Descomenta **PASO 2**: la función que conecta a ambos servers en secuencia y
construye los dos registros (`all_tools` y `tool_to_session`):

```python
# for config in SERVER_CONFIGS:
#     params = StdioServerParameters(...)
#     transport = await stack.enter_async_context(stdio_client(params))
#     session = await stack.enter_async_context(ClientSession(*transport))
#     await session.initialize()
#     result = await session.list_tools()
#     for tool in result.tools:
#         all_tools.append(tool)
#         tool_to_session[tool.name] = session
```

---

## Paso 3 — Dispatch con routing

Descomenta **PASO 3**: la función de routing que identifica a qué session pertenece
cada tool y despacha la llamada:

```python
# session = tool_to_session.get(tool_name)
# if session is None:
#     return f"Error: tool '{tool_name}' no encontrada"
# result = await session.call_tool(tool_name, tool_input)
```

---

## Paso 4 — Loop unificado

Descomenta **PASO 4**: el agentic loop que usa las tools de ambos servers juntas.
Claude elige libremente entre herramientas de gestión de libros y herramientas matemáticas.

---

## Paso 5 — Prompt multi-dominio

Descomenta **PASO 5** y ejecuta con el prompt:

> "Busca cuántos libros de Python hay en la base de datos, multiplica ese número por 3 y añade un libro nuevo con precio igual al resultado."

Verás cómo Claude usa tools de **ambos servers** en secuencia.

---

## ✅ Verificación final

La salida debería mostrar:

```
Tools registradas: search_books, add_book, get_book, ... (Library)
                   add, subtract, multiply, divide (Calculator)

Iteración 1 → search_books (Library Server)
Iteración 2 → multiply (Calculator Server)
Iteración 3 → add_book (Library Server)
Iteración 4 → end_turn

Respuesta final: Encontré N libros de Python. N × 3 = M. Añadí el libro 'X' con precio M.
```

---

## 🧩 Reto extra

Añade un tercer server (puedes copiar y modificar el Calculator Server) y conéctalo
al mismo agente. Verifica que el routing sigue funcionando con tres servers.
