# Glosario — Semana 06: Servers Avanzados — Los 3 Primitivos

Términos clave de esta semana, ordenados alfabéticamente.

---

### @mcp.prompt()

Decorador FastMCP para registrar un Prompt. La función decorada retorna `list[Message]`
con los mensajes iniciales de la conversación. Los parámetros de la función se publican
automáticamente como argumentos del prompt en `prompts/list`.

---

### @mcp.resource()

Decorador FastMCP para registrar un Resource con URI estático.
Ejemplo: `@mcp.resource("tasks://all")` registra el resource con esa URI exacta.

---

### @mcp.resource('{param}')

Decorador FastMCP para resource templates con URI variable.
El parámetro entre llaves (`{param}`) es extraído automáticamente de la URI y pasado
como argumento a la función. Ejemplo: `@mcp.resource("tasks://{task_id}")`.

---

### CallToolResult

Tipo de retorno de un tool en TypeScript SDK. Estructura:
```typescript
{ content: [{ type: "text", text: string }], isError?: boolean }
```

---

### Context (FastMCP)

Objeto inyectado automáticamente por FastMCP en los handlers que lo declaran como parámetro.
Proporciona acceso a: `ctx.info()`, `ctx.warning()`, `ctx.error()`, `ctx.debug()`,
`ctx.report_progress()`, `ctx.read_resource()`.

---

### GetPromptRequestSchema

Schema del SDK TypeScript para el handler `prompts/get`. Recibe `name` (string)
y `arguments` (Record<string, string>). Retorna `{ description, messages[] }`.

---

### list[Message]

Tipo de retorno de prompts en Python FastMCP. Cada `Message` tiene `role` ("user" o "assistant")
y `content` (generalmente `TextContent(type="text", text="...")`).

---

### ListPromptsRequestSchema

Schema del SDK TypeScript para el handler `prompts/list`.
Retorna `{ prompts: [{ name, description, arguments[] }] }`.

---

### ListResourcesRequestSchema

Schema del SDK TypeScript para el handler `resources/list`.
Retorna `{ resources: [{ uri, name, mimeType? }] }`.

---

### mimeType

Campo opcional en un resource que indica el tipo de contenido devuelto.
Valores comunes: `"application/json"`, `"text/plain"`, `"text/markdown"`.

---

### Prompt argument

Parámetro declarado en un Prompt. Tiene: `name` (string), `description` (string),
`required` (boolean). En Python FastMCP se infiere de los parámetros de la función.

---

### prompts/get

Método MCP invocado por el cliente para obtener los mensajes de un prompt específico.
Equivale a "ejecutar" el prompt con sus argumentos.

---

### prompts/list

Método MCP invocado por el cliente para descubrir los prompts disponibles en el server.
Similar a `tools/list` pero para prompts.

---

### ReadResourceRequestSchema

Schema del SDK TypeScript para el handler `resources/read`.
Recibe `uri` (string). Retorna `{ contents: [{ uri, mimeType, text }] }`.

---

### Resource template

URI con variables entre llaves `{param}` que permite leer recursos dinámicos.
En Python FastMCP se registra con `@mcp.resource("scheme://{param}")`.
En TypeScript se implementa con regex manual en el handler de `resources/read`.

---

### resources/list

Método MCP invocado por el cliente para descubrir los resources disponibles.
Devuelve URIs estáticas y plantillas de URI dinámicas.

---

### resources/read

Método MCP invocado por el cliente para leer el contenido de un resource específico.
Siempre requiere una URI concreta (no una plantilla).

---

### RFC 6570

Estándar (Request for Comments) que define la sintaxis de URI Templates.
MCP usa esta sintaxis para resource templates: `tasks://{task_id}`, `users://{id}/profile`.

---

### State (estado del server)

Datos mutables almacenados en el server (en memoria o en DB). Los Tools mutan el estado,
los Resources lo leen, los Prompts lo usan para generar mensajes contextuales.
Principio clave: **una sola fuente de verdad** compartida por los 3 primitivos.

---

### TextContent

Tipo de contenido de mensaje en MCP. En Python: `TextContent(type="text", text="...")`.
En TypeScript: `{ type: "text", text: string }`. Usado dentro de `Message.content`.

---

### URI scheme

Prefijo antes de `://` en una URI MCP. Define el dominio del resource.
Ejemplos: `tasks://`, `notes://`, `db://`, `file://`. Elegido por el desarrollador del server.

---

[← Volver al README de la semana](../README.md)
