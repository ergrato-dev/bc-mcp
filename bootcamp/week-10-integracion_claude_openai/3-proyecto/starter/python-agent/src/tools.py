"""
tools.py — Conversión de MCP Tool schemas al formato de Anthropic
           y despacho de tool calls via ClientSession.

TODO: Implementar las dos funciones de este módulo.
"""
from mcp import ClientSession
from mcp.types import Tool as MCPTool


def convert_mcp_tools_for_claude(tools: list[MCPTool]) -> list[dict]:
    """
    Convierte una lista de MCP Tools al formato que acepta la API de Anthropic.

    La diferencia principal entre MCP y Anthropic es el nombre del campo:
    - MCP:       tool.inputSchema
    - Anthropic: "input_schema"  ← clave requerida por la API

    Args:
        tools: Lista de MCPTool devuelta por session.list_tools()

    Returns:
        Lista de dicts en formato Anthropic:
        [{"name": ..., "description": ..., "input_schema": ...}, ...]

    TODO: Implementar usando list comprehension.
    # 1. Para cada tool en tools, crear un dict con:
    #    - "name": tool.name
    #    - "description": tool.description o "" si es None
    #    - "input_schema": tool.inputSchema   ← sin renombrar, solo reasignar la clave
    # 2. Retornar la lista resultante
    """
    pass   # TODO: reemplazar con la implementación


async def call_mcp_tool(
    session: ClientSession,
    tool_name: str,
    tool_input: dict,
) -> str:
    """
    Ejecuta una tool en el MCP Server y devuelve su resultado como string.

    Args:
        session:    Sesión MCP activa (ya inicializada)
        tool_name:  Nombre de la tool a ejecutar
        tool_input: Argumentos de la tool (dict con los parámetros)

    Returns:
        Resultado de la tool como string (texto plano)

    TODO: Implementar esta función.
    # 1. Llamar a session.call_tool(tool_name, tool_input)
    # 2. Extraer el texto del resultado:
    #    result.content[0].text si result.content tiene elementos
    #    "" (string vacío) si result.content está vacío
    # 3. Retornar el texto
    """
    pass   # TODO: reemplazar con la implementación
