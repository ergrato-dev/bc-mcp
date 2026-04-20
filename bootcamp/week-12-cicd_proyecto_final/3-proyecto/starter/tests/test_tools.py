"""Tests for MCP Library Server tools.

Valida que cada tool retorna el resultado esperado
usando sesiones MCP en memoria (sin Docker ni red).
"""

import pytest


# ============================================
# TODO 1: Implementar tests para add_book y search_books
# ============================================
# class TestBookCRUD:
#
#     async def test_add_book_returns_id(self, mcp_client):
#         """add_book should return a dict with an integer 'id'."""
#         # TODO: Llamar a mcp_client.call_tool("add_book", {...})
#         # TODO: Parsear el resultado (JSON en content[0].text)
#         # TODO: Verificar que result["id"] es un entero > 0
#         pass
#
#     async def test_search_books_finds_added_book(self, mcp_client):
#         """search_books should find a book that was previously added."""
#         # TODO: Añadir un libro con add_book
#         # TODO: Buscar por su título con search_books
#         # TODO: Verificar que aparece en los resultados
#         pass
#
#     async def test_search_books_returns_empty_on_no_match(self, mcp_client):
#         """search_books should return empty list when nothing matches."""
#         # TODO: Buscar con query="xyz_no_existe_abc"
#         # TODO: Verificar que la lista de resultados está vacía
#         pass


# ============================================
# TODO 2: Implementar tests para get_book y update_book
# ============================================
# class TestBookReadUpdate:
#
#     async def test_get_book_returns_correct_data(self, mcp_client):
#         """get_book should return the exact book data."""
#         # TODO: Añadir libro, obtener su ID
#         # TODO: Llamar get_book con ese ID
#         # TODO: Verificar title, author, year
#         pass
#
#     async def test_get_book_not_found(self, mcp_client):
#         """get_book with invalid ID should return error dict."""
#         # TODO: Llamar get_book con id=99999
#         # TODO: Verificar que result contiene "error"
#         pass
#
#     async def test_update_book_changes_title(self, mcp_client):
#         """update_book should persist the new title."""
#         # TODO: Añadir libro
#         # TODO: Actualizar solo el título
#         # TODO: Llamar get_book y verificar nuevo título
#         pass


# ============================================
# TODO 3: Implementar tests para delete_book
# ============================================
# class TestBookDelete:
#
#     async def test_delete_existing_book(self, mcp_client):
#         """delete_book should remove the book from the database."""
#         # TODO: Añadir libro, obtener su ID
#         # TODO: Eliminar con delete_book
#         # TODO: Verificar que get_book ya no lo encuentra
#         pass
#
#     async def test_delete_nonexistent_book_returns_error(self, mcp_client):
#         """delete_book with invalid ID should return error dict."""
#         # TODO: Llamar delete_book con id=99999
#         # TODO: Verificar que el resultado contiene "error"
#         pass


# ============================================
# TODO 4: Test de lista de tools disponibles
# ============================================
# async def test_list_tools_contains_all_expected(mcp_client):
#     """Server should expose all 7 expected tools."""
#     # TODO: Llamar mcp_client.list_tools()
#     # TODO: Extraer nombres de tools
#     # TODO: Verificar que contiene los 7 tools:
#     #   search_books, get_book, add_book, update_book,
#     #   delete_book, search_openlibrary, enrich_book
#     pass
