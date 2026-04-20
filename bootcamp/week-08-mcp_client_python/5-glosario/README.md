# Glosario — Semana 08: MCP Client en Python

Términos clave de esta semana, ordenados alfabéticamente.

---

### BrokenPipeError

Excepción Python que se lanza cuando el proceso server se cierra inesperadamente
mientras el client intenta leer o escribir en el pipe. Indica que la sesión está
muerta y hay que reiniciar el client completo.

### CallToolResult

Objeto retornado por `session.call_tool()`. Tiene dos campos principales:
- `content: list[TextContent | ImageContent | EmbeddedResource]` — los resultados
- `isError: bool` — si el tool reportó un error de dominio

No se lanza como excepción: siempre hay que verificar `result.isError` explícitamente.

### ClientSession

Clase principal del SDK MCP Python. Encapsula el protocolo MCP sobre un par de
streams (read/write) y expone métodos de alto nivel: `initialize()`, `list_tools()`,
`call_tool()`, `list_resources()`, `read_resource()`, `list_prompts()`, `get_prompt()`.
Se usa siempre dentro de un `async with ClientSession(read, write) as session:`.

### Discovery

Fase del flujo MCP en la que el client consulta qué tools, resources y prompts
ofrece el server usando `list_tools()`, `list_resources()` y `list_prompts()`.
Permite construir clients genéricos que no hardcodean los nombres.

### EmbeddedResource

Tipo de contenido MCP que incrusta un resource completo dentro del resultado de
un tool. Tiene un campo `resource` que puede ser `TextResourceContents` (con `.text`)
o `BlobResourceContents` (con `.blob` en base64).

### framing

Mecanismo por el que los mensajes JSON-RPC se delimitan en el stream de bytes.
En el transporte stdio de MCP, cada mensaje está en su propia línea (newline-delimited).
Permite que el receptor sepa dónde termina un mensaje y empieza el siguiente.

### GetPromptResult

Objeto retornado por `session.get_prompt(name, args)`. Contiene una lista de
`PromptMessage`, cada uno con `role` ("user" o "assistant") y `content` (texto
ya renderizado con los argumentos sustituidos). Listo para enviar a un LLM.

### ImageContent

Tipo de contenido MCP para datos de imagen. Tiene tres campos:
- `type: "image"`
- `data: str` — imagen codificada en base64
- `mimeType: str` — tipo MIME (ej. `"image/png"`, `"image/jpeg"`)

Para obtener los bytes: `base64.b64decode(item.data)`.

### InitializeResult

Objeto retornado por `session.initialize()`. Contiene:
- `serverInfo.name` y `serverInfo.version`
- `capabilities` — qué soporta el server (tools, resources, prompts)

### isError

Campo booleano de `CallToolResult`. Cuando es `True`, el tool reportó un error
de dominio (libro no encontrado, dato inválido, etc.). El mensaje de error está
en `result.content[0].text`. No es una excepción Python — el flujo continúa.

### JSON-RPC 2.0

Protocolo de llamada a procedimientos remotos sobre JSON. MCP lo usa como capa
de transporte. Cada mensaje tiene `jsonrpc: "2.0"`, `method`, `id` (para requests)
y `params` o `result`/`error`. Los IDs correlacionan requests con responses.

### ListToolsResult

Objeto retornado por `session.list_tools()`. Contiene `tools: list[Tool]`.
Cada `Tool` tiene `name`, `description` e `inputSchema` (JSON Schema).

### McpError

Excepción Python del SDK MCP. Se lanza cuando hay un error en el nivel del
**protocolo**: nombre de tool inexistente (`-32601`), parámetros inválidos
(`-32602`), error interno del server (`-32603`). A diferencia de `isError=True`,
McpError sí interrumpe el flujo con una excepción.

### ReadResourceResult

Objeto retornado por `session.read_resource(uri)`. Contiene
`contents: list[TextResourceContents | BlobResourceContents]`.

### stdio_client

Context manager del SDK MCP que lanza el proceso server como subprocess,
abre pipes `stdin`/`stdout` y devuelve `(read_stream, write_stream)`.
Al salir del bloque `async with`, cierra los pipes y termina el proceso.

### StdioServerParameters

Dataclass que describe cómo lanzar el proceso server:
- `command: str` — ejecutable (`"python"`, `"node"`, `"uv"`)
- `args: list[str]` — argumentos (ej. `["src/server.py"]`)
- `env: dict | None` — variables de entorno del proceso hijo

Si `env` se especifica, **reemplaza** el entorno completo. Para heredar
el entorno actual: `env={**os.environ, "MI_VAR": "valor"}`.

### subprocess

Proceso hijo lanzado por Python para ejecutar otro programa. El stdio transport
de MCP lanza el server como subprocess y se comunica con él por `stdin`/`stdout`.
El SDK usa `asyncio.create_subprocess_exec` internamente.

### TextContent

Tipo de contenido MCP más común. Tiene un campo `text: str` con el resultado
del tool. Los tools de este bootcamp retornan JSON serializado como string
en `TextContent`. Para deserializar: `json.loads(item.text)`.

### TimeoutError

Error que ocurre cuando una operación supera el tiempo máximo de espera.
Se produce con `asyncio.wait_for(coro, timeout=N)`. Indica que el server está
lento o bloqueado, no que la sesión esté muerta (se puede seguir usando).

---

[← Volver al README de la semana](../README.md)

Configuración del client para conectarse a un server via stdio

### TextContent

Tipo de contenido MCP para texto plano

### connect()

Método que inicia la conexión y el handshake con el server

### list_resources()

Método del client para obtener resources disponibles en el server

### list_tools()

Método del client para obtener la lista de tools disponibles en el server

### tool_result.content

Lista de contenidos devueltos por un tool (TextContent, ImageContent)

---

[← Volver al README de la semana](../README.md)
