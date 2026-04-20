# Práctica 02 — Descubrir Capacidades del Server

## 🎯 Objetivo

Usar `list_tools()`, `list_resources()` y `list_prompts()` para descubrir
dinámicamente todo lo que ofrece el server, sin hardcodear ningún nombre.

## 📋 Requisitos previos

- Práctica 01 completada y funcionando

## 🗂️ Estructura

```
practica-02-descubrir-capacidades/
├── README.md
└── starter/
    ├── pyproject.toml
    └── client.py
```

---

## Pasos

### Paso 1: Instalar dependencias

```bash
cd practica-02-descubrir-capacidades/starter
uv sync
```

### Paso 2: PASO 1 — Conectar (igual que práctica 01)

El boilerplate de conexión es el mismo. Descomenta la sección `PASO 1`.

### Paso 3: PASO 2 — list_tools() con schema

Descomenta la sección `PASO 2`.

`list_tools()` retorna un `ListToolsResult` con una lista de objetos `Tool`:
- `tool.name` — nombre exacto para usar en `call_tool()`
- `tool.description` — descripción para el LLM
- `tool.inputSchema` — JSON Schema con `properties` y `required`

```python
# Ejemplo explicativo
tools_result = await session.list_tools()
for tool in tools_result.tools:
    props = tool.inputSchema.get("properties", {})
    required = tool.inputSchema.get("required", [])
    for param, schema in props.items():
        marker = "(*)" if param in required else "   "
        print(f"  {marker} {param}: {schema.get('type', 'any')}")
```

### Paso 4: PASO 3 — list_resources()

Descomenta la sección `PASO 3`.

`list_resources()` retorna los resources disponibles con su URI. La URI es lo
que usarás luego en `read_resource(uri)`.

### Paso 5: PASO 4 — list_prompts() con argumentos

Descomenta la sección `PASO 4`.

`list_prompts()` retorna los prompts disponibles. Cada prompt tiene una lista
de `arguments` — cada argumento tiene `name`, `description` y `required`.

### Paso 6: Ejecutar

```bash
uv run python client.py
```

Salida esperada:
```
=== 7 Tools ===
• search_books
  Search local library by title or author
  (*) query: string — Search text
• add_book
  Add a new book to the local library
  (*) title: string
  ...

=== 2 Resources ===
• db://books/stats — Estadísticas de la biblioteca
• db://books/all   — Todos los libros

=== 1 Prompts ===
• analyze_book
  - book_id (requerido)
  - style (opcional)
```

## ✅ Criterio de éxito

- Lista todos los tools con sus parámetros marcando cuáles son requeridos
- Lista todos los resources con su URI
- Lista todos los prompts con sus argumentos

---

[← Práctica 01](../practica-01-primer-client/) | [Práctica 03 →](../practica-03-invocar-tools/)
