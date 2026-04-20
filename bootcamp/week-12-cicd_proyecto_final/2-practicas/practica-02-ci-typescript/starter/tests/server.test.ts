// Tests for the TypeScript CI practice MCP server
//
// INSTRUCCIONES: Descomenta las secciones indicadas en cada PASO.

import { describe, it, expect, beforeAll } from "vitest";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { setupTestClient } from "./helpers/test-setup.js";

// ============================================
// PASO 3: Setup del cliente de test
// ============================================
// Descomenta las siguientes líneas:

// let client: Client;
//
// beforeAll(async () => {
//   client = await setupTestClient();
// });

// ============================================
// PASO 4: Tests del tool `add`
// ============================================
// Descomenta el bloque describe:

// describe("add tool", () => {
//   it("should add two positive numbers", async () => {
//     const result = await client.callTool({ name: "add", arguments: { a: 2, b: 3 } });
//     const data = JSON.parse((result.content[0] as { text: string }).text);
//     expect(data.result).toBe(5);
//   });
//
//   it("should handle negative numbers", async () => {
//     const result = await client.callTool({ name: "add", arguments: { a: -5, b: 3 } });
//     const data = JSON.parse((result.content[0] as { text: string }).text);
//     expect(data.result).toBe(-2);
//   });
// });

// ============================================
// PASO 5: Tests del tool `greet`
// ============================================
// Descomenta el bloque describe:

// describe("greet tool", () => {
//   it("should greet in Spanish by default", async () => {
//     const result = await client.callTool({ name: "greet", arguments: { name: "Ana" } });
//     const data = JSON.parse((result.content[0] as { text: string }).text);
//     expect(data.greeting).toBe("Hola, Ana!");
//   });
//
//   it("should greet in English", async () => {
//     const result = await client.callTool({ name: "greet", arguments: { name: "Bob", language: "en" } });
//     const data = JSON.parse((result.content[0] as { text: string }).text);
//     expect(data.greeting).toBe("Hello, Bob!");
//   });
// });

// ============================================
// PASO 5: Test de lista de tools
// ============================================
// Descomenta la función:

// it("should list exactly 2 tools", async () => {
//   const tools = await client.listTools();
//   const names = tools.tools.map((t) => t.name);
//   expect(names).toContain("add");
//   expect(names).toContain("greet");
//   expect(tools.tools.length).toBe(2);
// });
