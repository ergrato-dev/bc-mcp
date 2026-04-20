# Connection Pooling — aiosqlite y httpx

## 🎯 Objetivos

- Entender que es un connection pool y por que mejora el rendimiento
- Implementar el patron lifespan para compartir conexiones en FastMCP
- Combinar conexion de BD y cliente HTTP en un solo lifespan
- Configurar el pool de httpx para APIs externas

## 📋 Contenido

![SQLite + aiosqlite Architecture](../0-assets/01-sqlite-aiosqlite-mcp.svg)

### 1. Que es el Connection Pooling

Un **connection pool** es un conjunto de conexiones reutilizables que se crean al
arrancar la aplicacion y se comparten entre multiples solicitudes.

**Sin pool (patron simple):**
```
Tool call 1 → abrir conexion → query → cerrar conexion
Tool call 2 → abrir conexion → query → cerrar conexion
Tool call 3 → abrir conexion → query → cerrar conexion
```

**Con pool (patron lifespan):**
```
Startup → abrir conexion (una vez)
Tool call 1 → reutilizar conexion → query
Tool call 2 → reutilizar conexion → query
Tool call 3 → reutilizar conexion → query
Shutdown → cerrar conexion (una vez)
```

Para SQLite, el beneficio es menor overhead al eliminar la apertura/cierre por cada
llamada. Para PostgreSQL o APIs HTTP, el impacto en rendimiento es mucho mayor.

### 2. Patron Lifespan en FastMCP

FastMCP acepta un `lifespan` que es un context manager async.
El valor que hace `yield` queda disponible en todos los tools via `ctx`:

```python
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context
import aiosqlite
import os

DB_PATH = os.environ.get("DB_PATH", "./data/books.db")


@asynccontextmanager
async def lifespan(server: FastMCP):
    """
    Lifecycle manager para el MCP Server.
    
    - Se ejecuta una vez al arrancar el server
    - El bloque antes del yield es el setup
    - El bloque despues del yield es el teardown (cleanup)
    - Lo que se hace yield queda disponible en ctx.request_context.lifespan_context
    """
    print("Starting server — opening database connection...")
    
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        
        # Inicializar schema (idempotente)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                title  TEXT NOT NULL,
                author TEXT NOT NULL,
                year   INTEGER,
                isbn   TEXT UNIQUE
            )
        """)
        await db.commit()
        
        print(f"Database ready at {DB_PATH}")
        
        # yield — el server esta listo para recibir llamadas
        yield {"db": db}
        
        # teardown: el async with cierra db automaticamente aqui
    
    print("Server shutting down — database connection closed")


mcp = FastMCP("books-server", lifespan=lifespan)


@mcp.tool()
async def search_books(query: str, ctx: Context) -> str:
    """Search books in the database by title or author."""
    # Obtener la conexion del lifespan context
    db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
    
    async with db.execute(
        "SELECT id, title, author, year FROM books "
        "WHERE title LIKE ? OR author LIKE ? LIMIT 20",
        (f"%{query}%", f"%{query}%"),
    ) as cursor:
        rows = await cursor.fetchall()
        return json.dumps([dict(r) for r in rows], ensure_ascii=False)
```

### 3. Lifespan combinado — BD + HTTP client

El patron lifespan es especialmente poderoso cuando combinamos multiples recursos:

