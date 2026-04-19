# Práctica 04 — Combinando los Tres Primitivos

**Semana 03 — Los Tres Primitivos**

## Objetivo

Implementar un MCP Server completo que expone los tres primitivos al mismo tiempo:
**Tools**, **Resources** y **Prompts**. Aprenderás a declararlos juntos, configurar
las `ServerCapabilities` correctamente y validar el servidor con MCP Inspector.

## Prerrequisitos

- Haber completado Prácticas 01, 02 y 03
- Haber leído [05 — Diseño de interfaces MCP: buenas prácticas](../../1-teoria/05-diseno-de-interfaces-mcp-buenas-practica.md)

## Escenario: Knowledge Base Server

Construirás un servidor MCP para una base de conocimientos:
- **Tools**: `add_note` (crea una nota), `search_notes` (busca notas)
- **Resources**: `kb://notes/all` (lista de notas), `kb://notes/{id}` (nota por ID)
- **Prompts**: `summarize_notes` (genera un resumen de notas por tema)

## Pasos

### Paso 1: ServerCapabilities con los 3 primitivos

Abre `python-server/src/server.py` y descomenta la **Sección A**.
Observa cómo se declaran `tools`, `resources` y `prompts` juntos.

### Paso 2: Implementar los Tools

Descomenta la **Sección B**: `add_note` y `search_notes`.
Nota el uso de `isError` cuando la nota no existe.

### Paso 3: Implementar los Resources

Descomenta la **Sección C**: lista de notas y nota por ID (template).
Nota que Resources y Tools acceden a los mismos datos en memoria.

### Paso 4: Implementar los Prompts

Descomenta la **Sección D**: `summarize_notes` que genera un mensaje
usando datos del servidor embebidos como `EmbeddedResource`.

### Paso 5: Repetir en TypeScript

Repite todos los pasos en `ts-server/src/index.ts`.

## Verificación

```bash
docker compose up --build
```

Flujo de prueba completo en MCP Inspector:
1. `tools/call add_note` con `{title: "MCP Intro", content: "MCP es..."}` → nota creada
2. `resources/read kb://notes/all` → lista con la nota creada
3. `tools/call search_notes` con `{query: "MCP"}` → encuentra la nota
4. `prompts/get summarize_notes` → retorna mensajes para el LLM
