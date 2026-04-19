# ============================================================
# SECCIÓN A — Importaciones y setup del servidor
# Descomenta las siguientes líneas:
# ============================================================
# import asyncio
# import sys
# from mcp.server import Server
# from mcp.server.stdio import stdio_server
# from mcp.types import Tool, TextContent
#
# server = Server("calculadora-stdio")

# ============================================================
# SECCIÓN B — Handler list_tools
# Este handler responde al mensaje tools/list
# Descomenta las siguientes líneas:
# ============================================================
# @server.list_tools()
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

# ============================================================
# SECCIÓN C — Handler call_tool
# Este handler responde al mensaje tools/call
# IMPORTANTE: usa sys.stderr.write() para logs, nunca print()
# Descomenta las siguientes líneas:
# ============================================================
# @server.call_tool()
# async def call_tool(name: str, arguments: dict) -> list[TextContent]:
#     if name != "calculate":
#         raise ValueError(f"Tool desconocido: {name}")
#
#     a: float = arguments["a"]
#     b: float = arguments["b"]
#     op: str = arguments["op"]
#
#     # Logging correcto — stderr no interfiere con stdio
#     sys.stderr.write(f"[calculate] a={a} b={b} op={op}\n")
#
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
#
#     return [TextContent(type="text", text=str(result))]

# ============================================================
# SECCIÓN D — Función main y punto de entrada
# Descomenta las siguientes líneas:
# ============================================================
# async def main() -> None:
#     async with stdio_server() as (read_stream, write_stream):
#         await server.run(
#             read_stream,
#             write_stream,
#             server.create_initialization_options(),
#         )
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
