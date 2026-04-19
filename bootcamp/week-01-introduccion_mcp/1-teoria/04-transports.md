# Transports en MCP: stdio, HTTP/SSE y WebSocket

![Arquitectura MCP con detalle de transports](../0-assets/01-mcp-architecture.svg)

## 🎯 Objetivos

- Entender qué es un transport en el contexto de MCP
- Conocer las diferencias entre stdio, HTTP/SSE y WebSocket
- Saber cuándo usar cada transport según el caso de uso
- Configurar un MCP Server con stdio (el más común en desarrollo)

---

## 📋 Contenido

### 1. ¿Qué es un Transport?

En MCP, el **transport** define el mecanismo físico por el que viajan los mensajes
JSON-RPC entre el MCP Client y el MCP Server. El protocolo (JSON-RPC 2.0) es siempre
el mismo; solo cambia el canal de comunicación.

```
MCP Client ──[transport]──► MCP Server

Transport puede ser:
  - stdio:    stdin/stdout del proceso
  - HTTP/SSE: peticiones HTTP + Server-Sent Events
  - WebSocket: conexión WebSocket bidireccional
```

Elegir el transport correcto depende de cómo vas a desplegar y usar el server.

### 2. Transport: stdio

#### Descripción

`stdio` usa la **entrada y salida estándar del proceso** como canal de comunicación.
El MCP Client lanza el Server como un subproceso y se comunica con él a través de
`stdin` (para enviar mensajes) y `stdout` (para recibir respuestas).

```
Host (Claude Desktop)
  └── spawn subprocess ──► mcp_server.py
        stdin  ◄── JSON-RPC requests
        stdout ──► JSON-RPC responses
```

#### Cuándo usar stdio

- ✅ **Desarrollo local**: es el transport más simple de configurar
- ✅ **Integración con Claude Desktop, Cursor, VS Code**: estos Hosts esperan stdio
- ✅ **Servers que corren en la misma máquina** que el Host
- ✅ **Scripting y automatización** donde el server es un proceso de corta duración

#### Configuración en Python

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mi-server")

@mcp.tool()
async def hello(name: str) -> str:
    """Saluda a alguien."""
    return f"Hola, {name}!"

# Ejecutar con transport stdio (por defecto)
if __name__ == "__main__":
    mcp.run()  # usa stdio por defecto
```

Para ejecutarlo:
```bash
# En la terminal
python src/server.py

# Claude Desktop lo ejecuta así automáticamente al conectarse
```

#### Configuración en TypeScript

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "mi-server", version: "1.0.0" });

server.tool(
  "hello",
  { name: z.string() },
  async ({ name }) => ({
    content: [{ type: "text", text: `Hola, ${name}!` }],
  })
);

// Conectar con stdio
const transport = new StdioServerTransport();
await server.connect(transport);
```

#### Configuración en Claude Desktop

Para que Claude Desktop use tu server con stdio, configura `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mi-server": {
      "command": "python",
      "args": ["/ruta/absoluta/a/src/server.py"],
      "env": {
        "DATABASE_URL": "sqlite:///data/app.db"
      }
    }
  }
}
```

O con Docker:

```json
{
  "mcpServers": {
    "mi-server": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "mi-mcp-server:latest"]
    }
  }
}
```

### 3. Transport: HTTP + SSE

#### Descripción

`HTTP/SSE` combina peticiones HTTP normales (para solicitudes del Client al Server)
con **Server-Sent Events** (para respuestas y notificaciones del Server al Client).

```
MCP Client
  ├── POST /mcp ────────────────────────►  HTTP Server
  │   (JSON-RPC request)                   (MCP Server)
  │
  └── GET /mcp/sse ◄────────────────────  HTTP Server
      (escuchar eventos)                   (SSE stream)
```

#### Cuándo usar HTTP/SSE

- ✅ **Servers en producción**: accesibles desde internet o red local
- ✅ **Múltiples Clients simultáneos**: cada Client tiene su propia conexión SSE
- ✅ **Servers que corren en Docker o Kubernetes**: exposición como servicio HTTP
- ✅ **Integración con herramientas web**: cualquier cliente HTTP puede conectarse
- ⚠️ Requiere más configuración que stdio

#### Configuración en Python

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mi-server")

@mcp.tool()
async def hello(name: str) -> str:
    return f"Hola, {name}!"

# Ejecutar con HTTP/SSE
if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)
```

#### Configuración en TypeScript

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import express from "express";

const app = express();
const server = new McpServer({ name: "mi-server", version: "1.0.0" });

app.get("/sse", async (req, res) => {
  const transport = new SSEServerTransport("/messages", res);
  await server.connect(transport);
});

app.post("/messages", async (req, res) => {
  // Manejar mensajes entrantes del client
});

app.listen(8080);
```

### 4. Transport: WebSocket

#### Descripción

WebSocket proporciona una **conexión bidireccional persistente** entre Client y Server.
A diferencia de HTTP/SSE (que usa dos canales separados), WebSocket usa un solo canal
full-duplex.

```
MCP Client ←──── WebSocket ────► MCP Server
           (mensajes en ambos sentidos
            por la misma conexión)
```

