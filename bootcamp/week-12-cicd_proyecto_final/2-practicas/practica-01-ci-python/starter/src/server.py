"""Simple MCP Server for CI practice — tools: add, greet."""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ci-practice-server")


@mcp.tool()
async def add(a: int, b: int) -> str:
    """Add two integers and return the result."""
    return json.dumps({"result": a + b})


@mcp.tool()
async def greet(name: str, language: str = "es") -> str:
    """Greet a person in the specified language."""
    greetings = {
        "es": f"Hola, {name}!",
        "en": f"Hello, {name}!",
        "fr": f"Bonjour, {name}!",
        "pt": f"Olá, {name}!",
    }
    if language not in greetings:
        return json.dumps({"error": f"Language '{language}' not supported. Use: {list(greetings.keys())}"})
    return json.dumps({"greeting": greetings[language]})


if __name__ == "__main__":
    mcp.run(transport="stdio")
