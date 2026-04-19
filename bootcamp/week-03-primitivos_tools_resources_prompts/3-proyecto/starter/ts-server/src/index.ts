/**
 * Knowledge Base MCP Server — Semana 03 Proyecto (TypeScript)
 *
 * Implementa los tres primitivos del protocolo MCP:
 *   - Tool:     search_docs
 *   - Resource: docs://catalog, docs://files/{filename}
 *   - Prompt:   summarize_doc
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    ListToolsRequestSchema,
    CallToolRequestSchema,
    ListResourcesRequestSchema,
    ListResourceTemplatesRequestSchema,
    ReadResourceRequestSchema,
    ListPromptsRequestSchema,
    GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { readFileSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const DOCS_DIR = join(__dirname, "..", "sample-docs");

// In-memory docs database
interface Doc {
    filename: string;
    title: string;
    content: string;
}
const docsDb = new Map<string, Doc>();

function loadDocs(): void {
    const files = readdirSync(DOCS_DIR).filter((f) => f.endsWith(".md"));
    for (const filename of files) {
        const content = readFileSync(join(DOCS_DIR, filename), "utf-8");
        let title = filename.replace(".md", "");
        for (const line of content.split("\n")) {
            if (line.startsWith("# ")) {
                title = line.replace(/^# /, "").trim();
                break;
            }
        }
        docsDb.set(filename, { filename, title, content });
    }
}

const server = new Server(
    { name: "week03-knowledge-base", version: "1.0.0" },
    {
        capabilities: {
            tools: {},
            resources: {},
            prompts: {},
        },
    }
);

// ============================================================
// TOOL: search_docs
// ============================================================
server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
        {
            name: "search_docs",
            description: "Searches documentation files by keyword in title or content",
            inputSchema: {
                type: "object",
                properties: {
                    query: {
                        type: "string",
                        description: "Text to search for in documentation",
                        minLength: 1,
                    },
                },
                required: ["query"],
                additionalProperties: false,
            },
            annotations: { readOnlyHint: true, idempotentHint: true },
        },
    ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === "search_docs") {
        // TODO 1: Implementar la búsqueda
        // 1. Obtener query de (args as Record<string, string>).query
        // 2. Convertir a minúsculas
        // 3. Filtrar docsDb donde query esté en doc.title o doc.content (toLowerCase)
        // 4. Si no hay resultados → return { content: [{type:"text", text:"No docs found..."}], isError: true }
        // 5. Si hay resultados → return { content: [{type:"text", text: JSON.stringify(results, null, 2)}] }
        //    Cada resultado debe ser { filename, title }
    }

    throw new Error(`Unknown tool: ${name}`);
});

// ============================================================
// RESOURCES: docs://catalog y docs://files/{filename}
// ============================================================
server.setRequestHandler(ListResourcesRequestSchema, async () => ({
    resources: [
        // TODO 2a: Agregar el resource docs://catalog
        // { uri: "docs://catalog", name: "...", description: "...", mimeType: "application/json" }
    ],
}));

server.setRequestHandler(ListResourceTemplatesRequestSchema, async () => ({
    resourceTemplates: [
        // TODO 2b: Agregar el template docs://files/{filename}
        // { uriTemplate: "docs://files/{filename}", name: "...", description: "...", mimeType: "text/markdown" }
    ],
}));

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
    const { uri } = request.params;

    if (uri === "docs://catalog") {
        // TODO 3a: Retornar lista de docs como JSON
        // summary = Array.from(docsDb.values()).map(d => ({ filename: d.filename, title: d.title }))
        // return { contents: [{ uri, text: JSON.stringify(summary, null, 2), mimeType: "application/json" }] }
    }

    if (uri.startsWith("docs://files/")) {
        // TODO 3b: Retornar contenido del documento
        // filename = uri.replace("docs://files/", "")
        // doc = docsDb.get(filename)
        // Si no existe → throw new Error(`Document '${filename}' not found`)
        // return { contents: [{ uri, text: doc.content, mimeType: "text/markdown" }] }
    }

    throw new Error(`Resource not found: ${uri}`);
});

// ============================================================
// PROMPT: summarize_doc
// ============================================================
server.setRequestHandler(ListPromptsRequestSchema, async () => ({
    prompts: [
        // TODO 4a: Agregar el prompt summarize_doc
        // {
        //     name: "summarize_doc",
        //     description: "Summarizes a documentation file",
        //     arguments: [
        //         { name: "filename", description: "Name of the doc file (e.g. intro.md)", required: true },
        //         { name: "style", description: "Summary style: bullet_points or paragraph", required: false },
        //     ],
        // }
    ],
}));

server.setRequestHandler(GetPromptRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    const safeArgs = args ?? {};

    if (name === "summarize_doc") {
        // TODO 4b: Implementar el prompt
        // 1. filename = safeArgs.filename (required)
        // 2. style = safeArgs.style ?? "paragraph"
        // 3. doc = docsDb.get(filename)
        // 4. Si no existe → throw new Error(`Document '${filename}' not found`)
        // 5. return {
        //     description: `Summary of ${filename}`,
        //     messages: [
        //       { role: "user", content: { type: "resource", resource: { uri: `docs://files/${filename}`, text: doc.content, mimeType: "text/markdown" } } },
        //       { role: "user", content: { type: "text", text: `Summarize the documentation above as ${style}.` } },
        //     ]
        //   }
    }

    throw new Error(`Unknown prompt: ${name}`);
});


loadDocs();
const transport = new StdioServerTransport();
await server.connect(transport);
