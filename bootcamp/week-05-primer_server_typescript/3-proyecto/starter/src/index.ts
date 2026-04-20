import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "week05-utility-server",
  version: "1.0.0",
});

// ============================================
// TOOL: calculate
// Perform basic arithmetic operations
// ============================================

server.tool(
  "calculate",
  "Perform a basic arithmetic operation on two numbers",
  {
    operation: z
      .enum(["add", "subtract", "multiply", "divide"])
      .describe("The arithmetic operation to perform"),
    a: z.number().describe("First operand"),
    b: z.number().describe("Second operand"),
  },
  async ({ operation, a, b }) => {
    // TODO: Implement the calculate logic
    // 1. Handle the "divide" operation — return isError: true if b === 0
    // 2. Compute the result based on the operation
    // 3. Return the result as a text string

    return {
      content: [{ type: "text", text: "Not implemented" }],
      isError: true,
    };
  },
);

// ============================================
// TOOL: transform_text
// Transform a text string using various operations
// ============================================

server.tool(
  "transform_text",
  "Transform a text string using the specified operation",
  {
    text: z.string().describe("The text to transform"),
    operation: z
      .enum(["upper", "lower", "reverse", "title", "word_count"])
      .describe("Transformation to apply"),
  },
  async ({ text, operation }) => {
    // TODO: Implement the transform_text logic
    // Operations:
    //   "upper"      → text.toUpperCase()
    //   "lower"      → text.toLowerCase()
    //   "reverse"    → reverse the characters
    //   "title"      → capitalize the first letter of each word
    //   "word_count" → return JSON with { words, characters, lines }

    return {
      content: [{ type: "text", text: "Not implemented" }],
      isError: true,
    };
  },
);

// ============================================
// TOOL: date_info
// Return information about a specific date
// ============================================

server.tool(
  "date_info",
  "Return detailed information about a date in YYYY-MM-DD format",
  {
    date_string: z.string().describe("Date in YYYY-MM-DD format (e.g. 2025-12-25)"),
  },
  async ({ date_string }) => {
    // TODO: Implement the date_info logic
    // 1. Parse the date_string — return isError: true if invalid
    // 2. Calculate days until the date (negative if past)
    // 3. Return JSON with: { date, weekday, is_weekend, days_until, is_past }
    // Hint: use new Date(date_string + "T00:00:00") to avoid timezone issues

    return {
      content: [{ type: "text", text: "Not implemented" }],
      isError: true,
    };
  },
);

// Start the server
const transport = new StdioServerTransport();
await server.connect(transport);
