# Práctica 02 — Descubrir Capacidades del Servidor

## 🎯 Objetivo

Usar `listTools()`, `listResources()` y `listPrompts()` para explorar todo lo que expone
el servidor MCP de semana 07. Entender los tipos TypeScript de cada resultado.

## 📋 Prerequisitos

- Práctica 01 completada

## 🛠️ Setup

```bash
cd starter
pnpm install
cp .env.example .env
# Ajustar SERVER_PATH en .env
```

---

## Paso a Paso

### Paso 1: Conectar al servidor

Descomenta la sección **PASO 1** en `starter/src/client.ts`. Es el mismo patrón de la
práctica anterior: `StdioClientTransport` + `Client` + `connect()`.

### Paso 2: Listar tools con schema

Descomenta la sección **PASO 2**. Itera sobre `result.tools` mostrando nombre,
descripción y parámetros requeridos:

```typescript
const result = await client.listTools();
for (const tool of result.tools) {
  const required = tool.inputSchema.required ?? [];
  const props = Object.keys(tool.inputSchema.properties ?? {});
  // ...
}
```

El tipo de `result` es `ListToolsResult` y `result.tools` es `Tool[]`.

### Paso 3: Listar resources

Descomenta la sección **PASO 3**. Cada resource tiene `uri`, `name`, `description` y
`mimeType`. El servidor de semana 07 expone al menos `db://books/stats`:

```typescript
const resources = await client.listResources();
for (const res of resources.resources) {
  console.log(`  URI:  ${res.uri}`);
}
```

### Paso 4: Listar prompts

Descomenta la sección **PASO 4**. Cada prompt tiene `name`, `description` y `arguments[]`
donde cada argumento tiene `name`, `description` y `required`:

```typescript
const prompts = await client.listPrompts();
for (const p of prompts.prompts) {
  const args = p.arguments ?? [];
  // ...
}
```

---

## ▶️ Ejecutar

```bash
pnpm dev
```

## ✅ Salida Esperada

```
🔌 Conectando...
✅ Conectado: library-manager v1.0.0

📦 Tools (7):
  • search_books        — Busca libros por texto
    Params: query* (requerido)
  • add_book            — Agrega un libro nuevo
    Params: title*, author*, year*, isbn
  [...]

📂 Resources (1):
  • db://books/stats    (application/json)
    Estadísticas de la base de datos de libros

💬 Prompts (0):
  (ninguno)
```

---

[← Volver a Prácticas](../README.md)
