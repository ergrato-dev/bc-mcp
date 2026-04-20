"""
test_tools.py — Suite de tests de integración para el Library Server (semana 11).

Cada clase de test cubre una tool. Implementa al menos 2 tests por clase.
Objetivo: ≥ 75% de cobertura total.

Ejecutar: uv run pytest -v
Con cobertura: uv run pytest --cov=src --cov-report=term-missing -v
"""
import json
import pytest


# ============================================================
# TODO 1: Tests para add_book
# ============================================================
# Mínimo 2 tests:
# a) add_book con datos válidos retorna {"success": True, "id": <int>}
# b) add_book con título vacío retorna {"error": "validation_error", ...}
#
# Pista:
#   result = await mcp_client.call_tool("add_book", {
#       "title": "Clean Code", "author": "Martin", "year": 2008
#   })
#   data = json.loads(result.content[0].text)
#   assert data["success"] is True
#
# class TestAddBook:
#     ...


# ============================================================
# TODO 2: Tests para search_books
# ============================================================
# Mínimo 2 tests:
# a) search_books encuentra un libro previamente añadido
# b) search_books retorna vacío/mensaje cuando no hay coincidencias
#
# class TestSearchBooks:
#     ...


# ============================================================
# TODO 3: Tests para get_book
# ============================================================
# Mínimo 2 tests:
# a) get_book retorna el libro correcto por ID
# b) get_book retorna error "not_found" para ID inexistente
#
# class TestGetBook:
#     ...


# ============================================================
# TODO 4: Tests para update_book
# ============================================================
# Mínimo 2 tests:
# a) update_book modifica el campo indicado y lo persiste
# b) update_book retorna error para ID inexistente
#
# class TestUpdateBook:
#     ...


# ============================================================
# TODO 5: Tests para delete_book
# ============================================================
# Mínimo 2 tests:
# a) delete_book elimina el libro y retorna success
# b) delete_book retorna error para ID inexistente
#
# class TestDeleteBook:
#     ...
