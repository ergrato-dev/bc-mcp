"""
client.py — Library CLI: MCP Client interactivo

Este módulo implementa un CLI que se conecta al Library Manager MCP Server
(semana 07) y permite buscar libros, agregar nuevos títulos, consultar la
API de Open Library y ver estadísticas de la biblioteca.

Estructura:
  connect_to_server()     — TODO 1: abrir sesión MCP
  list_available_tools()  — TODO 2: listar tools del server
  search_books()          — TODO 3: buscar libros locales
  add_book()              — TODO 4: agregar libro a la biblioteca
  search_openlibrary()    — TODO 5: buscar en API externa
  interactive_loop()      — TODO 6: bucle de comandos del CLI

Run:
  uv run python src/client.py
"""

import asyncio
import json
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from mcp import ClientSession, McpError, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

load_dotenv()

import config  # noqa: E402 — loaded after dotenv

# ─── Constants ────────────────────────────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════╗
║      Library CLI — MCP Client        ║
╚══════════════════════════════════════╝
"""

HELP = """Comandos disponibles:
  search <texto>        Buscar libros locales por título o autor
  add <título>          Agregar un libro (pedirá autor y año)
  openlibrary <título>  Buscar en Open Library API
  tools                 Listar todos los tools del server
  stats                 Ver estadísticas de la biblioteca
  quit                  Salir
"""

DIVIDER = "─" * 40


# ─── TODO 1: connect_to_server ─────────────────────────────────────────────


@asynccontextmanager
async def connect_to_server():
    """
    Open a stdio MCP session to the Library Manager server.

    This is a context manager — use it with `async with connect_to_server() as session:`.
    The session is fully initialized (handshake complete) when the block begins.

    Steps to implement:
      1. Create StdioServerParameters with config.SERVER_COMMAND, [config.SERVER_PATH],
         and env = {**os.environ, "DB_PATH": config.DB_PATH}
      2. Open the stdio transport with stdio_client(params)
      3. Create a ClientSession(read, write)
      4. Call await session.initialize()
      5. yield session

    Hints:
      - Nest two `async with` blocks: stdio_client → ClientSession
      - Use {**os.environ, "DB_PATH": config.DB_PATH} to inherit the current env
        and override DB_PATH for the server process
    """
    # TODO 1: Implement connect_to_server
    # params = StdioServerParameters(
    #     command=...,
    #     args=...,
    #     env=...,
    # )
    # async with stdio_client(params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()
    #         yield session
    raise NotImplementedError("TODO 1: implement connect_to_server()")
    yield  # unreachable — required for @asynccontextmanager type check


# ─── TODO 2: list_available_tools ──────────────────────────────────────────


async def list_available_tools(session: ClientSession) -> None:
    """
    Print all tools offered by the server with their descriptions.

    Steps to implement:
      1. Call await session.list_tools()
      2. Iterate over result.tools
      3. Print tool.name and tool.description for each tool

    Expected output format:
      Tools disponibles (7):
        • search_books     — Search local library by title or author
        • add_book         — Add a new book to the local library
        ...
    """
    # TODO 2: Implement list_available_tools
    pass


# ─── TODO 3: search_books ───────────────────────────────────────────────────


async def search_books(session: ClientSession, query: str) -> list[dict]:
    """
    Search for books in the local library and return a list of book dicts.

    Steps to implement:
      1. Call await session.call_tool("search_books", {"query": query})
      2. Check result.isError — if True, print the error and return []
      3. Parse result.content[0].text as JSON (json.loads)
      4. Return the list of book dicts

    Each book dict has: id, title, author, year, isbn (may be None), notes (may be None)

    Hints:
      - Wrap json.loads in try/except json.JSONDecodeError
      - Return [] if the parsed value is not a list
    """
    # TODO 3: Implement search_books
    return []


# ─── TODO 4: add_book ───────────────────────────────────────────────────────


async def add_book(
    session: ClientSession,
    title: str,
    author: str,
    year: int,
    isbn: str | None = None,
) -> dict | None:
    """
    Add a new book to the local library and return the created book dict.

    Steps to implement:
      1. Build the args dict: {"title": title, "author": author, "year": year}
         If isbn is not None, add "isbn": isbn to the dict
      2. Call await session.call_tool("add_book", args)
      3. Check result.isError — if True, print the error and return None
      4. Parse result.content[0].text as JSON and return the dict

    The returned dict includes the DB-assigned "id" field.
    """
    # TODO 4: Implement add_book
    return None


# ─── TODO 5: search_openlibrary ─────────────────────────────────────────────


async def search_openlibrary(session: ClientSession, title: str) -> list[dict]:
    """
    Search Open Library API for books matching the given title.

    Steps to implement:
      1. Call await session.call_tool("search_openlibrary", {"title": title})
      2. Check result.isError — if True, print the error and return []
      3. Parse result.content[0].text as JSON
      4. Return the list of result dicts

    Each result dict typically has: title, author_name (list), first_publish_year, isbn (list)

    Hints:
      - Open Library results may have missing fields — use .get() when accessing
      - The tool name is exactly "search_openlibrary" (check with list_tools() if unsure)
    """
    # TODO 5: Implement search_openlibrary
    return []


# ─── TODO 6: interactive_loop ───────────────────────────────────────────────


async def interactive_loop(session: ClientSession) -> None:
    """
    Run an interactive CLI loop that handles user commands until 'quit'.

    Commands to implement:
      search <text>         → call search_books(session, text), print results
      add <title>           → prompt for author and year, call add_book()
      openlibrary <title>   → call search_openlibrary(session, title), print results
      tools                 → call list_available_tools(session)
      stats                 → read resource "db://books/stats" and print
      quit                  → print farewell message and break

    Steps to implement:
      1. Print HELP and DIVIDER at the start
      2. Loop: use asyncio.get_event_loop().run_in_executor(None, input, ">> ")
         to read input without blocking the event loop
      3. Split the line: parts = line.strip().split(maxsplit=1)
      4. Dispatch on parts[0].lower() to the appropriate handler
      5. Handle EOFError and KeyboardInterrupt gracefully (break the loop)

    For the 'add' command, use input() inside run_in_executor to prompt
    for each field:
      author = await loop.run_in_executor(None, input, "  Autor: ")
      year_str = await loop.run_in_executor(None, input, "  Año: ")
      year = int(year_str) if year_str.isdigit() else 0

    For the 'stats' command:
      resource_result = await session.read_resource("db://books/stats")
      stats = json.loads(resource_result.contents[0].text)
      print(f"  Total libros: {stats.get('total_books', '?')}")
      print(f"  Con ISBN:     {stats.get('books_with_isbn', '?')}")
      print(f"  Año promedio: {stats.get('avg_year', '?')}")
    """
    # TODO 6: Implement interactive_loop
    pass


# ─── Entry point ────────────────────────────────────────────────────────────


async def main() -> None:
    print(BANNER)
    print("Conectando al server MCP...")

    try:
        async with connect_to_server() as session:
            tools = await session.list_tools()
            print(f"✓ Conectado — {len(tools.tools)} tools disponibles\n")
            await interactive_loop(session)

    except FileNotFoundError:
        print(f"✗ No se encontró el server: {config.SERVER_PATH}")
        print("  Verifica SERVER_PATH en tu archivo .env")
    except McpError as e:
        print(f"✗ Error de protocolo MCP: {e.error.message}")
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario")


if __name__ == "__main__":
    asyncio.run(main())
