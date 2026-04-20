# Practica 04 — Manejo de Errores en MCP Servers

## 🎯 Objetivo

Comparar y aplicar los dos enfoques principales de manejo de errores en MCP:
`isError: true` para errores de dominio y `McpError` para errores del protocolo.

## 📋 Que aprenderás

- Diferencia entre `McpError` (protocolo) e `isError: true` (dominio)
- Patron retry con backoff exponencial para APIs externas
- Manejo de errores de BD: `IntegrityError`, `OperationalError`
- Errores tipados en TypeScript con `instanceof`

## 🗂️ Estructura

```
practica-04-error-handling/
├── README.md
├── docker-compose.yml
├── python-server/
│   ├── Dockerfile.python
│   ├── pyproject.toml
│   └── src/server.py
└── ts-server/
    ├── Dockerfile.node
    ├── package.json
    ├── tsconfig.json
    └── src/index.ts
```

## ⚙️ Setup

```bash
cd practica-04-error-handling

# Solo Python
docker compose up python-server --build

# Solo TypeScript
docker compose up ts-server --build
```

## 📝 Instrucciones

### Python — src/python-server/server.py

El server base ya tiene un tool `divide` que muestra error de dominio.

**Paso 1**: Descomenta `safe_fetch` — funcion helper con retry.
**Paso 2**: Descomenta `get_book_safe` — errores de BD correctamente manejados.
**Paso 3**: Descomenta `fetch_with_retry` — retry con backoff exponencial.

### TypeScript — ts-server/src/index.ts

**Paso 1**: Descomenta el bloque de `get_book_typed` — errores con `isError: true`.
**Paso 2**: Descomenta `fetch_with_retry_ts` — retry en TypeScript.

## ✅ Criterios de éxito

- [ ] `divide(10, 0)` retorna error de dominio (no crash del server)
- [ ] `get_book_safe` retorna `isError: true` cuando el libro no existe
- [ ] El retry reintenta ante errores 5xx, no ante errores 4xx
- [ ] Los errores tienen mensajes descriptivos orientados al LLM
