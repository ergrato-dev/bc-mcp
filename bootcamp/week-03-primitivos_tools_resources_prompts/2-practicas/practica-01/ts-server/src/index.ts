/**
 * MCP Server — Práctica 01: Tools en TypeScript
 * Semana 03 — Los Tres Primitivos
 *
 * Objetivo: implementar Tools con inputSchema, isError y annotations.
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    ListToolsRequestSchema,
    CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

const server = new Server(
    { name: "practice-01-tools-ts", version: "1.0.0" },
    { capabilities: { tools: {} } }
);

// ============================================================
// SECCIÓN A: Declarar la lista de Tools (ListToolsRequest)
// ============================================================
// setRequestHandler recibe el schema de la request y el handler.
// ListToolsRequestSchema corresponde al método "tools/list".
//
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListToolsRequestSchema, async () => ({
//     tools: [
//         {
//             name: "calculate_discount",
//             description:
//                 "Calculates the final price after applying a percentage discount. " +
//                 "Use this when the user asks for a discounted price.",
//             inputSchema: {
//                 type: "object",
//                 properties: {
//                     price: {
//                         type: "number",
//                         description: "Original price (must be positive)",
//                         minimum: 0,
//                     },
//                     discount_percent: {
//                         type: "number",
//                         description: "Discount percentage (0-100)",
//                         minimum: 0,
//                         maximum: 100,
//                     },
//                 },
//                 required: ["price", "discount_percent"],
//                 additionalProperties: false,
//             },
//         },
//     ],
// }));


// ============================================================
// SECCIÓN B: Implementar el handler (CallToolRequest)
// ============================================================
// CallToolRequestSchema corresponde al método "tools/call".
// El handler recibe {name, arguments} y retorna {content: [...]}.
//
// Descomenta las líneas siguientes:
// server.setRequestHandler(CallToolRequestSchema, async (request) => {
//     const { name, arguments: args } = request.params;
//
//     if (name === "calculate_discount") {
//         const price = (args?.price as number) ?? 0;
//         const discountPercent = (args?.discount_percent as number) ?? 0;
//
//         const discountAmount = price * (discountPercent / 100);
//         const finalPrice = price - discountAmount;
//
//         return {
//             content: [
//                 {
//                     type: "text",
//                     text: [
//                         `Precio original: $${price.toFixed(2)}`,
//                         `Descuento (${discountPercent}%): $${discountAmount.toFixed(2)}`,
//                         `Precio final: $${finalPrice.toFixed(2)}`,
//                     ].join("\n"),
//                 },
//             ],
//         };
//     }
//
//     throw new Error(`Unknown tool: ${name}`);
// });


// ============================================================
// SECCIÓN C: Manejo de errores con isError
// ============================================================
// En TypeScript, isError se incluye en el objeto de retorno.
//
// Reemplaza el handler de la Sección B por esta versión:
//
// server.setRequestHandler(CallToolRequestSchema, async (request) => {
//     const { name, arguments: args } = request.params;
//
//     if (name === "calculate_discount") {
//         // Use Zod for runtime validation (extra safety beyond inputSchema)
//         const schema = z.object({
//             price: z.number().positive(),
//             discount_percent: z.number().min(0).max(100),
//         });
//
//         const parsed = schema.safeParse(args);
//         if (!parsed.success) {
//             return {
//                 content: [{ type: "text", text: `Validation error: ${parsed.error.message}` }],
//                 isError: true,
//             };
//         }
//
//         const { price, discount_percent: discountPercent } = parsed.data;
//         const discountAmount = price * (discountPercent / 100);
//         const finalPrice = price - discountAmount;
//
//         return {
//             content: [
//                 {
//                     type: "text",
//                     text: [
//                         `Precio original: $${price.toFixed(2)}`,
//                         `Descuento (${discountPercent}%): $${discountAmount.toFixed(2)}`,
//                         `Precio final: $${finalPrice.toFixed(2)}`,
//                     ].join("\n"),
//                 },
//             ],
//         };
//     }
//
//     throw new Error(`Unknown tool: ${name}`);
// });


// ============================================================
// SECCIÓN D: Annotations en TypeScript
// ============================================================
// Las annotations se agregan dentro del objeto del tool en ListTools:
//
// {
//     name: "calculate_discount",
//     description: "...",
//     inputSchema: { ... },
//     annotations: {
//         title: "Calcular descuento",
//         readOnlyHint: true,
//         idempotentHint: true,
//         destructiveHint: false,
//     }
// }


// ============================================================
// Punto de entrada del servidor MCP
// ============================================================
const transport = new StdioServerTransport();
await server.connect(transport);
