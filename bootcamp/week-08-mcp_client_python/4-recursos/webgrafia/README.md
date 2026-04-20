# Webgrafía — Semana 08: MCP Client en Python

## Documentación Oficial

| Recurso | URL | Descripción |
|---------|-----|-------------|
| MCP Python SDK — Client | <https://github.com/modelcontextprotocol/python-sdk> | Código fuente de `ClientSession`, `stdio_client` y `StdioServerParameters` |
| MCP Specification — Client Features | <https://spec.modelcontextprotocol.io/specification/client/> | Spec oficial de las capacidades del client |
| MCP Specification — Architecture | <https://spec.modelcontextprotocol.io/specification/architecture/> | Ciclo de vida de la sesión y estados del protocolo |
| MCP Specification — Tools | <https://spec.modelcontextprotocol.io/specification/server/tools/> | `CallToolResult`, `isError`, tipos de contenido |

## Python y asyncio

| Recurso | URL | Descripción |
|---------|-----|-------------|
| asyncio — Context Managers | <https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager> | `@asynccontextmanager` para context managers async |
| asyncio — run_in_executor | <https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor> | Correr funciones síncronas (como `input()`) sin bloquear |
| asyncio — TimeoutError | <https://docs.python.org/3/library/asyncio-exceptions.html> | Manejo de timeouts con `asyncio.wait_for()` |
| subprocess — Popen | <https://docs.python.org/3/library/subprocess.html> | Cómo Python lanza procesos hijo (base conceptual del stdio transport) |

## JSON-RPC 2.0

| Recurso | URL | Descripción |
|---------|-----|-------------|
| JSON-RPC 2.0 Specification | <https://www.jsonrpc.org/specification> | Protocolo base de MCP: requests, responses, errors |
| JSON-RPC Error Codes | <https://www.jsonrpc.org/specification#error_object> | Códigos de error estándar: -32601 MethodNotFound, -32602 InvalidParams |

## Artículos y Tutoriales

| Recurso | URL | Descripción |
|---------|-----|-------------|
| MCP Quickstart — Client | <https://modelcontextprotocol.io/quickstart/client> | Guía oficial de primeros pasos con el client |
| Building MCP Clients | <https://modelcontextprotocol.io/docs/concepts/architecture> | Conceptos de arquitectura client-server |

---

[← Volver a recursos](../README.md) | [← Semana](../../README.md)
