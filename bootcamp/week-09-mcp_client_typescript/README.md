# Semana 09 — MCP Client en TypeScript

> **Etapa**: MCP Clients + LLMs (Semanas 8–10) · **Dedicación**: 8 horas · **Lenguajes**: TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Construir un MCP Client en TypeScript usando el SDK oficial
- ✅ Conectarse a un MCP Server via stdio desde Node.js
- ✅ Listar y descubrir tools, resources y prompts
- ✅ Invocar tools y tipar correctamente sus resultados
- ✅ Comparar la experiencia de cliente en Python vs TypeScript

---

## 📚 Requisitos Previos

- Semana 08 completada
- MCP Client Python dominado
- TypeScript async/await dominado

---

## 🗂️ Estructura de la Semana

```
week-09-mcp_client_typescript/
├── README.md                 # Este archivo
├── rubrica-evaluacion.md     # Criterios de evaluación
├── 0-assets/                 # Diagramas SVG
├── 1-teoria/                 # Material teórico
│   └── README.md
├── 2-practicas/              # Ejercicios guiados
│   └── README.md
├── 3-proyecto/               # Proyecto semanal
│   ├── README.md
│   └── starter/
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### 📖 Teoría ([1-teoria/](1-teoria/README.md))

1. Client class del SDK TypeScript de MCP
2. StdioClientTransport: configuración y conexión
3. Tipado de resultados con interfaces TypeScript
4. Manejo de errores y timeouts en el client TS
5. Comparativa Python SDK vs TypeScript SDK

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. [practica-01-primer-client](2-practicas/practica-01-primer-client/) — Conectar e imprimir metadatos del servidor
2. [practica-02-descubrir-capacidades](2-practicas/practica-02-descubrir-capacidades/) — `listTools()`, `listResources()`, `listPrompts()`
3. [practica-03-invocar-tools](2-practicas/practica-03-invocar-tools/) — `callTool()`, `isError`, `readResource()` tipado
4. [practica-04-cli-interactivo](2-practicas/practica-04-cli-interactivo/) — CLI interactivo con `node:readline/promises`

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

**Library CLI TypeScript** — CLI TypeScript completo con 6 TODOs que replica el proyecto de semana 08 en TypeScript: `connectToServer()`, `listAvailableTools()`, `searchBooks()`, `addBook()`, `searchOpenLibrary()`, `interactiveLoop()`.

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] **TODO 1** — `connectToServer()`: `StdioClientTransport` + `Client` + `connect()`
- [ ] **TODO 2** — `listAvailableTools()`: lista tools con nombre y descripción
- [ ] **TODO 3** — `searchBooks()`: `callTool` + `isError` + `JSON.parse` → `Book[]`
- [ ] **TODO 4** — `addBook()`: `callTool` + `isError` + JSON → `Book | null`
- [ ] **TODO 5** — `searchOpenLibrary()`: `callTool` → `OpenLibraryResult[]`
- [ ] **TODO 6** — `interactiveLoop()`: readline + dispatch de comandos (search/add/ol/stats/quit)

---

## 🔗 Navegación

[← Semana 08](../week-08-mcp_client_python) · [Semana 10 →](../week-10-integracion_claude_openai)
