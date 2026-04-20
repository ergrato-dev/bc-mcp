# Glosario — Semana 10: Integración con Claude y OpenAI

Términos clave de esta semana, ordenados alfabéticamente.

---

### Agentic loop

Bucle `while` que permite a un LLM razonar, llamar herramientas y generar
una respuesta final de forma autónoma. Se repite hasta que el modelo indica
que ha terminado (`stop_reason: end_turn` o `finish_reason: stop`).

### Anthropic SDK

Librería oficial de Python/TypeScript de Anthropic para interactuar con
la API de Claude. Paquete: `anthropic`. Clase principal: `Anthropic`.

### AsyncExitStack

Context manager de Python (`contextlib.AsyncExitStack`) que permite gestionar
múltiples context managers asíncronos en una sola estructura. Esencial para
conectar a N servers MCP y garantizar el cierre correcto de todas las sesiones.

### Claude

Familia de modelos de lenguaje desarrollados por Anthropic.
Variantes principales: Haiku (rápido), Sonnet (equilibrado), Opus (máxima capacidad).

### dispatch (despacho)

En el contexto del agentic loop: la acción de identificar qué herramienta
pidió el LLM, ejecutarla en el MCP server correcto y devolver el resultado.

### end_turn

Valor de `stop_reason` en Anthropic que indica que el modelo ha terminado
de generar su respuesta y no necesita más tool calls. Condición de salida del loop.

### finish_reason

Campo en la respuesta de la API de OpenAI (`choices[0].finish_reason`) equivalente
a `stop_reason` de Anthropic. Valores relevantes: `"tool_calls"` y `"stop"`.

### Function calling

Mecanismo de la API de OpenAI para que el LLM invoque funciones definidas
por el usuario. El LLM devuelve `tool_calls[]` en el assistant message cuando
quiere ejecutar una función.

### input_schema

Campo requerido por la API de Anthropic en la definición de una tool.
Contiene el JSON Schema que describe los parámetros de la herramienta.
No confundir con `parameters` (OpenAI) ni `inputSchema` (MCP).

### inputSchema

Campo del objeto `Tool` devuelto por MCP (`session.list_tools()`).
Es un dict con JSON Schema. Se convierte a `input_schema` (Anthropic) o
`parameters` (OpenAI) al registrar las tools en cada API.

### MAX_ITERATIONS

Constante de seguridad en el agentic loop que limita el número máximo de
iteraciones para evitar loops infinitos o consumo excesivo de tokens.

### messages (array)

Historial de la conversación en la API de OpenAI. Se acumula en cada turno:
`user → assistant (tool_calls) → tool → assistant (final)`.

### Multi-turn

Conversación con múltiples rondas de mensajes. En un agente, cada par
`tool_use` + `tool_result` añade dos mensajes al historial.

### OpenAI SDK

Librería oficial de Python/TypeScript de OpenAI. Paquete: `openai`.
Clase principal: `OpenAI`. Método de chat: `client.chat.completions.create()`.

### parameters

Campo que usa OpenAI en la definición de una function para describir
sus parámetros con JSON Schema. Equivale a `input_schema` en Anthropic.

### stop_reason

Campo en la respuesta de la API de Anthropic que indica por qué dejó
de generar texto. Valores: `"tool_use"` (quiere llamar una tool) o
`"end_turn"` (respuesta final lista).

### tool_call_id

Identificador único en OpenAI que vincula un `tool_call` del assistant
con su `tool` result correspondiente en el historial de mensajes.

### tool_use_id

Identificador único en Anthropic que vincula un bloque `tool_use`
con su bloque `tool_result` en el turno siguiente. Debe copiarse exactamente.

### tool_to_session

Diccionario de routing en un agente multi-server: `{tool_name: ClientSession}`.
Permite saber a qué sesión MCP enviar cada tool call.

### ToolUseBlock

Tipo de bloque en la respuesta de Anthropic que contiene `id`, `name` e `input`
de una herramienta que Claude quiere ejecutar. Se accede en `response.content`.

---

[← Volver al README de la semana](../README.md)
