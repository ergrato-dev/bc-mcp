"""
Knowledge Base MCP Server — Semana 03 Proyecto
Implementa los tres primitivos del protocolo MCP:
  - Tool:     search_docs
  - Resource: docs://catalog, docs://files/{filename}
  - Prompt:   summarize_doc
"""

import asyncio
import json
from pathlib import Path
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

server = Server(
    "week03-knowledge-base",
    capabilities=types.ServerCapabilities(
        tools=types.ToolsCapability(listChanged=False),
        resources=types.ResourcesCapability(subscribe=False, listChanged=False),
        prompts=types.PromptsCapability(listChanged=False),
    ),
)

# In-memory docs database — loaded from sample-docs/ at startup
DOCS_DB: dict[str, dict] = {}

DOCS_DIR = Path(__file__).parent.parent / "sample-docs"


def load_docs() -> None:
    """Load all .md files from sample-docs/ into DOCS_DB."""
    for doc_file in DOCS_DIR.glob("*.md"):
        content = doc_file.read_text(encoding="utf-8")
        # Extract first H1 line as title, fallback to filename
        title = doc_file.stem
        for line in content.splitlines():
            if line.startswith("# "):
                title = line.lstrip("# ").strip()
                break
        DOCS_DB[doc_file.name] = {
            "filename": doc_file.name,
            "title": title,
            "content": content,
        }


# ============================================================
# TOOL: search_docs
# ============================================================
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search_docs",
            description="Searches documentation files by keyword in title or content",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Text to search for in documentation",
                        "minLength": 1,
                    }
                },
                "required": ["query"],
                "additionalProperties": False,
            },
            annotations=types.ToolAnnotations(readOnlyHint=True, idempotentHint=True),
        )
    ]


@server.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if name == "search_docs":
        # TODO 1: Implementar la búsqueda
        # 1. Obtener la query de arguments["query"]
        # 2. Convertir a minúsculas para búsqueda case-insensitive
        # 3. Filtrar DOCS_DB donde query aparezca en doc["title"] o doc["content"]
        # 4. Si no hay resultados, retornar isError=True con mensaje descriptivo
        # 5. Si hay resultados, retornar JSON con lista de {filename, title} encontrados
        pass

    raise ValueError(f"Unknown tool: {name}")


# ============================================================
# RESOURCES: docs://catalog y docs://files/{filename}
# ============================================================
@server.list_resources()
async def list_resources() -> list[types.Resource]:
    # TODO 2a: Retornar un Resource con uri="docs://catalog"
    # description="Catalog of all available documentation files"
    # mimeType="application/json"
    return []


@server.list_resource_templates()
async def list_resource_templates() -> list[types.ResourceTemplate]:
    # TODO 2b: Retornar un ResourceTemplate con uriTemplate="docs://files/{filename}"
    # name="Documentation file", description="Content of a documentation file"
    # mimeType="text/markdown"
    return []


@server.read_resource()
async def read_resource(uri: str) -> types.ReadResourceResult:
    # TODO 3: Manejar dos casos:
    #
    # Caso A — uri == "docs://catalog":
    #   Retornar lista de docs como JSON: [{filename, title}, ...]
    #   usar TextResourceContents con mimeType="application/json"
    #
    # Caso B — uri.startswith("docs://files/"):
    #   Extraer filename = uri.removeprefix("docs://files/")
    #   Si el filename no está en DOCS_DB → raise ValueError con mensaje claro
    #   Retornar contenido del archivo como TextResourceContents con mimeType="text/markdown"
    #
    # Si ningún caso coincide → raise ValueError(f"Resource not found: {uri}")
    raise ValueError(f"Resource not found: {uri}")


# ============================================================
# PROMPT: summarize_doc
# ============================================================
@server.list_prompts()
async def list_prompts() -> list[types.Prompt]:
    # TODO 4a: Retornar un Prompt con:
    # name="summarize_doc", description="Summarizes a documentation file"
    # arguments: [
    #   PromptArgument(name="filename", description="Name of the doc file (e.g. intro.md)", required=True),
    #   PromptArgument(name="style", description="Summary style: bullet_points or paragraph", required=False),
    # ]
    return []


@server.get_prompt()
async def get_prompt(name: str, arguments: dict | None) -> types.GetPromptResult:
    args = arguments or {}

    if name == "summarize_doc":
        # TODO 4b: Implementar el prompt
        # 1. Obtener filename de args (required) y style de args (optional, default="paragraph")
        # 2. Si filename no está en DOCS_DB → raise ValueError con mensaje claro
        # 3. Retornar GetPromptResult con description y messages:
        #    - Mensaje 1: EmbeddedResource con el contenido del documento
        #      uri="docs://files/{filename}", text=doc["content"], mimeType="text/markdown"
        #    - Mensaje 2: TextContent con instrucción al LLM:
        #      f"Summarize the documentation above as {style}."
        pass

    raise ValueError(f"Unknown prompt: {name}")


async def main() -> None:
    load_docs()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
