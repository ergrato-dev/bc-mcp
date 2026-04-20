# Práctica 03 — OpenAI: Function Calling

## 🎯 Objetivo

Implementar el mismo agentic loop de la Práctica 02 pero usando la API de OpenAI.
Verás las diferencias clave: `finish_reason`, `role: "tool"`, `json.loads(arguments)`.

---

## Requisitos previos

- Completadas Prácticas 01 y 02
- API key de OpenAI en `.env`

## Configuración inicial

```bash
uv sync
cp .env.example .env
# Edita .env con tu OPENAI_API_KEY
```

---

## Paso 1 — Imports y cliente OpenAI

Descomenta **PASO 1** en `starter/src/agent_openai.py`:

```python
# from openai import OpenAI
# client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
```

**Diferencia**: `OpenAI(...)` en lugar de `Anthropic(...)`

---

## Paso 2 — Convertir tools al formato OpenAI

Descomenta **PASO 2**. Nota las diferencias vs Anthropic:

```python
# def convert_tools_for_openai(tools: list) -> list[dict]:
#     return [
#         {
#             "type": "function",       # ← wrapper nuevo
#             "function": {             # ← wrapper nuevo
#                 "name": t.name,
#                 "description": t.description or "",
#                 "parameters": t.inputSchema,   # ← "parameters", no "input_schema"
#             },
#         }
#         for t in tools
#     ]
```

---

## Paso 3 — Detectar finish_reason y extraer tool_calls

Descomenta **PASO 3**. En OpenAI la lógica es diferente:

```python
# choice = response.choices[0]
# if choice.finish_reason == "tool_calls":    # ← "tool_calls", no "tool_use"
#     for tc in choice.message.tool_calls:
#         function_name = tc.function.name
#         arguments = json.loads(tc.function.arguments)   # ← parsear JSON
#         call_id = tc.id
```

---

## Paso 4 — Construir el mensaje tool result

Descomenta **PASO 4**. En OpenAI el resultado usa `role: "tool"`:

```python
# # 1. Añadir el mensaje del assistant al historial
# messages.append({
#     "role": "assistant",
#     "content": choice.message.content,    # puede ser None
#     "tool_calls": [...],
# })
#
# # 2. Resultado con role: "tool" (¡no "user" como en Anthropic!)
# messages.append({
#     "role": "tool",
#     "tool_call_id": tc.id,    # ← "tool_call_id", no "tool_use_id"
#     "content": result_text,
# })
```

---

## Paso 5 — Loop completo

Descomenta **PASO 5**: el while-loop con `finish_reason == "stop"` como condición de salida:

```python
# while iteration < MAX_ITERATIONS:
#     response = client.chat.completions.create(
#         model=MODEL, tools=tools, messages=messages, max_tokens=4096
#     )
#     choice = response.choices[0]
#     if choice.finish_reason == "stop":    # ← "stop", no "end_turn"
#         return choice.message.content or ""
#     ...
```

---

## ✅ Verificación final

Con el mismo prompt que la Práctica 02, la salida debería ser equivalente pero
usando los modelos de OpenAI. Compara las respuestas de Claude vs GPT.

---

## Tabla comparativa rápida

| | Anthropic | OpenAI |
|---|---|---|
| Tool call signal | `stop_reason == "tool_use"` | `finish_reason == "tool_calls"` |
| Final response | `stop_reason == "end_turn"` | `finish_reason == "stop"` |
| Tool result role | `"user"` | `"tool"` |
| Arguments | `block.input` (dict) | `json.loads(tc.function.arguments)` |

---

## 🧩 Reto extra

Crea una función `run_agent(provider: str)` que acepte `"anthropic"` o `"openai"` y
ejecute el loop con el proveedor correspondiente, usando el mismo prompt.
