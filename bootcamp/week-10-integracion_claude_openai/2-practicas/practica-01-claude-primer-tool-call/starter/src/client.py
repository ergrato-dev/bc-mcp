"""
Práctica 01 — Claude: Primer Tool Call

Conecta al Library Server, convierte sus tools al formato Anthropic
y realiza una sola llamada para detectar el bloque tool_use.

Instrucciones: descomenta cada sección PASO N y ejecuta el script.
"""
import asyncio

# ============================================================
# PASO 1: Inicializar el cliente Anthropic
# ============================================================
print("--- PASO 1: Inicializar cliente ---")

# Descomenta las siguientes líneas:
# import os
# from dotenv import load_dotenv
# from anthropic import Anthropic
#
# load_dotenv()
# ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
# MODEL = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-5")
# USER_PROMPT = "Busca libros sobre Python y muéstrame los resultados"
# client = Anthropic(api_key=ANTHROPIC_API_KEY)
# print("✓ Cliente Anthropic inicializado")


# ============================================================
# PASO 2: Conectar al MCP Server y obtener tools
# ============================================================
print("\n--- PASO 2: Conectar al MCP Server ---")

# Descomenta las siguientes líneas:
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
#
# SERVER_SCRIPT = os.getenv(
#     "SERVER_SCRIPT",
#     "../../../../week-07-servers_bd_apis_externas/3-proyecto/starter/python-server/src/server.py",
# )
#
# async def get_tools_from_server() -> list:
#     params = StdioServerParameters(
#         command="python",
#         args=[SERVER_SCRIPT],
#         env={"DB_PATH": os.getenv("DB_PATH", "books.db")},
#     )
#     async with stdio_client(params) as (stdio, write):
#         async with ClientSession(stdio, write) as session:
#             await session.initialize()
#             result = await session.list_tools()
#             print(f"Tools disponibles: {', '.join(t.name for t in result.tools)}")
#             return result.tools


# ============================================================
# PASO 3: Convertir tools al formato Anthropic
# ============================================================
print("\n--- PASO 3: Convertir tools para Anthropic ---")

# Descomenta las siguientes líneas:
# def convert_tools_for_anthropic(tools: list) -> list[dict]:
#     """Convierte MCP tools al formato de Anthropic: inputSchema → input_schema."""
#     return [
#         {
#             "name": t.name,
#             "description": t.description or "",
#             "input_schema": t.inputSchema,   # ← clave crítica
#         }
#         for t in tools
#     ]
# print("✓ Función de conversión definida")


# ============================================================
# PASO 4: Llamar a la API de Anthropic con las tools
# ============================================================
print("\n--- PASO 4: Primera llamada a la API ---")

# Descomenta las siguientes líneas:
# async def first_tool_call() -> None:
#     mcp_tools = await get_tools_from_server()
#     anthropic_tools = convert_tools_for_anthropic(mcp_tools)
#
#     messages = [{"role": "user", "content": USER_PROMPT}]
#
#     response = client.messages.create(
#         model=MODEL,
#         max_tokens=1024,
#         tools=anthropic_tools,
#         messages=messages,
#     )
#
#     print(f"stop_reason: {response.stop_reason}")
#     print(f"blocks recibidos: {len(response.content)}")


# ============================================================
# PASO 5: Inspeccionar el bloque tool_use
# ============================================================
print("\n--- PASO 5: Leer el bloque tool_use ---")

# Descomenta las siguientes líneas (dentro de first_tool_call, tras el create):
#     if response.stop_reason == "tool_use":
#         for block in response.content:
#             if block.type == "tool_use":
#                 print(f"  tool solicitada: {block.name}")
#                 print(f"  tool_use_id:     {block.id}")
#                 print(f"  argumentos:      {block.input}")
#     elif response.stop_reason == "end_turn":
#         print("  El modelo respondió directamente sin usar tools")
#         print(f"  Respuesta: {response.content[-1].text[:200]}")


# ============================================================
# MAIN — ejecutar cuando todos los pasos estén descomentados
# ============================================================
if __name__ == "__main__":
    # Cuando hayas descomentado todos los pasos, cambia esto por:
    # asyncio.run(first_tool_call())
    print("\n⚠️  Descomenta todos los pasos y luego ejecuta asyncio.run(first_tool_call())")
