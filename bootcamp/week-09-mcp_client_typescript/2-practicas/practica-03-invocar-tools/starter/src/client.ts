// ============================================
// PASO 1: Conectar al servidor y definir tipos
// ============================================
// Descomenta las siguientes líneas:
// import "dotenv/config";
// import { Client } from "@modelcontextprotocol/sdk/client/index.js";
// import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
// import type { ReadResourceResult } from "@modelcontextprotocol/sdk/types.js";
//
// // Interfaz que modela un libro de la biblioteca
// interface Book {
//   id: number;
//   title: string;
//   author: string;
//   year: number;
//   isbn?: string | null;
// }
//
// // Interfaz para las estadísticas del resource db://books/stats
// interface BookStats {
//   total_books: number;
//   books_with_isbn: number;
//   average_year: number;
// }
//
// async function connectToServer(): Promise<Client> {
//   const transport = new StdioClientTransport({
//     command: process.env.SERVER_COMMAND ?? "python",
//     args: [process.env.SERVER_PATH ?? "server.py"],
//     env: { ...process.env, DB_PATH: process.env.DB_PATH ?? "./data/library.db" },
//   });
//   const client = new Client({ name: "tools-client", version: "1.0.0" });
//   await client.connect(transport);
//   return client;
// }

// ============================================
// PASO 2: Buscar libros con search_books
// ============================================
// callTool retorna CallToolResult con content[0].text = JSON serializado
// Descomenta las siguientes líneas:
// async function searchBooks(client: Client, query: string): Promise<Book[]> {
//   console.log(`\n🔍 Buscando "${query}"...`);
//   const result = await client.callTool({
//     name: "search_books",
//     arguments: { query },
//   });
//   const first = result.content[0];
//   if (!first || first.type !== "text") return [];
//   const books = JSON.parse(first.text) as Book[];
//   console.log(`  Encontrados: ${books.length} libros`);
//   books.forEach((b, i) => {
//     console.log(`  ${i + 1}. ${b.title} (${b.author}, ${b.year})`);
//   });
//   return books;
// }

// ============================================
// PASO 3: Detectar isError — get_book con id inválido
// ============================================
// Cuando isError=true, content[0].text contiene el mensaje de error del server
// Descomenta las siguientes líneas:
// async function demonstrateIsError(client: Client): Promise<void> {
//   console.log("\n❌ Prueba de isError (id=9999)...");
//   const result = await client.callTool({
//     name: "get_book",
//     arguments: { id: 9999 },
//   });
//   if (result.isError) {
//     // Para acceder a .text, discriminar por type o hacer cast
//     const first = result.content[0];
//     const msg = first?.type === "text" ? first.text : "Error sin detalle";
//     console.log(`  Error del servidor: ${msg}`);
//   } else {
//     // Si no hay error, parsear y mostrar el libro
//     const first = result.content[0];
//     if (first?.type === "text") {
//       const book = JSON.parse(first.text) as Book;
//       console.log(`  Libro encontrado: ${book.title}`);
//     }
//   }
// }

// ============================================
// PASO 4: Agregar un libro con add_book
// ============================================
// Descomenta las siguientes líneas:
// async function addBook(
//   client: Client,
//   title: string,
//   author: string,
//   year: number,
//   isbn?: string,
// ): Promise<Book | null> {
//   console.log(`\n➕ Agregando "${title}"...`);
//   const args: Record<string, unknown> = { title, author, year };
//   if (isbn) args.isbn = isbn;
//   const result = await client.callTool({ name: "add_book", arguments: args });
//   if (result.isError) {
//     const first = result.content[0];
//     const msg = first?.type === "text" ? first.text : "Error";
//     console.log(`  ❌ ${msg}`);
//     return null;
//   }
//   const first = result.content[0];
//   if (!first || first.type !== "text") return null;
//   const book = JSON.parse(first.text) as Book;
//   console.log(`  ✅ Creado con id=${book.id}`);
//   return book;
// }

// ============================================
// PASO 5: Leer resource db://books/stats
// ============================================
// readResource retorna ReadResourceResult con contents[0].text = JSON
// Descomenta las siguientes líneas:
// async function showStats(client: Client): Promise<void> {
//   console.log("\n📊 Estadísticas:");
//   const result: ReadResourceResult = await client.readResource({
//     uri: "db://books/stats",
//   });
//   const first = result.contents[0];
//   if (!first || !("text" in first) || !first.text) {
//     console.log("  (sin datos)");
//     return;
//   }
//   const stats = JSON.parse(first.text) as BookStats;
//   console.log(`  Total libros:     ${stats.total_books}`);
//   console.log(`  Con ISBN:         ${stats.books_with_isbn}`);
//   console.log(`  Año promedio:     ${Math.round(stats.average_year ?? 0)}`);
// }

// ============================================
// Main
// ============================================
// Descomenta al completar todos los pasos:
// async function main(): Promise<void> {
//   console.log("🔌 Conectando al servidor MCP...");
//   const client = await connectToServer();
//   const info = client.getServerVersion();
//   console.log(`✅ Conectado: ${info?.name} v${info?.version}`);
//
//   try {
//     await searchBooks(client, "TypeScript");
//     await addBook(client, "Clean Code", "Robert C. Martin", 2008, "9780132350884");
//     await demonstrateIsError(client);
//     await showStats(client);
//   } finally {
//     await client.close();
//   }
// }
//
// main().catch((e: unknown) => {
//   console.error(`❌ ${e instanceof Error ? e.message : String(e)}`);
//   process.exit(1);
// });
