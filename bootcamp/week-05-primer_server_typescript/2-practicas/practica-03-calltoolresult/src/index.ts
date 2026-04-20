// ============================================
// SECCIÓN A — Imports y servidor
// ============================================
// import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
// import { z } from "zod";
//
// const server = new McpServer({
//   name: "practice-03",
//   version: "1.0.0",
// });

// ============================================
// SECCIÓN B — Retorno de texto simple
// ============================================
// server.tool(
//   "echo",
//   "Return the input text as-is",
//   { text: z.string().describe("Text to echo back") },
//   async ({ text }) => ({
//     content: [{ type: "text", text }],
//   }),
// );

// ============================================
// SECCIÓN C — Múltiples bloques de contenido
// ============================================
// server.tool(
//   "multi_info",
//   "Return multiple content blocks in a single response",
//   { name: z.string(), version: z.string() },
//   async ({ name, version }) => ({
//     content: [
//       { type: "text", text: `Server name: ${name}` },
//       { type: "text", text: `Version: ${version}` },
//       { type: "text", text: `Timestamp: ${new Date().toISOString()}` },
//     ],
//   }),
// );

// ============================================
// SECCIÓN D — JSON.stringify para objetos
// ============================================
// server.tool(
//   "stats",
//   "Calculate statistics for a list of numbers",
//   { numbers: z.array(z.number()).min(1).describe("List of numbers to analyze") },
//   async ({ numbers }) => {
//     const min = Math.min(...numbers);
//     const max = Math.max(...numbers);
//     const sum = numbers.reduce((a, b) => a + b, 0);
//     const avg = sum / numbers.length;
//     const result = { min, max, sum, avg: Math.round(avg * 100) / 100, count: numbers.length };
//     return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
//   },
// );

// ============================================
// SECCIÓN E — isError: true para errores de tool
// ============================================
// server.tool(
//   "safe_divide",
//   "Divide two numbers, returning an error if divisor is zero",
//   {
//     a: z.number().describe("Dividend"),
//     b: z.number().describe("Divisor"),
//   },
//   async ({ a, b }) => {
//     if (b === 0) {
//       return {
//         content: [{ type: "text", text: "Error: division by zero is not allowed" }],
//         isError: true,
//       };
//     }
//     return { content: [{ type: "text", text: String(a / b) }] };
//   },
// );

// ============================================
// SECCIÓN F — Conectar el transport
// ============================================
// const transport = new StdioServerTransport();
// await server.connect(transport);
