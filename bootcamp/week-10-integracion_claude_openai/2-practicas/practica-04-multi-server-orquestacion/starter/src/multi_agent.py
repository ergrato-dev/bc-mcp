"""
Práctica 04 — Multi-Server: Orquestación de N servidores MCP

Conecta a Library Server + Calculator Server simultáneamente.
Implementa el registro unificado de tools y el routing por tool_name.

Instrucciones: descomenta cada sección PASO N y ejecuta el script.
"""
import asyncio

# ============================================================
# PASO 1: Imports y configuraciones de los dos servers
# ============================================================
print("--- PASO 1: Imports y configuración multi-server ---")

# Descomenta las siguientes líneas:
# import os
# from contextlib import AsyncExitStack
# from dotenv import load_dotenv
# from anthropic import Anthropic
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
# from mcp.types import Tool as MCPTool
#
# load_dotenv()
# ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
# MODEL = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-5")
# MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "15"))
# USER_PROMPT = (
#     "Busca cuántos libros de Python hay en la base de datos, "
#     "multiplica ese número por 3 y añade un libro nuevo llamado "
#     "'Python Avanzado 2025' con ese resultado como año."
# )
#
# # Configuraciones de los dos servers
# SERVER_CONFIGS = [
#     {
#         "name": "library",
#         "command": "python",
#         "args": [os.getenv(
#             "LIBRARY_SERVER_SCRIPT",
#             "../../../../week-07-servers_bd_apis_externas/3-proyecto/starter/python-server/src/server.py",
#         )],
#         "env": {"DB_PATH": os.getenv("DB_PATH", "books.db")},
#     },
#     {
#         "name": "calculator",
#         "command": "python",
#         "args": [os.getenv("CALCULATOR_SERVER_SCRIPT", "servers/calculator_server.py")],
#         "env": None,
#     },
# ]
#
# client = Anthropic(api_key=ANTHROPIC_API_KEY)
# print(f"✓ Cliente listo | {len(SERVER_CONFIGS)} servers configurados")


# ============================================================
# PASO 2: Conectar a múltiples servers y construir registros
# ============================================================
print("\n--- PASO 2: Conectar a múltiples servers ---")

# Descomenta las siguientes líneas:
# async def connect_to_all_servers(
#     stack: AsyncExitStack,
# ) -> tuple[list[MCPTool], dict[str, ClientSession]]:
#     """
#     Conecta a todos los servers definidos en SERVER_CONFIGS.
#     Devuelve la lista unificada de tools y el mapa tool_name → session.
#     """
#     all_tools: list[MCPTool] = []
#     tool_to_session: dict[str, ClientSession] = {}
#
#     for config in SERVER_CONFIGS:
#         params = StdioServerParameters(
#             command=config["command"],
#             args=config["args"],
#             env=config.get("env"),
#         )
#         transport = await stack.enter_async_context(stdio_client(params))
#         session = await stack.enter_async_context(ClientSession(*transport))
#         await session.initialize()
#
#         result = await session.list_tools()
#         for tool in result.tools:
#             all_tools.append(tool)
#             tool_to_session[tool.name] = session   # routing: tool → session
#
#         print(f"  [{config['name']}] tools: {', '.join(t.name for t in result.tools)}")
#
#     print(f"\n✓ Total tools unificadas: {len(all_tools)}")
#     return all_tools, tool_to_session


# ============================================================
# PASO 3: Dispatch con routing por tool_name
# ============================================================
print("\n--- PASO 3: Dispatch con routing ---")

# Descomenta las siguientes líneas:
# async def dispatch_tool_call(
#     tool_name: str,
#     tool_input: dict,
#     tool_to_session: dict[str, ClientSession],
# ) -> str:
#     """
#     Despacha una tool call al server correcto usando el mapa de routing.
#     Si la tool no existe en ningún server, devuelve un mensaje de error.
#     """
#     session = tool_to_session.get(tool_name)
#     if session is None:
#         return f"Error: tool '{tool_name}' no registrada en ningún server."
#
#     print(f"  → Routing: {tool_name} → {session}")
#     result = await session.call_tool(tool_name, tool_input)
#     content = result.content[0].text if result.content else ""
#     print(f"  ← Resultado: {content[:120]}{'...' if len(content) > 120 else ''}")
#     return content


# ============================================================
# PASO 4: Loop unificado con todas las tools de ambos servers
# ============================================================
print("\n--- PASO 4: Agentic loop multi-server ---")

# Descomenta las siguientes líneas:
# async def multi_server_loop(
#     all_tools: list[MCPTool],
#     tool_to_session: dict[str, ClientSession],
# ) -> str:
#     """Loop que usa tools de todos los servers registrados."""
#     # Convertir al formato Anthropic
#     anthropic_tools = [
#         {"name": t.name, "description": t.description or "", "input_schema": t.inputSchema}
#         for t in all_tools
#     ]
#
#     messages = [{"role": "user", "content": USER_PROMPT}]
#     iteration = 0
#
#     while iteration < MAX_ITERATIONS:
#         iteration += 1
#         response = client.messages.create(
#             model=MODEL, max_tokens=4096, tools=anthropic_tools, messages=messages
#         )
#         print(f"\n[Iteración {iteration}] stop_reason: {response.stop_reason}")
#
#         if response.stop_reason == "end_turn":
#             for block in response.content:
#                 if hasattr(block, "text"):
#                     return block.text
#             return ""
#
#         if response.stop_reason == "tool_use":
#             tool_results = []
#             for block in response.content:
#                 if block.type != "tool_use":
#                     continue
#                 content = await dispatch_tool_call(block.name, block.input, tool_to_session)
#                 tool_results.append({
#                     "type": "tool_result",
#                     "tool_use_id": block.id,
#                     "content": content,
#                 })
#             messages.append({"role": "assistant", "content": response.content})
#             messages.append({"role": "user", "content": tool_results})
#         else:
#             break
#
#     return "Error: límite de iteraciones alcanzado."


# ============================================================
# PASO 5: Prompt multi-dominio y observar el routing
# ============================================================
print("\n--- PASO 5: Ejecutar con prompt multi-dominio ---")

# La variable USER_PROMPT del PASO 1 usa herramientas de ambos servers.
# Al ejecutar verás cómo el routing despacha:
#   - search_books  → Library Server (session 1)
#   - multiply      → Calculator Server (session 2)
#   - add_book      → Library Server (session 1)
# Modifica USER_PROMPT en PASO 1 para experimentar con distintas combinaciones.


# ============================================================
# MAIN
# ============================================================
async def main() -> None:
    # Cuando hayas descomentado todos los pasos, descomenta lo siguiente:
    # async with AsyncExitStack() as stack:
    #     all_tools, tool_to_session = await connect_to_all_servers(stack)
    #     answer = await multi_server_loop(all_tools, tool_to_session)
    #     print(f"\n{'='*60}")
    #     print("RESPUESTA FINAL (multi-server):")
    #     print(answer)
    print("⚠️  Descomenta todos los pasos para ejecutar el agente multi-server")


if __name__ == "__main__":
    asyncio.run(main())
