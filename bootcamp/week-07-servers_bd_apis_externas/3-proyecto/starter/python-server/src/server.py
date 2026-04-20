"""
Library Manager — MCP Server (Python)
Semana 07 — Proyecto Integrador

Combina:
  - SQLite local (aiosqlite) para la biblioteca personal
  - Open Library API (openlibrary.org) para busqueda y enrichment de metadata

Tools a implementar:
  SQLite CRUD:    search_books, get_book, add_book, update_book, delete_book
  External API:   search_openlibrary, enrich_book
"""
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Context
import aiosqlite
import httpx
import json
import os
import pathlib

load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DB_PATH = os.environ.get("DB_PATH", "./data/library.db")
OPENLIBRARY_URL = os.environ.get(
    "OPENLIBRARY_URL", "https://openlibrary.org/search.json"
)
MAX_SEARCH_RESULTS = int(os.environ.get("MAX_SEARCH_RESULTS", "10"))

pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Lifespan — shared SQLite connection + HTTP client
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(server: FastMCP):
    """
    Setup: open shared database connection and HTTP client.
    Teardown: both close automatically via async context managers.
    """
    async with (
        aiosqlite.connect(DB_PATH) as db,
        httpx.AsyncClient(timeout=15.0) as http,
    ):
        db.row_factory = aiosqlite.Row
        await _init_schema(db)
        yield {"db": db, "http": http}


async def _init_schema(db: aiosqlite.Connection) -> None:
    """Initialize database schema. Safe to run multiple times."""
    await db.executescript("""
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT    NOT NULL,
            author TEXT    NOT NULL,
            year   INTEGER,
            isbn   TEXT,
            notes  TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_books_title  ON books(title);
        CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
    """)
    await db.commit()


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP("library-manager", lifespan=lifespan)


# ============================================
# TOOL: search_books
# Busca libros en la BD local por titulo o autor
# ============================================

@mcp.tool()
async def search_books(query: str, ctx: Context) -> str:
    """Search local library by title or author.

    Args:
        query: Text to search in title or author fields

    Returns:
        JSON array of matching books
    """
    # TODO: Implementar busqueda en la BD local
    # 1. Obtener db de ctx.request_context.lifespan_context["db"]
    # 2. Ejecutar SELECT con LIKE en titulo y autor
    # 3. Retornar JSON array con los resultados (dict de cada row)
    # 4. Si no hay resultados, retornar {"message": "No books found for: {query}"}
    pass


# ============================================
# TOOL: get_book
# Retorna un libro por su ID
# ============================================

@mcp.tool()
async def get_book(book_id: int, ctx: Context) -> str:
    """Get a single book by ID from local library.

    Args:
        book_id: Integer ID of the book

    Returns:
        JSON object with full book details, or error if not found
    """
    # TODO: Implementar get por ID
    # 1. SELECT * FROM books WHERE id = ?
    # 2. Si row is None: retornar JSON con error "not_found"
    # 3. Si existe: retornar JSON con dict(row)
    pass


# ============================================
# TOOL: add_book
# Agrega un nuevo libro a la biblioteca
# ============================================

@mcp.tool()
async def add_book(
    title: str,
    author: str,
    year: int,
    isbn: str = "",
    notes: str = "",
    ctx: Context = None,
) -> str:
    """Add a new book to the local library.

    Args:
        title: Book title (required)
        author: Author name (required)
        year: Publication year (required)
        isbn: ISBN-13 or ISBN-10 (optional)
        notes: Personal notes about the book (optional)

    Returns:
        JSON with new book ID on success, or error on failure
    """
    # TODO: Implementar INSERT
    # 1. INSERT INTO books (title, author, year, isbn, notes) VALUES (?, ?, ?, ?, ?)
    # 2. await db.commit()
    # 3. Retornar JSON con {"success": True, "id": cursor.lastrowid}
    # 4. Capturar aiosqlite.IntegrityError para duplicados
    pass


# ============================================
# TOOL: update_book
# Actualiza campos de un libro existente
# ============================================

@mcp.tool()
async def update_book(
    book_id: int,
    title: str = "",
    author: str = "",
    year: int = 0,
    notes: str = "",
    ctx: Context = None,
) -> str:
    """Update one or more fields of an existing book.

    Only updates fields that are provided (non-empty/non-zero).

    Args:
        book_id: ID of the book to update
        title: New title (optional)
        author: New author (optional)
        year: New year (optional, 0 = no change)
        notes: New notes (optional)

    Returns:
        JSON with updated book on success, or error if not found
    """
    # TODO: Implementar UPDATE dinamico
    # 1. Construir SET clause solo con campos no vacios
    #    Ejemplo: fields = {}
    #             if title: fields["title"] = title
    #             if author: fields["author"] = author
    #             if year: fields["year"] = year
    #             if notes: fields["notes"] = notes
    # 2. Si fields esta vacio: retornar error "nothing_to_update"
    # 3. UPDATE books SET campo1=?, campo2=? WHERE id=?
    # 4. Si cursor.rowcount == 0: retornar error "not_found"
    # 5. Retornar el libro actualizado con get_book(book_id)
    pass


# ============================================
# TOOL: delete_book
# Elimina un libro de la biblioteca
# ============================================

@mcp.tool()
async def delete_book(book_id: int, ctx: Context) -> str:
    """Delete a book from the local library.

    Args:
        book_id: ID of the book to delete

    Returns:
        JSON confirming deletion, or error if not found
    """
    # TODO: Implementar DELETE
    # 1. DELETE FROM books WHERE id = ?
    # 2. await db.commit()
    # 3. Si cursor.rowcount == 0: retornar error "not_found"
    # 4. Retornar JSON {"success": True, "deleted_id": book_id}
    pass


# ============================================
# TOOL: search_openlibrary
# Busca libros en la API publica de Open Library
# ============================================

@mcp.tool()
async def search_openlibrary(title: str, ctx: Context) -> str:
    """Search for books using Open Library public API.

    No API key required. Returns rich metadata.

    Args:
        title: Book title to search

    Returns:
        JSON array of matching books from Open Library
    """
    # TODO: Implementar busqueda en Open Library
    # 1. Obtener http de ctx.request_context.lifespan_context["http"]
    # 2. GET https://openlibrary.org/search.json
    #    params: title=title, limit=MAX_SEARCH_RESULTS,
    #            fields=title,author_name,first_publish_year,subject,isbn
    # 3. response.raise_for_status()
    # 4. Mapear data["docs"] a lista de dicts con campos relevantes
    # 5. Capturar httpx.HTTPStatusError y httpx.TimeoutException
    pass


# ============================================
# TOOL: enrich_book
# Combina datos locales con metadata de Open Library
# ============================================

@mcp.tool()
async def enrich_book(book_id: int, ctx: Context) -> str:
    """Enrich a local book with metadata from Open Library.

    Searches Open Library by the book's title and merges the result
    with the local record.

    Args:
        book_id: ID of the local book to enrich

    Returns:
        JSON with local data + Open Library metadata merged
    """
    # TODO: Implementar enrichment
    # 1. Obtener libro local con get_book(book_id) o query directo
    # 2. Si no existe: retornar error "not_found"
    # 3. Buscar en Open Library con el titulo del libro
    # 4. Tomar el primer resultado (si existe)
    # 5. Retornar JSON combinado:
    #    {"local": {...local_data}, "openlibrary": {...api_data}}
    # 6. Manejar: libro local no encontrado, API sin resultados, errores HTTP
    pass


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import mcp.server.stdio
    import asyncio

    asyncio.run(mcp.server.stdio.stdio_server(mcp))
