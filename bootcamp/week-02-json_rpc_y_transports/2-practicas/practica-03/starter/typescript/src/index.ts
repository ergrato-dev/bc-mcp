// ============================================================
// SECCIÓN A — Importaciones y setup de Express + MCP
// Descomenta las siguientes líneas:
// ============================================================
// import express from "express";
// import { Server } from "@modelcontextprotocol/sdk/server/index.js";
// import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
// import {
//   ListToolsRequestSchema,
//   CallToolRequestSchema,
// } from "@modelcontextprotocol/sdk/types.js";
//
// const app = express();
// app.use(express.json());
//
// // Mapa de transports activos: sessionId → transport
// const activeTransports = new Map<string, SSEServerTransport>();

// ============================================================
// SECCIÓN B — Factory del servidor MCP
// Descomenta las siguientes líneas:
// ============================================================
// function createServer(): Server {
//   const server = new Server(
//     { name: "calculadora-sse", version: "1.0.0" },
//     { capabilities: { tools: {} } }
//   );
//
//   server.setRequestHandler(ListToolsRequestSchema, async () => ({
//     tools: [
//       {
//         name: "calculate",
//         description: "Realiza operaciones matemáticas básicas",
//         inputSchema: {
//           type: "object" as const,
//           properties: {
//             a: { type: "number", description: "Primer operando" },
//             b: { type: "number", description: "Segundo operando" },
//             op: {
//               type: "string",
//               enum: ["add", "sub", "mul", "div"],
//               description: "Operación: add, sub, mul, div",
//             },
//           },
//           required: ["a", "b", "op"],
//         },
//       },
//     ],
//   }));
//
//   server.setRequestHandler(CallToolRequestSchema, async (request) => {
//     const { name, arguments: args } = request.params;
//     if (name !== "calculate") throw new Error(`Tool desconocido: ${name}`);
//
//     const a = args?.a as number;
//     const b = args?.b as number;
//     const op = args?.op as string;
//     process.stderr.write(`[calculate] a=${a} b=${b} op=${op}\n`);
//
//     let result: number;
//     if (op === "add") result = a + b;
//     else if (op === "sub") result = a - b;
//     else if (op === "mul") result = a * b;
//     else if (op === "div") {
//       if (b === 0) return { content: [{ type: "text" as const, text: "Error: división por cero" }] };
//       result = a / b;
//     } else throw new Error(`Operación desconocida: ${op}`);
//
//     return { content: [{ type: "text" as const, text: String(result) }] };
//   });
//
//   return server;
// }

// ============================================================
// SECCIÓN C — Endpoints SSE y POST /message
// Descomenta las siguientes líneas:
// ============================================================
// app.get("/sse", async (req, res) => {
//   const transport = new SSEServerTransport("/message", res);
//   const server = createServer();
//   activeTransports.set(transport.sessionId, transport);
//   res.on("close", () => {
//     activeTransports.delete(transport.sessionId);
//     process.stderr.write(`Cliente desconectado: ${transport.sessionId}\n`);
//   });
//   process.stderr.write(`Cliente conectado: ${transport.sessionId}\n`);
//   await server.connect(transport);
// });
//
// app.post("/message", async (req, res) => {
//   const sessionId = req.query.sessionId as string;
//   const transport = activeTransports.get(sessionId);
//   if (!transport) {
//     res.status(404).json({ error: "Sesión no encontrada" });
//     return;
//   }
//   await transport.handlePostMessage(req, res);
// });

// ============================================================
// SECCIÓN D — Health check y arranque
// Descomenta las siguientes líneas:
// ============================================================
// app.get("/health", (_req, res) => res.json({ status: "ok" }));
//
// app.listen(8000, () => {
//   process.stderr.write("Servidor SSE en http://0.0.0.0:8000\n");
// });
