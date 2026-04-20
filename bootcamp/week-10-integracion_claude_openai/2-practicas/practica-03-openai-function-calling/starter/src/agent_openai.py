"""
Práctica 03 — OpenAI: Function Calling

Mismo agentic loop que la Práctica 02 pero usando la API de OpenAI.
Observa las diferencias en el formato de mensajes y las señales de control.

Instrucciones: descomenta cada sección PASO N y ejecuta el script.
"""
import asyncio

# ============================================================
# PASO 1: Imports y cliente OpenAI
# ============================================================
print("--- PASO 1: Imports y cliente OpenAI ---")

# Descomenta las siguientes líneas:
# import os
# import json
# from dotenv import load_dotenv
# from openai import OpenAI
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
#
# load_dotenv()
# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
# SERVER_SCRIPT = os.getenv(
#     "SERVER_SCRIPT",
#     "../../../../week-07-servers_bd_apis_externas/3-proyecto/starter/python-server/src/server.py",
# )
# DB_PATH = os.getenv("DB_PATH", "books.db")
# MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
# USER_PROMPT = "Busca libros de Python. Si encuentras menos de 3, añade uno llamado 'MCP en Python' del año 2024."
#
# client = OpenAI(api_key=OPENAI_API_KEY)   # ← OpenAI, no Anthropic
# print(f"✓ Cliente OpenAI listo | modelo: {MODEL}")


# ============================================================
# PASO 2: Convertir tools al formato OpenAI
# ============================================================
print("\n--- PASO 2: Convertir tools para OpenAI ---")

# Descomenta las siguientes líneas:
# async def connect_and_get_tools_openai(session: ClientSession) -> list[dict]:
#     """Conecta al server MCP y convierte las tools al formato OpenAI."""
#     await session.initialize()
#     result = await session.list_tools()
#     print(f"✓ Tools: {', '.join(t.name for t in result.tools)}")
#     return [
#         {
#             "type": "function",            # ← wrapper que requiere OpenAI
#             "function": {                  # ← envolver en "function"
#                 "name": t.name,
#                 "description": t.description or "",
#                 "parameters": t.inputSchema,  # ← "parameters", no "input_schema"
#             },
#         }
#         for t in result.tools
#     ]


# ============================================================
# PASO 3: Detectar finish_reason y extraer tool_calls
# ============================================================
print("\n--- PASO 3: Procesar finish_reason ---")

# Al inspeccionar la respuesta de OpenAI, la estructura es diferente:
# response.choices[0].finish_reason     → "tool_calls" o "stop"
# response.choices[0].message.tool_calls → lista de tool calls
#
# Descomenta las siguientes líneas para ver cómo se accede:
# def inspect_response(response: object) -> None:
#     """Muestra los detalles de la respuesta de OpenAI."""
#     choice = response.choices[0]
#     print(f"finish_reason: {choice.finish_reason}")
#     if choice.finish_reason == "tool_calls":
#         for tc in choice.message.tool_calls:
#             args = json.loads(tc.function.arguments)   # ← parsear JSON string
#             print(f"  tool: {tc.function.name}")
#             print(f"  id:   {tc.id}")
#             print(f"  args: {args}")
#     elif choice.finish_reason == "stop":
#         print(f"  respuesta: {choice.message.content[:200]}")


# ============================================================
# PASO 4: Despachador y construcción de tool results
# ============================================================
print("\n--- PASO 4: Despachar tools y construir resultados ---")

# Descomenta las siguientes líneas:
# async def dispatch_and_build_results(response: object, session: ClientSession) -> list[dict]:
#     """
#     Ejecuta los tool_calls via MCP y devuelve los mensajes para el historial.
#     En OpenAI se devuelven dos tipos de mensajes:
#     1. El mensaje del assistant (con tool_calls)
#     2. Uno o más mensajes con role: "tool"
#     """
#     choice = response.choices[0]
#
#     # Mensaje del assistant con el tool_call
#     assistant_message = {
#         "role": "assistant",
#         "content": choice.message.content,   # puede ser None
#         "tool_calls": [
#             {
#                 "id": tc.id,
#                 "type": "function",
#                 "function": {
#                     "name": tc.function.name,
#                     "arguments": tc.function.arguments,
#                 },
#             }
#             for tc in choice.message.tool_calls
#         ],
#     }
#
#     tool_messages = []
#     for tc in choice.message.tool_calls:
#         args = json.loads(tc.function.arguments)
#         print(f"  → Llamando tool: {tc.function.name}({args})")
#         result = await session.call_tool(tc.function.name, args)
#         content = result.content[0].text if result.content else ""
#         print(f"  ← Resultado: {content[:100]}{'...' if len(content) > 100 else ''}")
#
#         tool_messages.append({
#             "role": "tool",              # ← "tool", no "user" como en Anthropic
#             "tool_call_id": tc.id,       # ← "tool_call_id", no "tool_use_id"
#             "content": content,
#         })
#
#     return [assistant_message] + tool_messages


# ============================================================
# PASO 5: Loop completo con OpenAI
# ============================================================
print("\n--- PASO 5: Agentic loop con OpenAI ---")

# Descomenta las siguientes líneas:
# async def agentic_loop_openai(session: ClientSession, tools: list[dict]) -> str:
#     """
#     Loop completo con OpenAI:
#     - finish_reason == "tool_calls" → ejecutar tools y continuar
#     - finish_reason == "stop"       → respuesta final, salir
#     """
#     messages = [{"role": "user", "content": USER_PROMPT}]
#     iteration = 0
#
#     while iteration < MAX_ITERATIONS:
#         iteration += 1
#
#         response = client.chat.completions.create(
#             model=MODEL,
#             max_tokens=4096,
#             tools=tools,
#             messages=messages,
#         )
#
#         choice = response.choices[0]
#         print(f"\n[Iteración {iteration}] finish_reason: {choice.finish_reason}")
#
#         if choice.finish_reason == "stop":
#             return choice.message.content or ""
#
#         if choice.finish_reason == "tool_calls":
#             new_messages = await dispatch_and_build_results(response, session)
#             messages.extend(new_messages)
#         else:
#             break
#
#     return "Error: límite de iteraciones alcanzado."


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
    #         tools = await connect_and_get_tools_openai(session)
    #         answer = await agentic_loop_openai(session, tools)
    #         print(f"\n{'='*60}")
    #         print("RESPUESTA FINAL (OpenAI):")
    #         print(answer)
    print("⚠️  Descomenta todos los pasos para ejecutar el agente OpenAI")


if __name__ == "__main__":
    asyncio.run(main())
