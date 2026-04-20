// ============================================
// PASO 1: Importar módulos del SDK TypeScript
// ============================================
// Descomenta las siguientes líneas:
// import "dotenv/config";
// import { Client } from "@modelcontextprotocol/sdk/client/index.js";
// import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// ============================================
// PASO 2: Crear StdioClientTransport
// ============================================
// El transport configura cómo lanzar el proceso servidor.
// Descomenta las siguientes líneas:
// function createTransport(): StdioClientTransport {
//   return new StdioClientTransport({
//     command: process.env.SERVER_COMMAND ?? "python",
//     args: [process.env.SERVER_PATH ?? "server.py"],
//     env: {
//       ...process.env,                                    // heredar entorno completo
//       DB_PATH: process.env.DB_PATH ?? "./data/library.db",
//     },
//   });
// }

// ============================================
// PASO 3: Instanciar Client y conectar
// ============================================
// Descomenta la función main y el bloque try/finally:
// async function main(): Promise<void> {
//   const transport = createTransport();
//   const client = new Client({
//     name: "library-client",
//     version: "1.0.0",
//   });
//
//   console.log("🔌 Conectando al servidor MCP...");
//
//   try {
//     await client.connect(transport);
//     console.log("✅ Conectado exitosamente\n");
//
//     // ============================================
//     // PASO 4: Imprimir información del servidor
//     // ============================================
//     // getServerVersion() retorna { name, version } del servidor conectado.
//     // Descomenta las siguientes líneas:
//     // const serverInfo = client.getServerVersion();
//     // console.log("📋 Información del Servidor:");
//     // console.log(`   Nombre:  ${serverInfo?.name ?? "desconocido"}`);
//     // console.log(`   Versión: ${serverInfo?.version ?? "desconocida"}`);
//
//   } finally {
//     console.log("\n🔒 Cerrando conexión...");
//     await client.close();
//     console.log("✅ Listo");
//   }
// }
//
// main().catch((e: unknown) => {
//   const message = e instanceof Error ? e.message : String(e);
//   console.error(`❌ Error: ${message}`);
//   process.exit(1);
// });
