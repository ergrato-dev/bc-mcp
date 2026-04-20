# Webgrafía — Semana 09: MCP Client en TypeScript

## MCP TypeScript SDK

- [MCP TypeScript SDK — GitHub](https://github.com/modelcontextprotocol/typescript-sdk) — Repositorio oficial del SDK con ejemplos de client y server
- [MCP Docs — TypeScript Quickstart](https://modelcontextprotocol.io/docs/getting-started/clients) — Guía de inicio rápido para clients MCP
- [MCP Specification — Client Features](https://spec.modelcontextprotocol.io/specification/client/) — Especificación del protocolo para clients

## Node.js — Módulos y Streams

- [Node.js readline/promises API](https://nodejs.org/docs/latest-v22.x/api/readline.html#readline_promises_api) — API readline async (nativa, sin paquete extra)
- [Node.js child_process.spawn](https://nodejs.org/docs/latest-v22.x/api/child_process.html#child_processspawncommand-args-options) — Cómo StdioClientTransport lanza el proceso servidor
- [Node.js Streams](https://nodejs.org/docs/latest-v22.x/api/stream.html) — Streams Readable/Writable usados por el transport stdio

## TypeScript

- [TypeScript Handbook — Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) — Cómo usar discriminated unions y type guards (relevante para `content[0].type`)
- [TypeScript Handbook — Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) — Funciones genéricas como `callAndParse<T>()`
- [TypeScript ESM Modules](https://www.typescriptlang.org/docs/handbook/esm-node.html) — Configuración `"module": "NodeNext"` y `.js` en imports

## Artículos y Tutoriales

- [MCP SDK: Building Clients](https://modelcontextprotocol.io/docs/concepts/clients) — Conceptos de client MCP con ejemplos TypeScript
- [Anthropic Blog — MCP](https://www.anthropic.com/research/model-context-protocol) — Introducción oficial al protocolo por Anthropic
- [NDJSON Specification](https://ndjson.org/) — Formato de framing usado por stdio transport

---

[← Volver a Recursos](../README.md)
