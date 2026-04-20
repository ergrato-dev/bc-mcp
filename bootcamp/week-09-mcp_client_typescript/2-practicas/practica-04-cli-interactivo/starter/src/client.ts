// Constantes de presentación (pre-implementadas)
const BANNER = `
╔══════════════════════════════════════╗
║  Library CLI — MCP Client TypeScript ║
╚══════════════════════════════════════╝`;

const HELP = "Comandos: search <query> | add | tools | stats | quit";
const DIVIDER = "─".repeat(44);

// ============================================
// PASO 1: Conectar al servidor y configurar readline
// ============================================
// node:readline/promises es la API async nativa de Node.js 22 (sin paquete extra).
// Descomenta las siguientes líneas:
// import "dotenv/config";
// import { createInterface } from "node:readline/promises";
// import { Client } from "@modelcontextprotocol/sdk/client/index.js";
// import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
//
// async function connectToServer(): Promise<Client> {
//   const transport = new StdioClientTransport({
//     command: process.env.SERVER_COMMAND ?? "python",
//     args: [process.env.SERVER_PATH ?? "server.py"],
//     env: { ...process.env, DB_PATH: process.env.DB_PATH ?? "./data/library.db" },
//   });
//   const client = new Client({ name: "library-cli", version: "1.0.0" });
//   await client.connect(transport);
//   return client;
// }

// ============================================
// PASO 2: Función printHelp
// ============================================
// Descomenta las siguientes líneas:
// function printHelp(): void {
//   console.log("\n" + HELP);
//   console.log("  search <query>  — busca libros por texto");
//   console.log("  add             — agrega un libro (solicita datos)");
//   console.log("  tools           — lista los tools del servidor");
//   console.log("  stats           — muestra estadísticas de la BD");
//   console.log("  quit            — cierra el CLI");
//   console.log(DIVIDER);
// }

// ============================================
// PASO 3: Bucle principal de lectura de comandos
// ============================================
// rl.question() es async — no bloquea el event loop de Node.js.
// Descomenta las siguientes líneas:
// async function runLoop(client: Client): Promise<void> {
//   const rl = createInterface({ input: process.stdin, output: process.stdout });
//   printHelp();
//   try {
//     while (true) {
//       const line = await rl.question("\n>> ");
//       const parts = line.trim().split(/\s+/);
//       const command = parts[0]?.toLowerCase() ?? "";
//       const arg = parts.slice(1).join(" ");
//
//       // ============================================
//       // PASO 4: Despachar search y tools
//       // ============================================
//       // Descomenta las siguientes líneas:
//       // if (command === "search") {
//       //   if (!arg) { console.log("  Uso: search <query>"); continue; }
//       //   const result = await client.callTool({ name: "search_books", arguments: { query: arg } });
//       //   const first = result.content[0];
//       //   if (result.isError || !first || first.type !== "text") {
//       //     console.log("  Sin resultados o error.");
//       //     continue;
//       //   }
//       //   const books = JSON.parse(first.text) as Array<{ title: string; author: string; year: number }>;
//       //   if (books.length === 0) { console.log("  Sin resultados."); continue; }
//       //   books.forEach((b, i) => console.log(`  ${i + 1}. ${b.title} (${b.author}, ${b.year})`));
//
//       // } else if (command === "tools") {
//       //   const tools = await client.listTools();
//       //   console.log(`  Tools disponibles (${tools.tools.length}):`);
//       //   tools.tools.forEach((t) => console.log(`    • ${t.name}`));
//
//       // ============================================
//       // PASO 5: Despachar stats, quit y desconocidos
//       // ============================================
//       // Descomenta las siguientes líneas:
//       // } else if (command === "stats") {
//       //   const r = await client.readResource({ uri: "db://books/stats" });
//       //   const c = r.contents[0];
//       //   if (c && "text" in c && c.text) {
//       //     const s = JSON.parse(c.text) as { total_books: number; books_with_isbn: number; average_year: number };
//       //     console.log(`  Total libros: ${s.total_books} | Con ISBN: ${s.books_with_isbn} | Año promedio: ${Math.round(s.average_year ?? 0)}`);
//       //   }
//
//       // } else if (command === "quit" || command === "exit") {
//       //   console.log("  👋 ¡Hasta luego!");
//       //   break;
//
//       // } else {
//       //   console.log(`  Comando desconocido: "${command}"`);
//       //   printHelp();
//       // }
//     }
//   } finally {
//     rl.close();
//   }
// }

// ============================================
// Main
// ============================================
// Descomenta al completar todos los pasos:
// async function main(): Promise<void> {
//   console.log(BANNER);
//   const client = await connectToServer();
//   const info = client.getServerVersion();
//   console.log(`✅ Conectado: ${info?.name} v${info?.version}`);
//
//   try {
//     await runLoop(client);
//   } finally {
//     await client.close();
//   }
// }
//
// main().catch((e: unknown) => {
//   console.error(`❌ ${e instanceof Error ? e.message : String(e)}`);
//   process.exit(1);
// });
