# Semana 08 — MCP Client en Python

> **Etapa**: MCP Clients + LLMs (Semanas 8–10) · **Dedicación**: 8 horas · **Lenguajes**: Python

---

## 🎯 Objetivos de Aprendizaje

- ✅ Construir un MCP Client en Python usando el SDK oficial
- ✅ Conectarse a un MCP Server via stdio
- ✅ Listar y descubrir tools, resources y prompts disponibles
- ✅ Invocar tools y procesar sus resultados
- ✅ Manejar errores del client correctamente

---

## 📚 Requisitos Previos

- Semana 07 completada
- MCP Server funcionando (semana 07)
- Python async/await dominado

---

## 🗂️ Estructura de la Semana

```
week-08-mcp_client_python/
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

1. Arquitectura del MCP Client en Python
2. ClientSession y StdioServerParameters
3. Flujo: connect → initialize → discover → call → disconnect
4. Procesamiento de resultados: TextContent, ImageContent
5. Manejo de errores en el client

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. [Primer client](2-practicas/practica-01-primer-client/) — Conectar al server de semana 07 e imprimir serverInfo
2. [Descubrir capacidades](2-practicas/practica-02-descubrir-capacidades/) — list_tools, list_resources, list_prompts con schema completo
3. [Invocar tools](2-practicas/practica-03-invocar-tools/) — call_tool, TextContent JSON, isError, read_resource
4. [CLI interactivo](2-practicas/practica-04-cli-interactivo/) — Sesión única, bucle run_in_executor, comandos search/stats/quit

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

**Library CLI** — MCP Client Python con CLI interactivo que se conecta al Library Manager
MCP Server de la semana 07. Permite buscar libros, agregar títulos, consultar la API de
Open Library y ver estadísticas, todo desde una sesión MCP única.

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | 5 archivos: arquitectura, ClientSession, flujo, content types, errores |
| Prácticas | 3–3.5h | 4 ejercicios guiados (descomentar código, verificar output) |
| Proyecto | 2–2.5h | Library CLI — 6 TODOs en `src/client.py` |

---

## 📌 Entregables

- [ ] `connect_to_server()` implementado con StdioServerParameters + ClientSession
- [ ] `list_available_tools()` lista tools con nombre y descripción
- [ ] `search_books()` llama al tool y deserializa TextContent JSON
- [ ] `add_book()` agrega libro y verifica isError
- [ ] `search_openlibrary()` consulta API externa via tool
- [ ] `interactive_loop()` CLI con search, add, openlibrary, tools, stats, quit

---

## 🔗 Navegación

[← Semana 07](../week-07-servers_bd_apis_externas) · [Semana 09 →](../week-09-mcp_client_typescript)
