/**
 * Book catalog MCP server — práctica de Resources en TypeScript.
 * Semana 06 — Los 3 Primitivos
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// =============================================
// BASE DE DATOS — catálogo de libros
// =============================================
interface Book {
  isbn: string;
  title: string;
  author: string;
  year: number;
  available: boolean;
}

const BOOKS: Book[] = [
  {
    isbn: "978-0-13-110362-7",
    title: "The C Programming Language",
    author: "Brian Kernighan, Dennis Ritchie",
    year: 1978,
    available: true,
  },
  {
    isbn: "978-0-20-161622-4",
    title: "The Pragmatic Programmer",
    author: "Andrew Hunt, David Thomas",
    year: 1999,
    available: true,
  },
  {
    isbn: "978-0-59-651798-1",
    title: "Python Cookbook",
    author: "David Beazley, Brian Jones",
    year: 2013,
    available: false,
  },
  {
    isbn: "978-0-13-468599-1",
    title: "Clean Code",
    author: "Robert C. Martin",
    year: 2008,
    available: true,
  },
];

const server = new Server({ name: "book-catalog", version: "1.0.0" });

// =============================================
// SECCIÓN 1: Handler resources/list
// =============================================
// Registra los resources estáticos que este server expone.
// El cliente MCP llama a resources/list para descubrirlos.
// Descomenta las siguientes líneas:
// server.setRequestHandler(ListResourcesRequestSchema, async () => ({
//   resources: [
//     {
//       uri: "books://all",
//       name: "All Books",
//       description: "Complete book catalog",
//       mimeType: "application/json",
//     },
//     {
//       uri: "books://available",
//       name: "Available Books",
//       description: "Books available for loan",
//       mimeType: "application/json",
//     },
//   ],
// }));


// =============================================
// SECCIÓN 2: Handler resources/read (estáticos)
// =============================================
// Cuando el cliente pide leer una URI específica, este handler responde.
// Siempre retorna: { contents: [{ uri, mimeType, text }] }
// Descomenta las siguientes líneas:
// server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
//   const { uri } = request.params;
//
//   if (uri === "books://all") {
//     return {
//       contents: [
//         {
//           uri,
//           mimeType: "application/json",
//           text: JSON.stringify(BOOKS),
//         },
//       ],
//     };
//   }
//
//   if (uri === "books://available") {
//     const available = BOOKS.filter((b) => b.available);
//     return {
//       contents: [
//         {
//           uri,
//           mimeType: "application/json",
//           text: JSON.stringify(available),
//         },
//       ],
//     };
//   }
//
//   throw new Error(`Resource not found: ${uri}`);
// });


// =============================================
// SECCIÓN 3: Resource template books://isbn/{isbn}
// =============================================
// En TypeScript, los templates requieren matching manual con regex.
// Reemplaza el handler de la SECCIÓN 2 (comentando ese bloque)
// y descomenta este que soporta tanto los resources estáticos como el template:
// server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
//   const { uri } = request.params;
//
//   if (uri === "books://all") {
//     return {
//       contents: [{ uri, mimeType: "application/json", text: JSON.stringify(BOOKS) }],
//     };
//   }
//
//   if (uri === "books://available") {
//     return {
//       contents: [
//         { uri, mimeType: "application/json", text: JSON.stringify(BOOKS.filter((b) => b.available)) },
//       ],
//     };
//   }
//
//   // Template: books://isbn/{isbn}
//   const templateMatch = uri.match(/^books:\/\/isbn\/(.+)$/);
//   if (templateMatch) {
//     const isbn = templateMatch[1];
//     const book = BOOKS.find((b) => b.isbn === isbn);
//     const result = book ?? { error: `Book with ISBN '${isbn}' not found` };
//     return {
//       contents: [{ uri, mimeType: "application/json", text: JSON.stringify(result) }],
//     };
//   }
//
//   throw new Error(`Resource not found: ${uri}`);
// });


const transport = new StdioServerTransport();
await server.connect(transport);
