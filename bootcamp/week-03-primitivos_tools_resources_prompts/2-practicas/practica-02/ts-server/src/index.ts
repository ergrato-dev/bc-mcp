/**
 * MCP Server — Práctica 02: Resources en TypeScript
 * Semana 03 — Los Tres Primitivos
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    ListResourcesRequestSchema,
    ReadResourceRequestSchema,
    ListResourceTemplatesRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
    { name: "practice-02-resources-ts", version: "1.0.0" },
    { capabilities: { resources: {} } }
);

// In-memory data
const PRODUCTS_DB: Record<string, { id: number; name: string; price: number; category: string }> = {
    "1": { id: 1, name: "Laptop Pro", price: 1299.99, category: "electronics" },
    "2": { id: 2, name: "Mechanical Keyboard", price: 149.50, category: "electronics" },
    "3": { id: 3, name: "Desk Chair", price: 399.00, category: "furniture" },
};

const APP_SETTINGS = {
    app_name: "MCP Practice Store",
    version: "1.0.0",
    currency: "USD",
    max_items_per_page: 20,
};

const PRODUCTS_SCHEMA = {
    table: "products",
    columns: [
        { name: "id", type: "INTEGER", primary_key: true },
        { name: "name", type: "TEXT", not_null: true },
        { name: "price", type: "REAL", not_null: true },
        { name: "category", type: "TEXT" },
    ],
};


// ============================================================
// SECCIÓN A: Declarar lista de Resources estáticos
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListResourcesRequestSchema, async () => ({
//     resources: [
//         {
//             uri: "config://app/settings",
//             name: "Application settings",
//             description: "Current application configuration values",
//             mimeType: "application/json",
//         },
//         {
//             uri: "db://schema/products",
//             name: "Products table schema",
//             description: "Column definitions and types for the products table",
//             mimeType: "application/json",
//         },
//     ],
// }));


// ============================================================
// SECCIÓN B: Implementar read_resource
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
//     const { uri } = request.params;
//
//     if (uri === "config://app/settings") {
//         return {
//             contents: [{
//                 uri,
//                 text: JSON.stringify(APP_SETTINGS, null, 2),
//                 mimeType: "application/json",
//             }],
//         };
//     }
//
//     if (uri === "db://schema/products") {
//         return {
//             contents: [{
//                 uri,
//                 text: JSON.stringify(PRODUCTS_SCHEMA, null, 2),
//                 mimeType: "application/json",
//             }],
//         };
//     }
//
//     throw new Error(`Resource not found: ${uri}`);
// });


// ============================================================
// SECCIÓN C: Resource Templates
// ============================================================
// Descomenta las líneas siguientes:
// server.setRequestHandler(ListResourceTemplatesRequestSchema, async () => ({
//     resourceTemplates: [
//         {
//             uriTemplate: "db://products/{product_id}",
//             name: "Product by ID",
//             description: "Returns data for a specific product by its ID",
//             mimeType: "application/json",
//         },
//     ],
// }));
//
// Y actualiza el handler de ReadResource para manejar el template.
// Agrega este caso ANTES del throw en read_resource:
//
//     if (uri.startsWith("db://products/")) {
//         const productId = uri.replace("db://products/", "");
//         const product = PRODUCTS_DB[productId];
//         if (!product) {
//             throw new Error(`Product ${productId} not found`);
//         }
//         return {
//             contents: [{
//                 uri,
//                 text: JSON.stringify(product, null, 2),
//                 mimeType: "application/json",
//             }],
//         };
//     }


// ============================================================
// SECCIÓN D: BlobResourceContents (contenido binario)
// ============================================================
// En TypeScript, el blob es un string base64.
// Agrega a la lista de resources:
//
//     {
//         uri: "file://logo.png",
//         name: "Application logo",
//         mimeType: "image/png",
//     },
//
// Y en el read_resource handler:
//
//     if (uri === "file://logo.png") {
//         const pngBytes = Buffer.from([
//             0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
//             0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
//             0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
//             0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53, 0xDE,
//         ]);
//         return {
//             contents: [{
//                 uri,
//                 blob: pngBytes.toString("base64"),
//                 mimeType: "image/png",
//             }],
//         };
//     }


const transport = new StdioServerTransport();
await server.connect(transport);
