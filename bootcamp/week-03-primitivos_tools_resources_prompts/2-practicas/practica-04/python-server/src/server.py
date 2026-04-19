"""
MCP Server — Práctica 04: Los Tres Primitivos Combinados (Python)
Semana 03 — Los Tres Primitivos

Escenario: Knowledge Base Server
- Tools:     add_note, search_notes
- Resources: kb://notes/all, kb://notes/{id} (template)
- Prompts:   summarize_notes
"""

import asyncio
import json
from datetime import datetime
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

# ============================================================
# SECCIÓN A: Servidor con ServerCapabilities completas
# ============================================================
# Al crear el servidor, declaramos que expone los 3 primitivos.
# Esto permite que el cliente MCP sepa qué puede hacer.
#
# Descomenta las líneas siguientes:
# server = Server(
#     "practice-04-knowledge-base",
#     capabilities=types.ServerCapabilities(
#         tools=types.ToolsCapability(listChanged=False),
#         resources=types.ResourcesCapability(subscribe=False, listChanged=False),
#         prompts=types.PromptsCapability(listChanged=False)
#     )
# )
#
# In-memory knowledge base (shared between Tools and Resources)
# notes_db: dict[str, dict] = {}
# note_counter: int = 0

# Placeholder para que el módulo compile sin Sección A descomentada:
server = Server("practice-04-knowledge-base-placeholder")
notes_db: dict[str, dict] = {}
note_counter: int = 0


# ============================================================
# SECCIÓN B: Tools — add_note y search_notes
# ============================================================
# add_note crea una nota en notes_db (side-effect).
# search_notes busca en notes_db (podría ser Resource, pero
# aquí tiene lógica de búsqueda → Tool con readOnlyHint=True).
#
# Descomenta las líneas siguientes:
# @server.list_tools()
# async def list_tools() -> list[types.Tool]:
#     return [
#         types.Tool(
#             name="add_note",
#             description="Adds a new note to the knowledge base",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "title": {"type": "string", "description": "Note title", "minLength": 1, "maxLength": 100},
#                     "content": {"type": "string", "description": "Note content", "minLength": 1},
#                     "tags": {
#                         "type": "array",
#                         "items": {"type": "string"},
#                         "maxItems": 5,
#                         "description": "Optional tags for the note"
#                     }
#                 },
#                 "required": ["title", "content"],
#                 "additionalProperties": False
#             },
#             annotations=types.ToolAnnotations(destructiveHint=False, readOnlyHint=False)
#         ),
#         types.Tool(
#             name="search_notes",
#             description="Searches notes by title, content or tags",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "query": {"type": "string", "description": "Search text"},
#                 },
#                 "required": ["query"],
#                 "additionalProperties": False
#             },
#             annotations=types.ToolAnnotations(readOnlyHint=True, idempotentHint=True)
#         ),
#     ]
#
# @server.call_tool()
# async def call_tool(
#     name: str, arguments: dict
# ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
#     global note_counter
#
#     if name == "add_note":
#         note_counter += 1
#         note_id = str(note_counter)
#         notes_db[note_id] = {
#             "id": note_id,
#             "title": arguments["title"],
#             "content": arguments["content"],
#             "tags": arguments.get("tags", []),
#             "created_at": datetime.utcnow().isoformat()
#         }
#         return [types.TextContent(type="text", text=f"Note created with id={note_id}")]
#
#     if name == "search_notes":
#         query = arguments["query"].lower()
#         results = [
#             note for note in notes_db.values()
#             if query in note["title"].lower()
#             or query in note["content"].lower()
#             or any(query in tag.lower() for tag in note.get("tags", []))
#         ]
#         if not results:
#             return types.CallToolResult(
#                 content=[types.TextContent(type="text", text=f"No notes found for '{query}'")],
#                 isError=True
#             )
#         return [types.TextContent(type="text", text=json.dumps(results, indent=2))]
#
#     raise ValueError(f"Unknown tool: {name}")


# ============================================================
# SECCIÓN C: Resources — kb://notes/all y kb://notes/{id}
# ============================================================
# Nota: Resources y Tools comparten notes_db.
# Resources leen los datos; Tools los modifican.
#
# Descomenta las líneas siguientes:
# @server.list_resources()
# async def list_resources() -> list[types.Resource]:
#     return [
#         types.Resource(
#             uri="kb://notes/all",
#             name="All notes",
#             description="Lists all notes in the knowledge base",
#             mimeType="application/json"
#         )
#     ]
#
# @server.list_resource_templates()
# async def list_resource_templates() -> list[types.ResourceTemplate]:
#     return [
#         types.ResourceTemplate(
#             uriTemplate="kb://notes/{note_id}",
#             name="Note by ID",
#             description="Returns the full content of a specific note",
#             mimeType="application/json"
#         )
#     ]
#
# @server.read_resource()
# async def read_resource(uri: str) -> types.ReadResourceResult:
#     if uri == "kb://notes/all":
#         summary = [{"id": n["id"], "title": n["title"], "tags": n["tags"]} for n in notes_db.values()]
#         return types.ReadResourceResult(
#             contents=[types.TextResourceContents(
#                 uri=uri, text=json.dumps(summary, indent=2), mimeType="application/json"
#             )]
#         )
#
#     if uri.startswith("kb://notes/"):
#         note_id = uri.removeprefix("kb://notes/")
#         note = notes_db.get(note_id)
#         if not note:
#             raise ValueError(f"Note {note_id} not found")
#         return types.ReadResourceResult(
#             contents=[types.TextResourceContents(
#                 uri=uri, text=json.dumps(note, indent=2), mimeType="application/json"
#             )]
#         )
#
#     raise ValueError(f"Resource not found: {uri}")


# ============================================================
# SECCIÓN D: Prompts — summarize_notes
# ============================================================
# El Prompt embebe los datos actuales de la KB directamente
# usando EmbeddedResource, sin que el cliente haga otro request.
#
# Descomenta las líneas siguientes:
# @server.list_prompts()
# async def list_prompts() -> list[types.Prompt]:
#     return [
#         types.Prompt(
#             name="summarize_notes",
#             description="Generates a summary of all notes in the knowledge base",
#             arguments=[
#                 types.PromptArgument(
#                     name="focus",
#                     description="Topic or keyword to focus the summary on",
#                     required=False
#                 )
#             ]
#         )
#     ]
#
# @server.get_prompt()
# async def get_prompt(name: str, arguments: dict | None) -> types.GetPromptResult:
#     args = arguments or {}
#
#     if name == "summarize_notes":
#         focus = args.get("focus", "all topics")
#         all_notes = list(notes_db.values())
#
#         return types.GetPromptResult(
#             description="Knowledge base summary",
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.EmbeddedResource(
#                         type="resource",
#                         resource=types.TextResourceContents(
#                             uri="kb://notes/all",
#                             text=json.dumps(all_notes, indent=2),
#                             mimeType="application/json"
#                         )
#                     )
#                 ),
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=f"Summarize the notes above, focusing on: {focus}"
#                     )
#                 )
#             ]
#         )
#
#     raise ValueError(f"Unknown prompt: {name}")


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
