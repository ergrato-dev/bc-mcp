# Práctica 02 — Tests vitest para el TypeScript MCP Server

## 🎯 Objetivo

Escribir tests de integración para un MCP Server TypeScript usando
`InMemoryTransport` de `@modelcontextprotocol/sdk`.

---

## 🗂️ Estructura

```
practica-02-tests-vitest/
└── starter/
    ├── package.json
    ├── tsconfig.json
    ├── src/
    │   └── server.ts          ← server a testear
    └── tests/
        ├── helpers/
        │   └── test-setup.ts  ← helper reutilizable
        └── server.test.ts     ← tests a descomentar
```

---

## ⚙️ Setup

```bash
cd starter
pnpm install --frozen-lockfile
pnpm test
```

---

## 📝 Pasos

### Paso 1: Helper `setupTestServer`

Abre `tests/helpers/test-setup.ts`. Descomenta la sección **PASO 1**.

```typescript
// setupTestServer crea un par de transports en memoria
// y conecta el server al client.
// Retorna el client y una función cleanup.
```

Verifica que compila sin errores:

```bash
pnpm exec tsc --noEmit
```

---

### Paso 2: Test list_tools

Descomenta la sección **PASO 2** en `tests/server.test.ts`.

```typescript
// Verifica que el server expone las tools esperadas.
```

```bash
pnpm test -- --reporter=verbose
```

---

### Paso 3: Tests de add y get

Descomenta la sección **PASO 3** en `tests/server.test.ts`.

```typescript
// addBook retorna { success: true, id: number }
// getBook recupera el libro recién añadido
```

---

### Paso 4: Tests de search y delete

Descomenta la sección **PASO 4** y ejecuta con cobertura:

```bash
pnpm test -- --coverage
```

---

## ✅ Verificación

```bash
# Todos los tests en verde
pnpm test

# Con cobertura ≥ 70%
pnpm test -- --coverage
```

[← Volver a prácticas](../README.md)
