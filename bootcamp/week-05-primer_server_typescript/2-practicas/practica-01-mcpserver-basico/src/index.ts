// ============================================
// SECCIÓN A — Imports y creación del servidor
// ============================================
// Descomenta las siguientes líneas:
// import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
// import { z } from "zod";
//
// const server = new McpServer({
//   name: "practice-01",
//   version: "1.0.0",
// });

// ============================================
// SECCIÓN B — Registrar el tool "add"
// ============================================
// Descomenta las siguientes líneas (requiere Sección A):
// server.tool(
//   "add",
//   "Add two numbers and return the result",
//   { a: z.number(), b: z.number() },
//   async ({ a, b }) => ({
//     content: [{ type: "text", text: String(a + b) }],
//   }),
// );

// ============================================
// SECCIÓN D — Registrar el tool "greet"
// ============================================
// Descomenta las siguientes líneas (requiere Sección A):
// server.tool(
//   "greet",
//   "Greet a person by name",
//   { name: z.string().describe("The name of the person to greet") },
//   async ({ name }) => ({
//     content: [{ type: "text", text: `Hello, ${name}! Welcome to MCP TypeScript.` }],
//   }),
// );

// ============================================
// SECCIÓN C — Conectar el transport
// ============================================
// Descomenta las siguientes líneas (requiere Secciones A, B y D):
// const transport = new StdioServerTransport();
// await server.connect(transport);
