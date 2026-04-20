"""
Calculator MCP Server — servidor de apoyo para la Práctica 04.

Provee herramientas matemáticas básicas que complementan al Library Server.
Se ejecuta con: python servers/calculator_server.py
"""
from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("calculator")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Resta b de a."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a entre b. Lanza error si b es cero."""
    if b == 0:
        raise ValueError("División por cero no permitida")
    return a / b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Eleva base a la potencia exponent."""
    return base ** exponent


@mcp.tool()
def sqrt(number: float) -> float:
    """Calcula la raíz cuadrada de un número positivo."""
    if number < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(number)


if __name__ == "__main__":
    mcp.run()
