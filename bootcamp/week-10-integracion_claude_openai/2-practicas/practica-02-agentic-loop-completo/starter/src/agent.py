"""
Práctica 02 — Agentic Loop Completo con Claude

Implementa el while-loop completo: Claude decide qué tools usar,
las ejecuta via MCP y genera una respuesta final (end_turn).

Instrucciones: descomenta cada sección PASO N y ejecuta el script.
"""
import asyncio

# ============================================================
# PASO 1: Imports y configuración
# ============================================================
print("--- PASO 1: Imports y configuración ---")

# Descomenta las siguientes líneas:
# import os
# from dotenv import load_dotenv
# from anthropic import Anthropic
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
#
# load_dotenv()
# ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
# MODEL = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-5")
# SERVER_SCRIPT = os.getenv(
#     "SERVER_SCRIPT",
#     "../../../../week-07-servers_bd_apis_externas/3-proyecto/starter/python-server/src/server.py",
# )
# DB_PATH = os.getenv("DB_PATH", "books.db")
# MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
# USER_PROMPT = "Busca libros de Python. Si encuentras menos de 3, añade uno llamado 'MCP en Python' del año 2024."
#
# client = Anthropic(api_key=ANTHROPIC_API_KEY)
# print(f"✓ Cliente listo | modelo: {MODEL}")


# ============================================================
# PASO 2: Conectar al server y convertir tools
# ============================================================
print("\n--- PASO 2: Conectar al MCP Server ---")

# Descomenta las siguientes líneas:
# async def connect_and_get_tools(session: ClientSession) -> list[dict]:
#     """Inicializa la sesión, lista las tools y las convierte al formato Anthropic."""
#     await session.initialize()
#     result = await session.list_tools()
#     print(f"✓ Tools disponibles: {', '.join(t.name for t in result.tools)}")
#     return [
#         {
#             "name": t.name,
#             "description": t.description or "",
#             "input_schema": t.inputSchema,   # Anthropic usa input_schema
#         }
#         for t in result.tools
#     ]


# ============================================================
# PASO 3: Despachador de tool calls
# ============================================================
print("\n--- PASO 3: Despachador de tools ---")

# Descomenta las siguientes líneas:
# async def dispatch_tool_calls(response: object, session: ClientSession) -> list[dict]:
#     """
#     Ejecuta todos los tool_use blocks via MCP.
#     Devuelve lista de tool_result blocks para el siguiente turno de Anthropic.
#     """
#     tool_results = []
#     for block in response.content:
#         if block.type != "tool_use":
#             continue
#         print(f"  → Llamando tool: {block.name}({block.input})")
#         result = await session.call_tool(block.name, block.input)
#         content = result.content[0].text if result.content else ""
#         print(f"  ← Resultado: {content[:100]}{'...' if len(content) > 100 else ''}")
#         tool_results.append({
#             "type": "tool_result",
#             "tool_use_id": block.id,   # CRÍTICO: vincular con el tool_use block
#             "content": content,
#         })
#     return tool_results


# ============================================================
# PASO 4: El agentic loop
# ============================================================
print("\n--- PASO 4: Agentic loop ---")

# Descomenta las siguientes líneas:
# async def agentic_loop(session: ClientSession, tools: list[dict]) -> str:
#     """
#     Bucle principal: llama al LLM, ejecuta tools y repite
#     hasta que stop_reason == 'end_turn' o se alcanza MAX_ITERATIONS.
#     """
#     messages = [{"role": "user", "content": USER_PROMPT}]
#     iteration = 0
#
#     while iteration < MAX_ITERATIONS:
#         iteration += 1
#
#         response = client.messages.create(
#             model=MODEL,
#             max_tokens=4096,
#             tools=tools,
#             messages=messages,
#         )
#
#         print(f"\n[Iteración {iteration}] stop_reason: {response.stop_reason}")
#
#         if response.stop_reason == "end_turn":
#             for block in response.content:
#                 if hasattr(block, "text"):
#                     return block.text
#             return ""
#
#         if response.stop_reason == "tool_use":
#             tool_results = await dispatch_tool_calls(response, session)
#             messages.append({"role": "assistant", "content": response.content})
#             messages.append({"role": "user", "content": tool_results})
#         else:
#             break
#
#     return "Error: límite de iteraciones alcanzado."


# ============================================================
# PASO 5: Observar el historial de mensajes
# ============================================================
print("\n--- PASO 5: Observar historial ---")

# Modifica agentic_loop para añadir este print justo antes del while loop check:
#         print(f"  mensajes en historial: {len(messages)}")
# Esto te mostrará cómo crece el array messages en cada iteración.


# ============================================================
# MAIN
# ============================================================
async def main() -> None:
    # Cuando hayas descomentado todos los pasos, descomenta lo siguiente:
    # params = StdioServerParameters(
    #     command="python",
    #     args=[SERVER_SCRIPT],
    #     env={"DB_PATH": DB_PATH},
    # )
    # async with stdio_client(params) as (stdio, write):
    #     async with ClientSession(stdio, write) as session:
    #         tools = await connect_and_get_tools(session)
    #         answer = await agentic_loop(session, tools)
    #         print(f"\n{'='*60}")
    #         print("RESPUESTA FINAL:")
    #         print(answer)
    print("⚠️  Descomenta todos los pasos para ejecutar el agente")


if __name__ == "__main__":
    asyncio.run(main())
