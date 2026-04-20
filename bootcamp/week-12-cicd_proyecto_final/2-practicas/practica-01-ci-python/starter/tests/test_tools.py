"""Tests for the CI practice MCP server.

INSTRUCCIONES: Descomenta las secciones indicadas en cada PASO.
"""

import json
import pytest


# ============================================
# PASO 3: Tests del tool `add`
# ============================================
# Estos tests verifican que el tool `add` funciona correctamente.
# Descomenta las siguientes clases y métodos:

# class TestAddTool:
#     async def test_add_positive_numbers(self, mcp_client):
#         """add(2, 3) debe retornar {"result": 5}."""
#         result = await mcp_client.call_tool("add", {"a": 2, "b": 3})
#         data = json.loads(result.content[0].text)
#         assert data["result"] == 5
#
#     async def test_add_negative_numbers(self, mcp_client):
#         """add(-1, -1) debe retornar {"result": -2}."""
#         result = await mcp_client.call_tool("add", {"a": -1, "b": -1})
#         data = json.loads(result.content[0].text)
#         assert data["result"] == -2
#
#     async def test_add_zero(self, mcp_client):
#         """add(0, 0) debe retornar {"result": 0}."""
#         result = await mcp_client.call_tool("add", {"a": 0, "b": 0})
#         data = json.loads(result.content[0].text)
#         assert data["result"] == 0


# ============================================
# PASO 4: Tests del tool `greet`
# ============================================
# Descomenta la siguiente clase:

# class TestGreetTool:
#     async def test_greet_spanish(self, mcp_client):
#         """greet en español debe retornar saludo correcto."""
#         result = await mcp_client.call_tool("greet", {"name": "Ana", "language": "es"})
#         data = json.loads(result.content[0].text)
#         assert data["greeting"] == "Hola, Ana!"
#
#     async def test_greet_english(self, mcp_client):
#         """greet en inglés debe retornar saludo correcto."""
#         result = await mcp_client.call_tool("greet", {"name": "Bob", "language": "en"})
#         data = json.loads(result.content[0].text)
#         assert data["greeting"] == "Hello, Bob!"
#
#     async def test_greet_default_language(self, mcp_client):
#         """greet sin language debe usar español por defecto."""
#         result = await mcp_client.call_tool("greet", {"name": "Carlos"})
#         data = json.loads(result.content[0].text)
#         assert data["greeting"] == "Hola, Carlos!"
#
#     async def test_greet_unsupported_language(self, mcp_client):
#         """greet con idioma no soportado debe retornar error."""
#         result = await mcp_client.call_tool("greet", {"name": "Ana", "language": "zh"})
#         data = json.loads(result.content[0].text)
#         assert "error" in data


# ============================================
# PASO 5: Test de lista de tools disponibles
# ============================================
# Descomenta la siguiente función:

# async def test_list_tools(mcp_client):
#     """El server debe exponer exactamente 2 tools: add y greet."""
#     tools_result = await mcp_client.list_tools()
#     tool_names = {t.name for t in tools_result.tools}
#     assert tool_names == {"add", "greet"}
