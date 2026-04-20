"""
MCP Server — Books Library con SQLite y aiosqlite
Semana 07 — Practica 01

Domain: biblioteca de libros con operaciones CRUD
Transport: stdio (compatible con Claude Desktop, MCP Inspector)
"""
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context
import aiosqlite
import json
import os
import pathlib

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DB_PATH = os.environ.get("DB_PATH", "./data/books.db")

# Ensure data directory exists
pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Lifespan — database initialization
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Open one shared database connection for the server lifetime."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row

        # Initialize schema (idempotent — safe to run multiple times)
        await db.executescript("""
            CREATE TABLE IF NOT EXISTS books (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                title  TEXT    NOT NULL,
                author TEXT    NOT NULL,
                year   INTEGER,
                genre  TEXT
            );
            CREATE INDEX IF NOT EXISTS idx_books_title  ON books(title);
            CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
        """)

        # Insert sample data only if table is empty
        async with db.execute("SELECT COUNT(*) FROM books") as cursor:
            row = await cursor.fetchone()
            count = row[0]

        if count == 0:
            await db.executemany(
                "INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
                [
                    ("The Pragmatic Programmer", "David Thomas", 1999, "Programming"),
                    ("Clean Code", "Robert C. Martin", 2008, "Programming"),
                    ("Python Crash Course", "Eric Matthes", 2019, "Programming"),
                    ("The Hitchhiker Guide to the Galaxy", "Douglas Adams", 1979, "Fiction"),
                    ("Fluent Python", "Luciano Ramalho", 2022, "Programming"),
                ],
            )
            await db.commit()

        yield {"db": db}


# ---------------------------------------------------------------------------
# MCP Server setup
# ---------------------------------------------------------------------------

mcp = FastMCP("books-server", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Tool base (already working — observe this as the reference)
# ---------------------------------------------------------------------------

@mcp.tool()
async def list_books(ctx: Context) -> str:
    """List all books in the library.

    Returns a JSON array with all books and their details.
    """
    db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]

    async with db.execute(
        "SELECT id, title, author, year, genre FROM books ORDER BY title"
    ) as cursor:
        rows = await cursor.fetchall()

    books = [dict(r) for r in rows]
    return json.dumps(books, ensure_ascii=False, indent=2)


# ============================================
# PASO 2: search_books
# Busca libros por titulo o autor
# ============================================
print("--- Paso 2: search_books ---")

# Este tool filtra libros usando LIKE en titulo y autor.
# Descomenta las siguientes lineas:

# @mcp.tool()
# async def search_books(query: str, ctx: Context) -> str:
#     """Search books by title or author.
#
#     Args:
#         query: Text to search in title or author fields
#
#     Returns:
#         JSON array of matching books (up to 20 results)
#     """
#     db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
#
#     async with db.execute(
#         "SELECT id, title, author, year, genre FROM books "
#         "WHERE title LIKE ? OR author LIKE ? "
#         "ORDER BY title LIMIT 20",
#         (f"%{query}%", f"%{query}%"),
#     ) as cursor:
#         rows = await cursor.fetchall()
#
#     books = [dict(r) for r in rows]
#     if not books:
#         return json.dumps({"message": f"No books found for: {query!r}"})
#
#     return json.dumps(books, ensure_ascii=False, indent=2)


# ============================================
# PASO 3: get_book
# Obtiene un libro por su ID
# ============================================
print("--- Paso 3: get_book ---")

# Este tool retorna un libro especifico o un error si no existe.
# Descomenta las siguientes lineas:

# @mcp.tool()
# async def get_book(book_id: int, ctx: Context) -> str:
#     """Get a single book by its ID.
#
#     Args:
#         book_id: The integer ID of the book
#
#     Returns:
#         JSON object with book details, or error if not found
#     """
#     db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
#
#     async with db.execute(
#         "SELECT * FROM books WHERE id = ?", (book_id,)
#     ) as cursor:
#         row = await cursor.fetchone()
#
#     if row is None:
#         return json.dumps({
#             "error": "not_found",
#             "message": f"Book with id={book_id} does not exist",
#         })
#
#     return json.dumps(dict(row), ensure_ascii=False, indent=2)


# ============================================
# PASO 4: add_book
# Agrega un nuevo libro a la biblioteca
# ============================================
print("--- Paso 4: add_book ---")

# Este tool inserta un libro y retorna el ID asignado.
# Descomenta las siguientes lineas:

# @mcp.tool()
# async def add_book(
#     title: str,
#     author: str,
#     year: int,
#     genre: str = "Unknown",
#     ctx: Context = None,
# ) -> str:
#     """Add a new book to the library.
#
#     Args:
#         title: Book title
#         author: Author name
#         year: Publication year
#         genre: Book genre (default: Unknown)
#
#     Returns:
#         JSON with the new book's ID on success, or error on failure
#     """
#     db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
#
#     try:
#         async with db.execute(
#             "INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
#             (title, author, year, genre),
#         ) as cursor:
#             await db.commit()
#             new_id = cursor.lastrowid
#
#         return json.dumps({
#             "success": True,
#             "id": new_id,
#             "message": f"Book '{title}' added with id={new_id}",
#         })
#
#     except aiosqlite.IntegrityError as e:
#         return json.dumps({
#             "error": "duplicate_entry",
#             "message": f"Could not add book: {e}",
#         })


# ============================================
# PASO 5: delete_book
# Elimina un libro por su ID
# ============================================
print("--- Paso 5: delete_book ---")

# Este tool elimina un libro y retorna confirmacion.
# Descomenta las siguientes lineas:

# @mcp.tool()
# async def delete_book(book_id: int, ctx: Context) -> str:
#     """Delete a book from the library by its ID.
#
#     Args:
#         book_id: The integer ID of the book to delete
#
#     Returns:
#         JSON confirming deletion, or error if book not found
#     """
#     db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
#
#     async with db.execute(
#         "DELETE FROM books WHERE id = ?", (book_id,)
#     ) as cursor:
#         await db.commit()
#         deleted_count = cursor.rowcount
#
#     if deleted_count == 0:
#         return json.dumps({
#             "error": "not_found",
#             "message": f"Book with id={book_id} was not found",
#         })
#
#     return json.dumps({
#         "success": True,
#         "deleted_id": book_id,
#         "message": f"Book {book_id} deleted successfully",
#     })


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import mcp.server.stdio
    import asyncio

    asyncio.run(mcp.server.stdio.stdio_server(mcp))
