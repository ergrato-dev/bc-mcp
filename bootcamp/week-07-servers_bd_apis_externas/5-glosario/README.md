# Glosario — Semana 07: Servers con BD y APIs Externas

Términos clave de esta semana, ordenados alfabéticamente.

---

### aiosqlite

Librería Python que envuelve `sqlite3` para uso asíncrono con `async/await`. Permite operar con bases de datos SQLite sin bloquear el event loop.

```python
async with aiosqlite.connect("db.sqlite") as db:
    rows = await db.execute("SELECT * FROM books")
```

### asyncpg

Driver PostgreSQL nativo para Python async, más rápido que psycopg2 en cargas de trabajo IO-intensivas. Usa `$1, $2` en lugar de `?` para parámetros.

### better-sqlite3

Driver SQLite **síncrono** para Node.js/TypeScript. Más sencillo de usar que alternativas async. No requiere `await` porque las operaciones son bloqueantes.

```typescript
const rows = db.prepare("SELECT * FROM books").all();
```

### AUTOINCREMENT

Modificador de SQLite para columnas `INTEGER PRIMARY KEY` que garantiza que los IDs nunca se reutilizan, incluso después de eliminar filas.

### Connection pool

Conjunto de conexiones reutilizables a una base de datos que se mantienen abiertas para evitar el costo de crear nuevas conexiones en cada request.

### cursor

Objeto devuelto por `execute()` en aiosqlite que contiene el resultado de la query. Expone `fetchone()`, `fetchall()`, `lastrowid` y `rowcount`.

### dotenv / python-dotenv

Librerías que cargan variables de entorno desde un archivo `.env` al proceso. Permiten separar configuración del código fuente.

### env_file

Directiva en `docker-compose.yml` que indica qué archivo `.env` cargar para el servicio. Evita hardcodear credenciales en el compose.

```yaml
env_file:
  - .env
```

### exponential backoff

Estrategia de reintentos que espera un tiempo creciente entre intentos: 0.5s, 1s, 2s, 4s... Reduce la presión sobre servicios externos con problemas temporales.

### httpx

Cliente HTTP moderno para Python con soporte nativo para `async/await`. Alternativa a `requests` para entornos asíncronos.

### isError

Campo booleano en las respuestas de tools MCP que indica que el contenido es un mensaje de error manejado (dominio), no una excepción del protocolo.

```python
return {"content": [{"type": "text", "text": "Not found"}], "isError": True}
```

### lifespan

Patrón de FastMCP (y otros frameworks) para ejecutar código de inicialización y limpieza al arrancar y detener el servidor. Ideal para abrir/cerrar conexiones de BD y clientes HTTP.

### McpError

Excepción base del SDK MCP para errores del **protocolo** (ej: tool no encontrado, parámetros inválidos según el schema). Distinto de errores de dominio (`isError: true`).

### Open-Meteo

API meteorológica pública, gratuita y sin API key. Proporciona pronóstico del tiempo, datos históricos y geocoding.
- Geocoding: `https://geocoding-api.open-meteo.com/v1/search`
- Forecast: `https://api.open-meteo.com/v1/forecast`

### Open Library

API pública de Internet Archive para búsqueda de libros. Gratuita, sin API key, sin rate limit agresivo.
- Endpoint de búsqueda: `https://openlibrary.org/search.json?title=...`

### parametrized query

Query SQL que usa placeholders (`?` en SQLite Python, `$1` en asyncpg) en lugar de concatenar strings directamente. Previene SQL injection.

```python
# ✅ Correcto
await db.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{query}%",))

# ❌ Inseguro
await db.execute(f"SELECT * FROM books WHERE title LIKE '%{query}%'")
```

### raise_for_status()

Método de `httpx.Response` que lanza `HTTPStatusError` si el status HTTP es 4xx o 5xx. Equivalente a `response.raise_for_status()` en requests.

### Row factory

Configuración de aiosqlite/sqlite3 que hace que los resultados sean accesibles como objetos tipo diccionario (`row["column"]`) en lugar de tuplas (`row[0]`).

```python
db.row_factory = aiosqlite.Row
```

### SQL injection

Vulnerabilidad de seguridad que ocurre cuando se concatenan inputs de usuario directamente en queries SQL, permitiendo ejecutar queries arbitrarias.

### timeout (httpx)

Configuración que limita el tiempo máximo de espera para operaciones HTTP. httpx permite configurar timeout de conexión y lectura por separado.

```python
httpx.AsyncClient(timeout=httpx.Timeout(connect=5.0, read=15.0))
```

### WAL (Write-Ahead Log)

Modo de journaling de SQLite que permite lecturas concurrentes mientras se escribe. Recomendado para producción con múltiples accesos simultáneos.

```python
await db.execute("PRAGMA journal_mode=WAL")

### asyncpg

Driver async de PostgreSQL para Python

### dotenv

Herramienta para cargar variables de entorno desde un archivo .env

### httpx

Cliente HTTP async para Python (reemplaza requests en código async)

---

[← Volver al README de la semana](../README.md)
