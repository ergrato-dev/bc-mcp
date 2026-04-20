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
- [x] `04-transports.svg` — Comparativa stdio / HTTP/SSE / WebSocket con tabla

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
- [x] `01-jsonrpc-request-response.svg` — ciclo request/response/notification JSON-RPC
- [x] `02-stdio-transport.svg` — flujo stdin/stdout
- [x] `03-http-sse-transport.svg` — flujo HTTP + SSE
- [x] `04-websocket-transport.svg` — SSE vs WebSocket + árbol de decisión
- [x] `05-mensajes-mcp.svg` — ciclo de vida completo de sesión MCP (3 fases)

### Teoría (`1-teoria/`) — mín. 150 líneas por archivo
- [x] `01-json-rpc-2.md` — especificación JSON-RPC 2.0
- [x] `02-stdio-transport.md` — stdio: cómo funciona, cuándo usarlo
- [x] `03-http-sse-transport.md` — HTTP/SSE: setup, diferencias con stdio
- [x] `04-websocket-transport.md` — WebSocket: casos de uso avanzados
- [x] `05-mensajes-mcp.md` — tipos de mensajes: initialize, request, notification

### Prácticas (`2-practicas/`)
- [x] `practica-01/` — construir mensajes JSON-RPC manualmente via MCP Inspector
- [x] `practica-02/` — server con stdio transport (Python + TypeScript)
- [x] `practica-03/` — server con HTTP/SSE transport (Python + TypeScript)

### Proyecto (`3-proyecto/`)
- [x] `README.md`, `starter/` (session-analyzer.py + session-log.jsonl)

### Recursos + Glosario
- [x] `4-recursos/` — webgrafia, videografia, ebooks-free
- [x] `5-glosario/README.md` — 15 términos JSON-RPC y transports

---

## Semana 03 — Primitivos: Tools, Resources y Prompts

> Etapa: Fundamentos · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-03-primitivos_tools_resources_prompts/README.md`
- [x] `bootcamp/week-03-primitivos_tools_resources_prompts/rubrica-evaluacion.md`
- [x] Carpetas base

### Assets Visuales (`0-assets/`)
- [x] `01-tool-execution-flow.svg` — flujo completo de ejecución de un tool
- [x] `02-resource-fetch-flow.svg` — flujo de lectura de un resource
- [x] `03-prompt-flow.svg` — flujo de un prompt
- [x] `04-cuando-usar-cada-primitivo.svg` — árbol de decisión: tool vs resource vs prompt
- [x] `05-primitivos-comparativa.svg` — tabla comparativa de los 3 primitivos

### Teoría (`1-teoria/`)
- [x] `01-tools-schema-de-inputs-annotations-execu.md` — inputSchema, annotations, isError
- [x] `02-resources-uri-scheme-tipos-mime-resource.md` — URI scheme, tipos, templates
- [x] `03-prompts-argumentos-mensajes-y-role-based.md` — arguments, messages, EmbeddedResource
- [x] `04-cuando-usar-tool-vs-resource-vs-prompt.md` — guía de decisión y antipatrones
- [x] `05-diseno-de-interfaces-mcp-buenas-practica.md` — naming, seguridad, capabilities

### Prácticas (`2-practicas/`)
- [x] `practica-01/` — Tools: inputSchema, annotations, isError — Python + TypeScript
- [x] `practica-02/` — Resources: URIs, templates, blob — Python + TypeScript
- [x] `practica-03/` — Prompts: argumentos, messages, EmbeddedResource — Python + TypeScript
- [x] `practica-04/` — Los 3 primitivos combinados — Python + TypeScript

### Proyecto (`3-proyecto/`)
- [x] `README.md` (actualizado con escenario Knowledge Base)
- [x] `starter/` — docker-compose, python-server, ts-server, sample-docs

### Recursos + Glosario
- [x] `4-recursos/webgrafia/README.md`
- [x] `4-recursos/videografia/README.md`
- [x] `4-recursos/ebooks-free/README.md`
- [x] `5-glosario/README.md` — 16 términos clave

---

## Semana 04 — Primer MCP Server en Python

> Etapa: MCP Servers · Horas: 8h · Lenguaje: Python

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-04-primer_server_python/README.md`
- [x] `bootcamp/week-04-primer_server_python/rubrica-evaluacion.md`
- [x] Carpetas base

### Assets Visuales (`0-assets/`)
- [x] `01-fastmcp-anatomy.svg` — anatomía de un MCP server en Python
- [x] `02-decorator-schema-flow.svg` — decoradores FastMCP → JSON Schema
- [x] `03-server-lifecycle.svg` — ciclo de vida del server
- [x] `04-pyproject-uv-flow.svg` — flujo uv + pyproject.toml
- [x] `05-debugging-logging.svg` — canales stdout/stderr/ctx

### Teoría (`1-teoria/`)
- [x] `01-fastmcp-el-sdk-de-python-para-mcp.md`
- [x] `02-decorador-@mcp.tool-schema-automatico-co.md`
- [x] `03-ciclo-de-vida-del-server-startup-handlin.md`
- [x] `04-pyproject.toml-y-gestion-de-dependencias.md`
- [x] `05-debugging-de-servers-python-con-logging.md`

### Prácticas (`2-practicas/`)
- [x] `practica-01/` — FastMCP básico, tool `add`
- [x] `practica-02/` — Type hints y schema automático
- [x] `practica-03/` — Dependencias externas con uv + httpx
- [x] `practica-04/` — Context y lifespan
- [x] `practica-05/` — Múltiples tools

### Proyecto (`3-proyecto/`)
- [x] `README.md`, `starter/` (server.py con 3 tools: calculate, transform_text, date_info)

