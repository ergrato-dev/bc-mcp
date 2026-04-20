/**
 * test-setup.ts — Helper reutilizable para conectar server y client en memoria.
 *
 * Pasos a descomentar:
 *   PASO 1: función setupTestServer
 */

// ============================================================
// PASO 1: Helper setupTestServer
// ============================================================
// Este helper crea un par de transports en memoria y conecta
// el server al client. Retorna el client y una función cleanup.
//
// Descomenta las siguientes líneas:
// import { Client } from "@modelcontextprotocol/sdk/client/index.js";
// import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";
// import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
//
// export interface TestServerSetup {
//   client: Client;
//   cleanup: () => Promise<void>;
// }
//
// /**
//  * Conecta un McpServer a un Client usando transports en memoria.
//  * No abre sockets ni procesos — todo ocurre en memoria.
//  */
// export async function setupTestServer(
//   server: McpServer
// ): Promise<TestServerSetup> {
//   const [clientTransport, serverTransport] =
//     InMemoryTransport.createLinkedPair();
//
//   // Conectar el server al transport del lado server
//   await server.connect(serverTransport);
//
//   // Crear y conectar el client al transport del lado client
//   const client = new Client(
//     { name: "test-client", version: "1.0.0" },
//     { capabilities: {} }
//   );
//   await client.connect(clientTransport);
//
//   return {
//     client,
//     cleanup: async () => {
//       await client.close();
//     },
//   };
// }