```python
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context
import aiosqlite
import httpx
import json
import os

DB_PATH = os.environ.get("DB_PATH", "./data/books.db")


@asynccontextmanager
async def lifespan(server: FastMCP):
    """Setup: abrir DB + HTTP client al mismo tiempo."""
    # Python 3.10+: multiple async context managers con parenthesis
    async with (
        aiosqlite.connect(DB_PATH) as db,
        httpx.AsyncClient(timeout=10.0) as http,
    ):
        db.row_factory = aiosqlite.Row
        await _init_schema(db)
        
        yield {
            "db": db,     # conexion SQLite compartida
            "http": http, # cliente HTTP compartido
        }


async def _init_schema(db: aiosqlite.Connection) -> None:
    """Initialize database tables."""
    await db.executescript("""
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT NOT NULL,
            author TEXT NOT NULL,
            year   INTEGER
        );
        CREATE INDEX IF NOT EXISTS idx_books_title ON books(title);
        CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
    """)
    await db.commit()


mcp = FastMCP("books-weather-server", lifespan=lifespan)


@mcp.tool()
async def search_books(query: str, ctx: Context) -> str:
    """Search books in local database."""
    db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
    async with db.execute(
        "SELECT * FROM books WHERE title LIKE ? LIMIT 10",
        (f"%{query}%",),
    ) as cursor:
        return json.dumps([dict(r) for r in await cursor.fetchall()])


@mcp.tool()
async def get_weather(city: str, ctx: Context) -> str:
    """Get weather for a city via Open-Meteo API."""
    http: httpx.AsyncClient = ctx.request_context.lifespan_context["http"]
    
    # Geocoding
    geo = await http.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
    )
    geo.raise_for_status()
    results = geo.json().get("results", [])
    if not results:
        return json.dumps({"error": f"City not found: {city}"})
    
    loc = results[0]
    
    # Forecast
    weather = await http.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": loc["latitude"],
            "longitude": loc["longitude"],
            "current_weather": "true",
        },
    )
    weather.raise_for_status()
    return json.dumps({
        "city": loc["name"],
        **weather.json()["current_weather"],
    })
```

### 4. Pool de conexiones HTTP con httpx

Para servidores de alto trafico, httpx maneja un pool de conexiones HTTP
automaticamente via `AsyncClient`:

```python
# Cliente con configuracion de pool personalizada
http_client = httpx.AsyncClient(
    timeout=httpx.Timeout(connect=5.0, read=15.0),
    limits=httpx.Limits(
        max_connections=20,       # max conexiones simultaneas
        max_keepalive_connections=10,  # conexiones keep-alive en el pool
        keepalive_expiry=30.0,    # segundos antes de cerrar una idle
    ),
    headers={"User-Agent": "MCP-Server/1.0"},
)
```

Para MCP con `stdio` transport, el server maneja una sola sesion a la vez,
por lo que los valores por defecto de httpx son mas que suficientes.

### 5. Pool con PostgreSQL (asyncpg)

Cuando el proyecto escale a PostgreSQL, el patron lifespan facilita la migracion:

```python
# Con PostgreSQL + asyncpg (misma idea, diferente driver)
import asyncpg

DATABASE_URL = os.environ["DATABASE_URL"]
# Formato: postgresql://user:password@host:5432/database

@asynccontextmanager
async def lifespan(server: FastMCP):
    # asyncpg tiene connection pool nativo
    pool = await asyncpg.create_pool(
        DATABASE_URL,
        min_size=2,   # conexiones minimas activas
        max_size=10,  # conexiones maximas
    )
    yield {"pool": pool}
    await pool.close()

@mcp.tool()
async def search_books_pg(query: str, ctx: Context) -> str:
    pool: asyncpg.Pool = ctx.request_context.lifespan_context["pool"]
    # adquirir conexion del pool automaticamente
    rows = await pool.fetch(
        "SELECT * FROM books WHERE title ILIKE $1 LIMIT 20",
        f"%{query}%",
    )
    return json.dumps([dict(r) for r in rows])
```

**Diferencias SQLite vs PostgreSQL:**
| Aspecto | SQLite (aiosqlite) | PostgreSQL (asyncpg) |
|---------|--------------------|-----------------------|
| Pool | Manual via lifespan | Nativo con `create_pool()` |
| Placeholder | `?` | `$1`, `$2`, ... |
| Conexion | Archivo local | URL de red |
| Concurrencia | Limitada (write lock) | Alta (MVCC) |

### 6. TypeScript — reutilizando la conexion SQLite

`better-sqlite3` es sincrono y la conexion se abre una vez al inicio del modulo.
No hay necesidad de un lifespan explicito:

```typescript
import Database, { Database as DB } from "better-sqlite3";
import * as fs from "fs";
import * as path from "path";
import * as dotenv from "dotenv";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

dotenv.config();

const DB_PATH = process.env.DB_PATH ?? "./data/books.db";

// Crear directorio si no existe
fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });

// Abrir conexion una sola vez — se reutiliza en todos los tools
const db: DB = new Database(DB_PATH);

// Inicializar schema
db.exec(`
  CREATE TABLE IF NOT EXISTS books (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT NOT NULL,
    author TEXT NOT NULL,
    year   INTEGER
  );
  CREATE INDEX IF NOT EXISTS idx_books_title ON books(title);
