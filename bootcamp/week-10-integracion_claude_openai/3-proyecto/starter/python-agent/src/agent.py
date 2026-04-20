"""
agent.py — Agente Claude con agentic loop y conexión a MCP Server.

Punto de entrada del proyecto. Conecta al Library Server (semana 07),
convierte sus tools al formato de Anthropic y ejecuta el bucle de agente.

TODO: Implementar las 4 funciones marcadas con TODO.
"""
import asyncio

# ── Imports necesarios (no modificar) ─────────────────────────────────────────
# Importa las dependencias que necesitas:
# - anthropic.Anthropic
# - mcp.ClientSession, mcp.StdioServerParameters
# - mcp.client.stdio.stdio_client
# - src.config (las constantes de configuración)
# - src.tools (convert_mcp_tools_for_claude, call_mcp_tool)
#
# TODO: añadir los imports aquí


# ── Constante de prompt (puedes modificarla para probar) ──────────────────────
USER_PROMPT: str = (
    "Busca libros de Python en la base de datos. "
    "Si hay menos de 2, añade uno llamado 'Python Moderno 2025'. "
    "Al final dime cuántos libros de Python hay en total."
)


# ══════════════════════════════════════════════════════════════════════════════
# TODO 1: Función connect_to_server
# ══════════════════════════════════════════════════════════════════════════════
async def connect_to_server(session: ClientSession) -> list:
    """
    Inicializa la sesión MCP y devuelve la lista de tools disponibles.

    Args:
        session: ClientSession ya creada (el context manager la pasa)

    Returns:
        Lista de MCPTool con las tools del server

    TODO: Implementar esta función.
    # 1. Llamar await session.initialize()
    # 2. Llamar await session.list_tools() y guardar el resultado
    # 3. Imprimir los nombres de las tools disponibles
    # 4. Retornar result.tools
    """
    pass   # TODO: reemplazar con la implementación


# ══════════════════════════════════════════════════════════════════════════════
# TODO 2: Función dispatch_tool_calls
# ══════════════════════════════════════════════════════════════════════════════
async def dispatch_tool_calls(response: object, session: ClientSession) -> list[dict]:
    """
    Ejecuta todos los tool_use blocks de la respuesta via MCP.

    Itera sobre response.content buscando blocks de tipo "tool_use".
    Para cada uno: ejecuta la tool y construye el bloque tool_result.

    Args:
        response: Respuesta de Anthropic (messages.create)
        session:  Sesión MCP activa

    Returns:
        Lista de bloques tool_result para añadir al historial de mensajes

    TODO: Implementar esta función.
    # 1. Crear lista vacía tool_results = []
    # 2. Para cada block en response.content:
    #    a. Si block.type != "tool_use": continuar
    #    b. Imprimir qué tool se va a llamar y con qué argumentos
    #    c. Llamar a call_mcp_tool(session, block.name, block.input)
    #    d. Imprimir el resultado (primeros 100 chars)
    #    e. Añadir a tool_results el dict:
    #       {"type": "tool_result", "tool_use_id": block.id, "content": content}
    # 3. Retornar tool_results
    """
    pass   # TODO: reemplazar con la implementación


# ══════════════════════════════════════════════════════════════════════════════
# TODO 3: Función agentic_loop
# ══════════════════════════════════════════════════════════════════════════════
async def agentic_loop(
    client: object,
    session: ClientSession,
    tools: list[dict],
) -> str:
    """
    Bucle principal del agente.

    Llama a Claude con las tools disponibles, ejecuta las tools que pida
    y repite hasta que stop_reason sea "end_turn" o se alcance MAX_ITERATIONS.

    Args:
        client: Cliente de Anthropic inicializado
        session: Sesión MCP activa
        tools:  Lista de tools en formato Anthropic (output de convert_mcp_tools_for_claude)

    Returns:
        Texto de la respuesta final del agente

    TODO: Implementar esta función.
    # 1. Inicializar: messages = [{"role": "user", "content": USER_PROMPT}]
    #                 iteration = 0
    # 2. Mientras iteration < MAX_ITERATIONS:
    #    a. Incrementar iteration
    #    b. Llamar a client.messages.create(model=MODEL, max_tokens=MAX_TOKENS,
    #                                       tools=tools, messages=messages)
    #    c. Imprimir la iteración y el stop_reason
    #    d. Si stop_reason == "end_turn":
    #       - Buscar en response.content el block con atributo .text
    #       - Retornar ese texto
    #    e. Si stop_reason == "tool_use":
    #       - Llamar a dispatch_tool_calls(response, session)
    #       - Añadir el mensaje assistant al historial
    #       - Añadir los tool_results al historial (role: "user")
    #    f. En otro caso: break
    # 3. Si el loop termina sin respuesta, retornar mensaje de error
    """
    pass   # TODO: reemplazar con la implementación


# ══════════════════════════════════════════════════════════════════════════════
# TODO 4: Función main
# ══════════════════════════════════════════════════════════════════════════════
async def main() -> None:
    """
    Punto de entrada del agente:
    1. Crear el cliente Anthropic
    2. Abrir la conexión al MCP Server con stdio_client + ClientSession
    3. Obtener y convertir las tools
    4. Ejecutar el agentic loop
    5. Imprimir la respuesta final

    TODO: Implementar esta función.
    # 1. Crear: client = Anthropic(api_key=ANTHROPIC_API_KEY)
    # 2. Crear: params = StdioServerParameters(
    #               command="python",
    #               args=[SERVER_SCRIPT],
    #               env={"DB_PATH": DB_PATH},
    #           )
    # 3. Usar context managers anidados:
    #    async with stdio_client(params) as (stdio, write):
    #        async with ClientSession(stdio, write) as session:
    #            mcp_tools = await connect_to_server(session)
    #            anthropic_tools = convert_mcp_tools_for_claude(mcp_tools)
    #            answer = await agentic_loop(client, session, anthropic_tools)
    #            print("=" * 60)
    #            print("RESPUESTA FINAL:")
    #            print(answer)
    #            print("=" * 60)
    """
    pass   # TODO: reemplazar con la implementación


if __name__ == "__main__":
    asyncio.run(main())
