# Plan de Trabajo — Bootcamp MCP Zero to Hero

> Seguimiento del desarrollo completo del bootcamp.
> Actualizar este archivo al completar cada semana → commit + push.

---

## Estado General

| Etapa | Semanas | Horas | Estado |
|-------|---------|-------|--------|
| Fundamentos | 1–3 | 24h | 🔲 En progreso |
| MCP Servers | 4–7 | 32h | ⬜ Pendiente |
| MCP Clients + LLMs | 8–10 | 24h | ⬜ Pendiente |
| Producción | 11–12 | 16h | ⬜ Pendiente |

---

## Infraestructura y Documentación Base

- [x] `.gitignore` completo (Python, Node, Docker, `**/solution/`)
- [x] `README.md` (español) con estructura del bootcamp
- [x] `README_EN.md` (inglés)
- [x] `assets/bootcamp-header.svg` (banner dark, sin degradés)
- [x] `docs/setup/README.md` — índice de métodos de setup
- [x] `docs/setup/docker.md` — guía oficial con Docker
- [x] `docs/setup/local.md` — setup local sin Docker + modo híbrido
- [x] `.github/copilot-instructions.md` — instrucciones para Copilot
- [x] `.github/instructions/bootcamp-markdown.instructions.md`
- [x] `.github/instructions/python-mcp.instructions.md`
- [x] `.github/instructions/typescript-mcp.instructions.md`
- [x] `.github/instructions/docker-mcp.instructions.md`
- [x] `.github/prompts/` — prompts reutilizables (create-week, create-theory, etc.)
- [x] Scaffolding de 12 semanas (`bootcamp/week-01` → `week-12`)
- [x] `scripts/scaffold_bootcamp.py`

---

## Semana 01 — Introducción al Protocolo MCP

> Etapa: Fundamentos · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-01-introduccion_mcp/README.md`
- [x] `bootcamp/week-01-introduccion_mcp/rubrica-evaluacion.md`
- [x] Carpetas: `0-assets/`, `1-teoria/`, `2-practicas/`, `3-proyecto/`, `4-recursos/`, `5-glosario/`

### Assets Visuales (`0-assets/`)
- [x] `01-mcp-architecture.svg` — Host / Client / Server / Primitivos + JSON-RPC
- [x] `02-primitivos-overview.svg` — Tool · Resource · Prompt comparados
- [x] `03-mcp-vs-alternativas.svg` — Tabla MCP vs Function Calling vs REST vs Plugins

### Teoría (`1-teoria/`) — mín. 150 líneas por archivo
- [x] `01-que-es-mcp.md` — origen, motivación, casos de uso reales
- [x] `02-arquitectura.md` — Host, Client, Server; JSON-RPC 2.0; ciclo completo
- [x] `03-primitivos.md` — Tools, Resources y Prompts: estructura y guía de decisión
- [x] `04-transports.md` — stdio, HTTP/SSE y WebSocket: cuándo usar cada uno
- [x] `05-mcp-vs-alternativas.md` — MCP vs Function Calling, REST y Plugins

### Prácticas (`2-practicas/`) — formato descomentar
- [x] `practica-01/` — Configurar entorno Docker + MCP Inspector
- [x] `practica-02/` — Explorar server demo con MCP Inspector
- [x] `practica-03/` — Leer e interpretar mensajes JSON-RPC
- [x] `practica-04/` — Clasificar primitivos en servers reales + diseño propio

### Proyecto (`3-proyecto/`) — formato TODOs
- [x] `README.md` — instrucciones del proyecto
- [x] `starter/README.md` — guía de setup
- [x] `starter/docker-compose.yml` — TODO: descomentar mcp-inspector
- [x] `starter/architecture-diagram.svg` — TODO: crear diagrama propio
- [x] `starter/architecture-analysis.md` — TODO: análisis del diagrama
- [x] `starter/use-cases.md` — TODO: 3 casos de uso reales

### Recursos (`4-recursos/`)
- [x] `ebooks-free/README.md` — libros gratuitos: Python asyncio, TS Handbook, Docker Docs, Prompt Engineering Guide
- [x] `videografia/README.md` — videos MCP: demos Anthropic, tutoriales Python, canales recomendados
- [x] `webgrafia/README.md` — docs oficiales MCP, JSON-RPC spec, MCP Inspector, Awesome MCP Servers

### Glosario (`5-glosario/`)
- [x] `README.md` — 13 términos clave (Function Calling, Host, JSON-RPC, LLM, MCP, MCP Client, MCP Server, Primitivo, Prompt, Resource, stdio, Tool, Transport)

---

## Semana 02 — JSON-RPC 2.0 y Transports

> Etapa: Fundamentos · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-02-json_rpc_y_transports/README.md`
- [x] `bootcamp/week-02-json_rpc_y_transports/rubrica-evaluacion.md`
- [x] Carpetas: `0-assets/`, `1-teoria/`, `2-practicas/`, `3-proyecto/`, `4-recursos/`, `5-glosario/`

