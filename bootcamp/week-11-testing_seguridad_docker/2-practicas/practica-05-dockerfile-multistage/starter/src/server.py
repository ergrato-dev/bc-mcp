"""
server.py — MCP Server mínimo para la práctica de Docker.

No necesita descomentar nada aquí. El objetivo es dockerizar este server.
"""
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("docker-demo-server")


@mcp.tool()
def hello(name: str = "World") -> str:
    """Retorna un saludo para verificar que el server corre correctamente."""
    return f"Hello from Docker, {name}! DB path: {os.environ.get('DB_PATH', 'not set')}"


if __name__ == "__main__":
    mcp.run()
