"""Simple MCP Server for Docker GHCR practice."""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("docker-practice-server")


@mcp.tool()
async def add(a: int, b: int) -> str:
    """Add two integers and return the result."""
    return json.dumps({"result": a + b})


@mcp.tool()
async def greet(name: str, language: str = "es") -> str:
    """Greet a person in the specified language."""
    greetings = {"es": f"Hola, {name}!", "en": f"Hello, {name}!"}
    return json.dumps({"greeting": greetings.get(language, greetings["es"])})


if __name__ == "__main__":
    mcp.run(transport="stdio")
