# Transport WebSocket: Comunicación Bidireccional en Tiempo Real

## 🎯 Objetivos

- Entender cuándo WebSocket es preferible a HTTP/SSE en MCP
- Conocer la diferencia técnica entre SSE y WebSocket
- Implementar un MCP Server con WebSocket transport en Python y TypeScript
- Identificar los casos de uso avanzados donde WebSocket aporta valor

---

## 📋 Contenido

### 1. WebSocket vs SSE: ¿Cuál es la diferencia?

Tanto SSE como WebSocket permiten comunicación en tiempo real entre cliente y servidor,
pero con diferencias fundamentales:

| Aspecto | SSE (`text/event-stream`) | WebSocket (`ws://` / `wss://`) |
|---------|--------------------------|-------------------------------|
| Dirección | Unidireccional (server → client) | **Bidireccional** |
| Protocolo | HTTP/1.1 sobre TCP | Upgrade de HTTP a WS |
| Reconexión automática | ✅ Sí (nativa en el browser) | ❌ Debe implementarse |
| Soporte en proxies | ✅ Alto (es HTTP) | ⚠️ Requiere configuración |
| Overhead por mensaje | Bajo (texto plano) | Muy bajo (frames binarios) |
| Casos de uso MCP | Producción HTTP estándar | Streaming intensivo, baja latencia |

En MCP, SSE es el transport HTTP más usado porque los proxies y CDNs lo soportan
sin configuración especial. WebSocket es una alternativa para escenarios específicos.

---

### 2. Cuándo Usar WebSocket en MCP

WebSocket es apropiado cuando:

- Se necesita comunicación bidireccional genuina de alta frecuencia
- El servidor envía notificaciones en tiempo real con latencia mínima
- La infraestructura tiene soporte nativo para WebSocket (Nginx con `proxy_set_header Upgrade`)
- Se construye una interfaz de usuario reactiva que muestra actualizaciones en vivo

Ejemplos reales:
- MCP Server de monitoreo que empuja métricas cada 100ms
- Server de análisis de código que emite resultados incrementales conforme parsea
- Server de base de datos con notificaciones LISTEN/NOTIFY de PostgreSQL

---

### 3. MCP Server con WebSocket en Python

```python
# src/server_ws.py
import asyncio
import json

import websockets
import websockets.server
from mcp.server import Server
from mcp.types import Tool, TextContent

mcp_server = Server("mi-servidor-ws")


@mcp_server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="echo",
            description="Repite el mensaje recibido",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                },
                "required": ["message"],
            },
        )
    ]


@mcp_server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "echo":
        return [TextContent(type="text", text=f"Echo: {arguments['message']}")]
    raise ValueError(f"Tool desconocido: {name}")


class WebSocketStream:
    """Adaptador que envuelve un WebSocket como stream MCP."""

    def __init__(self, websocket: websockets.server.WebSocketServerProtocol) -> None:
        self.websocket = websocket
        self._queue: asyncio.Queue[dict] = asyncio.Queue()

    async def __aiter__(self):
        async for raw_message in self.websocket:
            try:
                yield json.loads(raw_message)
            except json.JSONDecodeError:
                continue

    async def send(self, message: dict) -> None:
        await self.websocket.send(json.dumps(message))


async def handle_connection(websocket: websockets.server.WebSocketServerProtocol) -> None:
    """Gestiona una conexión WebSocket de un cliente MCP."""
    import sys
    sys.stderr.write(f"Cliente WS conectado: {websocket.remote_address}\n")

    # El SDK MCP puede adaptarse a cualquier stream read/write
    # Aquí se usa una implementación manual de bajo nivel como referencia
    try:
        async for message in websocket:
            request = json.loads(message)
            sys.stderr.write(f"Recibido: {request.get('method', 'response')}\n")
            # En producción, usar el SDK correctamente con el transport oficial
    except websockets.exceptions.ConnectionClosed:
        sys.stderr.write("Cliente desconectado\n")


async def main() -> None:
    async with websockets.serve(handle_connection, "0.0.0.0", 8001):
        import sys
        sys.stderr.write("Servidor WebSocket en ws://localhost:8001\n")
        await asyncio.Future()  # correr indefinidamente


if __name__ == "__main__":
    asyncio.run(main())
```

> **Nota**: El SDK oficial de MCP Python tiene soporte experimental para WebSocket.
> Para producción, verificar la versión más reciente del SDK en el repositorio oficial.

---

### 4. MCP Server con WebSocket en TypeScript

```typescript
// src/index-ws.ts
import { WebSocketServer, WebSocket } from "ws";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { WebSocketServerTransport } from "@modelcontextprotocol/sdk/server/websocket.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const wss = new WebSocketServer({ port: 8001 });

function createMcpServer(): Server {
  const server = new Server(
    { name: "mi-servidor-ws", version: "1.0.0" },
    { capabilities: { tools: {} } }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
      {
        name: "echo",
        description: "Repite el mensaje recibido",
        inputSchema: {
          type: "object" as const,
          properties: {
            message: { type: "string" },
          },
          required: ["message"],
        },
      },
    ],
  }));

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    if (name === "echo") {
      return {
        content: [{ type: "text" as const, text: `Echo: ${args?.message}` }],
      };
    }
    throw new Error(`Tool desconocido: ${name}`);
  });

  return server;
}

wss.on("connection", async (ws: WebSocket) => {
  process.stderr.write("Cliente WebSocket conectado\n");

  const transport = new WebSocketServerTransport(ws);
  const server = createMcpServer();

  ws.on("close", () => {
    process.stderr.write("Cliente WebSocket desconectado\n");
  });

  await server.connect(transport);
});

process.stderr.write("Servidor WebSocket en ws://localhost:8001\n");
```

