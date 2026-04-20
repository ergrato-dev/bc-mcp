"""
server.py — Library Manager MCP Server (Semana 11)

Refactorización del server de semana 07 con:
  - Validación de inputs con Pydantic (src/validators.py)
  - SQL parametrizado en todas las queries
  - Timeout en llamadas a API externa
  - Errores seguros sin información interna

Instrucciones:
  1. Implementa src/validators.py primero
  2. Completa cada TODO en este archivo
  3. Ejecuta: uv run pytest -v
"""
import asyncio
import json
import os
import pathlib
from contextlib import asynccontextmanager

import aiosqlite
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Context
from pydantic import ValidationError

from .validators import AddBookInput, SearchBooksInput, UpdateBookInput

load_dotenv()

# ── Configuración ────────────────────────────────────────────
DB_PATH = os.environ.get("DB_PATH", "./data/library.db")
OPENLIBRARY_URL = os.environ.get(
    "OPENLIBRARY_URL", "https://openlibrary.org/search.json"
)
MAX_SEARCH_RESULTS = int(os.environ.get("MAX_SEARCH_RESULTS", "10"))

pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


def _make_error(code: str, message: str) -> str:
    """Retorna un error como JSON string."""
    return json.dumps({"error": code, "message": message})


# ── Schema ───────────────────────────────────────────────────
async def _init_schema(db: aiosqlite.Connection) -> None:
    """Inicializar esquema de la base de datos."""
    await db.executescript("""
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT    NOT NULL,
            author TEXT    NOT NULL,
            year   INTEGER,
            isbn   TEXT    DEFAULT '',
            notes  TEXT    DEFAULT '',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_books_title  ON books(title);
        CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
    """)
    await db.commit()


# ── Lifespan ─────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(server: FastMCP):
    async with (
        aiosqlite.connect(DB_PATH) as db,
        httpx.AsyncClient(timeout=15.0) as http,
    ):
        db.row_factory = aiosqlite.Row
        await _init_schema(db)
        yield {"db": db, "http": http}


mcp = FastMCP("library-manager-v2", lifespan=lifespan)


# ── Tools ─────────────────────────────────────────────────────

@mcp.tool()
async def search_books(query: str, ctx: Context) -> str:
    """Search local library by title or author.

    Args:
        query: Text to search (max 500 chars)
    """
    # TODO: Implementar con validación y SQL parametrizado
    # 1. Validar con SearchBooksInput — retornar _make_error si ValidationError
    # 2. Obtener db de ctx.request_context.lifespan_context["db"]
    # 3. SELECT con LIKE usando ? — NUNCA f-string en SQL
    #    cursor = await db.execute(
    #        "SELECT id,title,author,year FROM books WHERE title LIKE ? OR author LIKE ?",
    #        (f"%{params.query}%", f"%{params.query}%"),
    #    )
    # 4. Si no hay resultados: retornar {"message": "No books found"}
    # 5. Retornar JSON array con los resultados
    pass


@mcp.tool()
async def get_book(book_id: int, ctx: Context) -> str:
    """Get a single book by ID.

    Args:
        book_id: Positive integer ID of the book
    """
    # TODO: Implementar con validación básica y SQL parametrizado
    # 1. Validar book_id > 0 — retornar _make_error si no
    # 2. SELECT * FROM books WHERE id = ? (parametrizado)
    # 3. Si row is None: retornar _make_error("not_found", ...)
    # 4. Retornar JSON con dict(row)
    pass


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
        title: Book title (1-300 chars)
        author: Author name (1-200 chars)
        year: Publication year (1000-2100)
        isbn: ISBN optional (digits, X, hyphens only)
        notes: Personal notes (optional)
    """
    # TODO: Implementar con AddBookInput y SQL parametrizado
    # 1. Validar con AddBookInput — retornar _make_error si ValidationError
    # 2. INSERT INTO books (title,author,year,isbn,notes) VALUES (?,?,?,?,?)
    #    con los valores de data.title, data.author, etc. (YA validados)
    # 3. await db.commit()
    # 4. Retornar JSON {"success": True, "id": cursor.lastrowid}
    pass


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

    Args:
        book_id: ID of the book to update
        title: New title (optional)
        author: New author (optional)
        year: New year (optional, 0 = no change)
        notes: New notes (optional)
    """
    # TODO: Implementar con UpdateBookInput y UPDATE dinámico
    # 1. Validar con UpdateBookInput — retornar _make_error si ValidationError
    # 2. Si not data.has_updates(): retornar _make_error("nothing_to_update", ...)
    # 3. Construir SET clause dinámico:
    #    fields = {}
    #    if data.title: fields["title"] = data.title
    #    if data.author: fields["author"] = data.author
    #    if data.year: fields["year"] = data.year
    #    if data.notes is not None: fields["notes"] = data.notes
    # 4. UPDATE books SET campo1=?,campo2=? WHERE id=?
    # 5. Si cursor.rowcount == 0: retornar _make_error("not_found", ...)
    # 6. await db.commit()
    # 7. Retornar el libro actualizado (nueva query SELECT)
    pass


@mcp.tool()
async def delete_book(book_id: int, ctx: Context) -> str:
    """Delete a book from the local library.

    Args:
        book_id: Positive integer ID of the book to delete
    """
    # TODO: Implementar DELETE con SQL parametrizado
    # 1. Validar book_id > 0
    # 2. DELETE FROM books WHERE id = ? (parametrizado)
    # 3. await db.commit()
    # 4. Si cursor.rowcount == 0: retornar _make_error("not_found", ...)
    # 5. Retornar JSON {"success": True, "deleted_id": book_id}
    pass


@mcp.tool()
async def search_openlibrary(title: str, ctx: Context) -> str:
    """Search Open Library public API with timeout.

    Args:
        title: Book title to search (max 300 chars)
    """
    # TODO: Implementar con timeout y manejo de errores seguros
    # 1. Validar title (1-300 chars)
    # 2. Obtener http de ctx.request_context.lifespan_context["http"]
    # 3. Usar asyncio.timeout(10.0) para la llamada HTTP:
    #    async with asyncio.timeout(10.0):
    #        response = await http.get(OPENLIBRARY_URL, params={"title": title, "limit": 5})
    # 4. Capturar asyncio.TimeoutError → _make_error("timeout", ...)
    # 5. Capturar httpx.HTTPStatusError → _make_error("api_error", ...)
    # 6. Capturar httpx.ConnectError → _make_error("connection_error", ...)
    # 7. Mapear docs a lista simplificada: title, author, year
    pass


@mcp.tool()
async def enrich_book(book_id: int, ctx: Context) -> str:
    """Enrich a local book with Open Library metadata.

    Args:
        book_id: ID of the local book to enrich
    """
    # TODO: Implementar enrichment combinando DB local + Open Library
    # 1. Obtener libro local — retornar error si no existe
    # 2. Buscar en Open Library con el título del libro local
    # 3. Si hay resultados: tomar el primero
    # 4. Retornar JSON {"local": {...}, "openlibrary": {...} o null}
    pass


if __name__ == "__main__":
    mcp.run()
