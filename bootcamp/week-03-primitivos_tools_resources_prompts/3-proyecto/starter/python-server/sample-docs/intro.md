# Introduction to MCP

## What is MCP?

The **Model Context Protocol (MCP)** is an open standard that enables AI models to
connect with external tools, data sources, and services in a structured, secure way.

MCP defines three primitives that a server can expose:

- **Tools**: executable functions with side effects (e.g., create a file, call an API)
- **Resources**: read-only data sources accessible via URI (e.g., database records, files)
- **Prompts**: reusable message templates with typed arguments

## Why MCP?

Before MCP, each AI integration required custom code. MCP provides a common protocol
that any LLM client can speak, making integrations portable and composable.

## Key concepts

- **Client**: the application that connects to MCP servers (e.g., Claude Desktop)
- **Server**: the process that exposes tools, resources and prompts
- **Transport**: the communication channel (stdio, HTTP/SSE)
