---
applyTo: "**/*.ts"
---

# Convenciones TypeScript para bc-mcp

## Versión y entorno

- Node.js 22+ obligatorio
- TypeScript 5.x con modo estricto (`"strict": true` en `tsconfig.json`)
- ESM modules: `import/export` nativo, sin `require()`
- Top-level `await` donde aplique

## MCP SDK (`@modelcontextprotocol/sdk`)

- Usar `Server` de `@modelcontextprotocol/sdk/server/index.js`
- Validación de inputs con **Zod** obligatoria en todos los tools y resources
- Nombres de tools: `snake_case` (ej. `search_files`, `get_weather`)
- Transportes: `StdioServerTransport` para stdio, `SSEServerTransport` para HTTP

```typescript
// ✅ CORRECTO — tipos estrictos con Zod
import { z } from "zod";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({ name: "my-server", version: "1.0.0" });

server.tool(
  "search_files",
  {
    pattern: z.string().describe("Glob pattern to search"),
    directory: z.string().optional().default("."),
  },
  async ({ pattern, directory }) => {
    const files = await glob(pattern, { cwd: directory });
    return { content: [{ type: "text", text: files.join("\n") }] };
  },
);

// ❌ INCORRECTO — sin tipado Zod
server.tool("search_files", {}, async (args) => {
  return { content: [{ type: "text", text: "" }] };
});
```

## Validación de inputs

- Zod es la fuente de verdad del schema — nunca usar `any` o `unknown` sin validar
- Para queries a DB: siempre parámetros preparados, nunca interpolación de strings

```typescript
// ✅ CORRECTO — query parametrizada
const rows = await db.all("SELECT * FROM items WHERE name LIKE ? LIMIT ?", [
  `%${query}%`,
  limit,
]);

// ❌ INCORRECTO — inyección SQL
const rows = await db.all(`SELECT * FROM items WHERE name LIKE '%${query}%'`);
```

## Gestión de paquetes

- Usar `pnpm` exclusivamente (nunca `npm` ni `yarn`)
- Versiones **siempre exactas** en `package.json`, sin `^`, `~`, `>=` ni `*`

```json
// ✅ CORRECTO
{
  "dependencies": {
    "@modelcontextprotocol/sdk": "1.10.2",
    "zod": "3.24.2"
  }
}

// ❌ INCORRECTO
{
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0",
    "zod": "~3.24"
  }
}
```

## Estructura del servidor

```typescript
// src/index.ts — punto de entrada estándar
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { registerTools } from "./tools/index.js";
import { registerResources } from "./resources/index.js";
import { registerPrompts } from "./prompts/index.js";

const server = new Server({ name: "my-mcp-server", version: "1.0.0" });

registerTools(server);
registerResources(server);
registerPrompts(server);

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Testing

- Framework: `vitest`
- Usar `InMemoryTransport` de `@modelcontextprotocol/sdk/inMemory.js` para tests
- Un archivo de test por módulo: `tests/tools.test.ts`, `tests/resources.test.ts`

```typescript
import { describe, it, expect, beforeEach } from "vitest";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";

describe("search_files tool", () => {
  it("should return matching files", async () => {
    const [clientTransport, serverTransport] =
      InMemoryTransport.createLinkedPair();
    await server.connect(serverTransport);
    const client = new Client({ name: "test-client", version: "1.0.0" });
    await client.connect(clientTransport);

    const result = await client.callTool({
      name: "search_files",
      arguments: { pattern: "*.ts" },
    });
    expect(result.content).toHaveLength(1);
  });
});
```

## tsconfig.json mínimo recomendado

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  }
}
```
