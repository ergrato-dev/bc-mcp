"""Test fixtures for MCP Library Server tests."""

import pytest
from mcp.shared.memory import create_connected_server_and_client_session

# ============================================
# TODO 1: Importar el servidor para los tests
# ============================================
# from src.server import mcp, init_db


# ============================================
# TODO 2: Fixture que inicializa la BD en memoria
# ============================================
# Usa DB_PATH = ":memory:" para tests (no escribir en disco).
#
# @pytest.fixture(autouse=True)
# def setup_test_db(tmp_path, monkeypatch):
#     """Use a temporary SQLite database for each test."""
#     # TODO: Monkeypatch DB_PATH en src.server a ":memory:"
#     # TODO: Llamar a init_db() para crear las tablas
#     pass


# ============================================
# TODO 3: Fixture del cliente MCP para tests
# ============================================
# Crea una sesión en memoria usando el servidor importado.
#
# @pytest.fixture
# async def mcp_client():
#     """Create an in-memory MCP client connected to the library server."""
#     # TODO: Usar create_connected_server_and_client_session(mcp._mcp_server)
#     # async with create_connected_server_and_client_session(mcp._mcp_server) as (_, client):
#     #     yield client
#     pass