#### Cuándo usar WebSocket

- ✅ **Alta frecuencia de mensajes**: cuando hay muchas interacciones por segundo
- ✅ **Notificaciones frecuentes del Server**: cuando el server envía muchos eventos
- ✅ **Latencia crítica**: menor overhead que HTTP/SSE para conexiones largas
- ⚠️ Más complejo de implementar y depurar que stdio

### 5. Comparativa de Transports

| Característica | stdio | HTTP/SSE | WebSocket |
|----------------|-------|----------|-----------|
| Complejidad de setup | Muy baja | Media | Alta |
| Semanas 1-9 bootcamp | ✅ Recomendado | - | - |
| Producción / remoto | ❌ | ✅ Recomendado | ✅ |
| Claude Desktop / Cursor | ✅ | ✅ | - |
| Múltiples Clients | ❌ (1 proceso = 1 client) | ✅ | ✅ |
| Requiere puerto HTTP | ❌ | ✅ | ✅ |
| Notificaciones push del server | ❌ | ✅ (SSE) | ✅ |

**Regla práctica para este bootcamp:**
- Semanas 1–9: usar **stdio** siempre
- Semana 10+: introducir HTTP/SSE para servers de producción

### 6. El Transport en el Contexto de Docker

Cuando ejecutas un MCP Server con stdio dentro de Docker, el Host lanza el contenedor
como subproceso y se comunica por stdin/stdout del contenedor:

```bash
# Claude Desktop config con Docker + stdio
{
  "command": "docker",
  "args": ["run", "--rm", "-i",
           "-v", "/mi/proyecto:/app/data",
           "mi-mcp-server:latest"]
}
```

El flag `-i` (interactive) es crucial: mantiene stdin abierto para que el Host
pueda enviar mensajes JSON-RPC al contenedor.

```dockerfile
# Dockerfile para MCP Server con stdio
FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN pip install uv && uv sync --frozen --no-dev
COPY src/ ./src/
CMD ["uv", "run", "python", "src/server.py"]
# El CMD escribe/lee por stdin/stdout automáticamente
```

---

## 4. Errores Comunes

**Error: Mezclar `print()` con stdio transport**
Cuando usas stdio, cualquier `print()` o log que escribas a stdout **rompe el protocolo**.
El MCP Client espera JSON-RPC en stdout; un string arbitrario lo confunde.

```python
# ❌ MAL — rompe el protocolo stdio
@mcp.tool()
async def my_tool(x: int) -> int:
    print(f"Procesando {x}")  # NUNCA usar print() con stdio
    return x * 2

# ✅ BIEN — usar logging a stderr
import logging
logger = logging.getLogger(__name__)

@mcp.tool()
async def my_tool(x: int) -> int:
    logger.debug(f"Procesando {x}")  # stderr no interfiere con stdio
    return x * 2
```

**Error: Olvidar el flag `-i` en Docker con stdio**
Sin `-i`, Docker cierra stdin inmediatamente y el server no puede recibir mensajes.

**Error: Usar HTTP/SSE sin CORS configurado**
Si el Client y el Server están en dominios diferentes, necesitas configurar CORS
en el servidor HTTP. Sin CORS, el browser (si el Host es una web app) bloqueará
las peticiones.

**Error: Configurar el puerto incorrecto en HTTP/SSE**
Verificar siempre que el puerto en la configuración del Client coincide con el que
el Server escucha. Un error muy común es usar `8080` en uno y `3000` en el otro.

---

## 5. Ejercicios de Comprensión

1. ¿Por qué usar `print()` con stdio transport rompe el protocolo? ¿A qué stream
   deberías redirigir los logs de debug?

2. Tienes un MCP Server que quieres usar en Claude Desktop (en tu laptop) y también
   exponer para que lo use un equipo remoto. ¿Necesitas dos servers o uno? ¿Qué
   transports configurarías?

3. En el `docker run` con stdio, ¿qué hace exactamente el flag `-i`? Busca la
   documentación de Docker y explícalo con tus palabras.

4. Un compañero tiene un MCP Server en producción con HTTP/SSE pero nota que las
   respuestas llegan con mucho delay. ¿Qué transport alternativo le recomendarías
   para reducir la latencia? ¿Por qué?

---

## 📚 Recursos Adicionales

- [MCP Docs — Transports](https://modelcontextprotocol.io/docs/concepts/transports)
- [MCP Spec — Transport Layer](https://spec.modelcontextprotocol.io/specification/basic/transports/)
- [Server-Sent Events MDN](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

---

## ✅ Checklist de Verificación

- [ ] Sé qué transport usar para desarrollo local (stdio)
- [ ] Entiendo que `print()` a stdout rompe el protocolo stdio
- [ ] Puedo configurar un server Python con stdio transport
- [ ] Puedo configurar un server TypeScript con StdioServerTransport
- [ ] Conozco la diferencia entre HTTP/SSE y WebSocket
- [ ] Sé configurar Claude Desktop para conectarse a un server stdio

---

[← 03 — Los Tres Primitivos](03-primitivos.md) | [05 — MCP vs Alternativas →](05-mcp-vs-alternativas.md)
