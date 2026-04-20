"""
conftest.py — Fixtures compartidas para la suite de tests del Library Server.

Implementa las dos fixtures requeridas:
  TODO 1: fixture db — SQLite en memoria
  TODO 2: fixture mcp_client — client MCP en memoria con DB en memoria
"""
import pytest
from mcp.shared.memory import create_connected_server_and_client_session


# ============================================================
# TODO 1: Fixture de base de datos en memoria
# ============================================================
# Crea una conexión SQLite en memoria para cada test.
# El estado de la DB es destruido al terminar el test (aislamiento).
#
# Pasos:
# 1. Importar aiosqlite
# 2. Decorar con @pytest.fixture y async def db():
# 3. Abrir conexión: async with aiosqlite.connect(":memory:") as conn:
# 4. Configurar: conn.row_factory = aiosqlite.Row
# 5. Importar y llamar: from src.server import _init_schema; await _init_schema(conn)
# 6. yield conn


# ============================================================
# TODO 2: Fixture del client MCP conectado al server
# ============================================================
# Conecta el client MCP al Library Server usando DB en memoria.
# create_connected_server_and_client_session gestiona el protocolo MCP completo.
#
# Pasos:
# 1. Decorar con @pytest.fixture y async def mcp_client(monkeypatch):
# 2. monkeypatch.setenv("DB_PATH", ":memory:")
# 3. from src.server import mcp
# 4. async with create_connected_server_and_client_session(mcp._mcp_server) as (_, client):
# 5. yield client
