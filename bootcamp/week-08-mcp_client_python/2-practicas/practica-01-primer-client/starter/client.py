"""
Práctica 01 — Primer MCP Client en Python

Goal: Connect to the week-07 Library Manager server, perform the MCP
handshake, and print server information.

Instructions: uncomment each section labeled PASO 1, 2, 3, 4 in order.
Run with: uv run python client.py
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Path to the week-07 server — adjust to your local path
SERVER_PATH = "../../../../week-07-mcp_server_avanzado/3-proyecto/solution/src/server.py"


async def main() -> None:
    print("Iniciando MCP Client...")

    # ============================================================
    # PASO 1: Configurar StdioServerParameters
    # ============================================================
    # StdioServerParameters describes how to launch the server process.
    # - command: the executable (python, node, uv run, etc.)
    # - args: list of arguments passed to the command
    # - env: environment variables for the server process
    #   We use {**os.environ, ...} to inherit the current env
    #   and add/override specific variables.
    #
    # Uncomment the following lines:
    # params = StdioServerParameters(
    #     command="python",
    #     args=[SERVER_PATH],
    #     env={**os.environ, "DB_PATH": "./data/library.db"},
    # )

    # ============================================================
    # PASO 2: Abrir el canal de comunicación (stdio_client)
    # ============================================================
    # stdio_client() launches the server as a subprocess and opens
    # stdin/stdout pipes. It returns (read_stream, write_stream).
    # We use async with to ensure the process is properly closed.
    #
    # Uncomment the following lines (keep the indentation):
    # async with stdio_client(params) as (read, write):

    # ============================================================
    # PASO 3: Crear ClientSession e inicializar el protocolo
    # ============================================================
    # ClientSession wraps the streams and exposes the MCP protocol API.
    # session.initialize() performs the MCP handshake:
    #   Client → {"method": "initialize", "params": {...}}
    #   Server → {"result": {"serverInfo": {...}, "capabilities": {...}}}
    # Without this step, any subsequent call raises McpError.
    #
    # Uncomment the following lines (inside the stdio_client block):
    #     async with ClientSession(read, write) as session:
    #         info = await session.initialize()

    # ============================================================
    # PASO 4: Imprimir información del server
    # ============================================================
    # info.serverInfo → ServerInfo(name, version)
    # info.capabilities → ServerCapabilities(tools, resources, prompts)
    # Each capability is None if the server doesn't support it.
    #
    # Uncomment the following lines (inside the ClientSession block):
    #         print("✓ Conectado al server MCP")
    #         print("━" * 32)
    #         print(f"Server:  {info.serverInfo.name}")
    #         print(f"Version: {info.serverInfo.version}")
    #         print(f"Tools:   {'✓' if info.capabilities.tools else '✗'}")
    #         print(f"Resources: {'✓' if info.capabilities.resources else '✗'}")
    #         print(f"Prompts: {'✓' if info.capabilities.prompts else '✗'}")
    #         print("━" * 32)
    #         print("✓ Sesión cerrada correctamente")


if __name__ == "__main__":
    asyncio.run(main())
