"""
Práctica 03 — Invocar Tools y Procesar Resultados

Goal: Call call_tool(), parse TextContent as JSON, handle isError=True,
and read a resource with read_resource().

Instructions: uncomment each section labeled PASO 1–5 in order.
Run with: uv run python client.py
"""

import asyncio
import json
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

SERVER_PATH = "../../../../week-07-mcp_server_avanzado/3-proyecto/solution/src/server.py"


async def main() -> None:

    # ============================================================
    # PASO 1: Conectar al server
    # ============================================================
    # Uncomment the following lines:
    # params = StdioServerParameters(
    #     command="python",
    #     args=[SERVER_PATH],
    #     env={**os.environ, "DB_PATH": "./data/library.db"},
    # )
    # async with stdio_client(params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()

    # ============================================================
    # PASO 2: Buscar libros — call_tool + TextContent + JSON
    # ============================================================
    # call_tool() returns a CallToolResult:
    #   result.content → list[TextContent | ImageContent | EmbeddedResource]
    #   result.isError → bool
    #
    # The search_books tool returns a JSON string inside TextContent.
    # We parse it with json.loads() to get a list of dicts.
    #
    # Uncomment the following lines:
    #         print("\n=== PASO 2: Buscar libros ===")
    #         query = "async"
    #         print(f'Buscando: "{query}"')
    #         result = await session.call_tool("search_books", {"query": query})
    #
    #         if result.isError:
    #             print(f"Error: {result.content[0].text}")
    #         else:
    #             books = json.loads(result.content[0].text)
    #             if books:
    #                 for book in books:
    #                     print(f"  [{book['id']}] {book['title']} — {book['author']} ({book['year']})")
    #             else:
    #                 print("  Sin resultados")

    # ============================================================
    # PASO 3: Manejar isError — get_book con ID inexistente
    # ============================================================
    # When a tool encounters a domain error (book not found, invalid ID,
    # etc.) it returns isError=True with the error message in content[0].text.
    #
    # KEY POINT: isError=True is NOT a Python exception — the code continues
    # normally. Only McpError (wrong tool name, wrong params) raises an
    # exception.
    #
    # Uncomment the following lines:
    #         print("\n=== PASO 3: Manejo de isError ===")
    #         bad_id = 9999
    #         print(f"Buscando libro con ID={bad_id}...")
    #         result_bad = await session.call_tool("get_book", {"book_id": bad_id})
    #
    #         if result_bad.isError:
    #             error_msg = result_bad.content[0].text if result_bad.content else "Unknown"
    #             print(f"✓ Error manejado: {error_msg}")
    #         else:
    #             book = json.loads(result_bad.content[0].text)
    #             print(f"Libro: {book['title']}")

    # ============================================================
    # PASO 4: Agregar un libro — call_tool con múltiples parámetros
    # ============================================================
    # add_book() creates a new book and returns the created record
    # (with the DB-assigned id) as a JSON string in TextContent.
    #
    # Uncomment the following lines:
    #         print("\n=== PASO 4: Agregar libro ===")
    #         add_result = await session.call_tool(
    #             "add_book",
    #             {
    #                 "title": "Clean Code",
    #                 "author": "Robert C. Martin",
    #                 "year": 2008,
    #                 "isbn": "9780132350884",
    #             },
    #         )
    #
    #         if add_result.isError:
    #             print(f"Error al agregar: {add_result.content[0].text}")
    #         else:
    #             new_book = json.loads(add_result.content[0].text)
    #             print(f"Libro agregado: ID={new_book['id']}, {new_book['title']} — {new_book['author']} ({new_book['year']})")

    # ============================================================
    # PASO 5: Leer un resource — read_resource(uri)
    # ============================================================
    # read_resource() fetches a resource by its URI. Returns
    # ReadResourceResult with a list of TextResourceContents or
    # BlobResourceContents. Access the text with .contents[0].text
    #
    # Uncomment the following lines:
    #         print("\n=== PASO 5: Leer resource ===")
    #         resource_result = await session.read_resource("db://books/stats")
    #         raw_stats = resource_result.contents[0].text
    #         stats = json.loads(raw_stats)
    #         print(f"Total libros: {stats.get('total_books', '?')}")
    #         print(f"Con ISBN:     {stats.get('books_with_isbn', '?')}")
    #         print(f"Año promedio: {stats.get('avg_year', '?')}")


if __name__ == "__main__":
    asyncio.run(main())
