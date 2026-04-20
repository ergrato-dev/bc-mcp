"""
Notes MCP server — práctica del server completo (3 primitivos) en Python.
Semana 06 — Los 3 Primitivos
"""

import json
from mcp.server.fastmcp import FastMCP
from mcp.types import Message, TextContent

mcp = FastMCP("notes-manager")

# =============================================
# ESTADO COMPARTIDO — accesible por los 3 primitivos
# =============================================
NOTES: list[dict] = [
    {"id": 1, "title": "Reunion de equipo", "content": "Jueves 10am, sala B", "tag": "work"},
    {"id": 2, "title": "Ideas proyecto", "content": "API con FastMCP + Resources", "tag": "dev"},
]
_next_id = 3


# =============================================
# SECCIÓN 1 — TOOLS (mutan el estado)
# =============================================
# Los tools crean, actualizan y eliminan notas.
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def create_note(title: str, content: str, tag: str = "general") -> dict:
#     """Creates a new note.
#
#     Args:
#         title: Short title for the note.
#         content: Full content of the note.
#         tag: Category tag (e.g., work, dev, personal).
#     """
#     global _next_id
#     note = {"id": _next_id, "title": title, "content": content, "tag": tag}
#     NOTES.append(note)
#     _next_id += 1
#     return {"created": note}
#
# @mcp.tool()
# async def delete_note(note_id: int) -> dict:
#     """Deletes a note by ID.
#
#     Args:
#         note_id: The ID of the note to delete.
#     """
#     global NOTES
#     note = next((n for n in NOTES if n["id"] == note_id), None)
#     if note is None:
#         return {"error": f"Note {note_id} not found"}
#     NOTES = [n for n in NOTES if n["id"] != note_id]
#     return {"deleted": note}
#
# @mcp.tool()
# async def search_notes(query: str) -> list[dict]:
#     """Searches notes by title or content.
#
#     Args:
#         query: Text to search in titles and content.
#     """
#     q = query.lower()
#     return [n for n in NOTES if q in n["title"].lower() or q in n["content"].lower()]


# =============================================
# SECCIÓN 2 — RESOURCES (leen el estado)
# =============================================
# Los resources exponen el mismo estado que los tools modifican.
# Descomenta las siguientes líneas:
# @mcp.resource("notes://all")
# async def resource_all_notes() -> str:
#     """Returns all notes as JSON."""
#     return json.dumps(NOTES, ensure_ascii=False)
#
# @mcp.resource("notes://tags")
# async def resource_tags() -> str:
#     """Returns the list of unique tags used across notes."""
#     tags = sorted({n["tag"] for n in NOTES})
#     return json.dumps({"tags": tags}, ensure_ascii=False)
#
# @mcp.resource("notes://{note_id}")
# async def resource_note_by_id(note_id: str) -> str:
#     """Returns a specific note by ID."""
#     if not note_id.isdigit():
#         return json.dumps({"error": "note_id must be a positive integer"})
#     note = next((n for n in NOTES if n["id"] == int(note_id)), None)
#     if note is None:
#         return json.dumps({"error": f"Note {note_id} not found"})
#     return json.dumps(note, ensure_ascii=False)


# =============================================
# SECCIÓN 3 — PROMPTS (usan el estado para generar mensajes)
# =============================================
# Los prompts consultan el estado actual para generar conversaciones contextuales.
# Descomenta las siguientes líneas:
# @mcp.prompt()
# async def summarize_notes() -> list[Message]:
#     """Generates a prompt to summarize all current notes."""
#     notes_text = "\n".join(
#         f"- [{n['tag']}] {n['title']}: {n['content']}" for n in NOTES
#     )
#     return [
#         Message(
#             role="user",
#             content=TextContent(
#                 type="text",
#                 text=(
#                     f"Tengo las siguientes notas guardadas:\n\n{notes_text}\n\n"
#                     "Por favor, dame un resumen organizado por categoría."
#                 ),
#             ),
#         )
#     ]
#
# @mcp.prompt()
# async def find_related(topic: str) -> list[Message]:
#     """Finds notes related to a given topic.
#
#     Args:
#         topic: Topic to search for in the notes.
#     """
#     related = [n for n in NOTES if topic.lower() in n["content"].lower() or topic.lower() in n["title"].lower()]
#     notes_text = json.dumps(related, ensure_ascii=False) if related else "No se encontraron notas relacionadas."
#     return [
#         Message(
#             role="user",
#             content=TextContent(
#                 type="text",
#                 text=f"Sobre el tema '{topic}', tengo estas notas:\n\n{notes_text}\n\n¿Qué puedo aprender de esto?",
#             ),
#         )
#     ]


if __name__ == "__main__":
    mcp.run()
