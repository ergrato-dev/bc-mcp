# Practica 01 — Books SQLite con Python

## 🎯 Objetivo

Construir un MCP Server en Python que gestiona una biblioteca de libros usando
`aiosqlite` para acceso asincrono a SQLite.

## 📋 Que aprenderás

- Conectar un MCP Server a SQLite con `aiosqlite`
- Implementar CRUD (Create, Read, Update, Delete) via tools MCP
- Usar el patron `async with` por tool (patron simple)
- Retornar resultados estructurados en JSON desde un tool

## 🗂️ Estructura

```
practica-01-books-sqlite-python/
├── README.md
├── Dockerfile.python
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py       ← archivo principal (descomentar secciones)
```

## ⚙️ Setup con Docker

```bash
cd practica-01-books-sqlite-python
docker compose up --build
```

## 📝 Instrucciones

### Paso 1 — Explorar el server base

Abre `src/server.py`. Verás que el server ya arranca con:
- Un lifespan que inicializa la base de datos `books.db`
- La tabla `books` creada automaticamente
- Una tool `list_books` ya funcional

Ejecuta el server y verifica en MCP Inspector que `list_books` funciona.

### Paso 2 — Activar search_books

El tool `search_books` ya está escrito pero comentado.
Descomenta la seccion `# PASO 2` en `src/server.py`:

```python
# Busca libros por título o autor
# async def search_books(query: str, ctx: Context) -> str:
```

Verifica que `search_books` aparece en MCP Inspector y retorna resultados.

### Paso 3 — Activar get_book

Descomenta la seccion `# PASO 3`.
Este tool recibe un `book_id` y retorna el libro completo, o un error si no existe.

Prueba: busca un id que exista y uno que no exista. Observa las diferencias de respuesta.

### Paso 4 — Activar add_book

Descomenta la seccion `# PASO 4`.
El tool `add_book` inserta un nuevo libro y retorna el id asignado.

Prueba: agrega un libro, luego busca para verificar que aparece.

### Paso 5 — Activar delete_book

Descomenta la seccion `# PASO 5`.
El tool `delete_book` elimina un libro por id.

Prueba: elimina el libro que agregaste en el paso anterior.

## ✅ Criterios de éxito

- [ ] `list_books` muestra la lista de libros
- [ ] `search_books` filtra por título o autor
- [ ] `get_book` retorna el libro o un error claro si no existe
- [ ] `add_book` agrega el libro y retorna el id
- [ ] `delete_book` elimina el libro y confirma, o indica si no existia
