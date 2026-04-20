# Proyecto — Semana 09: Library CLI TypeScript

## 🎯 Descripción

Construir un **CLI TypeScript** completo que se conecta al servidor Library Manager de
semana 07 (Python + SQLite + Open Library API) y permite gestionar la biblioteca desde
la terminal. Es el equivalente TypeScript del proyecto de semana 08.

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/README.md) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/README.md) como preparación
3. Trabaja en `starter/typescript-client/src/` — implementa los 6 TODOs en orden
4. Usa Docker (`docker compose up --build`) o ejecución local (`pnpm dev`)
5. Verifica que todos los entregables estén completos antes de la entrega

## 📌 Entregables

- [ ] **TODO 1** — `connectToServer()`: `StdioClientTransport` + `Client` + `connect()`
- [ ] **TODO 2** — `listAvailableTools()`: lista tools con nombre y descripción
- [ ] **TODO 3** — `searchBooks()`: `callTool` + `isError` + `JSON.parse` → `Book[]`
- [ ] **TODO 4** — `addBook()`: `callTool` + `isError` + JSON → `Book | null`
- [ ] **TODO 5** — `searchOpenLibrary()`: `callTool` → lista de resultados externos
- [ ] **TODO 6** — `interactiveLoop()`: readline + dispatch de comandos (search/add/stats/quit)

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md
└── starter/
    ├── README.md                     # Instrucciones de setup local y Docker
    ├── .env.example                  # Variables de entorno
    ├── docker-compose.yml            # Orquestación de servicios
    └── typescript-client/
        ├── Dockerfile.node           # Imagen Docker Node.js 22
        ├── package.json              # @modelcontextprotocol/sdk, dotenv, zod
        ├── tsconfig.json
        └── src/
            ├── config.ts             # Variables de entorno con validación
            ├── types.ts              # Interfaces Book, BookStats, OpenLibraryResult
            └── client.ts             # Punto de entrada — 6 TODOs a implementar
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
