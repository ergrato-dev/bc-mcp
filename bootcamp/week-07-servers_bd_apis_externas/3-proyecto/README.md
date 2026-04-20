# Proyecto Semana 07 — Library Manager MCP Server

## 📋 Descripcion

Construir un MCP Server completo que gestiona una biblioteca personal de libros.
Combina SQLite local con la API publica de Open Library para enriquecer registros.

## 🎯 Objetivos del Proyecto

1. Implementar CRUD completo para una biblioteca de libros en SQLite
2. Integrar Open Library API (`openlibrary.org`) para buscar y enriquecer libros
3. Aplicar el patron lifespan con SQLite + cliente HTTP compartidos
4. Manejar errores de BD y HTTP de forma robusta en todos los tools
5. Disponible en Python y TypeScript (elige uno o implementa ambos)

## 🗂️ Estructura

```
3-proyecto/
├── README.md
└── starter/
    ├── .env.example
    ├── docker-compose.yml
    ├── python-server/          ← implementar TODOs en src/server.py
    └── ts-server/              ← implementar TODOs en src/index.ts
```

## 🔧 Tools a implementar

### SQLite (datos locales)
| Tool | Input | Output |
|------|-------|--------|
| `search_books` | `query: str` | Lista de libros que coinciden |
| `get_book` | `book_id: int` | Detalle del libro |
| `add_book` | `title, author, year` | ID del nuevo libro |
| `update_book` | `book_id, ...campos` | Libro actualizado |
| `delete_book` | `book_id: int` | Confirmacion |

### Open Library API (externa, sin API key)
| Tool | Input | Output |
|------|-------|--------|
| `search_openlibrary` | `title: str` | Libros de la API publica |
| `enrich_book` | `book_id: int` | Libro local + metadata externa |

## 🌐 Open Library API

```
GET https://openlibrary.org/search.json?title=clean+code&limit=3
```

Respuesta clave:
```json
{"docs": [{"title": "...", "author_name": [...], "first_publish_year": 2008}]}
```

## ⚙️ Setup

```bash
cd starter
cp .env.example .env
docker compose up --build
```

## 📝 Instrucciones

1. Lee la teoria de [`1-teoria/`](../1-teoria/README.md) primero
2. Completa las practicas de [`2-practicas/`](../2-practicas/README.md) como preparacion
3. Trabaja SOLO en `starter/` — no modificar archivos fuera de esa carpeta
4. Busca todos los comentarios `# TODO` o `// TODO` e implementalos
5. Verifica cada tool en MCP Inspector antes de entregar

## 📊 Criterios de Evaluacion

### Conocimiento 🧠 (30%)
- Explica la diferencia entre los dos patrones de conexion SQLite
- Describe cuando usar `isError: true` vs `McpError`

### Desempeño 💪 (40%)
- Los 5 tools de SQLite funcionan correctamente
- Los 2 tools de Open Library retornan datos reales
- Los errores de BD e HTTP se manejan sin crashear el server

### Producto 📦 (30%)
- El server arranca y responde en MCP Inspector
- `enrich_book` combina datos locales + Open Library correctamente
- El codigo tiene manejo de errores en todos los tools

## 📌 Entregables

- [ ] MCP Server Python con 7 tools funcionales (5 CRUD + 2 API)
- [ ] MCP Server TypeScript con la misma funcionalidad
- [ ] `.env.example` con todas las variables necesarias
- [ ] Todos los tools responden correctamente en MCP Inspector
- [ ] docker-compose.yml para levantar el entorno completo

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md          # Este archivo
└── starter/           # Tu código va aquí
    └── README.md      # Instrucciones de setup
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
