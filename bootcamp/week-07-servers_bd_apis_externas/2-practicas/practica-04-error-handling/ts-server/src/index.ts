/**
 * MCP Server — Error Handling Patterns (TypeScript)
 * Semana 07 — Practica 04 (TypeScript)
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import Database from "better-sqlite3";
import { z } from "zod";
import * as fs from "fs";
import * as path from "path";

const DB_PATH = "./data/errors_demo_ts.db";
fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });

const db = new Database(DB_PATH);
db.exec(`
  CREATE TABLE IF NOT EXISTS books (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT UNIQUE NOT NULL,
    author TEXT NOT NULL
  );
  INSERT OR IGNORE INTO books (title, author) VALUES ('Clean Code', 'Robert C. Martin');
`);

const server = new Server(
  { name: "error-demo-ts", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "divide",
      description: "Divide a by b — shows domain error for division by zero",
      inputSchema: {
        type: "object",
        properties: {
          a: { type: "number" },
          b: { type: "number" },
        },
        required: ["a", "b"],
      },
    },
    // PASO 1: uncomment after activating get_book_typed
    // { name: "get_book_typed", description: "Get book with typed error handling", ... },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  // ---------------------------------------------------------------------------
  // Base tool — already working
  // ---------------------------------------------------------------------------
  if (name === "divide") {
    const schema = z.object({ a: z.number(), b: z.number() });
    const { a, b } = schema.parse(args);

    if (b === 0) {
      // Domain error — use isError: true so the LLM knows the tool failed
      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({
              error: "division_by_zero",
              message: "Cannot divide by zero. Provide a non-zero divisor.",
              numerator: a,
            }),
          },
        ],
        isError: true,
      };
    }

    return {
      content: [{ type: "text", text: JSON.stringify({ result: a / b }) }],
    };
  }

  // ============================================
  // PASO 1: get_book_typed
  // Errores de BD con isError: true
  // ============================================
  console.log("--- Paso 1: get_book_typed ---");

  // Descomenta el bloque siguiente:

  // if (name === "get_book_typed") {
  //   const schema = z.object({ id: z.number().int().positive() });
  //   const { id } = schema.parse(args);
  //
  //   try {
  //     const row = db.prepare("SELECT * FROM books WHERE id = ?").get(id);
  //
  //     if (!row) {
  //       return {
  //         content: [{ type: "text", text: JSON.stringify({
  //           error: "not_found",
  //           message: `Book id=${id} does not exist.`,
  //           suggestion: "Check available books with list_books tool.",
  //         }) }],
  //         isError: true,
  //       };
  //     }
  //
  //     return { content: [{ type: "text", text: JSON.stringify(row) }] };
  //
  //   } catch (err) {
  //     // TypeScript: use instanceof for typed error handling
  //     if (err instanceof Error) {
  //       return {
  //         content: [{ type: "text", text: JSON.stringify({
  //           error: "database_error",
  //           message: err.message,
  //         }) }],
  //         isError: true,
  //       };
  //     }
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({ error: "unknown_error" }) }],
  //       isError: true,
  //     };
  //   }
  // }

  // ============================================
  // PASO 2: fetch_weather_with_retry
  // Retry con backoff exponencial en TypeScript
  // ============================================
  console.log("--- Paso 2: fetch_weather_with_retry ---");

  // Descomenta el bloque siguiente:

  // if (name === "get_weather_retry") {
  //   const schema = z.object({ city: z.string().min(1) });
  //   const { city } = schema.parse(args);
  //
  //   async function fetchWithRetry(
  //     url: URL,
  //     maxRetries = 3
  //   ): Promise<unknown> {
  //     let lastError: Error | null = null;
  //
  //     for (let attempt = 0; attempt < maxRetries; attempt++) {
  //       try {
  //         const resp = await fetch(url, { signal: AbortSignal.timeout(10_000) });
  //
  //         // 4xx = client error, do NOT retry
  //         if (resp.status >= 400 && resp.status < 500) {
  //           throw new Error(`Client error: HTTP ${resp.status}`);
  //         }
  //
  //         if (!resp.ok) {
  //           // 5xx = server error, retry
  //           throw new Error(`Server error: HTTP ${resp.status}`);
  //         }
  //
  //         return await resp.json();
  //       } catch (err) {
  //         lastError = err instanceof Error ? err : new Error(String(err));
  //
  //         // No retry on 4xx
  //         if (lastError.message.startsWith("Client error")) throw lastError;
  //
  //         if (attempt < maxRetries - 1) {
  //           // Wait 0.5s, 1s, 2s...
  //           await new Promise((r) => setTimeout(r, 500 * Math.pow(2, attempt)));
  //         }
  //       }
  //     }
  //     throw new Error(`All ${maxRetries} attempts failed: ${lastError?.message}`);
  //   }
  //
  //   try {
  //     const geoUrl = new URL("https://geocoding-api.open-meteo.com/v1/search");
  //     geoUrl.searchParams.set("name", city);
  //     geoUrl.searchParams.set("count", "1");
  //
  //     const geoData = await fetchWithRetry(geoUrl) as { results?: Array<{
  //       latitude: number; longitude: number; name: string;
  //     }> };
  //
  //     if (!geoData.results?.length) {
  //       return { content: [{ type: "text", text: `City not found: ${city}` }], isError: true };
  //     }
  //
  //     const loc = geoData.results[0];
  //     const weatherUrl = new URL("https://api.open-meteo.com/v1/forecast");
  //     weatherUrl.searchParams.set("latitude",        loc.latitude.toString());
  //     weatherUrl.searchParams.set("longitude",       loc.longitude.toString());
  //     weatherUrl.searchParams.set("current_weather", "true");
  //
  //     const weatherData = await fetchWithRetry(weatherUrl) as {
  //       current_weather: object;
  //     };
  //
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({
  //         city: loc.name,
  //         ...weatherData.current_weather,
  //       }) }],
  //     };
  //   } catch (err) {
  //     const msg = err instanceof Error ? err.message : String(err);
  //     return { content: [{ type: "text", text: `Error: ${msg}` }], isError: true };
  //   }
  // }

  return {
    content: [{ type: "text", text: `Unknown tool: ${name}` }],
    isError: true,
  };
});

const transport = new StdioServerTransport();
await server.connect(transport);
