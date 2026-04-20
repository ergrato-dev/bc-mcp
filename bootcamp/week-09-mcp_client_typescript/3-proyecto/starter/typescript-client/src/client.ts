import "dotenv/config";
import { createInterface } from "node:readline/promises";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { config } from "./config.js";
import type { Book, BookStats, OpenLibraryResult } from "./types.js";

// ============================================
// TODO 1: Conectar al servidor MCP
// ============================================
// Implementa connectToServer():
// 1. Crear StdioClientTransport con config.serverCommand, config.serverPath
//    y env: { ...process.env, DB_PATH: config.dbPath }
// 2. Crear Client con { name: "library-cli-ts", version: "1.0.0" }
// 3. Llamar await client.connect(transport)
// 4. Retornar el client conectado
//
// Referencia: teoria/02-stdioclienttransport-y-conexion.md
// ─────────────────────────────────────────────────────────
async function connectToServer(): Promise<Client> {
  // TODO 1: Implementar
  throw new Error("TODO 1: connectToServer() no implementado");
}

// ============================================
// TODO 2: Listar tools disponibles
// ============================================
// Implementa listAvailableTools(client):
// 1. Llamar await client.listTools()
// 2. Imprimir el total de tools con su nombre y descripción
// 3. No retornar nada (void)
//
// Referencia: teoria/03-discover-y-llamar-tools-resources-prompts.md
// ─────────────────────────────────────────────────────────
async function listAvailableTools(client: Client): Promise<void> {
  // TODO 2: Implementar
  throw new Error("TODO 2: listAvailableTools() no implementado");
}

// ============================================
// TODO 3: Buscar libros en la BD local
// ============================================
// Implementa searchBooks(client, query): Promise<Book[]>
// 1. Llamar client.callTool({ name: "search_books", arguments: { query } })
// 2. Verificar result.isError → retornar []
// 3. Discriminar result.content[0] por type === "text"
// 4. JSON.parse(first.text) as Book[] y retornar
//
// Referencia: teoria/04-tipado-y-procesamiento-de-resultados.md
// ─────────────────────────────────────────────────────────
async function searchBooks(client: Client, query: string): Promise<Book[]> {
  // TODO 3: Implementar
  throw new Error("TODO 3: searchBooks() no implementado");
}

// ============================================
// TODO 4: Agregar un libro a la BD local
// ============================================
// Implementa addBook(client, title, author, year, isbn?): Promise<Book | null>
// 1. Construir args: Record<string, unknown> = { title, author, year }
//    Agregar isbn solo si está definido
// 2. Llamar client.callTool({ name: "add_book", arguments: args })
// 3. Si result.isError → mostrar mensaje y retornar null
// 4. Parsear el libro retornado y retornar Book con id asignado
//
// Referencia: teoria/04-tipado-y-procesamiento-de-resultados.md
// ─────────────────────────────────────────────────────────
async function addBook(
  client: Client,
  title: string,
  author: string,
  year: number,
  isbn?: string,
): Promise<Book | null> {
  // TODO 4: Implementar
  throw new Error("TODO 4: addBook() no implementado");
}

// ============================================
// TODO 5: Buscar en Open Library API
// ============================================
// Implementa searchOpenLibrary(client, title): Promise<OpenLibraryResult[]>
// 1. Llamar client.callTool({ name: "search_openlibrary", arguments: { title } })
// 2. Verificar result.isError → retornar []
// 3. Discriminar content[0] por type === "text"
// 4. JSON.parse(first.text) as OpenLibraryResult[] y retornar
//
// Nota: El server ya hace la llamada HTTP — el client solo invoca el tool.
// ─────────────────────────────────────────────────────────
async function searchOpenLibrary(
  client: Client,
  title: string,
): Promise<OpenLibraryResult[]> {
  // TODO 5: Implementar
  throw new Error("TODO 5: searchOpenLibrary() no implementado");
}

// ============================================
// TODO 6: Bucle interactivo de comandos
// ============================================
// Implementa interactiveLoop(client): Promise<void>
// 1. Crear rl con createInterface({ input: process.stdin, output: process.stdout })
// 2. Mostrar HELP con los comandos disponibles
// 3. Bucle while(true): leer línea con await rl.question(">> ")
// 4. Parsear command y arg (primer token = command, resto = arg)
// 5. Despachar:
//    - "search <query>"   → searchBooks(client, arg) → imprimir libros
//    - "add"              → pedir title/author/year/isbn con rl.question() → addBook()
//    - "ol <title>"       → searchOpenLibrary(client, arg) → imprimir resultados
//    - "tools"            → listAvailableTools(client)
//    - "stats"            → readResource db://books/stats → imprimir estadísticas
//    - "quit" | "exit"    → break
//    - desconocido        → mostrar HELP
// 6. En finally: rl.close()
//
// Referencia: teoria/05-manejo-errores-y-comparativa-python-ts.md
// ─────────────────────────────────────────────────────────
async function interactiveLoop(client: Client): Promise<void> {
  // TODO 6: Implementar
  throw new Error("TODO 6: interactiveLoop() no implementado");
}

// ────────────────────────────────────────────
// Main — no modificar
// ────────────────────────────────────────────
async function main(): Promise<void> {
  console.log("\n╔═══════════════════════════════════════════╗");
  console.log("║  Library CLI — MCP Client TypeScript      ║");
  console.log("╚═══════════════════════════════════════════╝\n");

  const client = await connectToServer();
  const info = client.getServerVersion();
  console.log(`✅ Conectado: ${info?.name} v${info?.version}\n`);

  try {
    await interactiveLoop(client);
  } finally {
    await client.close();
  }
}

main().catch((e: unknown) => {
  console.error(`❌ ${e instanceof Error ? e.message : String(e)}`);
  process.exit(1);
});
