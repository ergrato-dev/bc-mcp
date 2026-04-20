# Práctica 04 — CLI Interactivo con readline

## 🎯 Objetivo

Construir un CLI interactivo en TypeScript que use `readline` de Node.js para leer
comandos del usuario y ejecutarlos sobre el servidor MCP de semana 07. Equivalente
TypeScript del CLI de semana 08.

## 📋 Prerequisitos

- Práctica 03 completada

## 🛠️ Setup

```bash
cd starter
pnpm install
cp .env.example .env
```

---

## Paso a Paso

### Paso 1: Conectar y configurar readline

Descomenta la sección **PASO 1**. Se usa `node:readline/promises` (API nativa de Node.js
22, no requiere paquete adicional) para leer líneas de forma asíncrona:

```typescript
import { createInterface } from "node:readline/promises";

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});
```

> **Nota**: A diferencia del SDK Python donde se usa `run_in_executor` para evitar
> bloquear el event loop, en Node.js `readline/promises` es nativo y ya es async.

### Paso 2: Función `printHelp`

Descomenta la sección **PASO 2**. La función muestra los comandos disponibles:
`search`, `add`, `openlibrary`, `tools`, `stats`, `quit`.

### Paso 3: Bucle de lectura de comandos

Descomenta la sección **PASO 3**. El bucle principal lee una línea con `rl.question()`,
parsea el comando y el primer argumento:

```typescript
while (true) {
  const line = await rl.question(">> ");
  const [command, ...rest] = line.trim().split(/\s+/);
  const arg = rest.join(" ");
  // ...dispatch
}
```

### Paso 4: Despachar `search` y `tools`

Descomenta la sección **PASO 4**:
- `search <query>` → llama al tool `search_books`
- `tools` → llama a `client.listTools()` y lista los nombres

### Paso 5: Despachar `stats` y `quit`

Descomenta la sección **PASO 5**:
- `stats` → lee resource `db://books/stats`
- `quit` → rompe el bucle con `break`
- Comandos desconocidos → imprimir mensaje de ayuda

---

## ▶️ Ejecutar

```bash
pnpm dev
```

## ✅ Interacción Esperada

```
╔══════════════════════════════════════╗
║  Library CLI — MCP Client TypeScript ║
╚══════════════════════════════════════╝
✅ Conectado: library-manager v1.0.0

Comandos: search <query> | add | tools | stats | quit

>> search python
  1. Learning Python (Mark Lutz, 2013)
  2. Python Crash Course (Eric Matthes, 2019)

>> stats
  Total libros: 4 | Con ISBN: 2 | Año promedio: 2016

>> quit
  👋 ¡Hasta luego!
```

---

[← Volver a Prácticas](../README.md)