### Recursos + Glosario
- [x] `4-recursos/webgrafia/`, `videografia/`, `ebooks-free/`
- [x] `5-glosario/README.md` (~14 términos)

---

## Semana 05 — Primer MCP Server en TypeScript

> Etapa: MCP Servers · Horas: 8h · Lenguaje: TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-05-primer_server_typescript/README.md`
- [x] `bootcamp/week-05-primer_server_typescript/rubrica-evaluacion.md`
- [x] Carpetas base

### Assets Visuales (`0-assets/`)
- [x] `01-mcpserver-anatomy.svg` — anatomía de un MCP server TypeScript con StdioServerTransport
- [x] `02-server-tool-zod-schema.svg` — flujo server.tool() → Zod → JSON Schema
- [x] `03-pnpm-typescript-workflow.svg` — ciclo pnpm + tsc + Docker
- [x] `04-fastmcp-vs-mcpserver.svg` — comparativa Python vs TypeScript
- [x] `05-esm-modules-node22.svg` — CJS vs ESM, top-level await

### Teoría (`1-teoria/`)
- [x] `01-mcpserver-el-sdk-de-typescript-para-mcp.md`
- [x] `02-server-tool-y-zod-esquemas-de-validacion.md`
- [x] `03-package-json-tsconfig-y-compilacion.md`
- [x] `04-esm-modules-y-node22.md`
- [x] `05-comparativa-fastmcp-vs-mcpserver.md`

### Prácticas (`2-practicas/`)
- [x] `practica-01-mcpserver-basico/` — McpServer + StdioServerTransport + tool add
- [x] `practica-02-zod-schemas/` — tipos Zod, optional, default, describe, z.object()
- [x] `practica-03-calltoolresult/` — CallToolResult: texto, multi-content, JSON, isError
- [x] `practica-04-error-handling/` — z.enum(), try/catch, errores de dominio
- [x] `practica-05-multiples-tools/` — servidor completo con tools matemáticas/texto/fechas

### Proyecto (`3-proyecto/`)
- [x] `README.md` — instrucciones completas con los 3 tools
- [x] `starter/` — código con TODOs: calculate, transform_text, date_info

### Recursos + Glosario
- [x] `4-recursos/webgrafia/`, `videografia/`, `ebooks-free/`
- [x] `5-glosario/README.md` — 14 términos

---

## Semana 06 — Servers Avanzados: Los 3 Primitivos

> Etapa: MCP Servers · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-06-servers_avanzados_primitivos/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [x] `0-assets/` — 5 SVGs: resources arquitectura, templates, prompts flow, 3 primitivos, Python vs TS
- [x] `1-teoria/` — 5 archivos: resources list/read, templates, prompts, combinando primitivos, context/estado
- [x] `2-practicas/` — 4 prácticas: resources Python, resources TS, prompts ambos, server completo ambos
- [x] `3-proyecto/` — Task Manager starter Python + TypeScript con TODOs (Tools + Resources + Prompts)
- [x] `4-recursos/`, `5-glosario/README.md` — 20 términos, 3 READMEs de recursos

---

## Semana 07 — Servers con BD y APIs Externas

> Etapa: MCP Servers · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-07-servers_bd_apis_externas/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [x] `0-assets/` — diagramas de integración DB y APIs
- [x] `1-teoria/` — SQLite/PostgreSQL con MCP, httpx, rate limiting
- [x] `2-practicas/` — server con BD SQLite, server con API externa
- [x] `3-proyecto/` — Library Manager (BD + Open Library API)
- [x] `4-recursos/`, `5-glosario/README.md`

---

## Semana 08 — MCP Client en Python

> Etapa: MCP Clients + LLMs · Horas: 8h · Lenguaje: Python

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-08-mcp_client_python/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [x] `0-assets/` — 5 SVGs: anillos concéntricos, máquina de estados, pipes, swimlanes, card grid
- [x] `1-teoria/` — arquitectura, ClientSession, flujo, content types, manejo de errores
- [x] `2-practicas/` — 4 prácticas (primer client, descubrir, invocar, CLI interactivo)
- [x] `3-proyecto/` — Library CLI (6 TODOs): connect, list_tools, search, add, openlibrary, loop
- [x] `4-recursos/`, `5-glosario/README.md`

---

## Semana 09 — MCP Client en TypeScript

> Etapa: MCP Clients + LLMs · Horas: 8h · Lenguaje: TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-09-mcp_client_typescript/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [x] `0-assets/` — 5 SVGs: capas SDK, Client API, StdioClientTransport, ciclo de vida, comparativa Python/TS
- [x] `1-teoria/` — 5 archivos: arquitectura, StdioClientTransport, discover/tools/resources/prompts, tipado, errores
- [x] `2-practicas/` — 4 prácticas: primer-client, descubrir-capacidades, invocar-tools, cli-interactivo
- [x] `3-proyecto/` — Library CLI TypeScript con 6 TODOs (connectToServer, listTools, search, add, openLibrary, interactive)
- [x] `4-recursos/`, `5-glosario/README.md`

---

## Semana 10 — Integración con Claude y OpenAI

> Etapa: MCP Clients + LLMs · Horas: 8h · Lenguajes: Python + TypeScript

### Estructura Base (Scaffolding)
- [x] `bootcamp/week-10-integracion_claude_openai/README.md`
- [x] Carpetas base

### Assets + Teoría + Prácticas + Proyecto + Recursos + Glosario
- [x] `0-assets/` — agentic loop diagram, tool selection flow
- [x] `1-teoria/` — Anthropic API, OpenAI API, agentic loop, orquestación
- [x] `2-practicas/` — chatbot con Claude + MCP tools, ídem OpenAI
- [x] `3-proyecto/` — asistente inteligente con múltiples MCP servers
- [x] `4-recursos/`, `5-glosario/README.md`

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
