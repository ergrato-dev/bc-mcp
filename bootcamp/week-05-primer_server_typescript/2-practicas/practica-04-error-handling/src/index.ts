// ============================================
// SECCIÓN A — Imports y servidor
// ============================================
// import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
// import { z } from "zod";
//
// const server = new McpServer({
//   name: "practice-04",
//   version: "1.0.0",
// });

// ============================================
// SECCIÓN B — z.enum() básico: idiomas
// ============================================
// server.tool(
//   "get_weekday",
//   "Return today's weekday name in the specified language",
//   {
//     lang: z.enum(["en", "es", "fr"]).describe("Language code"),
//     day: z.number().min(0).max(6).describe("Day number (0=Sunday, 6=Saturday)"),
//   },
//   async ({ lang, day }) => {
//     const days: Record<string, string[]> = {
//       en: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
//       es: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
//       fr: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
//     };
//     return { content: [{ type: "text", text: days[lang][day] }] };
//   },
// );

// ============================================
// SECCIÓN C — z.enum() + error de dominio
// ============================================
// server.tool(
//   "calculate",
//   "Perform a basic arithmetic operation with error handling",
//   {
//     op: z.enum(["add", "subtract", "multiply", "divide"]).describe("Operation to perform"),
//     a: z.number().describe("First operand"),
//     b: z.number().describe("Second operand"),
//   },
//   async ({ op, a, b }) => {
//     if (op === "divide" && b === 0) {
//       return {
//         content: [{ type: "text", text: "Error: cannot divide by zero" }],
//         isError: true,
//       };
//     }
//     const results: Record<string, number> = {
//       add: a + b,
//       subtract: a - b,
//       multiply: a * b,
//       divide: a / b,
//     };
//     return { content: [{ type: "text", text: String(results[op]) }] };
//   },
// );

// ============================================
// SECCIÓN D — try/catch para excepciones de runtime
// ============================================
// server.tool(
//   "parse_json",
//   "Parse a JSON string and return it formatted",
//   { json_string: z.string().describe("JSON string to parse") },
//   async ({ json_string }) => {
//     try {
//       const parsed: unknown = JSON.parse(json_string);
//       return { content: [{ type: "text", text: JSON.stringify(parsed, null, 2) }] };
//     } catch (error) {
//       return {
//         content: [{ type: "text", text: `Parse error: ${String(error)}` }],
//         isError: true,
//       };
//     }
//   },
// );

// ============================================
// SECCIÓN E — isError por validación de dominio
// ============================================
// const USERS: Record<number, { name: string; email: string }> = {
//   1: { name: "Alice", email: "alice@example.com" },
//   2: { name: "Bob", email: "bob@example.com" },
// };
//
// server.tool(
//   "get_user",
//   "Retrieve a user by ID",
//   { id: z.number().int().positive().describe("User ID to retrieve") },
//   async ({ id }) => {
//     const user = USERS[id];
//     if (!user) {
//       return {
//         content: [{ type: "text", text: `User with ID ${id} not found` }],
//         isError: true,
//       };
//     }
//     return { content: [{ type: "text", text: JSON.stringify(user, null, 2) }] };
//   },
// );

// ============================================
// SECCIÓN F — Conectar el transport
// ============================================
// const transport = new StdioServerTransport();
// await server.connect(transport);
