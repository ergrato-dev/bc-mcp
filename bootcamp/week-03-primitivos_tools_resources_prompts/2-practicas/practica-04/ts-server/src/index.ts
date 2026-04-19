/**
 * MCP Server — Práctica 04: Los Tres Primitivos Combinados (TypeScript)
 * Semana 03 — Los Tres Primitivos
 *
 * Escenario: Knowledge Base Server
 * - Tools:     add_note, search_notes
 * - Resources: kb://notes/all, kb://notes/{id}
 * - Prompts:   summarize_notes
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    ListToolsRequestSchema,
    CallToolRequestSchema,
    ListResourcesRequestSchema,
    ListResourceTemplatesRequestSchema,
    ReadResourceRequestSchema,
    ListPromptsRequestSchema,
    GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";


// ============================================================
// SECCIÓN A: Servidor con ServerCapabilities completas
// ============================================================
// Descomenta las líneas siguientes:
// const server = new Server(
//     { name: "practice-04-knowledge-base", version: "1.0.0" },
//     {
//         capabilities: {
//             tools: {},
//             resources: {},
//             prompts: {},
//         },
//     }
// );
//
// // In-memory knowledge base shared between Tools and Resources
// interface Note {
//     id: string;
//     title: string;
//     content: string;
//     tags: string[];
//     created_at: string;
// }
// const notesDb = new Map<string, Note>();
// let noteCounter = 0;

// Placeholder — reemplazar por la Sección A cuando se descomente:
const server = new Server(
    { name: "practice-04-kb-placeholder", version: "1.0.0" },
    { capabilities: {} }
);
interface Note { id: string; title: string; content: string; tags: string[]; created_at: string; }
const notesDb = new Map<string, Note>();
let noteCounter = 0;


// ============================================================
// SECCIÓN B: Tools — add_note y search_notes
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListToolsRequestSchema, async () => ({
//     tools: [
//         {
//             name: "add_note",
//             description: "Adds a new note to the knowledge base",
//             inputSchema: {
//                 type: "object",
//                 properties: {
//                     title: { type: "string", description: "Note title", minLength: 1, maxLength: 100 },
//                     content: { type: "string", description: "Note content", minLength: 1 },
//                     tags: { type: "array", items: { type: "string" }, maxItems: 5, description: "Optional tags" },
//                 },
//                 required: ["title", "content"],
//                 additionalProperties: false,
//             },
//             annotations: { destructiveHint: false, readOnlyHint: false },
//         },
//         {
//             name: "search_notes",
//             description: "Searches notes by title, content or tags",
//             inputSchema: {
//                 type: "object",
//                 properties: {
//                     query: { type: "string", description: "Search text" },
//                 },
//                 required: ["query"],
//                 additionalProperties: false,
//             },
//             annotations: { readOnlyHint: true, idempotentHint: true },
//         },
//     ],
// }));
//
// server.setRequestHandler(CallToolRequestSchema, async (request) => {
//     const { name, arguments: args } = request.params;
//
//     if (name === "add_note") {
//         noteCounter++;
//         const noteId = String(noteCounter);
//         notesDb.set(noteId, {
//             id: noteId,
//             title: (args as Record<string, unknown>).title as string,
//             content: (args as Record<string, unknown>).content as string,
//             tags: ((args as Record<string, unknown>).tags as string[]) ?? [],
//             created_at: new Date().toISOString(),
//         });
//         return { content: [{ type: "text", text: `Note created with id=${noteId}` }] };
//     }
//
//     if (name === "search_notes") {
//         const query = ((args as Record<string, unknown>).query as string).toLowerCase();
//         const results = [...notesDb.values()].filter(
//             (n) =>
//                 n.title.toLowerCase().includes(query) ||
//                 n.content.toLowerCase().includes(query) ||
//                 n.tags.some((t) => t.toLowerCase().includes(query))
//         );
//         if (results.length === 0) {
//             return {
//                 content: [{ type: "text", text: `No notes found for '${query}'` }],
//                 isError: true,
//             };
//         }
//         return { content: [{ type: "text", text: JSON.stringify(results, null, 2) }] };
//     }
//
//     throw new Error(`Unknown tool: ${name}`);
// });


// ============================================================
// SECCIÓN C: Resources — kb://notes/all y kb://notes/{id}
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListResourcesRequestSchema, async () => ({
//     resources: [
//         {
//             uri: "kb://notes/all",
//             name: "All notes",
//             description: "Lists all notes in the knowledge base",
//             mimeType: "application/json",
//         },
//     ],
// }));
//
// server.setRequestHandler(ListResourceTemplatesRequestSchema, async () => ({
//     resourceTemplates: [
//         {
//             uriTemplate: "kb://notes/{note_id}",
//             name: "Note by ID",
//             description: "Returns the full content of a specific note",
//             mimeType: "application/json",
//         },
//     ],
// }));
//
// server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
//     const { uri } = request.params;
//
//     if (uri === "kb://notes/all") {
//         const summary = [...notesDb.values()].map((n) => ({ id: n.id, title: n.title, tags: n.tags }));
//         return { contents: [{ uri, text: JSON.stringify(summary, null, 2), mimeType: "application/json" }] };
//     }
//
//     if (uri.startsWith("kb://notes/")) {
//         const noteId = uri.replace("kb://notes/", "");
//         const note = notesDb.get(noteId);
//         if (!note) throw new Error(`Note ${noteId} not found`);
//         return { contents: [{ uri, text: JSON.stringify(note, null, 2), mimeType: "application/json" }] };
//     }
//
//     throw new Error(`Resource not found: ${uri}`);
// });


// ============================================================
// SECCIÓN D: Prompts — summarize_notes
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListPromptsRequestSchema, async () => ({
//     prompts: [
//         {
//             name: "summarize_notes",
//             description: "Generates a summary of all notes in the knowledge base",
//             arguments: [
//                 {
//                     name: "focus",
//                     description: "Topic or keyword to focus the summary on",
//                     required: false,
//                 },
//             ],
//         },
//     ],
// }));
//
// server.setRequestHandler(GetPromptRequestSchema, async (request) => {
//     const { name, arguments: args } = request.params;
//     const safeArgs = args ?? {};
//
//     if (name === "summarize_notes") {
//         const focus = safeArgs.focus ?? "all topics";
//         const allNotes = [...notesDb.values()];
//
//         return {
//             description: "Knowledge base summary",
//             messages: [
//                 {
//                     role: "user",
//                     content: {
//                         type: "resource",
//                         resource: {
//                             uri: "kb://notes/all",
//                             text: JSON.stringify(allNotes, null, 2),
//                             mimeType: "application/json",
//                         },
//                     },
//                 },
//                 {
//                     role: "user",
//                     content: {
//                         type: "text",
//                         text: `Summarize the notes above, focusing on: ${focus}`,
//                     },
//                 },
//             ],
//         };
//     }
//
//     throw new Error(`Unknown prompt: ${name}`);
// });


const transport = new StdioServerTransport();
await server.connect(transport);
