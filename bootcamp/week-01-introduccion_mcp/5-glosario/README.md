# Glosario — Semana 01: Introducción al Protocolo MCP

Términos clave de esta semana, ordenados alfabéticamente.

---

### Host

Aplicación que gestiona múltiples MCP Clients (ej. Claude Desktop, Cursor)

### LLM

Large Language Model — modelo de lenguaje de gran escala (Claude, GPT, etc.)

### MCP

Model Context Protocol — protocolo abierto de Anthropic para conectar LLMs con herramientas y datos

### MCP Client

Componente que mantiene una conexión 1:1 con un MCP Server

### MCP Server

Proceso que expone Tools, Resources y Prompts a través del protocolo MCP

### Primitivo

Concepto fundamental del protocolo MCP: Tool, Resource o Prompt

### Prompt

Plantilla de instrucciones reutilizable expuesta por un MCP Server

### Protocol

Conjunto de reglas que define cómo se comunican los componentes de un sistema

### Resource

Dato o fuente de información expuesta por un MCP Server con URI único

### Tool

Función ejecutable expuesta por un MCP Server que un LLM puede invocar

### Transport

Mecanismo de comunicación entre Client y Server (stdio, HTTP/SSE)

---

[← Volver al README de la semana](../README.md)
