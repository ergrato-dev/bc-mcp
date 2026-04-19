"""
MCP Server — Práctica 02: Resources en Python
Semana 03 — Los Tres Primitivos

Objetivo: aprender a implementar Resources con URIs,
TextResourceContents, BlobResourceContents y ResourceTemplates.
"""

import asyncio
import base64
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

server = Server("practice-02-resources-python")

# In-memory "database" for practice purposes
PRODUCTS_DB: dict[str, dict] = {
    "1": {"id": 1, "name": "Laptop Pro", "price": 1299.99, "category": "electronics"},
    "2": {"id": 2, "name": "Mechanical Keyboard", "price": 149.50, "category": "electronics"},
    "3": {"id": 3, "name": "Desk Chair", "price": 399.00, "category": "furniture"},
}

APP_SETTINGS = {
    "app_name": "MCP Practice Store",
    "version": "1.0.0",
    "currency": "USD",
    "max_items_per_page": 20
}

PRODUCTS_SCHEMA = {
    "table": "products",
    "columns": [
        {"name": "id", "type": "INTEGER", "primary_key": True},
        {"name": "name", "type": "TEXT", "not_null": True},
        {"name": "price", "type": "REAL", "not_null": True},
        {"name": "category", "type": "TEXT"}
    ]
}


# ============================================================
# SECCIÓN A: Declarar lista de Resources estáticos
# ============================================================
# list_resources retorna todos los resources estáticos disponibles.
# Cada Resource tiene uri, name y mimeType.
# Los Resource Templates se declaran en list_resource_templates.
#
# Descomenta las líneas siguientes:
# @server.list_resources()
# async def list_resources() -> list[types.Resource]:
#     return [
#         types.Resource(
#             uri="config://app/settings",
#             name="Application settings",
#             description="Current application configuration values",
#             mimeType="application/json"
#         ),
#         types.Resource(
#             uri="db://schema/products",
#             name="Products table schema",
#             description="Column definitions and types for the products table",
#             mimeType="application/json"
#         ),
#     ]


# ============================================================
# SECCIÓN B: Implementar read_resource para URIs estáticas
# ============================================================
# read_resource recibe la URI y retorna ReadResourceResult.
# TextResourceContents se usa para datos legibles (JSON, Markdown, texto).
#
# Descomenta las líneas siguientes:
# @server.read_resource()
# async def read_resource(uri: str) -> types.ReadResourceResult:
#     if uri == "config://app/settings":
#         return types.ReadResourceResult(
#             contents=[
#                 types.TextResourceContents(
#                     uri=uri,
#                     text=json.dumps(APP_SETTINGS, indent=2),
#                     mimeType="application/json"
#                 )
#             ]
#         )
#
#     if uri == "db://schema/products":
#         return types.ReadResourceResult(
#             contents=[
#                 types.TextResourceContents(
#                     uri=uri,
#                     text=json.dumps(PRODUCTS_SCHEMA, indent=2),
#                     mimeType="application/json"
#                 )
#             ]
#         )
#
#     raise ValueError(f"Resource not found: {uri}")


# ============================================================
# SECCIÓN C: Resource Templates para URIs dinámicas
# ============================================================
# Un ResourceTemplate tiene un uriTemplate con {variables}.
# El read_resource handler parsea la variable desde la URI recibida.
#
# Descomenta las líneas siguientes y agrégalas a list_resource_templates:
# @server.list_resource_templates()
# async def list_resource_templates() -> list[types.ResourceTemplate]:
#     return [
#         types.ResourceTemplate(
#             uriTemplate="db://products/{product_id}",
#             name="Product by ID",
#             description="Returns data for a specific product by its ID",
#             mimeType="application/json"
#         )
#     ]
#
# También actualiza read_resource para manejar el template:
# Agrega esto ANTES del raise ValueError en read_resource:
#
#     if uri.startswith("db://products/"):
#         product_id = uri.removeprefix("db://products/")
#         product = PRODUCTS_DB.get(product_id)
#         if not product:
#             raise ValueError(f"Product {product_id} not found")
#         return types.ReadResourceResult(
#             contents=[
#                 types.TextResourceContents(
#                     uri=uri,
#                     text=json.dumps(product, indent=2),
#                     mimeType="application/json"
#                 )
#             ]
#         )


# ============================================================
# SECCIÓN D: BlobResourceContents (contenido binario)
# ============================================================
# BlobResourceContents se usa para datos binarios codificados en base64.
# Agrega este resource a list_resources y su handler a read_resource:
#
# En list_resources, agrega:
#     types.Resource(
#         uri="file://logo.png",
#         name="Application logo",
#         description="Logo of the application in PNG format",
#         mimeType="image/png"
#     ),
#
# En read_resource, agrega:
#     if uri == "file://logo.png":
#         # Simulate a tiny 1x1 white pixel PNG
#         png_bytes = bytes([
#             0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
#             0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
#             0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
#             0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
#             0xDE, 0x00, 0x00, 0x00, 0x0C, 0x49, 0x44, 0x41,
#             0x54, 0x08, 0xD7, 0x63, 0xF8, 0xFF, 0xFF, 0x3F,
#             0x00, 0x05, 0xFE, 0x02, 0xFE, 0xDC, 0xCC, 0x59,
#             0xE7, 0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E,
#             0x44, 0xAE, 0x42, 0x60, 0x82
#         ])
#         return types.ReadResourceResult(
#             contents=[
#                 types.BlobResourceContents(
#                     uri=uri,
#                     blob=base64.b64encode(png_bytes).decode("utf-8"),
#                     mimeType="image/png"
#                 )
#             ]
#         )


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
