/**
 * server.test.ts — Tests de integración para el MCP Server.
 *
 * Pasos a descomentar:
 *   PASO 2: test list_tools
 *   PASO 3: tests echo y add
 *   PASO 4: tests greet y validación
 */
import { describe, it, expect, beforeEach, afterEach } from "vitest";


// ============================================================
// PASO 2: Verificar que el server expone las tools esperadas
// ============================================================
// Descomenta el siguiente bloque:
// import { server } from "../src/server.js";
// import { setupTestServer, type TestServerSetup } from "./helpers/test-setup.js";
//
// describe("MCP Server — list tools", () => {
//   let setup: TestServerSetup;
//
//   beforeEach(async () => {
//     setup = await setupTestServer(server);
//   });
//
//   afterEach(async () => {
//     await setup.cleanup();
//   });
//
//   it("should expose echo, add and greet tools", async () => {
//     const { tools } = await setup.client.listTools();
//     const names = tools.map((t) => t.name);
//
//     expect(names).toContain("echo");
//     expect(names).toContain("add");
//     expect(names).toContain("greet");
//   });
// });


// ============================================================
// PASO 3: Tests de las tools echo y add
// ============================================================
// Descomenta el siguiente bloque:
// describe("Tool: echo", () => {
//   let setup: TestServerSetup;
//
//   beforeEach(async () => {
//     setup = await setupTestServer(server);
//   });
//
//   afterEach(async () => {
//     await setup.cleanup();
//   });
//
//   it("should return the same message", async () => {
//     const result = await setup.client.callTool({
//       name: "echo",
//       arguments: { message: "Hello MCP!" },
//     });
//     const text = (result.content[0] as { type: string; text: string }).text;
//     expect(text).toBe("Hello MCP!");
//   });
// });
//
// describe("Tool: add", () => {
//   let setup: TestServerSetup;
//
//   beforeEach(async () => {
//     setup = await setupTestServer(server);
//   });
//
//   afterEach(async () => {
//     await setup.cleanup();
//   });
//
//   it("should sum two positive numbers", async () => {
//     const result = await setup.client.callTool({
//       name: "add",
//       arguments: { a: 7, b: 5 },
//     });
//     const text = (result.content[0] as { type: string; text: string }).text;
//     expect(text).toBe("12");
//   });
//
//   it("should handle negative numbers", async () => {
//     const result = await setup.client.callTool({
//       name: "add",
//       arguments: { a: -3, b: 10 },
//     });
//     const text = (result.content[0] as { type: string; text: string }).text;
//     expect(text).toBe("7");
//   });
// });


// ============================================================
// PASO 4: Tests de greet y validación de inputs
// ============================================================
// Descomenta el siguiente bloque:
// describe("Tool: greet", () => {
//   let setup: TestServerSetup;
//
//   beforeEach(async () => {
//     setup = await setupTestServer(server);
//   });
//
//   afterEach(async () => {
//     await setup.cleanup();
//   });
//
//   it("should greet in English by default", async () => {
//     const result = await setup.client.callTool({
//       name: "greet",
//       arguments: { name: "Alice", language: "en" },
//     });
//     const text = (result.content[0] as { type: string; text: string }).text;
//     expect(text).toBe("Hello, Alice!");
//   });
//
//   it("should greet in Spanish", async () => {
//     const result = await setup.client.callTool({
//       name: "greet",
//       arguments: { name: "Carlos", language: "es" },
//     });
//     const text = (result.content[0] as { type: string; text: string }).text;
//     expect(text).toContain("Hola");
//   });
//
//   it("should reject invalid language", async () => {
//     // El schema Zod valida — el server debe retornar error
//     await expect(
//       setup.client.callTool({
//         name: "greet",
//         arguments: { name: "Bob", language: "de" },
//       })
//     ).rejects.toThrow();
//   });
// });
