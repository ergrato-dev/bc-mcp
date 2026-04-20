# Practica 03 — Books SQLite + Weather API con TypeScript

## 🎯 Objetivo

Implementar los mismos tools de las prácticas 01 y 02, pero en TypeScript.
Usar `better-sqlite3` (sincrono) para SQLite y `fetch` nativo de Node.js 22 para HTTP.

## 📋 Que aprenderás

- Diferencias de API entre aiosqlite (async) y better-sqlite3 (sync)
- Usar `fetch` nativo de Node.js 22 con `AbortSignal.timeout()`
- Typed responses con TypeScript interfaces
- Validacion de inputs con Zod

## 🗂️ Estructura

```
practica-03-typescript/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── package.json
├── tsconfig.json
└── src/
    └── index.ts        ← archivo principal (descomentar secciones)
```

## ⚙️ Setup

```bash
cd practica-03-typescript
docker compose up --build
```

## 📝 Instrucciones

### Paso 1 — Observar el servidor base

Abre `src/index.ts`. El server ya inicializa la BD SQLite y tiene el tool `list_books`.
Observa la diferencia con Python: `better-sqlite3` es sincrono — no necesita `await`.

### Paso 2 — Activar tools de SQLite (search, get, add, delete)

Descomenta la seccion `// PASO 2`. Incluye los 4 tools CRUD en un bloque.
Nota como `db.prepare(SQL).all(params)` vs `db.prepare(SQL).get(params)` en Python.

### Paso 3 — Activar get_current_weather

Descomenta la seccion `// PASO 3`.
Observa el uso de `URL().searchParams.set()` para construir URLs con parametros.

### Paso 4 — Activar get_forecast

Descomenta la seccion `// PASO 4`.
Compara este codigo con la version Python — misma logica, diferente sintaxis.

## ✅ Criterios de éxito

- [ ] `list_books` retorna la lista de libros
- [ ] Los 4 tools CRUD funcionan correctamente
- [ ] `get_current_weather` retorna temperatura actual
- [ ] `get_forecast` retorna pronostico de N dias
- [ ] TypeScript compila sin errores (`pnpm build`)