### Assets Visuales (`0-assets/`)
- [ ] `jsonrpc-request-response.svg` — ciclo request/response JSON-RPC
- [ ] `stdio-transport.svg` — flujo stdin/stdout
- [ ] `http-sse-transport.svg` — flujo HTTP + SSE
- [ ] `week-02-header.svg`

### Teoría (`1-teoria/`) — mín. 150 líneas por archivo
- [ ] `01-json-rpc-2.md` — especificación JSON-RPC 2.0
- [ ] `02-stdio-transport.md` — stdio: cómo funciona, cuándo usarlo
- [ ] `03-http-sse-transport.md` — HTTP/SSE: setup, diferencias con stdio
- [ ] `04-websocket-transport.md` — WebSocket: casos de uso avanzados
- [ ] `05-mensajes-mcp.md` — tipos de mensajes: initialize, request, notification

### Prácticas (`2-practicas/`)
- [ ] `01-jsonrpc-manual/` — construir mensajes JSON-RPC a mano
- [ ] `02-stdio-server/` — server con stdio transport
- [ ] `03-sse-server/` — server con HTTP/SSE transport

### Proyecto (`3-proyecto/`)
- [ ] `README.md`, `starter/`, `solution/`

### Recursos + Glosario
- [ ] `4-recursos/` — links relevantes
- [ ] `5-glosario/README.md` — términos JSON-RPC y transports

---

## Semana 03 — Primitivos: Tools, Resources y Prompts

> Etapa: Fundamentos · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-03-primitivos_tools_resources_prompts/README.md`
- [x] `bootcamp/week-03-primitivos_tools_resources_prompts/rubrica-evaluacion.md`
- [x] Carpetas base

### Assets Visuales (`0-assets/`)
- [ ] `tool-execution-flow.svg` — flujo completo de ejecución de un tool
- [ ] `resource-fetch-flow.svg` — flujo de lectura de un resource
- [ ] `prompt-flow.svg` — flujo de un prompt
- [ ] `primitivos-comparativa.svg` — tabla comparativa de los 3 primitivos

### Teoría (`1-teoria/`)
- [ ] `01-tools.md` — definición, schema, input/output, casos de uso
- [ ] `02-resources.md` — URI scheme, tipos, cuándo usar resources
- [ ] `03-prompts.md` — arguments, templates, integración con LLM
- [ ] `04-cuando-usar-cada-primitivo.md` — guía de decisión

### Prácticas (`2-practicas/`)
- [ ] `01-primer-tool/` — Python + TypeScript
- [ ] `02-primer-resource/` — Python + TypeScript
- [ ] `03-primer-prompt/` — Python + TypeScript
- [ ] `04-combinando-primitivos/` — server con los 3

### Proyecto (`3-proyecto/`)
- [ ] `README.md`, `starter/`, `solution/`

### Recursos + Glosario
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 04 — Primer MCP Server en Python

> Etapa: MCP Servers · Horas: 8h · Lenguaje: Python

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-04-primer_server_python/README.md`
- [x] `bootcamp/week-04-primer_server_python/rubrica-evaluacion.md`
- [x] Carpetas base

### Assets Visuales (`0-assets/`)
- [ ] `python-server-anatomy.svg` — anatomía de un MCP server en Python
- [ ] `fastmcp-decorator-flow.svg` — decoradores de FastMCP
- [ ] `week-04-header.svg`

### Teoría (`1-teoria/`)
- [ ] `01-mcp-python-sdk.md` — FastMCP, instalación, estructura
- [ ] `02-definir-tools-python.md` — decoradores, type hints, Pydantic
- [ ] `03-stdio-en-python.md` — transport stdio con Python SDK
- [ ] `04-testing-basico.md` — pytest + create_connected_server_and_client_session

### Prácticas (`2-practicas/`)
- [ ] `01-setup-entorno-python/` — pyproject.toml, uv, Docker
- [ ] `02-tool-calculadora/` — tool con operaciones básicas
- [ ] `03-tool-filesystem/` — tool para leer archivos
- [ ] `04-multiple-tools/` — server con 3+ tools

### Proyecto (`3-proyecto/`)
- [ ] `README.md`, `starter/`, `solution/`

### Recursos + Glosario
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 05 — Primer MCP Server en TypeScript

