---
description: "Genera un MCP Tool completo (Python y/o TypeScript) con schema de validación, implementación y test unitario."
mode: "agent"
---

Crea un MCP Tool completo siguiendo las convenciones del bootcamp bc-mcp.

## Información necesaria

Si no se especificó en la solicitud, pregunta:

1. **Nombre del tool** en `snake_case` (ej. `search_products`, `get_weather`, `run_query`)
2. **Descripción**: qué hace el tool (esta descripción la verá el LLM)
3. **Parámetros de entrada**: nombre, tipo, si es opcional y descripción de cada uno
4. **Tipo de retorno**: qué devuelve el tool (texto, JSON, lista, etc.)
5. **Lenguaje(s)**: Python, TypeScript o ambos
6. **Integración**: ¿DB, API externa, file system, cálculo puro?

## Python — archivos a generar

### src/tools/{tool_name}.py

```python
"""Tool: {tool_name} — {descripción breve}"""
from mcp.server.fastmcp import FastMCP

# mcp instance is imported from server.py
# This module registers the tool on import

def register(mcp: FastMCP) -> None:
    """Register the {tool_name} tool."""

    @mcp.tool()
    async def {tool_name}({params_with_types}) -> {return_type}:
        """{descripción completa del tool — el LLM la usa para decidir cuándo llamarlo}.

        Args:
            {param}: {descripción del parámetro}

        Returns:
            {descripción del retorno}
        """
        # TODO (proyecto) o implementación comentada (práctica)
        pass
```

### tests/test\_{tool_name}.py

```python
"""Tests for {tool_name} tool."""
import pytest
from mcp.shared.memory import create_connected_server_and_client_session

from src.server import mcp


@pytest.mark.asyncio
async def test_{tool_name}_basic():
    """Test basic functionality of {tool_name}."""
    async with create_connected_server_and_client_session(mcp._mcp_server) as (_, client):
        result = await client.call_tool("{tool_name}", {{test_args}})
        assert result.content[0].text is not None


@pytest.mark.asyncio
async def test_{tool_name}_invalid_input():
    """Test that invalid input raises an appropriate error."""
    async with create_connected_server_and_client_session(mcp._mcp_server) as (_, client):
        # Expect tool to handle gracefully or raise McpError
        result = await client.call_tool("{tool_name}", {{invalid_args}})
        assert result.isError or result.content[0].text
```

## TypeScript — archivos a generar

### src/tools/{toolName}.ts

```typescript
/**
 * Tool: {tool_name}
 * {descripción completa del tool}
 */
import { z } from "zod";
import type { Server } from "@modelcontextprotocol/sdk/server/index.js";

export function register{ToolName}Tool(server: Server): void {
  server.tool(
    "{tool_name}",
    {
      {param}: z.{type}().describe("{descripción}"),
      // parámetros adicionales...
    },
    async ({ {param} }) => {
      // implementación
      return {
        content: [{ type: "text", text: String(result) }],
      };
    }
  );
}
```

### tests/{toolName}.test.ts

```typescript
import { describe, it, expect, beforeAll, afterAll } from "vitest";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";
import { createServer } from "../src/index.js";

describe("{tool_name}", () => {
  let client: Client;

  beforeAll(async () => {
    const server = createServer();
    const [ct, st] = InMemoryTransport.createLinkedPair();
    await server.connect(st);
    client = new Client({ name: "test", version: "1.0.0" });
    await client.connect(ct);
  });

  afterAll(() => client.close());

  it("returns expected result for valid input", async () => {
    const result = await client.callTool({ name: "{tool_name}", arguments: { {test_args} } });
    expect(result.isError).toBeFalsy();
    expect((result.content[0] as { text: string }).text).toBeTruthy();
  });

  it("handles invalid input gracefully", async () => {
    const result = await client.callTool({ name: "{tool_name}", arguments: {} });
    // Zod validation should reject empty args
    expect(result.isError).toBeTruthy();
  });
});
```

## Reglas de generación

- El docstring/JSDoc del tool debe ser descriptivo: el LLM lo usa para entender cuándo y cómo llamarlo
- Validar TODOS los inputs — nunca confiar en que el LLM pasará parámetros válidos
- Si el tool accede a DB: usar queries parametrizadas, nunca interpolación de strings
- Si el tool llama a una API: manejar errores HTTP con mensajes claros en el retorno
- Para errores: devolver `isError: true` con mensaje legible en lugar de lanzar excepciones no controladas
- Incluir al menos 2 tests: caso feliz + caso de error/input inválido
