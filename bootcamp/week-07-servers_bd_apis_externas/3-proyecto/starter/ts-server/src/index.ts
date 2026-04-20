/**
 * Library Manager — MCP Server (TypeScript)
 * Semana 07 — Proyecto Integrador
 *
 * Tools a implementar:
 *   SQLite CRUD: search_books, get_book, add_book, update_book, delete_book
 *   External API: search_openlibrary, enrich_book
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import Database from "better-sqlite3";
import { z } from "zod";
import * as dotenv from "dotenv";
import * as fs from "fs";
import * as path from "path";

dotenv.config();

// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------

const DB_PATH = process.env.DB_PATH ?? "./data/library.db";
const OPENLIBRARY_URL =
  process.env.OPENLIBRARY_URL ?? "https://openlibrary.org/search.json";
const MAX_SEARCH_RESULTS = parseInt(process.env.MAX_SEARCH_RESULTS ?? "10", 10);

// ---------------------------------------------------------------------------
// Database setup
// ---------------------------------------------------------------------------

fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });

const db = new Database(DB_PATH);

db.exec(`
  CREATE TABLE IF NOT EXISTS books (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    author     TEXT    NOT NULL,
    year       INTEGER,
    isbn       TEXT,
    notes      TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );
  CREATE INDEX IF NOT EXISTS idx_books_title  ON books(title);
  CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
`);

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface BookRow {
  id: number;
  title: string;
  author: string;
  year: number | null;
  isbn: string | null;
  notes: string | null;
  created_at: string;
}

interface OpenLibraryDoc {
  title?: string;
  author_name?: string[];
  first_publish_year?: number;
  subject?: string[];
  isbn?: string[];
}

// ---------------------------------------------------------------------------
// Server setup
// ---------------------------------------------------------------------------

const server = new Server(
  { name: "library-manager-ts", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// ---------------------------------------------------------------------------
// Tool registry
// ---------------------------------------------------------------------------

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "search_books",
      description: "Search local library by title or author",
      inputSchema: {
        type: "object",
        properties: { query: { type: "string", description: "Search text" } },
        required: ["query"],
      },
    },
    {
      name: "get_book",
      description: "Get a single book by ID",
      inputSchema: {
        type: "object",
        properties: { id: { type: "number", description: "Book ID" } },
        required: ["id"],
      },
    },
    {
      name: "add_book",
      description: "Add a new book to the library",
      inputSchema: {
        type: "object",
        properties: {
          title:  { type: "string" },
          author: { type: "string" },
          year:   { type: "number" },
          isbn:   { type: "string" },
          notes:  { type: "string" },
        },
        required: ["title", "author", "year"],
      },
    },
    {
      name: "update_book",
      description: "Update fields of an existing book",
      inputSchema: {
        type: "object",
        properties: {
          id:     { type: "number" },
          title:  { type: "string" },
          author: { type: "string" },
          year:   { type: "number" },
          notes:  { type: "string" },
        },
        required: ["id"],
      },
    },
    {
      name: "delete_book",
      description: "Delete a book by ID",
      inputSchema: {
        type: "object",
        properties: { id: { type: "number" } },
        required: ["id"],
      },
    },
    {
      name: "search_openlibrary",
      description: "Search Open Library public API by title",
      inputSchema: {
        type: "object",
        properties: { title: { type: "string" } },
        required: ["title"],
      },
    },
    {
      name: "enrich_book",
      description: "Enrich a local book with Open Library metadata",
      inputSchema: {
        type: "object",
        properties: { id: { type: "number" } },
        required: ["id"],
      },
    },
  ],
}));

// ---------------------------------------------------------------------------
// Tool handlers
// ---------------------------------------------------------------------------

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  // ============================================
  // TOOL: search_books
  // ============================================
  if (name === "search_books") {
    const { query } = z.object({ query: z.string().min(1) }).parse(args);

    // TODO: Implementar busqueda
    // 1. db.prepare("SELECT ... FROM books WHERE title LIKE ? OR author LIKE ?")
    //    .all(`%${query}%`, `%${query}%`) — nota: better-sqlite3 usa .all() para SELECT
    // 2. Retornar JSON array
    // 3. Si rows.length === 0: retornar mensaje de "no results"
    throw new Error("TODO: implement search_books");
  }

  // ============================================
  // TOOL: get_book
  // ============================================
  if (name === "get_book") {
    const { id } = z.object({ id: z.number().int().positive() }).parse(args);

    // TODO: Implementar get por ID
    // 1. db.prepare("SELECT * FROM books WHERE id = ?").get(id) as BookRow | undefined
    // 2. Si undefined: retornar isError: true con error "not_found"
    // 3. Si existe: retornar JSON con el libro
    throw new Error("TODO: implement get_book");
  }

  // ============================================
  // TOOL: add_book
  // ============================================
  if (name === "add_book") {
    const schema = z.object({
      title:  z.string().min(1),
      author: z.string().min(1),
      year:   z.number().int().min(1000).max(2100),
      isbn:   z.string().optional().default(""),
      notes:  z.string().optional().default(""),
    });
    const { title, author, year, isbn, notes } = schema.parse(args);

    // TODO: Implementar INSERT
    // 1. db.prepare("INSERT INTO books (...) VALUES (?, ?, ?, ?, ?)").run(...)
    //    resultado: RunResult { lastInsertRowid, changes }
    // 2. Retornar JSON {"success": true, "id": result.lastInsertRowid}
    // 3. Capturar errores de DB (ej: titulo duplicado si hay UNIQUE constraint)
    throw new Error("TODO: implement add_book");
  }

  // ============================================
  // TOOL: update_book
  // ============================================
  if (name === "update_book") {
    const schema = z.object({
      id:     z.number().int().positive(),
      title:  z.string().optional(),
      author: z.string().optional(),
      year:   z.number().int().optional(),
      notes:  z.string().optional(),
    });
    const { id, ...fields } = schema.parse(args);

    // TODO: Implementar UPDATE dinamico
    // 1. Filtrar campos no undefined de 'fields'
    // 2. Construir: "UPDATE books SET campo1=?, campo2=? WHERE id=?"
    // 3. Si result.changes === 0: retornar isError con "not_found"
    // 4. Retornar el libro actualizado
    throw new Error("TODO: implement update_book");
  }

  // ============================================
  // TOOL: delete_book
  // ============================================
  if (name === "delete_book") {
    const { id } = z.object({ id: z.number().int().positive() }).parse(args);

    // TODO: Implementar DELETE
    // 1. db.prepare("DELETE FROM books WHERE id = ?").run(id)
    // 2. Si result.changes === 0: retornar isError con "not_found"
    // 3. Retornar {"success": true, "deleted_id": id}
    throw new Error("TODO: implement delete_book");
  }

  // ============================================
  // TOOL: search_openlibrary
  // ============================================
  if (name === "search_openlibrary") {
    const { title } = z.object({ title: z.string().min(1) }).parse(args);

    // TODO: Implementar busqueda en Open Library
    // 1. const url = new URL(OPENLIBRARY_URL)
    //    url.searchParams.set("title", title)
    //    url.searchParams.set("limit", MAX_SEARCH_RESULTS.toString())
    //    url.searchParams.set("fields", "title,author_name,first_publish_year,subject,isbn")
    // 2. const resp = await fetch(url, { signal: AbortSignal.timeout(15_000) })
    // 3. if (!resp.ok) throw error con status
    // 4. const data = await resp.json() as { docs: OpenLibraryDoc[] }
    // 5. Mapear data.docs a array de objetos limpios
    // 6. Capturar errores de red y timeout
    throw new Error("TODO: implement search_openlibrary");
  }

  // ============================================
  // TOOL: enrich_book
  // ============================================
  if (name === "enrich_book") {
    const { id } = z.object({ id: z.number().int().positive() }).parse(args);

    // TODO: Implementar enrichment
    // 1. Obtener libro local con db.prepare("SELECT...").get(id)
    // 2. Si no existe: retornar isError con "not_found"
    // 3. Buscar en Open Library por el titulo del libro
    // 4. Retornar JSON combinado:
    //    { local: bookRow, openlibrary: firstApiResult || null }
    throw new Error("TODO: implement enrich_book");
  }

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
