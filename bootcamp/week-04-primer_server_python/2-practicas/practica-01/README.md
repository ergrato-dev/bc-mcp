# Práctica 01 — FastMCP Básico: Tu Primer MCP Server

## 🎯 Objetivo

Crear un MCP Server mínimo y funcional con FastMCP registrando tools básicos.

## 📋 Prerrequisitos

- Haber leído [01-fastmcp-el-sdk-de-python-para-mcp.md](../../1-teoria/01-fastmcp-el-sdk-de-python-para-mcp.md)
- Docker y docker compose instalados

## 🗂️ Estructura

```
practica-01/
├── README.md            ← Este archivo
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py        ← Código a descomentar
```

## ⏱️ Tiempo estimado: 45 minutos

---

## Paso 1: El servidor FastMCP mínimo

FastMCP es la API de alto nivel del SDK de Python para MCP. Solo necesitas tres cosas:
1. Crear una instancia `FastMCP`
2. Decorar funciones con `@mcp.tool()`
3. Llamar a `mcp.run()`

**Abre `src/server.py`** y descomenta la **Sección A**.

```python
# Ejemplo de lo que descomendarás:
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("basic-server")
```

## Paso 2: Tu primer tool — add

El decorador `@mcp.tool()` convierte una función Python en un tool MCP.
Los type hints se convierten automáticamente en el JSON Schema del tool.

**Descomenta la Sección B** en `src/server.py`.

```python
@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b
```

## Paso 3: Arrancar el servidor con mcp.run()

`mcp.run()` inicia el transport loop de stdio. El servidor queda escuchando requests.

**Descomenta la Sección C** para completar el servidor.

## Paso 4: Agregar un segundo tool

Ahora agrega un tool que trabaje con strings. Observa cómo el type hint `str` genera un
JSON Schema distinto al de `int`.

**Descomenta la Sección D** para agregar el tool `greet`.

## Verificación

```bash
# Construir y ejecutar el contenedor
docker compose up --build

# El servidor queda en espera de conexiones stdio.
# Para detener: Ctrl+C
```

Para probar, usa MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run python src/server.py
```

---

## ✅ Criterios de Completitud

- [ ] El servidor inicia sin errores (`docker compose up --build`)
- [ ] El tool `add` está registrado
- [ ] El tool `greet` está registrado
- [ ] `mcp.run()` se llama al final del archivo
- [ ] No hay ningún `print()` en el código
