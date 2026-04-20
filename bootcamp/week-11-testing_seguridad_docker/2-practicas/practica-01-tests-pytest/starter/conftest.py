"""
conftest.py — Fixtures compartidas para todos los tests.

Pasos a descomentar:
  PASO 1: fixture db — SQLite en memoria
  PASO 2: fixture mcp_client — client MCP en memoria
"""
import pytest
import sys
import os

# Añadir el directorio raíz al path para importar el server
# Apunta al server de semana 07 (ajusta si usas tu propia copia)
SERVER_PATH = os.path.join(
    os.path.dirname(__file__),
    "..", "..", "..", "..", "..",
    "week-07-servers_bd_apis_externas",
    "3-proyecto", "starter", "python-server"
)
sys.path.insert(0, SERVER_PATH)


# ============================================================
# PASO 1: Fixture de base de datos en memoria
# ============================================================
# Esta fixture crea una conexión SQLite en memoria para cada test.
# La DB es destruida automáticamente al terminar el test.
#
# Descomenta las siguientes líneas:
# import aiosqlite
#
# @pytest.fixture
# async def db():
#     """SQLite en memoria — estado limpio para cada test."""
#     async with aiosqlite.connect(":memory:") as conn:
#         conn.row_factory = aiosqlite.Row
#         # Importar e inicializar el esquema del server
#         from src.server import _init_schema
#         await _init_schema(conn)
#         yield conn


# ============================================================
# PASO 2: Fixture del client MCP conectado al server en memoria
# ============================================================
# Esta fixture crea un client MCP conectado al Library Server.
# Usa DB en memoria para que cada test tenga datos frescos.
#
# Descomenta las siguientes líneas:
# from mcp.shared.memory import create_connected_server_and_client_session
#
# @pytest.fixture
# async def mcp_client(monkeypatch):
#     """
#     Client MCP conectado al server en memoria.
#     Cada test obtiene un server limpio con DB vacía.
#     """
#     # Usar DB en memoria para tests aislados
#     monkeypatch.setenv("DB_PATH", ":memory:")
#
#     from src.server import mcp
#
#     async with create_connected_server_and_client_session(
#         mcp._mcp_server
#     ) as (_, client):
#         yield client
#
# @pytest.fixture
# async def test_list_tools(mcp_client):
#     """Test mínimo para verificar que el server arranca y expone tools."""
#     tools = await mcp_client.list_tools()
#     tool_names = [t.name for t in tools.tools]
#     assert "add_book" in tool_names
#     assert "search_books" in tool_names
#     assert "get_book" in tool_names
