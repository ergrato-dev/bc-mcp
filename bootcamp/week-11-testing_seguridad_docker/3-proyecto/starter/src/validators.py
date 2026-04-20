"""
validators.py — Modelos Pydantic v2 para validar inputs del Library Server.

Implementa los tres modelos siguientes para proteger todas las tools.
"""
from pydantic import BaseModel, Field, field_validator
from typing import Optional


# ============================================================
# TODO 1: Modelo AddBookInput
# ============================================================
# Implementa la validación de datos para añadir un libro.
# Requisitos:
#   - title: str, 1-300 chars, strip de espacios en before validator
#   - author: str, 1-200 chars, strip de espacios en before validator
#   - year: int, entre 1000 y 2100
#   - isbn: str opcional, máx 20 chars, solo dígitos/X/guiones
#   - notes: str opcional, máx 1000 chars
#
# class AddBookInput(BaseModel):
#     ...


# ============================================================
# TODO 2: Modelo SearchBooksInput
# ============================================================
# Implementa la validación de parámetros de búsqueda.
# Requisitos:
#   - query: str, 1-500 chars, strip + lower en before validator
#   - limit: int, entre 1 y 100, default=10
#
# class SearchBooksInput(BaseModel):
#     ...


# ============================================================
# TODO 3: Modelo UpdateBookInput
# ============================================================
# Implementa la validación de datos para actualizar un libro.
# Todos los campos son opcionales EXCEPTO book_id.
# Requisitos:
#   - book_id: int, mayor que 0
#   - title: Optional[str], 1-300 chars si se provee
#   - author: Optional[str], 1-200 chars si se provee
#   - year: Optional[int], entre 1000 y 2100 si se provee
#   - notes: Optional[str], máx 1000 chars si se provee
#   - Método has_updates() → bool: True si al menos un campo tiene valor
#
# class UpdateBookInput(BaseModel):
#     ...
