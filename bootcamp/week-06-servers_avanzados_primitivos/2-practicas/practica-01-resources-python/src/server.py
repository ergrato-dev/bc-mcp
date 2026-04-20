"""
Book catalog MCP server — práctica de Resources en Python.
Semana 06 — Los 3 Primitivos
"""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("book-catalog")

# =============================================
# BASE DE DATOS — catálogo de libros
# =============================================
BOOKS: list[dict] = [
    {
        "isbn": "978-0-13-110362-7",
        "title": "The C Programming Language",
        "author": "Brian Kernighan, Dennis Ritchie",
        "year": 1978,
        "available": True,
    },
    {
        "isbn": "978-0-20-161622-4",
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "year": 1999,
        "available": True,
    },
    {
        "isbn": "978-0-59-651798-1",
        "title": "Python Cookbook",
        "author": "David Beazley, Brian Jones",
        "year": 2013,
        "available": False,
    },
    {
        "isbn": "978-0-13-468599-1",
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": True,
    },
]


# =============================================
# SECCIÓN 1: Resource estático books://all
# =============================================
# Este resource devuelve todos los libros del catálogo.
# El decorador registra la URI "books://all" en resources/list.
# Descomenta las siguientes líneas:
# @mcp.resource("books://all")
# async def all_books() -> str:
#     """Returns all books in the catalog as JSON."""
#     return json.dumps(BOOKS, ensure_ascii=False)


# =============================================
# SECCIÓN 2: Resource estático books://available
# =============================================
# Este resource filtra solo los libros disponibles para préstamo.
# Descomenta las siguientes líneas:
# @mcp.resource("books://available")
# async def available_books() -> str:
#     """Returns only available books as JSON."""
#     available = [b for b in BOOKS if b["available"]]
#     return json.dumps(available, ensure_ascii=False)


# =============================================
# SECCIÓN 3: Resource template books://{isbn}
# =============================================
# El parámetro {isbn} en la URI se extrae y pasa a la función.
# FastMCP automáticamente registra esto como un resourceTemplate.
# Descomenta las siguientes líneas:
# @mcp.resource("books://{isbn}")
# async def book_by_isbn(isbn: str) -> str:
#     """Returns a specific book by ISBN."""
#     book = next((b for b in BOOKS if b["isbn"] == isbn), None)
#     if book is None:
#         return json.dumps({"error": f"Book with ISBN {isbn!r} not found"})
#     return json.dumps(book, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run()
