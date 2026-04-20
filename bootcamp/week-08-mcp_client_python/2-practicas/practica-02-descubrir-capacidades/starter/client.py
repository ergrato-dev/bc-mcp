"""
Práctica 02 — Descubrir Capacidades del Server MCP

Goal: Use list_tools(), list_resources(), and list_prompts() to dynamically
discover everything the server offers — without hardcoding any names.

Instructions: uncomment each section labeled PASO 1–4 in order.
Run with: uv run python client.py
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = "../../../../week-07-mcp_server_avanzado/3-proyecto/solution/src/server.py"


async def main() -> None:

    # ============================================================
    # PASO 1: Conectar al server (mismo patrón que práctica 01)
    # ============================================================
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
    # PASO 2: Listar tools con su schema completo
    # ============================================================
    # list_tools() returns ListToolsResult with a list of Tool objects.
    # Each Tool has:
    #   - name: str — exact name to use in call_tool()
    #   - description: str — human-readable description
    #   - inputSchema: dict — JSON Schema with properties and required
    #
    # Uncomment the following lines (inside the ClientSession block):
    #         tools_result = await session.list_tools()
    #         print(f"\n=== {len(tools_result.tools)} Tools ===")
    #         for tool in tools_result.tools:
    #             print(f"\n• {tool.name}")
    #             print(f"  {tool.description}")
    #             props = tool.inputSchema.get("properties", {})
    #             required = tool.inputSchema.get("required", [])
    #             for param, schema in props.items():
    #                 marker = "(*)" if param in required else "   "
    #                 tipo = schema.get("type", "any")
    #                 desc = schema.get("description", "")
    #                 desc_str = f" — {desc}" if desc else ""
    #                 print(f"  {marker} {param}: {tipo}{desc_str}")

    # ============================================================
    # PASO 3: Listar resources
    # ============================================================
    # list_resources() returns ListResourcesResult with a list of Resource.
    # Each Resource has:
    #   - uri: str — the URI to use in read_resource()
    #   - name: str — human-readable name
    #   - description: str — description
    #   - mimeType: str | None — content type
    #
    # Uncomment the following lines:
    #         resources_result = await session.list_resources()
    #         print(f"\n=== {len(resources_result.resources)} Resources ===")
    #         for r in resources_result.resources:
    #             mime = f" [{r.mimeType}]" if r.mimeType else ""
    #             print(f"• {r.uri}{mime}")
    #             if r.description:
    #                 print(f"  {r.description}")

    # ============================================================
    # PASO 4: Listar prompts con sus argumentos
    # ============================================================
    # list_prompts() returns ListPromptsResult with a list of Prompt.
    # Each Prompt has:
    #   - name: str — name to use in get_prompt()
    #   - description: str — description
    #   - arguments: list[PromptArgument] | None
    #       Each PromptArgument has: name, description, required
    #
    # Uncomment the following lines:
    #         prompts_result = await session.list_prompts()
    #         print(f"\n=== {len(prompts_result.prompts)} Prompts ===")
    #         for p in prompts_result.prompts:
    #             print(f"\n• {p.name}")
    #             if p.description:
    #                 print(f"  {p.description}")
    #             if p.arguments:
    #                 for arg in p.arguments:
    #                     req = "(requerido)" if arg.required else "(opcional)"
    #                     desc = f" — {arg.description}" if arg.description else ""
    #                     print(f"  - {arg.name} {req}{desc}")


if __name__ == "__main__":
    asyncio.run(main())
