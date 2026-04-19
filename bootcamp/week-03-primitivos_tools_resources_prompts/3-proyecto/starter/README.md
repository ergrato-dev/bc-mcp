# Starter — Knowledge Base MCP Server

## Setup

```bash
cd bootcamp/week-03-primitivos_tools_resources_prompts/3-proyecto/starter
docker compose up --build
```

Esto levanta dos servidores:
- `python-kb-server` — implementación en Python
- `ts-kb-server` — implementación en TypeScript

## Tu trabajo

Abre **`python-server/src/server.py`** y busca los comentarios `# TODO`.
Implementa cada sección en el orden indicado:

1. **TODO 1** — `search_docs`: buscar en `DOCS_DB` por título y contenido
2. **TODO 2** — `list_resources`: retornar `docs://catalog` y la template `docs://files/{filename}`
3. **TODO 3** — `read_resource`: manejar `docs://catalog` y `docs://files/{filename}`
4. **TODO 4** — `list_prompts` y `get_prompt` para `summarize_doc`

Luego repite el mismo proceso en **`ts-server/src/index.ts`**.

## Verificación

Prueba cada primitivo con MCP Inspector o con un cliente MCP:

```
# Verificar tool
tools/call search_docs {"query": "MCP"}

# Verificar resources
resources/list
resources/read docs://catalog
resources/read docs://files/intro.md

# Verificar prompt
prompts/list
prompts/get summarize_doc {"filename": "intro.md"}
```

## Referencia

- [README del proyecto](../README.md)
- [Teoría — Semana 03](../../1-teoria/README.md)
- [Prácticas completadas](../../2-practicas/README.md)

---

[← Volver al proyecto](../README.md)
