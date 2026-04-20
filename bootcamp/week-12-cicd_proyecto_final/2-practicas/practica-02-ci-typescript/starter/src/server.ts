// Simple MCP Server for CI TypeScript practice
// Tools: add, greet

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

export const server = new McpServer({
  name: "ci-practice-ts-server",
  version: "0.1.0",
});

// Tool: add — sum two integers
server.tool(
  "add",
  "Add two integers and return the result",
  { a: z.number().int().describe("First integer"), b: z.number().int().describe("Second integer") },
  async ({ a, b }) => ({
    content: [{ type: "text", text: JSON.stringify({ result: a + b }) }],
  }),
);

// Tool: greet — greet a person in the specified language
const GREETINGS: Record<string, string> = {
  es: "Hola",
  en: "Hello",
  fr: "Bonjour",
  pt: "Olá",
};

server.tool(
  "greet",
  "Greet a person in the specified language",
  {
    name: z.string().min(1).describe("Person's name"),
    language: z.enum(["es", "en", "fr", "pt"]).default("es").describe("Language code"),
  },
  async ({ name, language }) => {
    const greeting = GREETINGS[language] ?? GREETINGS["es"];
    return {
      content: [{ type: "text", text: JSON.stringify({ greeting: `${greeting}, ${name}!` }) }],
    };
  },
);

// Start with stdio transport when run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}
