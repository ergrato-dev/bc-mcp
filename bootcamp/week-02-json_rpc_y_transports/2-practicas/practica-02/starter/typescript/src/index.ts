// ============================================================
// SECCIÓN A — Importaciones y creación del servidor
// Descomenta las siguientes líneas:
// ============================================================
// import { Server } from "@modelcontextprotocol/sdk/server/index.js";
// import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
// import {
//   ListToolsRequestSchema,
//   CallToolRequestSchema,
// } from "@modelcontextprotocol/sdk/types.js";
//
// const server = new Server(
//   { name: "calculadora-stdio", version: "1.0.0" },
//   { capabilities: { tools: {} } }
// );

// ============================================================
// SECCIÓN B — Handler para tools/list
// Descomenta las siguientes líneas:
// ============================================================
// server.setRequestHandler(ListToolsRequestSchema, async () => ({
//   tools: [
//     {
//       name: "calculate",
//       description: "Realiza operaciones matemáticas básicas",
//       inputSchema: {
//         type: "object" as const,
//         properties: {
//           a: { type: "number", description: "Primer operando" },
//           b: { type: "number", description: "Segundo operando" },
//           op: {
//             type: "string",
//             enum: ["add", "sub", "mul", "div"],
//             description: "Operación: add, sub, mul, div",
//           },
//         },
//         required: ["a", "b", "op"],
//       },
//     },
//   ],
// }));

// ============================================================
// SECCIÓN C — Handler para tools/call
// IMPORTANTE: usa process.stderr.write() para logs, nunca console.log()
// Descomenta las siguientes líneas:
// ============================================================
// server.setRequestHandler(CallToolRequestSchema, async (request) => {
//   const { name, arguments: args } = request.params;
//
//   if (name !== "calculate") {
//     throw new Error(`Tool desconocido: ${name}`);
//   }
//
//   const a = args?.a as number;
//   const b = args?.b as number;
//   const op = args?.op as string;
//
//   // Logging correcto — stderr no interfiere con stdio
//   process.stderr.write(`[calculate] a=${a} b=${b} op=${op}\n`);
//
//   let result: number;
//   if (op === "add") {
//     result = a + b;
//   } else if (op === "sub") {
//     result = a - b;
//   } else if (op === "mul") {
//     result = a * b;
//   } else if (op === "div") {
//     if (b === 0) {
//       return {
//         content: [{ type: "text" as const, text: "Error: división por cero" }],
//       };
//     }
//     result = a / b;
//   } else {
//     throw new Error(`Operación desconocida: ${op}`);
//   }
//
//   return {
//     content: [{ type: "text" as const, text: String(result) }],
//   };
// });

// ============================================================
// SECCIÓN D — Función main y arranque del servidor
// Descomenta las siguientes líneas:
// ============================================================
// async function main(): Promise<void> {
//   const transport = new StdioServerTransport();
//   await server.connect(transport);
//   process.stderr.write("Servidor calculadora-stdio iniciado\n");
// }
//
// main().catch((error) => {
//   process.stderr.write(`Error fatal: ${error}\n`);
//   process.exit(1);
// });
