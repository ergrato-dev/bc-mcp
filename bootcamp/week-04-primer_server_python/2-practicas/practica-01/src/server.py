# Week 04 — Practice 01: First FastMCP Server
# Learn: FastMCP class, @mcp.tool() decorator, mcp.run()

import sys
import logging

# Configure logging to stderr (NEVER stdout — stdout is reserved for the MCP protocol)
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

# ============================================
# SECCIÓN A: Crear el servidor FastMCP
# ============================================
# FastMCP is the high-level Python API for MCP servers.
# It auto-generates JSON Schema from type hints and manages the stdio loop.

# Descomenta las siguientes líneas:
# from mcp.server.fastmcp import FastMCP
#
# mcp = FastMCP("basic-server")
# logger.info("FastMCP server instance created")


# ============================================
# SECCIÓN B: Primer tool — add
# ============================================
# @mcp.tool() registers the function as an MCP tool.
# Type hints (int, str, bool, etc.) become the JSON Schema automatically.
# The docstring becomes the tool description.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def add(a: int, b: int) -> int:
#     """Add two integers and return their sum.
#
#     Args:
#         a: First integer.
#         b: Second integer.
#     """
#     logger.debug(f"add({a}, {b})")
#     return a + b


# ============================================
# SECCIÓN C: Arrancar el servidor
# ============================================
# mcp.run() starts the stdio transport loop.
# The server reads JSON-RPC messages from stdin and writes responses to stdout.
# It runs until stdin is closed.

# Descomenta las siguientes líneas:
# if __name__ == "__main__":
#     logger.info("Starting MCP server via stdio...")
#     mcp.run()


# ============================================
# SECCIÓN D: Segundo tool — greet
# ============================================
# Notice how str type hint generates {"type": "string"} in the JSON Schema,
# while int generates {"type": "integer"}.
# Add the greeting tool BEFORE the if __name__ == "__main__" block.

# Descomenta las siguientes líneas y muévelas ANTES de la Sección C:
# @mcp.tool()
# async def greet(name: str, formal: bool = False) -> str:
#     """Greet a person by name.
#
#     Args:
#         name: The person's name.
#         formal: If True, use formal greeting. Defaults to False.
#     """
#     logger.debug(f"greet(name={name!r}, formal={formal})")
#     if formal:
#         return f"Good day, {name}. How do you do?"
#     return f"Hey {name}! 👋"
