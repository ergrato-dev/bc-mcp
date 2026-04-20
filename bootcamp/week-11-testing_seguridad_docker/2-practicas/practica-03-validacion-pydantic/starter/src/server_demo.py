"""
server_demo.py — Server de demo que muestra integración de Pydantic en tools.

Pasos a descomentar:
  PASO 3: tool add_book_validated con AddBookInput
  PASO 4: tool search_books_validated con SearchBooksInput y manejo de errores
"""
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo-validation-server")

# Base de datos en memoria para el demo
_books: dict[int, dict] = {}
_next_id: int = 1


def _make_error(code: str, message: str) -> str:
    """Retorna un error como JSON string."""
    return json.dumps({"error": code, "message": message})


# ============================================================
# PASO 3: Tool con validación Pydantic — add_book_validated
# ============================================================
# Esta tool usa AddBookInput para validar antes de guardar.
# Si los datos no son válidos, retorna un error descriptivo.
#
# Descomenta las siguientes líneas:
# from .validators import AddBookInput
# from pydantic import ValidationError
#
# @mcp.tool()
# async def add_book_validated(
#     title: str, author: str, year: int, isbn: str = ""
# ) -> str:
#     """
#     Agrega un libro a la colección con validación completa de inputs.
#
#     Args:
#         title: Título del libro (1-300 caracteres)
#         author: Autor del libro (1-200 caracteres)
#         year: Año de publicación (1000-2100)
#         isbn: ISBN opcional (solo dígitos, X y guiones)
#     """
#     global _next_id
#
#     try:
#         # Validar inputs con Pydantic — lanza ValidationError si hay errores
#         data = AddBookInput(title=title, author=author, year=year, isbn=isbn)
#     except ValidationError as e:
#         # Extraer mensajes de error legibles del LLM
#         errors = [f"{err['loc'][0]}: {err['msg']}" for err in e.errors()]
#         return _make_error("validation_error", " | ".join(errors))
#
#     # Guardar el libro validado
#     book_id = _next_id
#     _next_id += 1
#     _books[book_id] = {
#         "id": book_id,
#         "title": data.title,   # ya viene con strip aplicado
#         "author": data.author,
#         "year": data.year,
#         "isbn": data.isbn,
#     }
#     return json.dumps({"success": True, "id": book_id})


# ============================================================
# PASO 4: Tool search_books_validated con manejo de errores
# ============================================================
# Descomenta las siguientes líneas:
# from .validators import SearchBooksInput
#
# @mcp.tool()
# async def search_books_validated(query: str, limit: int = 10) -> str:
#     """
#     Busca libros por título o autor con validación de parámetros.
#
#     Args:
#         query: Texto a buscar (1-500 caracteres)
#         limit: Número máximo de resultados (1-100)
#     """
#     try:
#         params = SearchBooksInput(query=query, limit=limit)
#     except ValidationError as e:
#         errors = [f"{err['loc'][0]}: {err['msg']}" for err in e.errors()]
#         return _make_error("validation_error", " | ".join(errors))
#
#     # Buscar en la base de datos en memoria
#     results = [
#         book for book in _books.values()
#         if params.query in book["title"].lower() or
#            params.query in book["author"].lower()
#     ][:params.limit]
#
#     if not results:
#         return json.dumps({"message": "No books found matching the query"})
#
#     return json.dumps(results)


if __name__ == "__main__":
    mcp.run()
