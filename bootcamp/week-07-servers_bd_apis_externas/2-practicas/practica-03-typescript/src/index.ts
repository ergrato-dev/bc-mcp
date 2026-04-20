/**
 * MCP Server — Books SQLite + Weather API en TypeScript
 * Semana 07 — Practica 03
 *
 * Equivalent to practicas 01 and 02, but in TypeScript.
 * Uses better-sqlite3 (sync) and native fetch (Node.js 22).
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import Database from "better-sqlite3";
import { z } from "zod";
import * as fs from "fs";
import * as path from "path";

// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------

const DB_PATH = process.env.DB_PATH ?? "./data/books.db";
const GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search";
const FORECAST_URL = "https://api.open-meteo.com/v1/forecast";

// ---------------------------------------------------------------------------
// Database setup — better-sqlite3 is synchronous (no async/await needed)
// ---------------------------------------------------------------------------

fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });

const db = new Database(DB_PATH);

// Initialize schema
db.exec(`
  CREATE TABLE IF NOT EXISTS books (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT    NOT NULL,
    author TEXT    NOT NULL,
    year   INTEGER,
    genre  TEXT
  );
  CREATE INDEX IF NOT EXISTS idx_books_title  ON books(title);
  CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
`);

// Insert sample data if empty
const count = (db.prepare("SELECT COUNT(*) as n FROM books").get() as { n: number }).n;
if (count === 0) {
  const insert = db.prepare(
    "INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)"
  );
  [
    ["The Pragmatic Programmer", "David Thomas", 1999, "Programming"],
    ["Clean Code", "Robert C. Martin", 2008, "Programming"],
    ["Python Crash Course", "Eric Matthes", 2019, "Programming"],
    ["The Hitchhiker Guide to the Galaxy", "Douglas Adams", 1979, "Fiction"],
    ["Fluent Python", "Luciano Ramalho", 2022, "Programming"],
  ].forEach((row) => insert.run(...row));
}

// ---------------------------------------------------------------------------
// Helper types
// ---------------------------------------------------------------------------

interface GeocodingResult {
  latitude: number;
  longitude: number;
  name: string;
  country?: string;
}

// ---------------------------------------------------------------------------
// Server setup
// ---------------------------------------------------------------------------

const server = new Server(
  { name: "books-weather-ts", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// ---------------------------------------------------------------------------
// Tool definitions
// ---------------------------------------------------------------------------

// Base tool — already working
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "list_books",
      description: "List all books in the library",
      inputSchema: { type: "object", properties: {}, required: [] },
    },
    // PASO 2: uncomment when activating CRUD tools
    // { name: "search_books", description: "Search by title/author", inputSchema: {...} },
    // { name: "get_book",     description: "Get book by ID",         inputSchema: {...} },
    // { name: "add_book",     description: "Add a new book",         inputSchema: {...} },
    // { name: "delete_book",  description: "Delete book by ID",      inputSchema: {...} },
    // PASO 3: uncomment when activating weather tools
    // { name: "get_current_weather", description: "Current weather", inputSchema: {...} },
    // PASO 4: uncomment when activating forecast
    // { name: "get_forecast", description: "N-day forecast",         inputSchema: {...} },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  // ==========================================
  // BASE TOOL: list_books (already working)
  // ==========================================
  if (name === "list_books") {
    const rows = db
      .prepare("SELECT id, title, author, year, genre FROM books ORDER BY title")
      .all();
    return {
      content: [{ type: "text", text: JSON.stringify(rows, null, 2) }],
    };
  }

  // ============================================
  // PASO 2: CRUD tools
  // Descomenta el bloque completo siguiente:
  // ============================================
  console.log("--- Paso 2: CRUD tools ---");

  // if (name === "search_books") {
  //   const schema = z.object({ query: z.string() });
  //   const { query } = schema.parse(args);
  //
  //   // Note: better-sqlite3 uses ? placeholders like Python aiosqlite
  //   const rows = db
  //     .prepare(
  //       "SELECT id, title, author, year, genre FROM books " +
  //       "WHERE title LIKE ? OR author LIKE ? ORDER BY title LIMIT 20"
  //     )
  //     .all(`%${query}%`, `%${query}%`);
  //
  //   if (rows.length === 0) {
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({ message: `No books found for: ${query}` }) }],
  //     };
  //   }
  //   return { content: [{ type: "text", text: JSON.stringify(rows, null, 2) }] };
  // }
  //
  // if (name === "get_book") {
  //   const schema = z.object({ id: z.number().int().positive() });
  //   const { id } = schema.parse(args);
  //
  //   // .get() returns one row or undefined (vs Python's fetchone() which returns None)
  //   const row = db.prepare("SELECT * FROM books WHERE id = ?").get(id);
  //
  //   if (!row) {
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({ error: "not_found", id }) }],
  //       isError: true,
  //     };
  //   }
  //   return { content: [{ type: "text", text: JSON.stringify(row, null, 2) }] };
  // }
  //
  // if (name === "add_book") {
  //   const schema = z.object({
  //     title:  z.string().min(1),
  //     author: z.string().min(1),
  //     year:   z.number().int().min(1000).max(2100),
  //     genre:  z.string().default("Unknown"),
  //   });
  //   const { title, author, year, genre } = schema.parse(args);
  //
  //   try {
  //     // .run() executes INSERT/UPDATE/DELETE, returns { lastInsertRowid, changes }
  //     const result = db
  //       .prepare("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)")
  //       .run(title, author, year, genre);
  //
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({
  //         success: true,
  //         id: result.lastInsertRowid,
  //         message: `Book '${title}' added`,
  //       }) }],
  //     };
  //   } catch (err) {
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({ error: "db_error", message: String(err) }) }],
  //       isError: true,
  //     };
  //   }
  // }
  //
  // if (name === "delete_book") {
  //   const schema = z.object({ id: z.number().int().positive() });
  //   const { id } = schema.parse(args);
  //
  //   const result = db.prepare("DELETE FROM books WHERE id = ?").run(id);
  //
  //   if (result.changes === 0) {
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({ error: "not_found", id }) }],
  //       isError: true,
  //     };
  //   }
  //   return {
  //     content: [{ type: "text", text: JSON.stringify({ success: true, deleted_id: id }) }],
  //   };
  // }

  // ============================================
  // PASO 3: get_current_weather
  // Descomenta el bloque siguiente:
  // ============================================
  console.log("--- Paso 3: get_current_weather ---");

  // if (name === "get_current_weather") {
  //   const schema = z.object({ city: z.string().min(1) });
  //   const { city } = schema.parse(args);
  //
  //   try {
  //     // Step 1: geocoding — convert city name to lat/lon
  //     const geoUrl = new URL(GEOCODING_URL);
  //     geoUrl.searchParams.set("name", city);
  //     geoUrl.searchParams.set("count", "1");
  //
  //     const geoResp = await fetch(geoUrl, { signal: AbortSignal.timeout(10_000) });
  //     if (!geoResp.ok) {
  //       return { content: [{ type: "text", text: `Geocoding error: HTTP ${geoResp.status}` }], isError: true };
  //     }
  //
  //     const geoData = await geoResp.json() as { results?: GeocodingResult[] };
  //     if (!geoData.results?.length) {
  //       return { content: [{ type: "text", text: `City not found: ${city}` }], isError: true };
  //     }
  //
  //     const loc = geoData.results[0];
  //
  //     // Step 2: forecast — get current weather using lat/lon
  //     const weatherUrl = new URL(FORECAST_URL);
  //     weatherUrl.searchParams.set("latitude",        loc.latitude.toString());
  //     weatherUrl.searchParams.set("longitude",       loc.longitude.toString());
  //     weatherUrl.searchParams.set("current_weather", "true");
  //     weatherUrl.searchParams.set("timezone",        "auto");
  //
  //     const weatherResp = await fetch(weatherUrl, { signal: AbortSignal.timeout(10_000) });
  //     if (!weatherResp.ok) {
  //       return { content: [{ type: "text", text: `Weather error: HTTP ${weatherResp.status}` }], isError: true };
  //     }
  //
  //     const weatherData = await weatherResp.json() as { current_weather: object };
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({
  //         city: loc.name,
  //         country: loc.country ?? "",
  //         ...weatherData.current_weather,
  //       }) }],
  //     };
  //   } catch (err) {
  //     const msg = err instanceof Error ? err.message : String(err);
  //     return { content: [{ type: "text", text: `Error: ${msg}` }], isError: true };
  //   }
  // }

  // ============================================
  // PASO 4: get_forecast
  // Descomenta el bloque siguiente:
  // ============================================
  console.log("--- Paso 4: get_forecast ---");

  // if (name === "get_forecast") {
  //   const schema = z.object({
  //     city: z.string().min(1),
  //     days: z.number().int().min(1).max(7).default(3),
  //   });
  //   const { city, days } = schema.parse(args);
  //
  //   try {
  //     const geoUrl = new URL(GEOCODING_URL);
  //     geoUrl.searchParams.set("name", city);
  //     geoUrl.searchParams.set("count", "1");
  //
  //     const geoResp = await fetch(geoUrl, { signal: AbortSignal.timeout(10_000) });
  //     if (!geoResp.ok) {
  //       return { content: [{ type: "text", text: `Geocoding error: HTTP ${geoResp.status}` }], isError: true };
  //     }
  //
  //     const geoData = await geoResp.json() as { results?: GeocodingResult[] };
  //     if (!geoData.results?.length) {
  //       return { content: [{ type: "text", text: `City not found: ${city}` }], isError: true };
  //     }
  //
  //     const loc = geoData.results[0];
  //
  //     const forecastUrl = new URL(FORECAST_URL);
  //     forecastUrl.searchParams.set("latitude",      loc.latitude.toString());
  //     forecastUrl.searchParams.set("longitude",     loc.longitude.toString());
  //     forecastUrl.searchParams.set("daily",         "temperature_2m_max,temperature_2m_min,precipitation_sum");
  //     forecastUrl.searchParams.set("timezone",      "auto");
  //     forecastUrl.searchParams.set("forecast_days", days.toString());
  //
  //     const forecastResp = await fetch(forecastUrl, { signal: AbortSignal.timeout(10_000) });
  //     if (!forecastResp.ok) {
  //       return { content: [{ type: "text", text: `Forecast error: HTTP ${forecastResp.status}` }], isError: true };
  //     }
  //
  //     const forecastData = await forecastResp.json() as { daily: object };
  //     return {
  //       content: [{ type: "text", text: JSON.stringify({
  //         city: loc.name,
  //         forecast_days: days,
  //         daily: forecastData.daily,
  //       }) }],
  //     };
  //   } catch (err) {
  //     const msg = err instanceof Error ? err.message : String(err);
  //     return { content: [{ type: "text", text: `Error: ${msg}` }], isError: true };
  //   }
  // }

  // Unknown tool
  return {
    content: [{ type: "text", text: `Unknown tool: ${name}` }],
    isError: true,
  };
});

// ---------------------------------------------------------------------------
// Entry point
// ---------------------------------------------------------------------------

const transport = new StdioServerTransport();
await server.connect(transport);
