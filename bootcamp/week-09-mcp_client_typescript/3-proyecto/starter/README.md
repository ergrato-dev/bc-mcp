# Starter — Semana 09: Library CLI TypeScript

## Setup Local (sin Docker)

```bash
cd typescript-client
pnpm install
cp ../.env.example ../.env
pnpm dev
```

## Setup con Docker

```bash
# Desde el directorio starter/
docker compose up --build
```

## Estructura del Starter

```
starter/
├── .env.example              # Variables de entorno
├── docker-compose.yml        # Orquestación Node + Python server
└── typescript-client/
    ├── Dockerfile.node
    ├── package.json
    ├── tsconfig.json
    └── src/
        ├── config.ts         # Validación de env vars
        ├── types.ts          # Interfaces compartidas
        └── client.ts         # ← AQUÍ están los 6 TODOs a implementar
```

## Implementar los TODOs

Abre `typescript-client/src/client.ts` e implementa cada TODO en orden:

1. `connectToServer()` — crear `StdioClientTransport` y `Client`, retornar conectado
2. `listAvailableTools()` — listar nombres y descripciones de tools
3. `searchBooks()` — `callTool("search_books")` → `Book[]`
4. `addBook()` — `callTool("add_book")` → `Book | null`
5. `searchOpenLibrary()` — `callTool("search_openlibrary")` → `OpenLibraryResult[]`
6. `interactiveLoop()` — bucle readline con dispatch de comandos

## Referencia

Ver teoría en [`../../1-teoria/`](../../1-teoria/README.md) y
prácticas en [`../../2-practicas/`](../../2-practicas/README.md).


---

[← Volver al proyecto](../README.md)
