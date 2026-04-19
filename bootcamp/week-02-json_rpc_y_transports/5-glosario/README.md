# Glosario — Semana 02: JSON-RPC 2.0 y Transports

Términos clave de esta semana, ordenados alfabéticamente.

---

### Batch

Envío de múltiples requests JSON-RPC en un solo array. Permite al cliente enviar
varias solicitudes en una sola llamada de red y recibir todas las respuestas juntas.
MCP soporta batch a nivel de protocolo, aunque pocas implementaciones lo usan en producción.

```json
// Ejemplo de batch request
[
  {"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}},
  {"jsonrpc":"2.0","id":2,"method":"resources/list","params":{}}
]
```

---

### Capabilities

Las capacidades (`capabilities`) que un cliente o servidor MCP declara durante
el handshake `initialize`. Especifican qué primitivos soporta cada lado:
`tools`, `resources`, `prompts`, `logging`, `sampling`, `roots`, `experimental`.

```json
// Server capabilities example
{ "tools": {}, "resources": {"subscribe": true}, "prompts": {} }
```

---

### Framing

Mecanismo para delimitar mensajes en un stream continuo. En el transport stdio,
MCP usa **newline framing**: cada mensaje JSON-RPC ocupa exactamente **una línea**
(terminada en `\n`). Esto permite al receptor saber cuándo termina un mensaje
sin necesitar longitudes ni delimitadores especiales.

---

### Handshake

El intercambio inicial de tres pasos al comenzar una sesión MCP:
1. Cliente envía `initialize` (con `protocolVersion` y `capabilities`)
2. Servidor responde con su `protocolVersion` y `capabilities`
3. Cliente envía `notifications/initialized` (confirma que está listo)

Sin completar el handshake, el servidor rechaza cualquier otro mensaje.

---

### HTTP/SSE

Transport MCP sobre HTTP que usa **Server-Sent Events** (SSE) para el canal
servidor → cliente, y `HTTP POST` para el canal cliente → servidor.
Permite múltiples clientes simultáneos y es debuggeable con herramientas de red.

---

### id

Campo obligatorio en requests y responses JSON-RPC. Debe ser un `string`, `number`
o `null`. El cliente usa el mismo `id` en la request y la response para correlacionar
mensajes en entornos asíncronos. Las **notifications** NO llevan `id`.

---

### initialized (notification)

La notificación `notifications/initialized` que el cliente envía al servidor
después de procesar el response de `initialize`. Indica que el cliente está
listo para enviar requests normales. Es el tercer paso del handshake MCP.

---

### isError

Campo booleano en el resultado de `tools/call`. Cuando es `true`, indica que
el tool ejecutó pero retornó un error semántico (ej. "división por cero").
Diferente al JSON-RPC `error` que indica un error de protocolo.

```json
// Tool error (semántico)
{"result":{"content":[{"type":"text","text":"Error: file not found"}],"isError":true}}

// Protocol error (JSON-RPC)
{"error":{"code":-32601,"message":"Method not found"}}
```

---

### JSON-RPC 2.0

Protocolo ligero de Remote Procedure Call (RPC) basado en JSON. Define el
formato de mensajes: `request` (method + params + id), `response` (result o error),
y `notification` (method + params, sin id). MCP usa JSON-RPC 2.0 como capa
de transporte de todos sus mensajes.

---

### keepalive

Mecanismo para mantener activa una conexión persistente (SSE o WebSocket).
En SSE, el servidor envía comentarios periódicos (`: keepalive\n\n`) para
evitar que intermediarios (proxies, load balancers) cierren la conexión por timeout.

---

### Lifecycle

El ciclo de vida completo de una sesión MCP: **initialization** (handshake),
**operation** (requests/responses/notifications), y **shutdown** (cierre limpio
con `notifications/cancelled` o simplemente cerrando la conexión).

---

### Notification

Un mensaje JSON-RPC que **no lleva `id`** y no espera respuesta. En MCP se usa
para eventos unidireccionales como `notifications/initialized`, `notifications/tools/list_changed`,
o `notifications/progress`. El receptor los procesa pero no puede responder.

---

### protocolVersion

La versión del protocolo MCP negociada durante `initialize`. Formato: `"YYYY-MM-DD"`.
La versión actual es `"2024-11-05"`. Si cliente y servidor no pueden acordar
una versión compatible, la conexión falla.

---

### sessionId

Identificador único de una sesión SSE, asignado por el servidor al momento de
la conexión. El cliente incluye el `sessionId` en cada `POST /message` para que
el servidor sepa a qué conexión SSE pertenece el mensaje. Es fundamental para
soportar múltiples clientes simultáneos.

---

### SSE (Server-Sent Events)

Tecnología HTTP estándar para streaming unidireccional del servidor al cliente.
Una conexión `GET` queda abierta y el servidor envía eventos en el formato:
`data: <payload>\n\n`. MCP usa SSE para el canal servidor → cliente en el
transport HTTP/SSE.

---

### stdio

Transport MCP que usa **stdin** y **stdout** del proceso para transmitir mensajes.
El cliente escribe en el stdin del servidor y lee respuestas del stdout.
Es el transport más simple, ideal para integración local con Claude Desktop.
Restricción: solo soporta un cliente a la vez.

---

### WebSocket

Protocolo de comunicación bidireccional full-duplex sobre TCP. A diferencia de SSE,
permite que tanto cliente como servidor envíen mensajes en cualquier momento.
En MCP se usa cuando se necesita baja latencia o eventos frecuentes del servidor
(telemetría, streaming de métricas).

---

[← Volver al README de la semana](../README.md)

Mensaje JSON-RPC sin id — no requiere respuesta

### Request

Mensaje JSON-RPC con id que espera una response del servidor

### Response

Mensaje JSON-RPC de respuesta a un request, con result o error

### Sesión MCP

Conexión completa entre un Client y un Server desde initialize hasta shutdown

### WebSocket

Protocolo de comunicación bidireccional en tiempo real (transport MCP alternativo)

### initialize

Primer mensaje de una sesión MCP para negociar capabilities

### shutdown

Mensaje para terminar ordenadamente una sesión MCP

### stdio

Transport MCP que usa stdin/stdout del proceso para la comunicación

---

[← Volver al README de la semana](../README.md)