> Etapa: MCP Servers · Horas: 8h · Lenguaje: TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-05-primer_server_typescript/README.md`
- [x] `bootcamp/week-05-primer_server_typescript/rubrica-evaluacion.md`
- [x] Carpetas base

### Assets Visuales (`0-assets/`)
- [ ] `typescript-server-anatomy.svg` — anatomía de un MCP server en TypeScript
- [ ] `zod-validation-flow.svg` — validación de inputs con Zod
- [ ] `week-05-header.svg`

### Teoría (`1-teoria/`)
- [ ] `01-mcp-typescript-sdk.md` — @modelcontextprotocol/sdk, pnpm, estructura
- [ ] `02-definir-tools-typescript.md` — Zod, tipos estrictos, CallToolResult
- [ ] `03-stdio-en-typescript.md` — StdioServerTransport
- [ ] `04-testing-basico.md` — vitest + InMemoryTransport

### Prácticas (`2-practicas/`)
- [ ] `01-setup-entorno-typescript/` — package.json, pnpm, tsconfig, Docker
- [ ] `02-tool-calculadora/` — equivalente TypeScript de semana 04
- [ ] `03-tool-filesystem/` — tool para leer archivos en TypeScript
- [ ] `04-multiple-tools/` — server con 3+ tools

### Proyecto (`3-proyecto/`)
- [ ] `README.md`, `starter/`, `solution/`

### Recursos + Glosario
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 06 — Servers Avanzados: Los 3 Primitivos

> Etapa: MCP Servers · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-06-servers_avanzados_primitivos/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — SVGs de los 3 primitivos integrados
- [ ] `1-teoria/` — tools complejos, resources con DB, prompts dinámicos
- [ ] `2-practicas/` — server completo con Tools + Resources + Prompts
- [ ] `3-proyecto/` — server de documentación con los 3 primitivos
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 07 — Servers con BD y APIs Externas

> Etapa: MCP Servers · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-07-servers_bd_apis_externas/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — diagramas de integración DB y APIs
- [ ] `1-teoria/` — SQLite/PostgreSQL con MCP, httpx, rate limiting
- [ ] `2-practicas/` — server con BD SQLite, server con API externa
- [ ] `3-proyecto/` — MCP server de e-commerce (BD + API de pagos)
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 08 — MCP Client en Python

> Etapa: MCP Clients + LLMs · Horas: 8h · Lenguaje: Python

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-08-mcp_client_python/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — diagrama client-server communication
- [ ] `1-teoria/` — MCP Client Python SDK, llamadas a tools, listing
- [ ] `2-practicas/` — client que conecta a server de semana 04
- [ ] `3-proyecto/` — CLI client con múltiples servers
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 09 — MCP Client en TypeScript

> Etapa: MCP Clients + LLMs · Horas: 8h · Lenguaje: TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-09-mcp_client_typescript/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — diagramas client TypeScript
- [ ] `1-teoria/` — MCP Client TypeScript SDK, tipos, manejo de errores
- [ ] `2-practicas/` — client que conecta a server de semana 05
- [ ] `3-proyecto/` — web client con Express + MCP
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 10 — Integración con Claude y OpenAI

> Etapa: MCP Clients + LLMs · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-10-integracion_claude_openai/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — agentic loop diagram, tool selection flow
- [ ] `1-teoria/` — Anthropic API, OpenAI API, agentic loop, orquestación
- [ ] `2-practicas/` — chatbot con Claude + MCP tools, ídem OpenAI
- [ ] `3-proyecto/` — asistente inteligente con múltiples MCP servers
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 11 — Testing, Seguridad y Docker

> Etapa: Producción · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-11-testing_seguridad_docker/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — test pyramid MCP, security checklist diagram
- [ ] `1-teoria/` — pytest avanzado, vitest, OWASP + MCP, Docker multi-stage
- [ ] `2-practicas/` — suite de tests completa, hardening de server
- [ ] `3-proyecto/` — refactorizar server de semana 07 con tests + Docker prod
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Semana 12 — CI/CD y Proyecto Final

> Etapa: Producción · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-12-cicd_proyecto_final/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [ ] `0-assets/` — CI/CD pipeline diagram, project architecture diagram
- [ ] `1-teoria/` — GitHub Actions, deploy a Railway/Fly.io, monorepo patterns
- [ ] `2-practicas/` — configurar CI/CD, deploy del server de semana 07
- [ ] `3-proyecto/` — **Proyecto Final**: MCP system completo (server + client + LLM + CI/CD)
- [ ] `4-recursos/`, `5-glosario/README.md`

---

## Leyenda

| Símbolo | Significado |
|---------|-------------|
| `[x]` | Completado |
| `[ ]` | Pendiente |
| 🔲 | En progreso |
| ⬜ | Sin iniciar |

---

*Última actualización: 2026-04-19*
