# Conexiones Async a SQLite desde MCP Servers

## 🎯 Objetivos

- Conectar un MCP Server a SQLite usando `aiosqlite` en Python
- Entender los dos patrones de conexion: simple y lifespan
- Ejecutar queries parametrizadas de forma segura (sin SQL injection)
- Inicializar la base de datos automaticamente al arrancar el server

## 📋 Contenido

![Arquitectura MCP + SQLite + aiosqlite](../0-assets/01-sqlite-aiosqlite-mcp.svg)

### 1. Por que SQLite para MCP Servers

SQLite es la eleccion natural para aprender integracion de bases de datos en MCP:

- **Sin servidor separado**: el archivo `.db` vive junto al codigo
- **Zero configuracion**: no requiere instalacion ni configuracion
- **Perfecto para aprender**: mismos conceptos que PostgreSQL, menos friccion
- **Soporte async en Python**: la libreria `aiosqlite` envuelve sqlite3 con async/await
- **Sync en TypeScript**: `better-sqlite3` es sincrono pero muy simple y rapido

El objetivo de esta semana es aprender los patrones de integracion. Una vez dominados,
migrar a PostgreSQL es cambiar el driver y la cadena de conexion.

### 2. aiosqlite en Python

`aiosqlite` es un wrapper async sobre el modulo `sqlite3` de la libreria estandar.

**Instalacion:**
```toml
# pyproject.toml
[project]
dependencies = [
    "mcp==1.9.0",
    "aiosqlite==0.20.0",
]
```

**Uso basico:**
```python
import aiosqlite
import json

async def example():
    # abre conexion, ejecuta query, cierra conexion automaticamente
    async with aiosqlite.connect("books.db") as db:
        db.row_factory = aiosqlite.Row  # acceso por nombre de columna
        async with db.execute(
            "SELECT * FROM books WHERE title LIKE ?",
            (f"%{query}%",),
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
```

**Puntos clave de aiosqlite:**
- El `async with aiosqlite.connect(...)` abre y cierra la conexion automaticamente
- Las queries usan `?` como placeholder para parametros (previene SQL injection)
- `db.row_factory = aiosqlite.Row` permite acceder a columnas por nombre
- Siempre usar `await` en operaciones de I/O (execute, fetchall, commit, etc.)

### 3. Patron Simple — async with por tool

El patron mas directo: cada tool abre su propia conexion cuando se llama.

```python
from mcp.server.fastmcp import FastMCP
import aiosqlite
import json
import os

DB_PATH = os.environ.get("DB_PATH", "./data/books.db")

mcp = FastMCP("books-server")

@mcp.tool()
async def search_books(query: str) -> str:
    """Search books by title or author in the local database."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT id, title, author, year FROM books "
            "WHERE title LIKE ? OR author LIKE ?",
            (f"%{query}%", f"%{query}%"),
        ) as cursor:
            rows = await cursor.fetchall()
            return json.dumps([dict(r) for r in rows], ensure_ascii=False)


@mcp.tool()
async def get_book(book_id: int) -> str:
    """Get a single book by its ID."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM books WHERE id = ?", (book_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row is None:
                return json.dumps({"error": f"Book {book_id} not found"})
            return json.dumps(dict(row), ensure_ascii=False)
```

**Ventajas del patron simple:**
- Facil de entender: cada tool es autocontenido
- La conexion siempre se cierra (context manager)
- No requiere configuracion de lifespan

**Desventajas:**
- Abre una nueva conexion por cada llamada al tool
- Mayor overhead en servidores con muchas llamadas

### 4. Patron Lifespan — conexion compartida (recomendado)

Para produccion, es mejor compartir una sola conexion a traves de todo el servidor.
FastMCP admite un `lifespan` que abre recursos al arrancar y los cierra al apagar.

```python
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context
import aiosqlite
import json
import os

DB_PATH = os.environ.get("DB_PATH", "./data/books.db")


@asynccontextmanager
async def lifespan(server: FastMCP):
    """Open the DB connection on startup, close on shutdown."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        # Crear tabla si no existe (init schema)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                title  TEXT NOT NULL,
                author TEXT NOT NULL,
                year   INTEGER
            )
        """)
        await db.commit()
        yield {"db": db}  # disponible en ctx.request_context.lifespan_context


mcp = FastMCP("books-server", lifespan=lifespan)


@mcp.tool()
async def search_books(query: str, ctx: Context) -> str:
    """Search books by title or author in the local database."""
    db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
    async with db.execute(
        "SELECT id, title, author, year FROM books "
        "WHERE title LIKE ? OR author LIKE ?",
        (f"%{query}%", f"%{query}%"),
    ) as cursor:
        rows = await cursor.fetchall()
        return json.dumps([dict(r) for r in rows], ensure_ascii=False)


@mcp.tool()
async def add_book(title: str, author: str, year: int, ctx: Context) -> str:
    """Add a new book to the database."""
    db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
    async with db.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year),
    ) as cursor:
        await db.commit()
        return json.dumps({"id": cursor.lastrowid, "message": "Book added"})
```

**Ventajas del patron lifespan:**
- Una sola conexion para todo el servidor
- Schema se inicializa una sola vez al arrancar
- La conexion esta disponible en `ctx.request_context.lifespan_context`
- Patron recomendado para produccion

### 5. Queries CRUD completas

Los cuatro tipos de operaciones SQL fundamentales:

