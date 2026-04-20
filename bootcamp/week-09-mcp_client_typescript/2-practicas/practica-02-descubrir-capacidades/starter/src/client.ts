// ============================================
// PASO 1: Conectar al servidor
// ============================================
// Descomenta las siguientes líneas:
// import "dotenv/config";
// import { Client } from "@modelcontextprotocol/sdk/client/index.js";
// import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
// import type {
//   ListToolsResult,
//   ListResourcesResult,
//   ListPromptsResult,
// } from "@modelcontextprotocol/sdk/types.js";
//
// async function connectToServer(): Promise<Client> {
//   const transport = new StdioClientTransport({
//     command: process.env.SERVER_COMMAND ?? "python",
//     args: [process.env.SERVER_PATH ?? "server.py"],
//     env: { ...process.env, DB_PATH: process.env.DB_PATH ?? "./data/library.db" },
//   });
//   const client = new Client({ name: "discovery-client", version: "1.0.0" });
//   await client.connect(transport);
//   return client;
// }

// ============================================
// PASO 2: Listar tools con schema completo
// ============================================
// Muestra nombre, descripción y parámetros (marcando los requeridos con *)
// Descomenta las siguientes líneas:
// async function showTools(client: Client): Promise<void> {
//   const result: ListToolsResult = await client.listTools();
//   console.log(`\n📦 Tools (${result.tools.length}):\n`);
//   for (const tool of result.tools) {
//     const required: string[] = tool.inputSchema.required ?? [];
//     const props = Object.keys(tool.inputSchema.properties ?? {});
//     const paramStr = props
//       .map((p) => (required.includes(p) ? `${p}*` : p))
//       .join(", ");
//     console.log(`  • ${tool.name.padEnd(22)} — ${tool.description ?? ""}`);
//     if (paramStr) console.log(`    Params: ${paramStr}  (* = requerido)`);
//   }
// }

// ============================================
// PASO 3: Listar resources
// ============================================
// Descomenta las siguientes líneas:
// async function showResources(client: Client): Promise<void> {
//   const result: ListResourcesResult = await client.listResources();
//   console.log(`\n📂 Resources (${result.resources.length}):\n`);
//   for (const res of result.resources) {
//     const mime = res.mimeType ? ` (${res.mimeType})` : "";
//     console.log(`  • ${res.uri}${mime}`);
//     if (res.description) console.log(`    ${res.description}`);
//   }
// }

// ============================================
// PASO 4: Listar prompts
// ============================================
// Descomenta las siguientes líneas:
// async function showPrompts(client: Client): Promise<void> {
//   const result: ListPromptsResult = await client.listPrompts();
//   console.log(`\n💬 Prompts (${result.prompts.length}):\n`);
//   if (result.prompts.length === 0) {
//     console.log("  (ninguno)");
//     return;
//   }
//   for (const p of result.prompts) {
//     const args = (p.arguments ?? [])
//       .map((a) => (a.required ? `${a.name}*` : a.name))
//       .join(", ");
//     console.log(`  • ${p.name}  —  ${p.description ?? ""}`);
//     if (args) console.log(`    Args: ${args}`);
//   }
// }

// ============================================
// Main — orquesta todo
// ============================================
// Descomenta el bloque main al completar los pasos anteriores:
// async function main(): Promise<void> {
//   console.log("🔌 Conectando...");
//   const client = await connectToServer();
//   const info = client.getServerVersion();
//   console.log(`✅ Conectado: ${info?.name} v${info?.version}\n`);
//
//   try {
//     await showTools(client);
//     await showResources(client);
//     await showPrompts(client);
//   } finally {
//     await client.close();
//   }
// }
//
// main().catch((e: unknown) => {
//   console.error(`❌ ${e instanceof Error ? e.message : String(e)}`);
//   process.exit(1);
// });
