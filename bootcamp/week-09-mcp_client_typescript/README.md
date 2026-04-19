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

1. Crear un client TypeScript que se conecte al server de semana 07
2. Listar tools con client.listTools()
3. Invocar tools con client.callTool() y tipar resultados
4. Listar y leer resources con client.listResources()
5. Construir un CLI TypeScript equivalente al de semana 08

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

MCP Client TypeScript con CLI que se conecta al server de semana 07

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] MCP Client TypeScript funcional con conexión a server stdio
- [ ] CLI TypeScript que permite invocar cualquier tool del server
- [ ] Tests del client con InMemoryTransport
- [ ] README con comparativa Python vs TypeScript client

---

## 🔗 Navegación

[← Semana 08](../week-08-mcp_client_python) · [Semana 10 →](../week-10-integracion_claude_openai)
