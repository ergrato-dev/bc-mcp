"""
test_library_server.py — Suite de tests para el Library Server (semana 07).

Cada clase agrupa tests de una tool específica.
Pasos a descomentar:
  PASO 3: tests de add_book (3 casos)
  PASO 4: tests de search_books y delete_book (4 casos)
  PASO 5: tests de update_book (2 casos)
"""
import json
import pytest


# ============================================================
# PASO 3: Tests para la tool add_book
# ============================================================
# Descomenta la siguiente clase completa:
# class TestAddBook:
#     """Tests de la tool add_book."""
#
#     async def test_add_book_success(self, mcp_client):
#         """add_book debe retornar un ID numérico positivo."""
#         result = await mcp_client.call_tool("add_book", {
#             "title": "Clean Code",
#             "author": "Robert C. Martin",
#             "year": 2008,
#         })
#         data = json.loads(result.content[0].text)
#         # Verificar estructura de la respuesta
#         assert data.get("success") is True
#         assert isinstance(data.get("id"), int)
#         assert data["id"] > 0
#
#     async def test_add_book_makes_retrievable(self, mcp_client):
#         """Un libro añadido debe ser recuperable con get_book."""
#         # Arrange — añadir
#         add_result = await mcp_client.call_tool("add_book", {
#             "title": "Dune",
#             "author": "Frank Herbert",
#             "year": 1965,
#         })
#         book_id = json.loads(add_result.content[0].text)["id"]
#
#         # Act — recuperar
#         get_result = await mcp_client.call_tool("get_book", {"book_id": book_id})
#         book = json.loads(get_result.content[0].text)
#
#         # Assert — datos correctos
#         assert book["title"] == "Dune"
#         assert book["author"] == "Frank Herbert"
#         assert book["year"] == 1965
#
#     async def test_add_book_multiple(self, mcp_client):
#         """Múltiples libros deben tener IDs distintos."""
#         ids = set()
#         for i in range(3):
#             result = await mcp_client.call_tool("add_book", {
#                 "title": f"Book {i}",
#                 "author": "Author",
#                 "year": 2020 + i,
#             })
#             book_id = json.loads(result.content[0].text)["id"]
#             ids.add(book_id)
#         assert len(ids) == 3  # IDs únicos


# ============================================================
# PASO 4: Tests para search_books y delete_book
# ============================================================
# Descomenta las siguientes clases:
# class TestSearchBooks:
#     """Tests de la tool search_books."""
#
#     async def test_search_finds_added_book(self, mcp_client):
#         """search_books debe encontrar un libro previamente añadido."""
#         # Arrange — añadir libro con título distintivo
#         await mcp_client.call_tool("add_book", {
#             "title": "Python Moderno 2025",
#             "author": "Guido",
#             "year": 2025,
#         })
#
#         # Act — buscar por parte del título
#         result = await mcp_client.call_tool("search_books", {"query": "Python"})
#         books = json.loads(result.content[0].text)
#
#         # Assert
#         assert isinstance(books, list)
#         assert len(books) >= 1
#         assert any("Python" in b["title"] for b in books)
#
#     async def test_search_no_results(self, mcp_client):
#         """Una búsqueda sin resultados debe retornar lista vacía o mensaje."""
#         result = await mcp_client.call_tool("search_books", {"query": "xyzzy_nonexistent"})
#         data = json.loads(result.content[0].text)
#         # Aceptar lista vacía O dict con "message"
#         assert isinstance(data, list) and len(data) == 0 or \
#                isinstance(data, dict) and "message" in data
#
#
# class TestDeleteBook:
#     """Tests de la tool delete_book."""
#
#     async def test_delete_existing_book(self, mcp_client):
#         """delete_book debe confirmar la eliminación con success=True."""
#         # Arrange
#         add_result = await mcp_client.call_tool("add_book", {
#             "title": "To Delete",
#             "author": "Temp",
#             "year": 2024,
#         })
#         book_id = json.loads(add_result.content[0].text)["id"]
#
#         # Act
#         del_result = await mcp_client.call_tool("delete_book", {"book_id": book_id})
#         data = json.loads(del_result.content[0].text)
#
#         # Assert
#         assert data.get("success") is True
#
#     async def test_delete_nonexistent_book(self, mcp_client):
#         """delete_book con ID inexistente debe retornar error."""
#         result = await mcp_client.call_tool("delete_book", {"book_id": 99999})
#         data = json.loads(result.content[0].text)
#         assert "error" in data


# ============================================================
# PASO 5: Tests para update_book
# ============================================================
# Descomenta la siguiente clase:
# class TestUpdateBook:
#     """Tests de la tool update_book."""
#
#     async def test_update_title(self, mcp_client):
#         """update_book debe modificar solo el campo indicado."""
#         # Arrange
#         add_result = await mcp_client.call_tool("add_book", {
#             "title": "Old Title",
#             "author": "Author",
#             "year": 2020,
#         })
#         book_id = json.loads(add_result.content[0].text)["id"]
#
#         # Act
#         await mcp_client.call_tool("update_book", {
#             "book_id": book_id,
#             "title": "New Title",
#         })
#
#         # Assert — verificar con get_book
#         get_result = await mcp_client.call_tool("get_book", {"book_id": book_id})
#         book = json.loads(get_result.content[0].text)
#         assert book["title"] == "New Title"
#         assert book["author"] == "Author"  # no cambió
#
#     async def test_update_nonexistent_book(self, mcp_client):
#         """update_book con ID inexistente debe retornar error."""
#         result = await mcp_client.call_tool("update_book", {
#             "book_id": 99999,
#             "title": "Ghost",
#         })
#         data = json.loads(result.content[0].text)
#         assert "error" in data