---

### 5. Configuración Docker para WebSocket

```yaml
# docker-compose.yml
services:
  mcp-server-ws:
    build: .
    ports:
      - "8001:8001"   # Puerto WebSocket
    environment:
      - WS_PORT=8001
    restart: unless-stopped
```

Nginx como proxy inverso con soporte WebSocket:

```nginx
# nginx.conf (fragmento)
location /ws {
    proxy_pass http://mcp-server-ws:8001;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;    # CRÍTICO para WebSocket
    proxy_set_header Connection "Upgrade";
    proxy_set_header Host $host;
    proxy_read_timeout 3600s;   # conexiones largas
}
```

---

### 6. Comparativa de los Tres Transports

```
Decisión de transport:

¿Necesitas múltiples clientes simultáneos?
├── No  → stdio (más simple, desarrollo local)
└── Sí  → ¿Necesitas despliegue en nube o proxies estándar?
          ├── Sí → HTTP/SSE (producción, compatibilidad máxima)
          └── Alta frecuencia + baja latencia → WebSocket
```

**Resumen de uso por semana del bootcamp:**

| Semanas | Transport | Razón |
|---------|-----------|-------|
| 02–09 | stdio | Aprendizaje, integración con Claude Desktop |
| 10–11 | HTTP/SSE | Producción, múltiples clientes, Docker |
| 12 | WebSocket | Casos avanzados, proyecto final opcional |

---

### 7. Seguridad en WebSocket

A diferencia de HTTP, WebSocket no tiene headers por cada mensaje, lo que
requiere gestionar autenticación al momento de la conexión:

```python
# Verificar token en el handshake WebSocket
async def handle_connection(
    websocket: websockets.server.WebSocketServerProtocol,
    path: str,
) -> None:
    # Obtener token de query params: ws://server:8001/mcp?token=xxx
    import urllib.parse
    query = urllib.parse.parse_qs(urllib.parse.urlparse(path).query)
    token = query.get("token", [None])[0]

    if token != EXPECTED_TOKEN:
        await websocket.close(code=1008, reason="Unauthorized")
        return

    # Proceder con la conexión MCP...
```

```typescript
// TypeScript — validar token en upgrade HTTP
wss.on("upgrade", (request, socket) => {
  const url = new URL(request.url ?? "", "http://localhost");
  const token = url.searchParams.get("token");

  if (token !== process.env.WS_TOKEN) {
    socket.write("HTTP/1.1 401 Unauthorized\r\n\r\n");
    socket.destroy();
  }
});
```

---

## ⚠️ Errores Comunes

**1. Proxies que no soportan WebSocket**
Muchos proxies corporativos bloquean WebSocket. Verificar con el equipo de
infraestructura o usar HTTP/SSE como alternativa más compatible.

**2. No manejar reconexión**
A diferencia de SSE, WebSocket no reconecta automáticamente. El cliente debe
implementar lógica de reconexión con backoff exponencial.

**3. `proxy_read_timeout` demasiado corto en Nginx**
El timeout por defecto (60s) cierra conexiones WebSocket inactivas. Aumentar
a 3600s para sesiones largas de MCP.

**4. Confundir `ws://` con `wss://`**
En producción siempre usar `wss://` (WebSocket Secure, sobre TLS).
`ws://` envía datos en texto plano y es solo para desarrollo local.

---

## 🧪 Ejercicios de Comprensión

1. ¿Por qué SSE reconecta automáticamente pero WebSocket no?
2. Describe un caso de uso de MCP donde WebSocket sería claramente superior a SSE.
3. ¿Qué header HTTP es obligatorio para que Nginx haga proxy de WebSocket?
4. ¿Por qué se recomienda `wss://` (WebSocket Secure) en producción?

---

## 📚 Recursos Adicionales

- [MDN — WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [MCP Spec — WebSocket Transport](https://spec.modelcontextprotocol.io/specification/basic/transports/)
- [websockets library (Python)](https://websockets.readthedocs.io/)
- [ws library (Node.js)](https://github.com/websockets/ws)

---

## ✅ Checklist de Verificación

- [ ] Entiendo la diferencia técnica entre SSE y WebSocket
- [ ] Conozco el árbol de decisión: stdio → HTTP/SSE → WebSocket
- [ ] Sé cuándo WebSocket aporta valor real en MCP
- [ ] Comprendo cómo agregar autenticación en el handshake WebSocket
- [ ] Sé configurar Nginx como proxy inverso con soporte WebSocket
- [ ] Entiendo por qué `wss://` es obligatorio en producción

---

[← 03](03-http-sse-transport.md) | [Índice](README.md) | [05 →](05-mensajes-mcp.md)
