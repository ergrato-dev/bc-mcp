// Test setup helper — creates an in-memory MCP client for testing
// Uses InMemoryTransport to connect client and server without network

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";
import { server } from "../../src/server.js";

export async function setupTestClient(): Promise<Client> {
  const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();
  await server.connect(serverTransport);
  const client = new Client(
    { name: "test-client", version: "1.0.0" },
    { capabilities: {} },
  );
  await client.connect(clientTransport);
  return client;
}
