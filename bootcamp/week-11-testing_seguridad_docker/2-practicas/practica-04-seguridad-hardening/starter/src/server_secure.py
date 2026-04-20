"""
server_secure.py — Versión con correcciones de seguridad del Library Server.

Pasos a descomentar:
  PASO 1: search_books con query parametrizada (fix SQL injection)
  PASO 2: configuración de secretos desde variables de entorno
  PASO 3: timeout en llamadas a API externa
  PASO 4: mensajes de error seguros sin detalles internos
"""
import json
import os
import asyncio
import aiosqlite
import httpx
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context

from dotenv import load_dotenv
load_dotenv()

DB_PATH = os.environ.get("DB_PATH", "./library.db")
mcp = FastMCP("library-server-secure")


# ── Lifespan — inicializar DB ────────────────────────────────
@asynccontextmanager
async def lifespan(app):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        await db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                isbn TEXT DEFAULT ''
            )
        """)
        await db.commit()
        async with httpx.AsyncClient() as http:
            yield {"db": db, "http": http}

mcp = FastMCP("library-server-secure", lifespan=lifespan)


# ── Versión VULNERABLE (referencia — NO usar en producción) ──
# Esta función muestra el problema de SQL injection para comparación.
# La interpolación directa de `query` en el SQL permite inyectar comandos.
async def _search_books_unsafe(query: str, db: aiosqlite.Connection) -> list:
    # ❌ VULNERABLE: f-string en SQL
    sql = f"SELECT * FROM books WHERE title LIKE '%{query}%'"
    cursor = await db.execute(sql)
    return await cursor.fetchall()


# ============================================================
# PASO 1: Fix SQL Injection — usar parámetros en lugar de f-strings
# ============================================================
# La diferencia clave: usar ? y una tupla de valores en lugar de
# interpolar directamente el valor del usuario en el SQL.
#
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def search_books(query: str, ctx: Context) -> str:
#     """
#     Busca libros por título o autor.
#
#     Args:
#         query: Texto a buscar (título o autor)
#     """
#     if not query or len(query) > 500:
#         return json.dumps({"error": "invalid_query", "message": "Query too long or empty"})
#
#     db = ctx.request_context.lifespan_context["db"]
#
#     # ✅ SEGURO: query parametrizada — el driver sanitiza el valor
#     cursor = await db.execute(
#         "SELECT id, title, author, year FROM books WHERE title LIKE ? OR author LIKE ?",
#         (f"%{query}%", f"%{query}%"),  # tupla de parámetros, nunca concatenación
#     )
#     rows = await cursor.fetchall()
#
#     if not rows:
#         return json.dumps({"message": "No books found"})
#
#     return json.dumps([dict(r) for r in rows])


# ============================================================
# PASO 2: Secretos desde variables de entorno
# ============================================================
# Los API keys y URLs sensibles deben leerse del entorno,
# nunca estar hardcoded en el código fuente.
#
# Descomenta las siguientes líneas:
# # ✅ SEGURO: leer del entorno — falla explícitamente si no está configurado
# OPENLIBRARY_URL = os.environ.get(
#     "OPENLIBRARY_URL", "https://openlibrary.org/search.json"
# )
#
# # Si tu server necesita un API key propio:
# # ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
# # KeyError si no está configurado — falla rápido en startup, no en producción


# ============================================================
# PASO 3: Timeout en llamadas a API externa
# ============================================================
# asyncio.timeout() garantiza que la tool responde en un tiempo máximo.
# Sin timeout, una API lenta puede bloquear el agentic loop.
#
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def search_openlibrary(title: str, ctx: Context) -> str:
#     """
#     Busca libros en Open Library API con timeout de 10 segundos.
#
#     Args:
#         title: Título del libro a buscar
#     """
#     if not title or len(title) > 300:
#         return json.dumps({"error": "invalid_input", "message": "Title required (max 300 chars)"})
#
#     http = ctx.request_context.lifespan_context["http"]
#
#     try:
#         # ✅ SEGURO: timeout explícito — nunca bloquear indefinidamente
#         async with asyncio.timeout(10.0):
#             response = await http.get(
#                 OPENLIBRARY_URL,
#                 params={"title": title, "limit": 5},
#             )
#             response.raise_for_status()
#
#     except asyncio.TimeoutError:
#         # Respuesta genérica — no exponer detalles internos
#         return json.dumps({
#             "error": "timeout",
#             "message": "Search service did not respond in time",
#         })
#     except httpx.HTTPStatusError:
#         return json.dumps({
#             "error": "api_error",
#             "message": "Search service returned an error",
#         })
#     except httpx.ConnectError:
#         return json.dumps({
#             "error": "connection_error",
#             "message": "Could not reach search service",
#         })
#
#     docs = response.json().get("docs", [])
#     return json.dumps([
#         {
#             "title": d.get("title", "Unknown"),
#             "author": d.get("author_name", ["Unknown"])[0] if d.get("author_name") else "Unknown",
#             "year": d.get("first_publish_year"),
#         }
#         for d in docs[:5]
#     ])


# ============================================================
# PASO 4: Mensajes de error seguros
# ============================================================
# Los errores no deben exponer: traceback, config interna, paths del
# sistema ni API keys. Solo información útil para el LLM.
#
# Descomenta el siguiente bloque para comparar ambos enfoques:
# @mcp.tool()
# async def get_book(book_id: int, ctx: Context) -> str:
#     """
#     Obtiene un libro por su ID.
#
#     Args:
#         book_id: ID numérico del libro
#     """
#     if book_id <= 0:
#         return json.dumps({"error": "invalid_id", "message": "book_id must be positive"})
#
#     db = ctx.request_context.lifespan_context["db"]
#
#     try:
#         cursor = await db.execute("SELECT * FROM books WHERE id = ?", (book_id,))
#         row = await cursor.fetchone()
#     except aiosqlite.Error:
#         # ✅ SEGURO: error genérico — no exponer detalles de DB
#         return json.dumps({
#             "error": "database_error",
#             "message": "Could not retrieve book",
#             # ❌ NO incluir: str(e), DB_PATH, query SQL, etc.
#         })
#
#     if row is None:
#         return json.dumps({"error": "not_found", "message": f"Book {book_id} not found"})
#
#     return json.dumps(dict(row))


if __name__ == "__main__":
    mcp.run()
