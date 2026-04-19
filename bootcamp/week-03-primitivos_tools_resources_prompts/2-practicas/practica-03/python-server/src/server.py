"""
MCP Server — Práctica 03: Prompts en Python
Semana 03 — Los Tres Primitivos

Objetivo: aprender a implementar Prompts con PromptArgument,
generar messages[] con roles user/assistant y usar EmbeddedResource.
"""

import asyncio
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

server = Server("practice-03-prompts-python")


# ============================================================
# SECCIÓN A: Declarar lista de Prompts (list_prompts)
# ============================================================
# Cada Prompt tiene name, description y arguments.
# PromptArgument tiene name, description y required (bool).
#
# Descomenta las líneas siguientes:
# @server.list_prompts()
# async def list_prompts() -> list[types.Prompt]:
#     return [
#         types.Prompt(
#             name="code_review",
#             description="Generates a detailed code review for the given code snippet",
#             arguments=[
#                 types.PromptArgument(
#                     name="language",
#                     description="Programming language (python, typescript, go, etc.)",
#                     required=True
#                 ),
#                 types.PromptArgument(
#                     name="code",
#                     description="The code snippet to review",
#                     required=True
#                 ),
#                 types.PromptArgument(
#                     name="focus",
#                     description="Review focus: security, performance, style, or general",
#                     required=False    # Opcional: el cliente puede omitirlo
#                 ),
#             ]
#         ),
#         types.Prompt(
#             name="explain_concept",
#             description="Explains a programming concept at the specified level",
#             arguments=[
#                 types.PromptArgument(
#                     name="concept",
#                     description="The programming concept to explain",
#                     required=True
#                 ),
#                 types.PromptArgument(
#                     name="level",
#                     description="Explanation level: beginner, intermediate, or advanced",
#                     required=False
#                 ),
#             ]
#         ),
#     ]


# ============================================================
# SECCIÓN B: Implementar get_prompt
# ============================================================
# get_prompt recibe name y arguments (puede ser None).
# SIEMPRE inicializar con: args = arguments or {}
# Los argumentos opcionales usan args.get("key", default).
#
# Descomenta las líneas siguientes:
# @server.get_prompt()
# async def get_prompt(
#     name: str,
#     arguments: dict | None
# ) -> types.GetPromptResult:
#     args = arguments or {}
#
#     if name == "code_review":
#         language = args.get("language", "unknown")
#         code = args.get("code", "")
#         focus = args.get("focus", "general quality")
#
#         return types.GetPromptResult(
#             description=f"Code review for {language} code",
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=(
#                             f"Please review the following {language} code "
#                             f"with focus on {focus}:\n\n"
#                             f"```{language}\n{code}\n```\n\n"
#                             "Provide specific feedback on:\n"
#                             "1. Correctness\n"
#                             "2. Edge cases\n"
#                             "3. Performance\n"
#                             "4. Best practices"
#                         )
#                     )
#                 )
#             ]
#         )
#
#     if name == "explain_concept":
#         concept = args.get("concept", "")
#         level = args.get("level", "intermediate")
#
#         return types.GetPromptResult(
#             description=f"Explanation of {concept}",
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=f"Explain the concept of '{concept}' at a {level} level."
#                     )
#                 )
#             ]
#         )
#
#     raise ValueError(f"Unknown prompt: {name}")


# ============================================================
# SECCIÓN C: Multi-turn con role "assistant" seed
# ============================================================
# Un mensaje con role="assistant" "pre-orienta" la respuesta del LLM.
# Reemplaza el código_review de Sección B por esta versión con seed:
#
#     if name == "code_review":
#         language = args.get("language", "unknown")
#         code = args.get("code", "")
#         focus = args.get("focus", "general quality")
#
#         return types.GetPromptResult(
#             description=f"Code review for {language}",
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=(
#                             f"Review this {language} code (focus: {focus}):\n\n"
#                             f"```{language}\n{code}\n```"
#                         )
#                     )
#                 ),
#                 # Assistant seed: orienta el estilo de la respuesta
#                 types.PromptMessage(
#                     role="assistant",
#                     content=types.TextContent(
#                         type="text",
#                         text="I'll analyze this code systematically:"
#                     )
#                 ),
#             ]
#         )


# ============================================================
# SECCIÓN D: EmbeddedResource dentro de un Prompt
# ============================================================
# EmbeddedResource incluye datos de un Resource directamente
# en el mensaje del Prompt, sin que el cliente haga un segundo request.
#
# Agrega este nuevo Prompt en list_prompts y su handler en get_prompt:
#
# En list_prompts agrega:
#     types.Prompt(
#         name="query_with_schema",
#         description="Generates a SQL query with the table schema as context",
#         arguments=[
#             types.PromptArgument(name="task", description="What data to retrieve", required=True),
#         ]
#     ),
#
# En get_prompt agrega:
#     if name == "query_with_schema":
#         task = args.get("task", "")
#         schema_data = {"table": "products", "columns": ["id", "name", "price"]}
#
#         return types.GetPromptResult(
#             description="SQL query generation with schema context",
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.EmbeddedResource(
#                         type="resource",
#                         resource=types.TextResourceContents(
#                             uri="db://schema/products",
#                             text=json.dumps(schema_data, indent=2),
#                             mimeType="application/json"
#                         )
#                     )
#                 ),
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=f"Using the schema above, write a SQL query to: {task}"
#                     )
#                 ),
#             ]
#         )


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
