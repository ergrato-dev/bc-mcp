# Mensajes del Protocolo MCP — Análisis Paso a Paso

Descomenta cada sección según las instrucciones del README.

---

## Paso 1: Handshake de Inicialización

<!-- Descomenta el bloque completo de abajo: -->

<!--
### Solicitud initialize (Client → Server)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": { "listChanged": true }
    },
    "clientInfo": {
      "name": "mcp-inspector",
      "version": "1.0.0"
    }
  }
}
```

**Campos obligatorios de toda solicitud JSON-RPC:**
- `jsonrpc`: siempre "2.0" — identifica la versión del protocolo
- `id`: número único que el Client asigna para correlacionar la respuesta
- `method`: el método que se invoca (aquí "initialize")
- `params`: argumentos del método (puede ser objeto o array)

### Respuesta initialize (Server → Client)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": { "subscribe": false, "listChanged": true },
      "prompts": { "listChanged": true }
    },
    "serverInfo": {
      "name": "server-everything",
      "version": "0.6.2"
    }
  }
}
```

**Notar:** el `id` de la respuesta coincide con el `id` de la solicitud (1).
Así el Client sabe a qué solicitud corresponde esta respuesta.

### Notification initialized (Client → Server)

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

**Notar:** las notificaciones NO tienen campo `id` — son mensajes unidireccionales
que no esperan respuesta.
-->

---

## Paso 2: Llamada a Tool

<!-- Descomenta el bloque completo de abajo: -->

<!--
### Solicitud tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "method": "tools/call",
  "params": {
    "name": "add",
    "arguments": {
      "a": 5,
      "b": 3
    }
  }
}
```

### Respuesta exitosa

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "8"
      }
    ],
    "isError": false
  }
}
```

**Estructura de content:**
- `type`: siempre "text" para respuestas de texto (también puede ser "image" o "resource")
- `text`: el valor de retorno serializado como string
- `isError`: false en respuestas exitosas
-->

---

## Paso 3: Respuesta de Error

<!-- Descomenta el bloque completo de abajo: -->

<!--
### Solicitud con parámetro incorrecto

```json
{
  "jsonrpc": "2.0",
  "id": 7,
  "method": "tools/call",
  "params": {
    "name": "add",
    "arguments": {
      "a": "no-soy-un-numero",
      "b": 3
    }
  }
}
```

### Respuesta de error del protocolo

```json
{
  "jsonrpc": "2.0",
  "id": 7,
  "error": {
    "code": -32602,
    "message": "Invalid params: a must be a number"
  }
}
```

**Códigos de error estándar JSON-RPC:**
- -32700: Parse error (JSON inválido)
- -32600: Invalid Request (solicitud malformada)
- -32601: Method not found (método desconocido)
- -32602: Invalid params (parámetros incorrectos)
- -32603: Internal error (error del server)
-->

---

## Paso 4: Reflexión

<!-- Descomenta y responde: -->

<!--
**Pregunta 1:** Si el Client envía dos solicitudes simultáneas con id=10 e id=11,
¿cómo sabe a cuál corresponde cada respuesta cuando llegan?

**Tu respuesta:**


**Pregunta 2:** ¿Por qué las notificaciones no tienen `id`? ¿Qué implicación
tiene eso para el protocolo?

**Tu respuesta:**


**Pregunta 3:** El campo `result.content` es siempre un array, incluso si solo
hay un elemento. ¿Por qué crees que se diseñó así?

**Tu respuesta:**

-->
