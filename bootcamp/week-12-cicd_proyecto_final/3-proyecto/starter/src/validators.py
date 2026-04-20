"""Pydantic validators for MCP Library Server input validation."""

from pydantic import BaseModel, Field, field_validator


# ============================================
# TODO 1: Implementar AddBookInput
# ============================================
# Schema para validar los parámetros del tool add_book.
# Requisitos:
# - title: str, no vacío, máximo 200 caracteres
# - author: str, no vacío, máximo 150 caracteres
# - year: int, entre 1000 y 2100
# Ejemplo de uso:
#   validated = AddBookInput(title="Ficciones", author="Borges", year=1944)
#
# class AddBookInput(BaseModel):
#     title: str = Field(..., min_length=1, max_length=200, description="Book title")
#     author: str = Field(..., min_length=1, max_length=150, description="Author name")
#     year: int = Field(..., ge=1000, le=2100, description="Publication year")
#
#     @field_validator("title", "author", mode="before")
#     @classmethod
#     def strip_whitespace(cls, v: str) -> str:
#         """Remove leading/trailing whitespace from string fields."""
#         return v.strip()


# ============================================
# TODO 2: Implementar SearchBooksInput
# ============================================
# Schema para validar los parámetros del tool search_books.
# Requisitos:
# - query: str, no vacío, máximo 100 caracteres
# - limit: int, entre 1 y 100, valor por defecto 10
#
# class SearchBooksInput(BaseModel):
#     query: str = Field(..., min_length=1, max_length=100, description="Search query")
#     limit: int = Field(default=10, ge=1, le=100, description="Max results to return")
#
#     @field_validator("query", mode="before")
#     @classmethod
#     def strip_whitespace(cls, v: str) -> str:
#         return v.strip()


# ============================================
# TODO 3: Implementar UpdateBookInput
# ============================================
# Schema para validar los parámetros del tool update_book.
# Requisitos:
# - Todos los campos opcionales (solo se actualiza lo que se envía)
# - title: str opcional, máximo 200 caracteres
# - author: str opcional, máximo 150 caracteres
# - year: int opcional, entre 1000 y 2100
# - Validar que al menos un campo esté presente
#
# class UpdateBookInput(BaseModel):
#     title: str | None = Field(default=None, max_length=200)
#     author: str | None = Field(default=None, max_length=150)
#     year: int | None = Field(default=None, ge=1000, le=2100)
#
#     @field_validator("title", "author", mode="before")
#     @classmethod
#     def strip_whitespace(cls, v: str | None) -> str | None:
#         return v.strip() if v is not None else None
#
#     def has_updates(self) -> bool:
#         """Return True if at least one field has a value to update."""
#         return any(v is not None for v in [self.title, self.author, self.year])
