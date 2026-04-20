"""
validators.py — Modelos Pydantic v2 para validar inputs de tools MCP.

Pasos a descomentar:
  PASO 1: AddBookInput
  PASO 2: SearchBooksInput
  PASO 3: UpdateBookInput
"""

# ============================================================
# PASO 1: Modelo AddBookInput
# ============================================================
# Este modelo valida los parámetros de la tool add_book.
# Pydantic v2 usa Field() para definir límites de forma declarativa.
#
# Descomenta las siguientes líneas:
# from pydantic import BaseModel, Field, field_validator
#
# class AddBookInput(BaseModel):
#     """Valida los datos de un libro antes de guardarlo en DB."""
#
#     title: str = Field(min_length=1, max_length=300)
#     author: str = Field(min_length=1, max_length=200)
#     year: int = Field(ge=1000, le=2100)
#     isbn: str = Field(default="", max_length=20, pattern=r"^[0-9X\-]*$")
#
#     @field_validator("title", "author", mode="before")
#     @classmethod
#     def strip_whitespace(cls, v: str) -> str:
#         """Eliminar espacios al inicio y final del valor."""
#         return v.strip()


# ============================================================
# PASO 2: Modelo SearchBooksInput
# ============================================================
# Limita el tamaño del query y el número máximo de resultados.
# max_length=500 previene queries que indiquen DoS o prompt injection.
#
# Descomenta las siguientes líneas:
# class SearchBooksInput(BaseModel):
#     """Valida los parámetros de búsqueda."""
#
#     query: str = Field(min_length=1, max_length=500)
#     limit: int = Field(default=10, ge=1, le=100)
#
#     @field_validator("query", mode="before")
#     @classmethod
#     def clean_query(cls, v: str) -> str:
#         """Normalizar query: strip y lower."""
#         return v.strip().lower()


# ============================================================
# PASO 3: Modelo UpdateBookInput
# ============================================================
# Todos los campos son opcionales — solo se actualizan los que se envíen.
# Pydantic maneja esto con Optional y None como default.
#
# Descomenta las siguientes líneas:
# from typing import Optional
#
# class UpdateBookInput(BaseModel):
#     """Valida los datos de actualización de un libro."""
#
#     book_id: int = Field(ge=1)
#     title: Optional[str] = Field(default=None, min_length=1, max_length=300)
#     author: Optional[str] = Field(default=None, min_length=1, max_length=200)
#     year: Optional[int] = Field(default=None, ge=1000, le=2100)
#     isbn: Optional[str] = Field(
#         default=None, max_length=20, pattern=r"^[0-9X\-]*$"
#     )
#
#     @field_validator("title", "author", mode="before")
#     @classmethod
#     def strip_if_provided(cls, v: Optional[str]) -> Optional[str]:
#         """Strip solo si el valor fue proporcionado."""
#         if v is not None:
#             return v.strip()
#         return v
#
#     def has_updates(self) -> bool:
#         """Retorna True si al menos un campo fue proporcionado."""
#         return any([self.title, self.author, self.year, self.isbn])
