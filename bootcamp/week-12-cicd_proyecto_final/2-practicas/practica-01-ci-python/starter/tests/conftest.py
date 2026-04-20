"""Shared fixtures for CI practice tests."""

import pytest
from mcp.shared.memory import create_connected_server_and_client_session

from src.server import mcp


@pytest.fixture
async def mcp_client():
    """Create an in-memory MCP client connected to the server."""
    async with create_connected_server_and_client_session(mcp._mcp_server) as (_, client):
        yield client
