/**
 * Notes MCP server — práctica del server completo (3 primitivos) en TypeScript.
 * Semana 06 — Los 3 Primitivos
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// =============================================
// ESTADO COMPARTIDO
// =============================================
interface Note {
  id: number;
  title: string;
  content: string;
  tag: string;
}

const notesDb: Note[] = [
  { id: 1, title: "Reunion de equipo", content: "Jueves 10am, sala B", tag: "work" },
  { id: 2, title: "Ideas proyecto", content: "API con MCP + Resources", tag: "dev" },
];
let nextId = 3;

const server = new Server({ name: "notes-manager", version: "1.0.0" });

// =============================================
// SECCIÓN 1 TS — TOOLS
// =============================================
// Descomenta las siguientes líneas:
// server.setRequestHandler(ListToolsRequestSchema, async () => ({
//   tools: [
//     {
//       name: "create_note",
//       description: "Creates a new note",
//       inputSchema: {
//         type: "object",
//         properties: {
//           title: { type: "string", description: "Short title" },
//           content: { type: "string", description: "Note content" },
//           tag: { type: "string", description: "Category tag", default: "general" },
//         },
//         required: ["title", "content"],
//       },
//     },
//     {
//       name: "delete_note",
//       description: "Deletes a note by ID",
//       inputSchema: {
//         type: "object",
//         properties: { note_id: { type: "number" } },
//         required: ["note_id"],
//       },
//     },
//     {
//       name: "search_notes",
//       description: "Searches notes by title or content",
//       inputSchema: {
//         type: "object",
//         properties: { query: { type: "string" } },
//         required: ["query"],
//       },
//     },
//   ],
// }));
//
// server.setRequestHandler(CallToolRequestSchema, async (request) => {
//   const { name, arguments: args } = request.params;
//
//   if (name === "create_note") {
//     const { title, content, tag = "general" } = args as { title: string; content: string; tag?: string };
//     const note: Note = { id: nextId++, title, content, tag };
//     notesDb.push(note);
//     return { content: [{ type: "text" as const, text: JSON.stringify({ created: note }) }] };
//   }
//
//   if (name === "delete_note") {
//     const { note_id } = args as { note_id: number };
//     const idx = notesDb.findIndex((n) => n.id === note_id);
//     if (idx === -1) {
//       return { content: [{ type: "text" as const, text: JSON.stringify({ error: "Not found" }) }], isError: true };
//     }
//     const [deleted] = notesDb.splice(idx, 1);
//     return { content: [{ type: "text" as const, text: JSON.stringify({ deleted }) }] };
//   }
//
//   if (name === "search_notes") {
//     const { query } = args as { query: string };
//     const q = query.toLowerCase();
//     const results = notesDb.filter((n) => n.title.toLowerCase().includes(q) || n.content.toLowerCase().includes(q));
//     return { content: [{ type: "text" as const, text: JSON.stringify(results) }] };
//   }
//
//   throw new Error(`Unknown tool: ${name}`);
// });


// =============================================
// SECCIÓN 2 TS — RESOURCES
// =============================================
// Descomenta las siguientes líneas:
// server.setRequestHandler(ListResourcesRequestSchema, async () => ({
//   resources: [
//     { uri: "notes://all", name: "All Notes", mimeType: "application/json" },
//     { uri: "notes://tags", name: "All Tags", mimeType: "application/json" },
//   ],
// }));
//
// server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
//   const { uri } = request.params;
//
//   if (uri === "notes://all") {
//     return { contents: [{ uri, mimeType: "application/json", text: JSON.stringify(notesDb) }] };
//   }
//   if (uri === "notes://tags") {
//     const tags = [...new Set(notesDb.map((n) => n.tag))].sort();
//     return { contents: [{ uri, mimeType: "application/json", text: JSON.stringify({ tags }) }] };
//   }
//   const match = uri.match(/^notes:\/\/(\d+)$/);
//   if (match) {
//     const note = notesDb.find((n) => n.id === parseInt(match[1], 10));
//     const result = note ?? { error: "Note not found" };
//     return { contents: [{ uri, mimeType: "application/json", text: JSON.stringify(result) }] };
//   }
//   throw new Error(`Resource not found: ${uri}`);
// });


// =============================================
// SECCIÓN 3 TS — PROMPTS
// =============================================
// Descomenta las siguientes líneas:
// server.setRequestHandler(ListPromptsRequestSchema, async () => ({
//   prompts: [
//     {
//       name: "summarize_notes",
//       description: "Generates a prompt to summarize all current notes",
//       arguments: [],
//     },
//     {
//       name: "find_related",
//       description: "Finds notes related to a topic",
//       arguments: [{ name: "topic", description: "Topic to search for", required: true }],
//     },
//   ],
// }));
//
// server.setRequestHandler(GetPromptRequestSchema, async (request) => {
//   const { name, arguments: args } = request.params;
//
//   if (name === "summarize_notes") {
//     const notesText = notesDb.map((n) => `- [${n.tag}] ${n.title}: ${n.content}`).join("\n");
//     return {
//       description: "Summarize all notes",
//       messages: [
//         {
//           role: "user" as const,
//           content: {
//             type: "text" as const,
//             text: `Tengo las siguientes notas:\n\n${notesText}\n\nDame un resumen organizado por categoría.`,
//           },
//         },
//       ],
//     };
//   }
//
//   if (name === "find_related") {
//     const topic = args?.topic ?? "general";
//     const q = topic.toLowerCase();
//     const related = notesDb.filter((n) => n.title.toLowerCase().includes(q) || n.content.toLowerCase().includes(q));
//     const notesText = related.length > 0 ? JSON.stringify(related) : "No se encontraron notas relacionadas.";
//     return {
//       description: `Notes related to: ${topic}`,
//       messages: [
//         {
//           role: "user" as const,
//           content: {
//             type: "text" as const,
//             text: `Sobre '${topic}', tengo estas notas:\n\n${notesText}\n\n¿Qué puedo aprender de esto?`,
//           },
//         },
//       ],
//     };
//   }
//
//   throw new Error(`Unknown prompt: ${name}`);
// });


const transport = new StdioServerTransport();
await server.connect(transport);
