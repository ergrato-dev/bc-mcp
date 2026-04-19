# ============================================================
# SECCIÓN A — Importaciones y setup de FastAPI + MCP
# Descomenta las siguientes líneas:
# ============================================================
# import sys
# import uvicorn
# from mcp.server import Server
# from mcp.server.sse import SseServerTransport
# from mcp.types import Tool, TextContent
# from starlette.applications import Starlette
# from starlette.requests import Request
# from starlette.responses import JSONResponse
# from starlette.routing import Mount, Route
#
# mcp_server = Server("calculadora-sse")
# sse_transport = SseServerTransport("/message")

# ============================================================
# SECCIÓN B — Tools (mismos que en practica-02)
# Descomenta las siguientes líneas:
# ============================================================
# @mcp_server.list_tools()
# async def list_tools() -> list[Tool]:
#     return [
#         Tool(
#             name="calculate",
#             description="Realiza operaciones matemáticas básicas",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "a": {"type": "number", "description": "Primer operando"},
#                     "b": {"type": "number", "description": "Segundo operando"},
#                     "op": {
#                         "type": "string",
#                         "enum": ["add", "sub", "mul", "div"],
#                         "description": "Operación: add, sub, mul, div",
#                     },
#                 },
#                 "required": ["a", "b", "op"],
#             },
#         )
#     ]
#
#
# @mcp_server.call_tool()
# async def call_tool(name: str, arguments: dict) -> list[TextContent]:
#     if name != "calculate":
#         raise ValueError(f"Tool desconocido: {name}")
#     a: float = arguments["a"]
#     b: float = arguments["b"]
#     op: str = arguments["op"]
#     sys.stderr.write(f"[calculate] a={a} b={b} op={op}\n")
#     if op == "add":
#         result = a + b
#     elif op == "sub":
#         result = a - b
#     elif op == "mul":
#         result = a * b
#     elif op == "div":
#         if b == 0:
#             return [TextContent(type="text", text="Error: división por cero")]
#         result = a / b
#     else:
#         raise ValueError(f"Operación desconocida: {op}")
#     return [TextContent(type="text", text=str(result))]

# ============================================================
# SECCIÓN C — Endpoint SSE (GET /sse)
# Este endpoint abre la conexión SSE persistente
# El cliente se conecta aquí y recibe responses/notifications
# Descomenta las siguientes líneas:
# ============================================================
# async def handle_sse(request: Request):
#     sys.stderr.write(f"Nueva conexión SSE desde {request.client}\n")
#     async with sse_transport.connect_sse(
#         request.scope, request.receive, request._send
#     ) as (read_stream, write_stream):
#         await mcp_server.run(
#             read_stream,
#             write_stream,
#             mcp_server.create_initialization_options(),
#         )

# ============================================================
# SECCIÓN D — Health check y aplicación Starlette
# Descomenta las siguientes líneas:
# ============================================================
# async def health(request: Request) -> JSONResponse:
#     return JSONResponse({"status": "ok"})
#
#
# app = Starlette(
#     routes=[
#         Route("/health", endpoint=health),
#         Route("/sse", endpoint=handle_sse),
#         Mount("/message", app=sse_transport.handle_post_message),
#     ]
# )

# ============================================================
# SECCIÓN E — Arranque del servidor con uvicorn
# Descomenta las siguientes líneas:
# ============================================================
# if __name__ == "__main__":
#     sys.stderr.write("Servidor SSE iniciando en http://0.0.0.0:8000\n")
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
