"""MCP Library Server — Proyecto Final.

Sistema MCP completo con 7 tools para gestión de biblioteca
e integración con OpenLibrary API externa.

Transport: HTTP + SSE (producción)
"""

import sqlite3
from pathlib import Path

import httpx
from mcp.server.fastmcp import FastMCP

# ============================================
# TODO 1: Leer configuración desde variables de entorno
# ============================================
# Importa y usa la clase Settings de config.py
# para leer DB_PATH, OPENLIBRARY_URL, MAX_SEARCH_RESULTS
#
# from src.config import Settings
# settings = Settings()
# DB_PATH = settings.db_path
# OPENLIBRARY_URL = settings.openlibrary_url
# MAX_SEARCH_RESULTS = settings.max_search_results

# Valores por defecto (para desarrollo sin .env):
DB_PATH = "./library.db"
OPENLIBRARY_URL = "https://openlibrary.org"
MAX_SEARCH_RESULTS = 20

# ============================================
# TODO 2: Inicializar el servidor MCP
# ============================================
# Crea la instancia FastMCP con nombre descriptivo
# y configura el transporte HTTP + SSE para producción.
#
# mcp = FastMCP("library-server")

# (placeholder temporal para que el archivo sea importable)
mcp = None  # type: ignore[assignment]  # TODO: reemplazar con FastMCP(...)


# ============================================
# Helpers de base de datos
# ============================================

def get_db_connection() -> sqlite3.Connection:
    """Create and return a database connection with row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Initialize the SQLite database schema."""
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                title   TEXT NOT NULL,
                author  TEXT NOT NULL,
                year    INTEGER NOT NULL,
                isbn    TEXT,
                cover   TEXT
            )
        """)
        conn.commit()


# ============================================
# TODO 3: Implementar tool search_books
# ============================================
# Busca libros en la BD por título o autor (LIKE, case-insensitive).
# Parámetros: query: str, limit: int = 10
# Retorna: list[dict] con los libros encontrados
# Validar inputs con SearchBooksInput de validators.py
#
# @mcp.tool()
# async def search_books(query: str, limit: int = 10) -> list[dict]:
#     """Search books by title or author."""
#     # TODO: Validar inputs con SearchBooksInput
#     # TODO: Ejecutar query SQL con LIKE en title y author
#     # TODO: Retornar lista de dicts (id, title, author, year, isbn)
#     pass


# ============================================
# TODO 4: Implementar tool get_book
# ============================================
# Obtiene un libro por ID exacto.
# Retorna dict con datos del libro o error si no existe.
#
# @mcp.tool()
# async def get_book(book_id: int) -> dict:
#     """Get a book by ID."""
#     # TODO: Buscar libro por ID en la BD
#     # TODO: Si no existe, retornar {"error": "Book not found", "id": book_id}
#     pass


# ============================================
# TODO 5: Implementar tool add_book
# ============================================
# Añade un nuevo libro a la base de datos.
# Validar inputs con AddBookInput de validators.py.
# Retorna dict con el ID asignado y mensaje de éxito.
#
# @mcp.tool()
# async def add_book(title: str, author: str, year: int) -> dict:
#     """Add a new book to the library."""
#     # TODO: Validar inputs con AddBookInput
#     # TODO: Insertar en la BD y retornar {"id": new_id, "message": "Book added successfully"}
#     pass


# ============================================
# TODO 6: Implementar tool update_book
# ============================================
# Actualiza campos de un libro existente.
# Solo actualiza los campos que se envían (PATCH semántico).
# Validar inputs con UpdateBookInput de validators.py.
#
# @mcp.tool()
# async def update_book(
#     book_id: int,
#     title: str | None = None,
#     author: str | None = None,
#     year: int | None = None,
# ) -> dict:
#     """Update one or more fields of an existing book."""
#     # TODO: Validar inputs con UpdateBookInput
#     # TODO: Si ningún campo se envía, retornar error
#     # TODO: Construir UPDATE dinámico solo con los campos enviados
#     # TODO: Retornar {"message": "Book updated successfully", "id": book_id}
#     pass


# ============================================
# TODO 7: Implementar tool delete_book
# ============================================
# Elimina un libro por ID.
# Retorna error si el libro no existe antes de eliminar.
#
# @mcp.tool()
# async def delete_book(book_id: int) -> dict:
#     """Delete a book from the library."""
#     # TODO: Verificar que el libro existe (usa get_book)
#     # TODO: Eliminar de la BD
#     # TODO: Retornar {"message": "Book deleted", "id": book_id}
#     pass


# ============================================
# TODO 8: Implementar tool search_openlibrary
# ============================================
# Busca libros en OpenLibrary.org (API externa).
# Usa httpx.AsyncClient para la petición.
# URL: {OPENLIBRARY_URL}/search.json?title={title}&limit=5
# Retorna: list[dict] con title, author, year de los resultados
#
# @mcp.tool()
# async def search_openlibrary(title: str) -> list[dict]:
#     """Search books in OpenLibrary.org external API."""
#     # TODO: Validar que title no esté vacío
#     # TODO: Hacer GET a OPENLIBRARY_URL/search.json?title=...&limit=5
#     # TODO: Parsear docs de la respuesta JSON
#     # TODO: Retornar lista de {title, author_name, first_publish_year}
#     pass


# ============================================
# TODO 9: Implementar tool enrich_book
# ============================================
# Enriquece un libro de la BD con datos de OpenLibrary.
# Busca por título en OpenLibrary y actualiza isbn/cover si los encuentra.
#
# @mcp.tool()
# async def enrich_book(book_id: int) -> dict:
#     """Enrich a book with data from OpenLibrary API."""
#     # TODO: Obtener el libro de la BD con get_book
#     # TODO: Buscar en OpenLibrary por título
#     # TODO: Si hay resultados, actualizar isbn y cover en la BD
#     # TODO: Retornar {"message": "Book enriched", "book_id": book_id, "isbn": ..., "cover": ...}
#     pass


# ============================================
# TODO 10: Punto de entrada del servidor
# ============================================
# Inicializa la BD y arranca el server con transporte HTTP+SSE.
# Puerto: 8000, host: 0.0.0.0 (para Docker)
#
# if __name__ == "__main__":
#     init_db()
#     # Para desarrollo local (stdio):
#     # mcp.run()
#     # Para producción (HTTP+SSE en Docker):
#     mcp.run(transport="sse", host="0.0.0.0", port=8000)
