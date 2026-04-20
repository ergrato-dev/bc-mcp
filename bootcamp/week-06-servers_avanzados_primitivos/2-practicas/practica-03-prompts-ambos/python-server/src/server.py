"""
Writing assistant MCP server — práctica de Prompts en Python.
Semana 06 — Los 3 Primitivos
"""

from mcp.server.fastmcp import FastMCP
from mcp.types import Message, TextContent

mcp = FastMCP("writing-assistant")


# =============================================
# SECCIÓN 1: Prompt simple sin argumentos
# =============================================
# @mcp.prompt() registra el prompt en prompts/list.
# La función retorna list[Message] con los mensajes iniciales.
# Descomenta las siguientes líneas:
# @mcp.prompt()
# async def brainstorm_ideas() -> list[Message]:
#     """Starter prompt for brainstorming creative ideas."""
#     return [
#         Message(
#             role="user",
#             content=TextContent(
#                 type="text",
#                 text=(
#                     "Necesito generar ideas creativas para un proyecto. "
#                     "Por favor ayúdame a hacer un brainstorming efectivo. "
#                     "¿Cuáles son las mejores técnicas que debería usar?"
#                 ),
#             ),
#         )
#     ]


# =============================================
# SECCIÓN 2: Prompt con argumento obligatorio
# =============================================
# El parámetro "topic" es un argumento del prompt.
# FastMCP lo publica automáticamente en prompts/list con required=True.
# Descomenta las siguientes líneas:
# @mcp.prompt()
# async def explain_concept(topic: str) -> list[Message]:
#     """Explains a technical concept clearly.
#
#     Args:
#         topic: The concept or technology to explain.
#     """
#     return [
#         Message(
#             role="user",
#             content=TextContent(
#                 type="text",
#                 text=(
#                     f"Explícame el concepto de '{topic}' de forma clara y sencilla. "
#                     f"Incluye: qué es, para qué sirve y un ejemplo práctico."
#                 ),
#             ),
#         )
#     ]


# =============================================
# SECCIÓN 3: Prompt con múltiples mensajes
# =============================================
# Un prompt puede iniciar una conversación con múltiples turnos.
# La lista puede mezclar mensajes "user" y "assistant".
# Descomenta las siguientes líneas:
# @mcp.prompt()
# async def code_review(language: str, code: str) -> list[Message]:
#     """Starts a code review conversation.
#
#     Args:
#         language: Programming language of the code.
#         code: The code snippet to review.
#     """
#     return [
#         Message(
#             role="user",
#             content=TextContent(
#                 type="text",
#                 text=f"Voy a mostrarte un fragmento de código en {language}:",
#             ),
#         ),
#         Message(
#             role="assistant",
#             content=TextContent(
#                 type="text",
#                 text="Entendido, muéstrame el código y lo analizaré detalladamente.",
#             ),
#         ),
#         Message(
#             role="user",
#             content=TextContent(
#                 type="text",
#                 text=f"```{language}\n{code}\n```\n\nPor favor revisa: legibilidad, errores y mejoras.",
#             ),
#         ),
#     ]


if __name__ == "__main__":
    mcp.run()