```python
# CREATE — insertar
await db.execute(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    (title, author, year),
)
await db.commit()  # siempre hacer commit despues de escrituras

# READ — consultar
async with db.execute(
    "SELECT * FROM books WHERE id = ?", (book_id,)
) as cursor:
    row = await cursor.fetchone()  # un solo resultado
    rows = await cursor.fetchall()  # todos los resultados

# UPDATE — actualizar
await db.execute(
    "UPDATE books SET title = ? WHERE id = ?",
    (new_title, book_id),
)
await db.commit()

# DELETE — eliminar
await db.execute("DELETE FROM books WHERE id = ?", (book_id,))
await db.commit()
```

**Regla critica de seguridad: NUNCA interpolar strings directamente en SQL**
```python
# PELIGROSO — SQL Injection
await db.execute(f"SELECT * FROM books WHERE title = '{user_input}'")

# CORRECTO — parametros preparados
await db.execute("SELECT * FROM books WHERE title = ?", (user_input,))
```

### 6. Inicializacion del Schema

Es buena practica inicializar la base de datos al arrancar el server:

```python
async def init_db(db: aiosqlite.Connection) -> None:
    """Initialize database schema."""
    await db.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT NOT NULL,
            author TEXT NOT NULL,
            year   INTEGER,
            isbn   TEXT UNIQUE
        )
    """)
    await db.execute("""
        CREATE INDEX IF NOT EXISTS idx_books_title ON books(title)
    """)
    await db.commit()
```

`CREATE TABLE IF NOT EXISTS` es idempotente: si la tabla ya existe, no hace nada.
Esto permite levantar el server multiples veces sin errores.

### 7. TypeScript con better-sqlite3

En TypeScript, `better-sqlite3` ofrece una API sincrona y muy rapida.
A diferencia de Python, no necesitamos `await` para las operaciones SQLite.

```typescript
import Database from "better-sqlite3";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { z } from "zod";

const DB_PATH = process.env.DB_PATH ?? "./data/books.db";

// Abrir conexion (global, persistente)
const db = new Database(DB_PATH);

// Inicializar schema
db.exec(`
  CREATE TABLE IF NOT EXISTS books (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT NOT NULL,
    author TEXT NOT NULL,
    year   INTEGER
  )
`);

const server = new Server({ name: "books-server", version: "1.0.0" });

server.tool(
  "search_books",
  { query: z.string().describe("Search term for title or author") },
  async ({ query }) => {
    // better-sqlite3 es SINCRONO — no necesita await
    const rows = db
      .prepare(
        "SELECT id, title, author, year FROM books " +
        "WHERE title LIKE ? OR author LIKE ?"
      )
      .all(`%${query}%`, `%${query}%`);

    return {
      content: [{ type: "text", text: JSON.stringify(rows) }],
    };
  },
);

server.tool(
  "add_book",
  {
    title: z.string(),
    author: z.string(),
    year: z.number().int().min(1000).max(2100),
  },
  async ({ title, author, year }) => {
    // Escrituras tambien son sincronas
    const result = db
      .prepare("INSERT INTO books (title, author, year) VALUES (?, ?, ?)")
      .run(title, author, year);

    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({
            id: result.lastInsertRowid,
            message: "Book added",
          }),
        },
      ],
    };
  },
);
```

**Diferencias clave Python vs TypeScript para SQLite:**
| Aspecto | Python (aiosqlite) | TypeScript (better-sqlite3) |
|---------|--------------------|-----------------------------|
| API | Async (await) | Sincrona |
| Placeholder | `?` | `?` (igual) |
| Fetch rows | `await cursor.fetchall()` | `stmt.all(params)` |
| Fetch one | `await cursor.fetchone()` | `stmt.get(params)` |
| Insert | `cursor.lastrowid` | `result.lastInsertRowid` |
| Commit | `await db.commit()` | Automatico (no requerido) |

## 4. Errores Comunes

### Error: "no such table: books"
**Causa**: El server arranco sin inicializar la base de datos.
**Solucion**: Agregar `CREATE TABLE IF NOT EXISTS` en el lifespan o en la funcion de init.

### Error: "SQLITE_BUSY: database is locked"
**Causa**: Multiples escrituras concurrentes al mismo archivo SQLite.
**Solucion**: Usar `journal_mode=WAL` para mejor concurrencia.
```python
await db.execute("PRAGMA journal_mode=WAL")
```

### Error: OperationalError: "unable to open database file"
**Causa**: El directorio para el archivo `.db` no existe.
**Solucion**: Crear el directorio antes de conectar.
```python
import pathlib
pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
```

### Error: Inyeccion SQL (SQL Injection)
**Causa**: Interpolar directamente variables de usuario en SQL.
**Solucion**: SIEMPRE usar `?` como placeholders y pasar parametros como tupla.

## 5. Ejercicios de Comprension

1. ¿Cual es la diferencia entre `cursor.fetchone()` y `cursor.fetchall()`?
2. ¿Por que es importante hacer `await db.commit()` despues de escrituras?
3. ¿Que ventaja tiene el patron lifespan sobre abrir una conexion por tool?
4. ¿Como previene `?` el SQL injection en aiosqlite?
5. ¿Por que `better-sqlite3` es sincrono mientras `aiosqlite` es async?

## 📚 Recursos Adicionales

- [aiosqlite Documentation](https://aiosqlite.omnilib.dev/)
- [better-sqlite3 Documentation](https://github.com/WiseLibs/better-sqlite3)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

## ✅ Checklist de Verificacion

- [ ] El server crea la tabla con `CREATE TABLE IF NOT EXISTS` al arrancar
- [ ] Todas las queries usan `?` como placeholders (sin f-strings en SQL)
- [ ] Se hace `await db.commit()` despues de INSERT/UPDATE/DELETE
- [ ] El `DB_PATH` se lee desde variable de entorno, no hardcodeado
- [ ] El context manager `async with aiosqlite.connect(...)` cierra la conexion
- [ ] Los resultados se serializan a JSON antes de retornar desde el tool
