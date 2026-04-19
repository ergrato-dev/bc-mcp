# Semana 02 — JSON-RPC 2.0 y Transports

> **Etapa**: Fundamentos (Semanas 1–3) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Entender la estructura de mensajes JSON-RPC 2.0
- ✅ Diferenciar requests, responses y notifications en MCP
- ✅ Comprender el ciclo de vida de una sesión MCP
- ✅ Conocer los transports disponibles: stdio, HTTP/SSE
- ✅ Inspeccionar mensajes MCP reales con herramientas de debug

---

## 📚 Requisitos Previos

- Semana 01 completada
- Conocimiento básico de JSON
- Docker funcionando

---

## 🗂️ Estructura de la Semana

```
week-02-json_rpc_y_transports/
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

1. JSON-RPC 2.0: estructura de mensajes
2. Requests, responses, notifications y batches
3. Ciclo de vida de una sesión MCP: initialize → use → shutdown
4. Transport stdio: comunicación por stdin/stdout
5. Transport HTTP/SSE: Server-Sent Events para streaming

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Enviar mensajes JSON-RPC manualmente vía stdin
2. Inspeccionar el handshake MCP con logs detallados
3. Comparar stdio vs HTTP/SSE en ejemplos reales
4. Implementar un echo server minimal con JSON-RPC

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

Analizador de mensajes MCP que parsea y muestra el ciclo de vida de una sesión

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] Script que captura y analiza mensajes JSON-RPC de una sesión MCP real
- [ ] Diagrama del ciclo de vida de sesión MCP (initialize / method calls / shutdown)
- [ ] Comparativa documentada: stdio vs HTTP/SSE

---

## 🔗 Navegación

[← Semana 01](../week-01-introduccion_mcp) · [Semana 03 →](../week-03-primitivos_tools_resources_prompts)
