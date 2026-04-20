# Práctica 03 — Invocar Tools y Leer Resources

## 🎯 Objetivo

Usar `callTool()` para ejecutar tools del servidor de semana 07, procesar resultados JSON
tipados, detectar `isError` y leer un resource con `readResource()`.

## 📋 Prerequisitos

- Práctica 02 completada

## 🛠️ Setup

```bash
cd starter
pnpm install
cp .env.example .env
```

---

## Paso a Paso

### Paso 1: Conectar y definir tipos

Descomenta la sección **PASO 1**. Además del setup de conexión, se define la interfaz
`Book` que modela los datos que devuelven los tools del servidor:

```typescript
interface Book {
  id: number;
  title: string;
  author: string;
  year: number;
  isbn?: string | null;
}
```

Los tipos del dominio hacen el código más seguro y legible.

### Paso 2: Buscar libros con `search_books`

Descomenta la sección **PASO 2**. El tool `search_books` retorna JSON serializado en
`result.content[0].text`. El flujo es:

```typescript
const result = await client.callTool({ name: "search_books", arguments: { query } });
// → verificar isError
// → result.content[0].type === "text"
// → JSON.parse(result.content[0].text) as Book[]
```

### Paso 3: Detectar y manejar `isError`

Descomenta la sección **PASO 3**. Cuando `isError` es `true`, el contenido del tool
es un mensaje de error (no datos). En TypeScript, para acceder a `.text` debes discriminar
por `item.type === "text"` o hacer un type cast:

```typescript
if (result.isError) {
  const first = result.content[0];
  const msg = first?.type === "text" ? first.text : "Error sin detalle";
  console.error(`Error del servidor: ${msg}`);
}
```

### Paso 4: Agregar un libro con `add_book`

Descomenta la sección **PASO 4**. El tool `add_book` crea un libro y retorna el libro
creado con su `id` asignado por la base de datos:

```typescript
const result = await client.callTool({
  name: "add_book",
  arguments: { title, author, year, isbn },
});
// → JSON.parse → Book con id asignado
```

### Paso 5: Leer resource con `readResource`

Descomenta la sección **PASO 5**. El resource `db://books/stats` retorna estadísticas
de la biblioteca. `readResource()` retorna `ReadResourceResult`:

```typescript
const result = await client.readResource({ uri: "db://books/stats" });
// result.contents[0].text → JSON con { total_books, books_with_isbn, average_year }
```

---

## ▶️ Ejecutar

```bash
pnpm dev
```

## ✅ Salida Esperada

```
🔌 Conectado: library-manager v1.0.0

🔍 Buscando "TypeScript"...
  Encontrados: 2 libros
  1. Programming TypeScript (Boris Cherny, 2019)
  2. TypeScript Deep Dive (Basarat Ali Syed, 2018)

➕ Agregando "Clean Code"...
  ✅ Creado con id=5

❌ Prueba de isError (id=9999)...
  Error del servidor: Book with id 9999 not found

📊 Estadísticas:
  Total libros:     5
  Con ISBN:         3
  Año promedio:     2017
```

---

[← Volver a Prácticas](../README.md)
