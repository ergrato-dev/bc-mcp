// ============================================
// SECCIÓN A — Imports y servidor
// ============================================
// import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
// import { z } from "zod";
//
// const server = new McpServer({
//   name: "practice-02",
//   version: "1.0.0",
// });

// ============================================
// SECCIÓN B — Tipos básicos: string, number, boolean
// ============================================
// server.tool(
//   "validate_types",
//   "Demonstrate basic Zod types: string, number, boolean",
//   {
//     text: z.string(),
//     count: z.number(),
//     active: z.boolean(),
//   },
//   async ({ text, count, active }) => ({
//     content: [{
//       type: "text",
//       text: `text="${text}" | count=${count} | active=${active}`,
//     }],
//   }),
// );

// ============================================
// SECCIÓN C — z.enum(), .optional(), .default()
// ============================================
// server.tool(
//   "format_text",
//   "Format a text string using a specified operation",
//   {
//     text: z.string(),
//     format: z.enum(["upper", "lower", "title"]).default("upper"),
//     suffix: z.string().optional(),
//   },
//   async ({ text, format, suffix }) => {
//     let result: string;
//     if (format === "upper") result = text.toUpperCase();
//     else if (format === "lower") result = text.toLowerCase();
//     else result = text.replace(/\b\w/g, (c) => c.toUpperCase());
//     if (suffix) result += suffix;
//     return { content: [{ type: "text", text: result }] };
//   },
// );

// ============================================
// SECCIÓN D — .describe() para documentar parámetros
// ============================================
// server.tool(
//   "search_items",
//   "Search items with filtering options",
//   {
//     query: z.string().describe("Search term to look for"),
//     limit: z.number().min(1).max(100).default(10).describe("Maximum number of results to return"),
//     category: z.string().optional().describe("Optional category filter"),
//   },
//   async ({ query, limit, category }) => {
//     const info = `Searching for "${query}" (limit: ${limit}${category ? `, category: ${category}` : ""})`;
//     return { content: [{ type: "text", text: info }] };
//   },
// );

// ============================================
// SECCIÓN E — z.object() anidado
// ============================================
// server.tool(
//   "create_profile",
//   "Create a user profile with nested address information",
//   {
//     name: z.string().describe("Full name of the user"),
//     age: z.number().min(0).max(150).describe("Age in years"),
//     address: z.object({
//       city: z.string(),
//       country: z.string().default("Spain"),
//     }).describe("User address"),
//   },
//   async ({ name, age, address }) => {
//     const profile = { name, age, address };
//     return { content: [{ type: "text", text: JSON.stringify(profile, null, 2) }] };
//   },
// );

// ============================================
// SECCIÓN F — Conectar el transport
// ============================================
// const transport = new StdioServerTransport();
// await server.connect(transport);
