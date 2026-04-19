"""
MCP Server — Práctica 01: Tools en Python
Semana 03 — Los Tres Primitivos

Objetivo: aprender a implementar Tools con inputSchema,
manejo de errores (isError) y annotations.
"""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

server = Server("practice-01-tools-python")


# ============================================================
# SECCIÓN A: Declarar la lista de Tools (list_tools)
# ============================================================
# Un Tool necesita: name, description e inputSchema.
# El inputSchema es un JSON Schema que valida los argumentos
# que envía el LLM antes de ejecutar el tool.
#
# Descomenta las líneas siguientes:
# @server.list_tools()
# async def list_tools() -> list[types.Tool]:
#     return [
#         types.Tool(
#             name="calculate_discount",
#             description="Calculates the final price after applying a percentage discount. "
#                         "Use this when the user asks for a discounted price.",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "price": {
#                         "type": "number",
#                         "description": "Original price (must be positive)",
#                         "minimum": 0
#                     },
#                     "discount_percent": {
#                         "type": "number",
#                         "description": "Discount percentage (0-100)",
#                         "minimum": 0,
#                         "maximum": 100
#                     }
#                 },
#                 "required": ["price", "discount_percent"],
#                 "additionalProperties": False
#             }
#         )
#     ]


# ============================================================
# SECCIÓN B: Implementar el handler (call_tool)
# ============================================================
# call_tool recibe el nombre del tool y los argumentos.
# Retorna una lista de TextContent, ImageContent o EmbeddedResource.
#
# Descomenta las líneas siguientes:
# @server.call_tool()
# async def call_tool(
#     name: str,
#     arguments: dict
# ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
#     if name == "calculate_discount":
#         price = arguments.get("price", 0)
#         discount_percent = arguments.get("discount_percent", 0)
#
#         discount_amount = price * (discount_percent / 100)
#         final_price = price - discount_amount
#
#         result = (
#             f"Precio original: ${price:.2f}\n"
#             f"Descuento ({discount_percent}%): ${discount_amount:.2f}\n"
#             f"Precio final: ${final_price:.2f}"
#         )
#         return [types.TextContent(type="text", text=result)]
#
#     raise ValueError(f"Unknown tool: {name}")


# ============================================================
# SECCIÓN C: Manejo de errores con isError
# ============================================================
# isError=True indica al LLM que el tool falló a nivel de negocio.
# NO es un error técnico del servidor (eso usaría raise/excepción).
#
# Reemplaza el call_tool de la Sección B por esta versión
# que valida el rango del descuento y retorna isError:
#
# @server.call_tool()
# async def call_tool(
#     name: str,
#     arguments: dict
# ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
#     if name == "calculate_discount":
#         price = arguments.get("price", 0)
#         discount_percent = arguments.get("discount_percent", 0)
#
#         # Validate business rules beyond what inputSchema enforces
#         if price <= 0:
#             return types.CallToolResult(
#                 content=[types.TextContent(type="text", text="Error: price must be greater than 0")],
#                 isError=True
#             )
#         if not (0 <= discount_percent <= 100):
#             return types.CallToolResult(
#                 content=[types.TextContent(type="text", text="Error: discount_percent must be between 0 and 100")],
#                 isError=True
#             )
#
#         discount_amount = price * (discount_percent / 100)
#         final_price = price - discount_amount
#
#         result = (
#             f"Precio original: ${price:.2f}\n"
#             f"Descuento ({discount_percent}%): ${discount_amount:.2f}\n"
#             f"Precio final: ${final_price:.2f}"
#         )
#         return [types.TextContent(type="text", text=result)]
#
#     raise ValueError(f"Unknown tool: {name}")


# ============================================================
# SECCIÓN D: Agregar annotations al Tool
# ============================================================
# Las annotations son metadatos que indican al cliente MCP
# cómo es el tool: ¿solo lectura? ¿destructivo? ¿idempotente?
#
# Reemplaza la definición del Tool en list_tools por esta versión:
#
# types.Tool(
#     name="calculate_discount",
#     description="Calculates the final price after applying a discount",
#     inputSchema={ ... },  # igual que antes
#     annotations=types.ToolAnnotations(
#         title="Calcular descuento",
#         readOnlyHint=True,       # No modifica ningún estado
#         idempotentHint=True,     # Mismos inputs → mismo output siempre
#         destructiveHint=False    # No elimina ni daña datos
#     )
# )


# ============================================================
# Punto de entrada del servidor MCP
# ============================================================
async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
