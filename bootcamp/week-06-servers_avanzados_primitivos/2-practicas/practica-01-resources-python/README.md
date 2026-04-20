# Práctica 01 — Resources en Python (FastMCP)

## 🎯 Objetivo

Agregar **Resources** a un servidor MCP Python. Implementarás los handlers `list` y `read`
usando el decorador `@mcp.resource()` de FastMCP.

## 📋 Prerrequisitos

- Semana 04 completada (primer server Python)
- Docker instalado y funcionando

## 🚀 Pasos

### Paso 1: Levantar el entorno

```bash
docker compose up --build
```

### Paso 2: Verificar que el server arranca

```bash
docker compose logs server
```

Deberías ver: `Starting server "book-catalog" ...`

### Paso 3: Resource estático — books://all

Abre `src/server.py` y descomenta la **Sección 1**.

Este resource retorna todos los libros del catálogo en JSON.

```python
# Qué hace @mcp.resource("books://all"):
# 1. Registra el resource en resources/list con esa URI
# 2. Cuando el cliente llame resources/read con uri="books://all",
#    ejecuta la función y devuelve el string retornado
```

Verifica con MCP Inspector:

```bash
npx @modelcontextprotocol/inspector docker compose exec server uv run python src/server.py
```

→ Pestaña **Resources** → **List Resources** → deberías ver `books://all`

### Paso 4: Segundo resource estático — books://available

Descomenta la **Sección 2**.

Este resource filtra solo los libros que están disponibles para préstamo.

### Paso 5: Resource template — books://{isbn}

Descomenta la **Sección 3**.

El template `books://{isbn}` permite leer un libro específico por su ISBN.
El parámetro `isbn` llega como `str` a la función.

### Paso 6: Verificar todos los resources

En MCP Inspector → Resources:
- `books://all` → JSON con todos los libros
- `books://available` → JSON con libros disponibles
- Template `books://{isbn}` aparece en la lista de templates
- Prueba leer `books://978-0-13-110362-7` → datos del libro específico

---

## 📁 Estructura

```
practica-01-resources-python/
├── README.md
├── Dockerfile.python
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py
```
