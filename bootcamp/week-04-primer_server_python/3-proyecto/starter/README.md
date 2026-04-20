# Starter — Semana 04: Utility MCP Server

Tu punto de partida para el proyecto de la semana.

## Setup y ejecución

```bash
# Posicionarse en este directorio
cd bootcamp/week-04-primer_server_python/3-proyecto/starter

# Construir y levantar el server
docker compose up --build

# Probar con MCP Inspector (en otra terminal)
npx @modelcontextprotocol/inspector uv run python src/server.py
```

## Archivos que debes editar

```
starter/
└── src/
    └── server.py    ← ⭐ ESTE es el único archivo que debes modificar
```

## Qué implementar

En `src/server.py` encontrarás 3 tools con sus firmas y docstrings completos.
Cada tool tiene comentarios `# TODO` que describen exactamente qué implementar:

1. **`calculate`** — operaciones matemáticas: add, subtract, multiply, divide
2. **`transform_text`** — transformaciones: upper, lower, reverse, title, word_count
3. **`date_info`** — información de una fecha: weekday, days_until, is_weekend, etc.

## Verificación

Tu implementación es correcta cuando:
- `docker compose up --build` no produce errores
- El MCP Inspector muestra los 3 tools con sus schemas
- Cada tool retorna el resultado esperado con inputs válidos
- Los tools retornan errores descriptivos con inputs inválidos

Consulta las instrucciones completas en [../README.md](../README.md).

---

[← Volver al proyecto](../README.md)
