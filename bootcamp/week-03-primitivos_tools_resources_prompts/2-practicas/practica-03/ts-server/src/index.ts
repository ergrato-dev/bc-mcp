/**
 * MCP Server — Práctica 03: Prompts en TypeScript
 * Semana 03 — Los Tres Primitivos
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    ListPromptsRequestSchema,
    GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
    { name: "practice-03-prompts-ts", version: "1.0.0" },
    { capabilities: { prompts: {} } }
);


// ============================================================
// SECCIÓN A: Declarar lista de Prompts (ListPrompts)
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListPromptsRequestSchema, async () => ({
//     prompts: [
//         {
//             name: "code_review",
//             description: "Generates a detailed code review for the given code snippet",
//             arguments: [
//                 {
//                     name: "language",
//                     description: "Programming language (python, typescript, go, etc.)",
//                     required: true,
//                 },
//                 {
//                     name: "code",
//                     description: "The code snippet to review",
//                     required: true,
//                 },
//                 {
//                     name: "focus",
//                     description: "Review focus: security, performance, style, or general",
//                     required: false,    // Optional argument
//                 },
//             ],
//         },
//         {
//             name: "explain_concept",
//             description: "Explains a programming concept at the specified level",
//             arguments: [
//                 {
//                     name: "concept",
//                     description: "The programming concept to explain",
//                     required: true,
//                 },
//                 {
//                     name: "level",
//                     description: "Level: beginner, intermediate, or advanced",
//                     required: false,
//                 },
//             ],
//         },
//     ],
// }));


// ============================================================
// SECCIÓN B: Implementar get_prompt (GetPrompt)
// ============================================================
// args ?? {} previene el caso donde arguments es undefined.
// Los argumentos opcionales usan args.argName ?? "default".
//
// Descomenta las líneas siguientes:
// server.setRequestHandler(GetPromptRequestSchema, async (request) => {
//     const { name, arguments: args } = request.params;
//     const safeArgs = args ?? {};
//
//     if (name === "code_review") {
//         const language = safeArgs.language ?? "unknown";
//         const code = safeArgs.code ?? "";
//         const focus = safeArgs.focus ?? "general quality";
//
//         return {
//             description: `Code review for ${language}`,
//             messages: [
//                 {
//                     role: "user",
//                     content: {
//                         type: "text",
//                         text: [
//                             `Please review the following ${language} code with focus on ${focus}:`,
//                             "",
//                             `\`\`\`${language}`,
//                             code,
//                             "```",
//                             "",
//                             "Provide specific feedback on:",
//                             "1. Correctness",
//                             "2. Edge cases",
//                             "3. Performance",
//                             "4. Best practices",
//                         ].join("\n"),
//                     },
//                 },
//             ],
//         };
//     }
//
//     if (name === "explain_concept") {
//         const concept = safeArgs.concept ?? "";
//         const level = safeArgs.level ?? "intermediate";
//
//         return {
//             description: `Explanation of ${concept}`,
//             messages: [
//                 {
//                     role: "user",
//                     content: {
//                         type: "text",
//                         text: `Explain the concept of '${concept}' at a ${level} level.`,
//                     },
//                 },
//             ],
//         };
//     }
//
//     throw new Error(`Unknown prompt: ${name}`);
// });


// ============================================================
// SECCIÓN C: Multi-turn con role "assistant" seed
// ============================================================
// Reemplaza el handler de code_review de la Sección B por:
//
//     if (name === "code_review") {
//         ...
//         return {
//             description: `Code review for ${language}`,
//             messages: [
//                 {
//                     role: "user",
//                     content: { type: "text", text: `Review this ${language} code:\n\n\`\`\`${language}\n${code}\n\`\`\`` },
//                 },
//                 // Assistant seed — guides LLM response style
//                 {
//                     role: "assistant",
//                     content: { type: "text", text: "I'll analyze this code systematically:" },
//                 },
//             ],
//         };
//     }


// ============================================================
// SECCIÓN D: EmbeddedResource dentro de un Prompt
// ============================================================
// En TypeScript, EmbeddedResource tiene type: "resource".
// Agrega en ListPrompts y en GetPrompt:
//
// En ListPrompts:
//     {
//         name: "query_with_schema",
//         description: "Generates SQL with table schema as context",
//         arguments: [{ name: "task", description: "What data to retrieve", required: true }],
//     },
//
// En GetPrompt:
//     if (name === "query_with_schema") {
//         const task = safeArgs.task ?? "";
//         const schemaData = { table: "products", columns: ["id", "name", "price"] };
//
//         return {
//             description: "SQL query generation with schema context",
//             messages: [
//                 {
//                     role: "user",
//                     content: {
//                         type: "resource",
//                         resource: {
//                             uri: "db://schema/products",
//                             text: JSON.stringify(schemaData, null, 2),
//                             mimeType: "application/json",
//                         },
//                     },
//                 },
//                 {
//                     role: "user",
//                     content: { type: "text", text: `Using the schema above, write a SQL query to: ${task}` },
//                 },
//             ],
//         };
//     }


const transport = new StdioServerTransport();
await server.connect(transport);
