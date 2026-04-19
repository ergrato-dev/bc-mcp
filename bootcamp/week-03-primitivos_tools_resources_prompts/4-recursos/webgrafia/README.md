# Webgrafía — Semana 03: Los Tres Primitivos

## Documentación oficial MCP

- [MCP Specification — Tools](https://spec.modelcontextprotocol.io/specification/server/tools/) — Definición formal del primitivo Tool, inputSchema y ToolAnnotations
- [MCP Specification — Resources](https://spec.modelcontextprotocol.io/specification/server/resources/) — Tipos de recursos, URIs, templates y MIME types
- [MCP Specification — Prompts](https://spec.modelcontextprotocol.io/specification/server/prompts/) — Estructura de Prompts, PromptArgument y mensajes

## JSON Schema

- [JSON Schema — Getting Started](https://json-schema.org/learn/getting-started-step-by-step) — Introducción a JSON Schema para diseñar inputSchema de tools
- [JSON Schema Specification (Draft 2020-12)](https://json-schema.org/specification) — Referencia completa de types, properties, required, additionalProperties

## URI Templates

- [RFC 6570 — URI Template](https://www.rfc-editor.org/rfc/rfc6570) — Estándar que define la sintaxis `{variable}` usada en ResourceTemplates

## MCP Python SDK

- [MCP Python SDK — Server](https://github.com/modelcontextprotocol/python-sdk/tree/main/src/mcp/server) — Código fuente del servidor, decoradores y tipos
- [MCP Python SDK — Types](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/types.py) — Referencia completa de `TextContent`, `BlobResourceContents`, `ToolAnnotations`, etc.

## MCP TypeScript SDK

- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — SDK oficial con ejemplos de servers
- [MCP TypeScript SDK — Types](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/src/types.ts) — Referencia de los schemas Zod (ListToolsRequestSchema, etc.)

## Artículos complementarios

- [MCP Docs — Building MCP Servers](https://modelcontextprotocol.io/docs/concepts/architecture) — Arquitectura general: cómo client y server se comunican
- [Anthropic Blog — Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anuncio oficial del protocolo MCP
