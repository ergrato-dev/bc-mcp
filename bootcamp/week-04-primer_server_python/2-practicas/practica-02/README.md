# Práctica 02 — Type Hints y Docstrings como Schema Automático

## 🎯 Objetivo

Profundizar en cómo FastMCP convierte type hints de Python en JSON Schema automáticamente,
incluyendo tipos opcionales, valores por defecto, listas y modelos Pydantic.

## 📋 Prerrequisitos

- Haber completado la Práctica 01
- Haber leído [02-decorador-@mcp.tool-schema-automatico-co.md](../../1-teoria/02-decorador-@mcp.tool-schema-automatico-co.md)

## 🗂️ Estructura

```
practica-02/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py        ← Código a descomentar
```

## ⏱️ Tiempo estimado: 45 minutos

---

## Paso 1: Parámetros opcionales y valores por defecto

Un parámetro con valor por defecto es opcional en el JSON Schema.
Sin valor por defecto, es requerido.

**Abre `src/server.py`** y descomenta la **Sección A**.

```python
@mcp.tool()
async def search(
    query: str,            # requerido — sin default
    limit: int = 10,       # opcional — con default
    case_sensitive: bool = False,   # opcional — con default
) -> list[str]:
    ...
```

Verifica en MCP Inspector que solo `query` aparece en `required`.

## Paso 2: Tipos complejos — list y dict

FastMCP soporta tipos genéricos de Python como `list[str]` y `dict[str, int]`.

**Descomenta la Sección B** para explorar estos tipos.

## Paso 3: str | None — parámetros verdaderamente opcionales

Usa `str | None = None` para parámetros que pueden omitirse completamente.

**Descomenta la Sección C** para ver la diferencia.

## Paso 4: Pydantic BaseModel como input

Para grupos de parámetros relacionados, usa `BaseModel`. FastMCP genera el schema
del modelo automáticamente con las descripciones de `Field()`.

**Descomenta la Sección D** para implementar un tool con Pydantic.

## Verificación

```bash
docker compose up --build
# Luego conectar con MCP Inspector y verificar los schemas generados
npx @modelcontextprotocol/inspector uv run python src/server.py
```

Observa en MCP Inspector cómo cada type hint genera un schema diferente.

---

## ✅ Criterios de Completitud

- [ ] El tool `search` tiene `query` como único parámetro requerido
- [ ] El tool `process_list` acepta `list[str]` y retorna `dict`
- [ ] El tool `get_user` tiene un parámetro `str | None = None`
- [ ] El tool `analyze` usa Pydantic `BaseModel` como input
- [ ] Los schemas son visibles y correctos en MCP Inspector
