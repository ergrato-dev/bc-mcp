# Glosario — Semana 03: Los Tres Primitivos: Tools, Resources y Prompts

Términos clave de esta semana, ordenados alfabéticamente.

---

### Annotation

Metadato opcional declarado en un Tool que describe su comportamiento esperado:
`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`. Ayuda al
cliente y al LLM a decidir si invocar el tool automáticamente.

---

### BlobResourceContents

Tipo de contenido de un Resource para datos binarios (imágenes, PDFs, etc.).
El campo `blob` contiene los bytes codificados en Base64. Ejemplo:
```python
types.BlobResourceContents(uri="file://logo.png", blob="aGVsbG8=", mimeType="image/png")
```

---

### CallToolResult

Objeto de respuesta de un Tool. Contiene `content` (lista de TextContent/ImageContent/
EmbeddedResource) e `isError` (bool, default False). Si `isError=True`, el contenido
es un mensaje de error legible por el LLM, no una excepción.

---

### destructiveHint

Annotation de Tool que indica que puede eliminar o sobreescribir datos permanentemente
(ej. `delete_file`, `drop_table`). El cliente puede pedir confirmación al usuario.

---

### EmbeddedResource

Tipo de contenido que incluye un Resource completo dentro de un PromptMessage o
CallToolResult. Permite pasar datos contextuales directamente al LLM sin un segundo
request `resources/read`.

---

### GetPromptResult

Objeto de respuesta del handler `get_prompt`. Contiene `description` (str opcional)
y `messages` (lista de `PromptMessage`). Los mensajes definen el contexto inicial de
la conversación.

---

### idempotentHint

Annotation de Tool que indica que llamar con los mismos argumentos produce siempre
el mismo resultado sin efectos adicionales. Permite reintentos seguros.

---

### inputSchema

Campo obligatorio de un Tool. Define un JSON Schema (tipo `object`) que valida
los argumentos de entrada. Buena práctica: incluir `"additionalProperties": false`.

---

### isError

Campo booleano de `CallToolResult`. Cuando es `True`, el LLM interpreta el contenido
como un mensaje de error y puede reintentarlo o informar al usuario. A diferencia de
lanzar una excepción, `isError=True` es un fallo **lógico** esperado.

---

### MIME type

Identificador de formato de datos (Media Type). Define cómo interpretar el contenido
de un Resource o EmbeddedResource. Ejemplos: `"text/plain"`, `"application/json"`,
`"text/markdown"`, `"image/png"`, `"application/pdf"`.

---

### PromptArgument

Parámetro declarado en un Prompt. Tiene `name`, `description` y `required` (bool).
Los argumentos opcionales (`required=False`) se acceden con `.get(key, default)`.

---

### PromptMessage

Elemento de la lista `messages` en `GetPromptResult`. Tiene `role` ("user" o
"assistant") y `content` (TextContent, ImageContent o EmbeddedResource).
Un mensaje con `role="assistant"` actúa como *seed* para orientar la respuesta del LLM.

---

### ReadResourceResult

Objeto de respuesta del handler `read_resource`. Contiene `contents`: lista de
`TextResourceContents` o `BlobResourceContents`.

---

### readOnlyHint

Annotation de Tool que indica que el tool no modifica ningún estado externo.
Equivalente a un `GET` en REST. El LLM puede invocarlo libremente.

---

### ResourceTemplate

Plantilla de Resource con URI parametrizado usando la sintaxis RFC 6570:
`"docs://files/{filename}"`. Permite que el cliente genere URIs dinámicos para
acceder a recursos individuales sin conocerlos de antemano.

---

### TextContent

Tipo de contenido de texto plano en tools y prompts. Siempre tiene `type="text"`.
```python
types.TextContent(type="text", text="Hello, world!")
```

---

### TextResourceContents

Tipo de contenido de un Resource para datos de texto (JSON, Markdown, CSV, etc.).
Campos: `uri` (str), `text` (str), `mimeType` (str opcional).

---

### ToolAnnotations

Clase Python / objeto TypeScript que agrupa las annotations de un Tool:
`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.
Todos son opcionales con default `None`/`undefined`.

---

### URI Template

Cadena que define un patrón de URI parametrizado, per RFC 6570.
Variables se encierran en `{}`. Ejemplo: `"db://users/{user_id}"`.
Se usa en `ResourceTemplate.uriTemplate`.

---

[← Volver al README de la semana](../README.md)

### Content

Unidad de contenido MCP: text, image o resource

### Input Schema

JSON Schema que define los parámetros de entrada de un Tool

### MIME Type

Tipo de contenido de un Resource (text/plain, application/json, etc.)

### Prompt

Plantilla de instrucciones con argumentos definidos por el servidor

### Prompt Argument

Parámetro requerido u opcional de un Prompt MCP

### Resource

Fuente de datos expuesta con URI único (db://..., file://..., etc.)

### Resource Template

Patrón de URI con variables para generar resources dinámicos

### Tool

Función con schema de inputs que un LLM puede invocar a través de MCP

### URI

Identificador único de un Resource en formato scheme://path

---

[← Volver al README de la semana](../README.md)
