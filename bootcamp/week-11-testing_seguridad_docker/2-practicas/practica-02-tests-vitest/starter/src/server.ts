/**
 * server.ts — MCP Server mínimo con una tool "echo" para tests.
 *
 * Para tests más complejos, adaptar al Library Server de semana 07.
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

// Create server instance
export const server = new McpServer({
  name: "practica-02-server",
  version: "1.0.0",
});

// ── Tool: echo ──────────────────────────────────────────────
// Tool simple para verificar la comunicación MCP
server.tool(
  "echo",
  "Retorna el mensaje recibido",
  {
    message: z.string().min(1).max(500).describe("Mensaje a retornar"),
  },
  async ({ message }) => ({
    content: [{ type: "text", text: message }],
  }),
);

// ── Tool: add ───────────────────────────────────────────────
// Tool aritmética para tests de entrada/salida
server.tool(
  "add",
  "Suma dos números enteros",
  {
    a: z.number().int().describe("Primer número"),
    b: z.number().int().describe("Segundo número"),
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }],
  }),
);

// ── Tool: greet ─────────────────────────────────────────────
server.tool(
  "greet",
  "Genera un saludo personalizado",
  {
    name: z.string().min(1).max(100).describe("Nombre de la persona"),
    language: z
      .enum(["en", "es", "fr"])
      .default("en")
      .describe("Idioma del saludo"),
  },
  async ({ name, language }) => {
    const greetings: Record<string, string> = {
      en: `Hello, ${name}!`,
      es: `¡Hola, ${name}!`,
      fr: `Bonjour, ${name}!`,
    };
    return {
      content: [{ type: "text", text: greetings[language] }],
    };
  },
);
