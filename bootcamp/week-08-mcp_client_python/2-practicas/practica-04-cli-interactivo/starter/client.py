"""
Práctica 04 — CLI Interactivo con MCP Client

Goal: Build an interactive CLI that keeps a single MCP session open and
handles multiple user commands (search, stats, quit) until the user exits.

KEY CONCEPT: One connection, many calls — the session is opened once and
reused for all commands, which is more efficient than reconnecting per call.

Instructions: uncomment each section labeled PASO 1–5 in order.
Run with: uv run python client.py
"""

import asyncio
import json
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = "../../../../week-07-mcp_server_avanzado/3-proyecto/solution/src/server.py"

BANNER = """
Biblioteca MCP — CLI Interactivo
Comandos: search <texto> | stats | quit
"""
DIVIDER = "━" * 32


def print_help() -> None:
    """Print available commands."""
    print(BANNER)
    print(DIVIDER)


async def cmd_search(session: ClientSession, query: str) -> None:
    """Handle the 'search' command — call search_books and print results."""
    result = await session.call_tool("search_books", {"query": query})
    if result.isError:
        print(f"  Error: {result.content[0].text}")
        return
    books = json.loads(result.content[0].text)
    if not books:
        print("  Sin resultados")
        return
    for book in books:
        print(f"  [{book['id']}] {book['title']} — {book['author']} ({book['year']})")


async def cmd_stats(session: ClientSession) -> None:
    """Handle the 'stats' command — read the db://books/stats resource."""
    resource_result = await session.read_resource("db://books/stats")
    stats = json.loads(resource_result.contents[0].text)
    print(f"  Total libros: {stats.get('total_books', '?')}")
    print(f"  Con ISBN:     {stats.get('books_with_isbn', '?')}")
    print(f"  Año promedio: {stats.get('avg_year', '?')}")


async def main() -> None:

    # ============================================================
    # PASO 1: Conectar al server
    # ============================================================
    # Same connection pattern as previous practices.
    # The key difference here: the session stays open for the entire
    # duration of the CLI — we don't reconnect per command.
    #
    # Uncomment the following lines:
    # params = StdioServerParameters(
    #     command="python",
    #     args=[SERVER_PATH],
    #     env={**os.environ, "DB_PATH": "./data/library.db"},
    # )
    # async with stdio_client(params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()

    # ============================================================
    # PASO 2: Mostrar el menú de ayuda
    # ============================================================
    # print_help() is already implemented above.
    # Call it here to show the banner when the CLI starts.
    #
    # Uncomment the following line:
    #         print_help()

    # ============================================================
    # PASO 3: Bucle interactivo principal
    # ============================================================
    # The loop reads one line at a time from the user.
    # We use run_in_executor to avoid blocking the asyncio event loop
    # while waiting for user input (input() is a blocking call).
    #
    # loop.run_in_executor(None, fn, *args) runs fn(*args) in a
    # thread pool and awaits the result without blocking other coroutines.
    #
    # Uncomment the following lines:
    #         loop = asyncio.get_event_loop()
    #         while True:
    #             try:
    #                 line = await loop.run_in_executor(None, input, ">> ")
    #             except (EOFError, KeyboardInterrupt):
    #                 print("\n¡Hasta luego!")
    #                 break
    #
    #             parts = line.strip().split(maxsplit=1)
    #             if not parts:
    #                 continue
    #             command = parts[0].lower()

    # ============================================================
    # PASO 4: Comando search
    # ============================================================
    # When the user types "search python", parts = ["search", "python"].
    # We extract the query from parts[1] and call cmd_search().
    #
    # Uncomment the following lines (inside the while loop):
    #             if command == "search":
    #                 if len(parts) < 2:
    #                     print("  Uso: search <texto>")
    #                 else:
    #                     await cmd_search(session, parts[1])

    # ============================================================
    # PASO 5: Comando stats y quit
    # ============================================================
    # stats reads the db://books/stats resource (already implemented
    # in cmd_stats above). quit breaks the loop and closes the session.
    #
    # Uncomment the following lines (inside the while loop, after PASO 4):
    #             elif command == "stats":
    #                 await cmd_stats(session)
    #             elif command == "quit":
    #                 print("¡Hasta luego!")
    #                 break
    #             else:
    #                 print(f"  Comando desconocido: '{command}'. Escribe 'quit' para salir.")


if __name__ == "__main__":
    asyncio.run(main())
