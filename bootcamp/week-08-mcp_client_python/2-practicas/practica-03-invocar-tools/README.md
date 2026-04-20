# Práctica 03 — Invocar Tools y Procesar Resultados

## 🎯 Objetivo

Llamar a `call_tool()`, procesar `TextContent` con JSON, manejar `isError`,
y leer un resource con `read_resource()`.

## 📋 Requisitos previos

- Práctica 02 completada

## 🗂️ Estructura

```
practica-03-invocar-tools/
├── README.md
└── starter/
    ├── pyproject.toml
    └── client.py
```

---

## Pasos

### Paso 1: PASO 1 — Conectar al server

Igual que las prácticas anteriores. Descomenta la sección `PASO 1`.

### Paso 2: PASO 2 — Buscar libros (call_tool + JSON)

Descomenta la sección `PASO 2`.

`call_tool()` devuelve un `CallToolResult`. El resultado más común es
`TextContent` con un JSON string:

```python
# Ejemplo explicativo
result = await session.call_tool("search_books", {"query": "Python"})
if not result.isError:
    books = json.loads(result.content[0].text)
    for book in books:
        print(f"  [{book['id']}] {book['title']} — {book['author']}")
```

### Paso 3: PASO 3 — Manejar isError

Descomenta la sección `PASO 3`.

Cuando un tool no puede completar su tarea (libro no existe, ID inválido, etc.)
retorna `isError=True`. El mensaje de error está en `result.content[0].text`.

**Importante**: `isError=True` NO es una excepción Python. El flujo continúa.

```python
# Ejemplo explicativo
result = await session.call_tool("get_book", {"book_id": 9999})
if result.isError:
    print(f"Error esperado: {result.content[0].text}")
```

### Paso 4: PASO 4 — Agregar un libro

Descomenta la sección `PASO 4`.

`add_book` devuelve el libro recién creado con su ID asignado por la DB.

### Paso 5: PASO 5 — Leer un resource

Descomenta la sección `PASO 5`.

`read_resource(uri)` retorna `ReadResourceResult` con una lista de
`TextResourceContents` o `BlobResourceContents`.

```python
# Ejemplo explicativo
content = await session.read_resource("db://books/stats")
print(content.contents[0].text)
```

### Paso 6: Ejecutar

```bash
uv run python client.py
```

Salida esperada:
```
=== PASO 2: Buscar libros ===
Buscando: "async"
  [3] Python Asyncio Jump-Start — Matthew MacDougall (2022)
  [7] Using Asyncio in Python — Caleb Hattingh (2020)

=== PASO 3: Manejo de isError ===
Buscando libro con ID=9999...
✓ Error manejado: Book with id=9999 not found

=== PASO 4: Agregar libro ===
Libro agregado: ID=8, Clean Code — Robert C. Martin (2008)

=== PASO 5: Leer resource ===
{"total_books": 8, "books_with_isbn": 4, "avg_year": 2016}
```

## ✅ Criterio de éxito

- Deserializa correctamente el JSON de `TextContent`
- Detecta y muestra el mensaje de `isError=True` sin crashes
- Agrega un libro y muestra el ID generado
- Lee y muestra el contenido del resource `db://books/stats`

---

[← Práctica 02](../practica-02-descubrir-capacidades/) | [Práctica 04 →](../practica-04-cli-interactivo/)
