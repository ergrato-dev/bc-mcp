// ============================================
// SECCIÓN A — Imports y servidor
// ============================================
// import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
// import { z } from "zod";
//
// const server = new McpServer({
//   name: "practice-05-multi-tools",
//   version: "1.0.0",
// });

// ============================================
// SECCIÓN B — Tools matemáticos
// ============================================
// server.tool(
//   "add",
//   "Add two numbers",
//   { a: z.number().describe("First number"), b: z.number().describe("Second number") },
//   async ({ a, b }) => ({ content: [{ type: "text", text: String(a + b) }] }),
// );
//
// server.tool(
//   "multiply",
//   "Multiply two numbers",
//   { a: z.number().describe("First number"), b: z.number().describe("Second number") },
//   async ({ a, b }) => ({ content: [{ type: "text", text: String(a * b) }] }),
// );
//
// server.tool(
//   "power",
//   "Raise a base number to an exponent",
//   {
//     base: z.number().describe("The base number"),
//     exponent: z.number().min(0).describe("The exponent (must be >= 0)"),
//   },
//   async ({ base, exponent }) => ({
//     content: [{ type: "text", text: String(Math.pow(base, exponent)) }],
//   }),
// );

// ============================================
// SECCIÓN C — Tools de texto
// ============================================
// server.tool(
//   "word_count",
//   "Count words, characters, and lines in a text",
//   { text: z.string().describe("Text to analyze") },
//   async ({ text }) => {
//     const words = text.trim() === "" ? 0 : text.trim().split(/\s+/).length;
//     const chars = text.length;
//     const lines = text.split("\n").length;
//     return {
//       content: [{
//         type: "text",
//         text: JSON.stringify({ words, characters: chars, lines }, null, 2),
//       }],
//     };
//   },
// );
//
// server.tool(
//   "reverse_text",
//   "Reverse a text string",
//   { text: z.string().describe("Text to reverse") },
//   async ({ text }) => ({
//     content: [{ type: "text", text: text.split("").reverse().join("") }],
//   }),
// );

// ============================================
// SECCIÓN D — Tool de fechas
// ============================================
// server.tool(
//   "date_info",
//   "Return information about a specific date",
//   {
//     date_string: z.string().describe("Date in YYYY-MM-DD format"),
//   },
//   async ({ date_string }) => {
//     try {
//       const d = new Date(date_string + "T00:00:00");
//       if (isNaN(d.getTime())) {
//         return {
//           content: [{ type: "text", text: `Invalid date: "${date_string}"` }],
//           isError: true,
//         };
//       }
//       const today = new Date();
//       today.setHours(0, 0, 0, 0);
//       const diffMs = d.getTime() - today.getTime();
//       const daysUntil = Math.round(diffMs / (1000 * 60 * 60 * 24));
//       const info = {
//         date: date_string,
//         weekday: d.toLocaleDateString("en-US", { weekday: "long" }),
//         is_weekend: d.getDay() === 0 || d.getDay() === 6,
//         days_until: daysUntil,
//         is_past: daysUntil < 0,
//       };
//       return { content: [{ type: "text", text: JSON.stringify(info, null, 2) }] };
//     } catch (error) {
//       return {
//         content: [{ type: "text", text: `Error: ${String(error)}` }],
//         isError: true,
//       };
//     }
//   },
// );

// ============================================
// SECCIÓN E — Conectar el transport
// ============================================
// const transport = new StdioServerTransport();
// await server.connect(transport);
