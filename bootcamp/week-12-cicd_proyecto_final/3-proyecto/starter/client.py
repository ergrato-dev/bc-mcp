"""MCP Library Client — Agente LLM con Claude.

Cliente MCP que usa Claude como LLM para interpretar preguntas
en lenguaje natural y ejecutar tools del servidor.

Transport: HTTP + SSE (conecta al server en puerto 8000)
"""

import asyncio
import os

# ============================================
# TODO 1: Imports necesarios
# ============================================
# from anthropic import Anthropic
# from mcp.client.sse import sse_client
# from mcp import ClientSession


# ============================================
# TODO 2: Configuración desde variables de entorno
# ============================================
# Lee ANTHROPIC_API_KEY, MCP_SERVER_URL, ANTHROPIC_MODEL desde os.environ
#
# ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]  # Obligatorio
# MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://mcp-server:8000/sse")
# ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-5")
# MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))


# ============================================
# TODO 3: Función para convertir tools MCP a formato Anthropic
# ============================================
# Claude necesita los tools en formato específico.
# Cada tool MCP tiene: name, description, inputSchema
# Anthropic espera: {"name", "description", "input_schema"}
#
# def mcp_tools_to_anthropic(mcp_tools: list) -> list[dict]:
#     """Convert MCP tool definitions to Anthropic API format."""
#     # TODO: Mapear cada tool al formato {"name": ..., "description": ..., "input_schema": ...}
#     pass


# ============================================
# TODO 4: Agentic loop principal
# ============================================
# El agentic loop:
# 1. Envía el mensaje del usuario a Claude con los tools disponibles
# 2. Si Claude llama un tool, ejecutarlo vía MCP y enviar resultado
# 3. Repetir hasta que Claude dé una respuesta sin llamadas a tools
#
# async def agent_loop(user_message: str, session: "ClientSession") -> str:
#     """Run the agentic loop: LLM decides which tools to call."""
#     # TODO: Obtener tools disponibles del servidor MCP (session.list_tools)
#     # TODO: Convertir a formato Anthropic con mcp_tools_to_anthropic
#     # TODO: Inicializar messages = [{"role": "user", "content": user_message}]
#     # TODO: Loop hasta MAX_ITERATIONS:
#     #   - Llamar a Anthropic API con messages + tools
#     #   - Si stop_reason == "end_turn": retornar respuesta de texto
#     #   - Si stop_reason == "tool_use": ejecutar cada tool_use block
#     #     - session.call_tool(name, arguments)
#     #     - Añadir resultado a messages como role "user" (tool_result)
#     pass


# ============================================
# TODO 5: Función principal interactiva
# ============================================
# Conecta al servidor MCP y acepta preguntas del usuario.
#
# async def main() -> None:
#     """Connect to MCP server and start interactive chat."""
#     print(f"Conectando al servidor MCP en {MCP_SERVER_URL}...")
#
#     # TODO: Usar sse_client para conectar al server
#     # async with sse_client(MCP_SERVER_URL) as (read, write):
#     #     async with ClientSession(read, write) as session:
#     #         await session.initialize()
#     #         print("✅ Conectado. Escribe tu pregunta (o 'salir' para terminar):")
#     #
#     #         while True:
#     #             user_input = input("\n> ").strip()
#     #             if user_input.lower() in ("salir", "exit", "quit"):
#     #                 break
#     #             if not user_input:
#     #                 continue
#     #
#     #             response = await agent_loop(user_input, session)
#     #             print(f"\n{response}")
#
#     pass


if __name__ == "__main__":
    asyncio.run(main())  # type: ignore[name-defined]
