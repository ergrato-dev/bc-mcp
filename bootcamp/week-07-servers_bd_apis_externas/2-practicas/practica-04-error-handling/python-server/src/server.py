"""
MCP Server — Patrones de Manejo de Errores
Semana 07 — Practica 04 (Python)

Muestra la diferencia entre:
- isError: errores de dominio (book not found, division by zero)
- McpError: errores del protocolo MCP
- Retry pattern: reintento con backoff exponencial
"""
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context
from mcp.shared.exceptions import McpError
from mcp.types import ErrorCode
import aiosqlite
import asyncio
import httpx
import json
import pathlib

DB_PATH = "./data/errors_demo.db"
pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


@asynccontextmanager
async def lifespan(server: FastMCP):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        await db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                author TEXT NOT NULL
            )
        """)
        await db.execute(
            "INSERT OR IGNORE INTO books (title, author) VALUES (?, ?)",
            ("Clean Code", "Robert C. Martin"),
        )
        await db.commit()
        yield {"db": db}


mcp = FastMCP("error-demo-server", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Base tool — already shows domain error pattern
# ---------------------------------------------------------------------------

@mcp.tool()
async def divide(a: float, b: float) -> str:
    """Divide a by b. Returns domain error for division by zero.

    This shows isError pattern — the server keeps running.
    """
    if b == 0:
        # Domain error: return descriptive JSON, do NOT raise McpError
        return json.dumps({
            "error": "division_by_zero",
            "message": "Cannot divide by zero. Please provide a non-zero divisor.",
            "numerator": a,
        })

    return json.dumps({"result": a / b, "operation": f"{a} / {b}"})


# ---------------------------------------------------------------------------
# When would you use McpError? Almost never from tool handlers.
# This shows the only valid use: when the server config is fundamentally broken.
# ---------------------------------------------------------------------------

@mcp.tool()
async def demonstrate_mcp_error(ctx: Context) -> str:
    """Show when McpError is appropriate vs domain errors.

    In practice: almost never raise McpError from tools.
    Use isError (return JSON with error field) instead.
    """
    # CORRECT: return domain error as JSON
    return json.dumps({
        "lesson": "Domain errors go in the JSON response, not as McpError.",
        "use_mcperror_when": [
            "Server config is fundamentally broken at startup",
            "A required tool does not exist (protocol level)",
        ],
        "use_iserror_when": [
            "Resource not found (book, user, etc.)",
            "API is temporarily unavailable",
            "Validation fails for business rules",
            "Any recoverable error the LLM can act on",
        ],
    })


# ============================================
# PASO 1: get_book_safe
# Manejo de errores de BD
# ============================================
print("--- Paso 1: get_book_safe ---")

# Este tool muestra el patron completo para errores de BD.
# Descomenta las siguientes lineas:

# @mcp.tool()
# async def get_book_safe(book_id: int, ctx: Context) -> str:
#     """Get book with full error handling.
#
#     Demonstrates:
#     - not_found: return isError-style JSON
#     - OperationalError: database issue
#     - Unexpected errors: log and return generic message
#     """
#     db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
#
#     try:
#         async with db.execute(
#             "SELECT * FROM books WHERE id = ?", (book_id,)
#         ) as cursor:
#             row = await cursor.fetchone()
#
#         if row is None:
#             # Domain error — LLM can suggest searching by title instead
#             return json.dumps({
#                 "error": "not_found",
#                 "message": f"Book id={book_id} does not exist.",
#                 "suggestion": "Use list_books to see available IDs.",
#             })
#
#         return json.dumps(dict(row))
#
#     except aiosqlite.OperationalError as e:
#         await ctx.error(f"Database error: {e}")
#         return json.dumps({
#             "error": "database_error",
#             "message": "Database is temporarily unavailable. Try again.",
#         })
#
#     except Exception as e:
#         await ctx.error(f"Unexpected error in get_book_safe: {e}")
#         return json.dumps({
#             "error": "internal_error",
#             "message": "An unexpected error occurred.",
#         })


# ============================================
# PASO 2: add_book_safe
# Manejo de IntegrityError (duplicados)
# ============================================
print("--- Paso 2: add_book_safe ---")

# Descomenta las siguientes lineas:

# @mcp.tool()
# async def add_book_safe(title: str, author: str, ctx: Context) -> str:
#     """Add book, handling duplicate title gracefully.
#
#     The 'title' column has a UNIQUE constraint.
#     Instead of crashing, we return a helpful error.
#     """
#     db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
#
#     try:
#         async with db.execute(
#             "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
#         ) as cursor:
#             await db.commit()
#             return json.dumps({
#                 "success": True,
#                 "id": cursor.lastrowid,
#                 "message": f"Book '{title}' added.",
#             })
#
#     except aiosqlite.IntegrityError:
#         # UNIQUE constraint violation — not a crash, a domain error
#         return json.dumps({
#             "error": "duplicate_title",
#             "message": f"A book titled '{title}' already exists.",
#             "suggestion": "Use a different title or check the existing entry.",
#         })


# ============================================
# PASO 3: fetch_with_retry
# Patron retry con backoff exponencial
# ============================================
print("--- Paso 3: fetch_with_retry ---")

# Descomenta las siguientes lineas:

# async def fetch_with_retry(
#     client: httpx.AsyncClient,
#     url: str,
#     params: dict,
#     max_retries: int = 3,
# ) -> dict:
#     """Fetch with exponential backoff retry.
#
#     Retry intervals: 0.5s, 1.0s, 2.0s
#     Only retries on 5xx errors or connection issues.
#     Does NOT retry on 4xx (client errors).
#     """
#     last_error: Exception | None = None
#
#     for attempt in range(max_retries):
#         try:
#             response = await client.get(url, params=params)
#             response.raise_for_status()
#             return response.json()
#
#         except httpx.HTTPStatusError as e:
#             # 4xx = client error, do NOT retry
#             if e.response.status_code < 500:
#                 raise
#             last_error = e
#             await asyncio.sleep(0.5 * (2 ** attempt))  # 0.5s, 1s, 2s
#
#         except (httpx.TimeoutException, httpx.ConnectError) as e:
#             last_error = e
#             if attempt < max_retries - 1:
#                 await asyncio.sleep(0.5 * (2 ** attempt))
#
#     raise RuntimeError(f"All {max_retries} attempts failed: {last_error}")
#
#
# @mcp.tool()
# async def get_weather_with_retry(city: str, ctx: Context) -> str:
#     """Get weather using fetch_with_retry pattern.
#
#     Retries on transient errors (5xx, timeout, connection).
#     """
#     try:
#         async with httpx.AsyncClient(timeout=10.0) as http:
#             geo = await fetch_with_retry(
#                 http,
#                 "https://geocoding-api.open-meteo.com/v1/search",
#                 {"name": city, "count": 1},
#             )
#             results = geo.get("results", [])
#             if not results:
#                 return json.dumps({"error": "city_not_found", "city": city})
#
#             loc = results[0]
#             weather = await fetch_with_retry(
#                 http,
#                 "https://api.open-meteo.com/v1/forecast",
#                 {
#                     "latitude": loc["latitude"],
#                     "longitude": loc["longitude"],
#                     "current_weather": "true",
#                 },
#             )
#             return json.dumps({"city": loc["name"], **weather["current_weather"]})
#
#     except RuntimeError as e:
#         return json.dumps({"error": "api_unavailable", "message": str(e)})


if __name__ == "__main__":
    import mcp.server.stdio
    asyncio.run(mcp.server.stdio.stdio_server(mcp))
