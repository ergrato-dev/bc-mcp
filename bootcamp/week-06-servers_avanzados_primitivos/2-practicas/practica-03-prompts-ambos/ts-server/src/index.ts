/**
 * Writing assistant MCP server — práctica de Prompts en TypeScript.
 * Semana 06 — Los 3 Primitivos
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server({ name: "writing-assistant", version: "1.0.0" });

// =============================================
// SECCIÓN 1 TS: Handler prompts/list
// =============================================
// Registra los prompts disponibles con sus argumentos.
// "arguments" define qué parámetros acepta cada prompt.
// Descomenta las siguientes líneas:
// server.setRequestHandler(ListPromptsRequestSchema, async () => ({
//   prompts: [
//     {
//       name: "brainstorm_ideas",
//       description: "Starter prompt for brainstorming creative ideas",
//       arguments: [],
//     },
//     {
//       name: "explain_concept",
//       description: "Explains a technical concept clearly",
//       arguments: [
//         {
//           name: "topic",
//           description: "The concept or technology to explain",
//           required: true,
//         },
//       ],
//     },
//     {
//       name: "code_review",
//       description: "Starts a code review conversation",
//       arguments: [
//         {
//           name: "language",
//           description: "Programming language",
//           required: true,
//         },
//         {
//           name: "code",
//           description: "The code snippet to review",
//           required: true,
//         },
//       ],
//     },
//   ],
// }));


// =============================================
// SECCIÓN 2 TS: Handler prompts/get
// =============================================
// Genera los mensajes para el prompt solicitado.
// "request.params.name" tiene el nombre del prompt.
// "request.params.arguments" tiene los argumentos como Record<string, string>.
// Descomenta las siguientes líneas:
// server.setRequestHandler(GetPromptRequestSchema, async (request) => {
//   const { name, arguments: args } = request.params;
//
//   if (name === "brainstorm_ideas") {
//     return {
//       description: "Brainstorming starter",
//       messages: [
//         {
//           role: "user" as const,
//           content: {
//             type: "text" as const,
//             text: "Necesito generar ideas creativas para un proyecto. ¿Cuáles son las mejores técnicas de brainstorming?",
//           },
//         },
//       ],
//     };
//   }
//
//   if (name === "explain_concept") {
//     const topic = args?.topic ?? "unknown topic";
//     return {
//       description: `Explain: ${topic}`,
//       messages: [
//         {
//           role: "user" as const,
//           content: {
//             type: "text" as const,
//             text: `Explícame el concepto de '${topic}' de forma clara. Incluye: qué es, para qué sirve y un ejemplo.`,
//           },
//         },
//       ],
//     };
//   }
//
//   if (name === "code_review") {
//     const language = args?.language ?? "unknown";
//     const code = args?.code ?? "";
//     return {
//       description: `Code review: ${language}`,
//       messages: [
//         {
//           role: "user" as const,
//           content: { type: "text" as const, text: `Voy a mostrarte código en ${language}:` },
//         },
//         {
//           role: "assistant" as const,
//           content: { type: "text" as const, text: "Entendido, muéstrame el código y lo analizaré." },
//         },
//         {
//           role: "user" as const,
//           content: {
//             type: "text" as const,
//             text: `\`\`\`${language}\n${code}\n\`\`\`\n\nPor favor revisa: legibilidad, errores y mejoras.`,
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