`);

// Preparar statements una sola vez (mas eficiente)
const searchBooks = db.prepare(
  "SELECT id, title, author, year FROM books WHERE title LIKE ? LIMIT ?"
);
const getBook = db.prepare("SELECT * FROM books WHERE id = ?");
const addBook = db.prepare(
  "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
);
const deleteBook = db.prepare("DELETE FROM books WHERE id = ?");

const server = new Server({ name: "books-server", version: "1.0.0" });

// Los tools usan los prepared statements directamente
server.tool(
  "search_books",
  { query: z.string(), limit: z.number().int().min(1).max(50).default(10) },
  async ({ query, limit }) => {
    const rows = searchBooks.all(`%${query}%`, limit);
    return { content: [{ type: "text", text: JSON.stringify(rows) }] };
  },
);
```

**Prepared statements**: se compilan una vez y se ejecutan multiples veces,
lo que mejora el rendimiento cuando el mismo query se llama frecuentemente.

### 7. Monitoreo de la conexion

Para servidores de larga duracion, es util verificar periodicamente el estado:

```python
@mcp.tool()
async def health_check(ctx: Context) -> str:
    """Check database connection health."""
    try:
        db: aiosqlite.Connection = ctx.request_context.lifespan_context["db"]
        async with db.execute("SELECT 1") as cursor:
            await cursor.fetchone()
        return json.dumps({"status": "healthy", "database": "connected"})
    except Exception as e:
        return json.dumps({"status": "unhealthy", "error": str(e)})
```

## 4. Errores Comunes

### Error: "Cannot use a closed database"
**Causa**: Se intento usar la conexion del lifespan despues de que el server termino.
**Solucion**: No guardar referencias a la conexion fuera del contexto del lifespan.

### Error: aiosqlite.OperationalError en multiples writes concurrentes
**Causa**: SQLite solo permite un writer a la vez por defecto.
**Solucion**: 
```python
await db.execute("PRAGMA journal_mode=WAL")   # Write-Ahead Logging
await db.execute("PRAGMA synchronous=NORMAL")  # balance de rendimiento
```

### Error: La conexion de httpx cierra antes de tiempo
**Causa**: El `async with httpx.AsyncClient()` termino antes de que todos los tools respondieran.
**Solucion**: La conexion debe mantenerse en el lifespan, no crearse dentro del tool.

### Error: "connection pool exhausted" (PostgreSQL)
**Causa**: El pool de asyncpg se lleno y no hay conexiones disponibles.
**Solucion**: Aumentar `max_size` en `create_pool()` o optimizar el tiempo que cada tool retiene la conexion.

## 5. Ejercicios de Comprension

1. ¿Que diferencia hay entre crear un cliente httpx en el lifespan vs dentro de cada tool?
2. ¿Por que `db.row_factory = aiosqlite.Row` facilita el trabajo con los resultados?
3. ¿Que ocurre si no se hace `await db.commit()` despues de un INSERT?
4. ¿Como se migra un server de SQLite a PostgreSQL usando el patron lifespan?
5. ¿Que ventaja tienen los prepared statements en TypeScript con better-sqlite3?

## 📚 Recursos Adicionales

- [aiosqlite GitHub](https://github.com/omnilib/aiosqlite)
- [httpx Connection Pooling](https://www.python-httpx.org/advanced/connection-pooling/)
- [asyncpg Documentation](https://magicstack.github.io/asyncpg/)
- [SQLite WAL Mode](https://www.sqlite.org/wal.html)

## ✅ Checklist de Verificacion

- [ ] La conexion a la BD se abre en el lifespan, no en cada tool
- [ ] `db.row_factory = aiosqlite.Row` esta configurado para acceso por nombre
- [ ] El schema se inicializa con `CREATE TABLE IF NOT EXISTS` en el lifespan
- [ ] Se usa `await db.commit()` despues de todas las operaciones de escritura
- [ ] El lifespan hace `yield` con un dict que incluye todos los recursos
- [ ] Los tools obtienen la conexion desde `ctx.request_context.lifespan_context`
