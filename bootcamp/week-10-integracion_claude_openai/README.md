# Semana 10 — Integración con Claude y OpenAI

> **Etapa**: MCP Clients + LLMs (Semanas 8–10) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Integrar un MCP Client con la API de Claude (Anthropic)
- ✅ Integrar un MCP Client con la API de OpenAI (function calling)
- ✅ Implementar el agentic loop completo: planning → tool call → result → synthesis
- ✅ Orquestar múltiples MCP Servers desde un solo client
- ✅ Construir un agente funcional que use LLM + MCP tools

---

## 📚 Requisitos Previos

- Semana 09 completada
- API keys de Anthropic y/o OpenAI
- MCP Client en Python y TypeScript dominado

---

## 🗂️ Estructura de la Semana

```
week-10-integracion_claude_openai/
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

1. Agentic loop: cómo un LLM decide qué tool usar
2. Anthropic API: tool_use, tool_result y conversación multi-turn
3. OpenAI API: function_calling y messages con tool results
4. Conversión de MCP tool schemas a formatos de LLM
5. Orquestación multi-server: conectar N servers desde 1 client

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Conectar Claude a un MCP Server y ejecutar tool calls
2. Implementar el loop completo con Anthropic SDK
3. Replicar con OpenAI SDK (function calling)
4. Orquestar 2 servers desde un agente Claude

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

Agente LLM (Claude o OpenAI) que usa MCP tools del server de semana 07

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] Agente Python con Claude + MCP Server funcionando
- [ ] Agente TypeScript equivalente
- [ ] Demo del agentic loop con 3+ tool calls encadenados
- [ ] .env.example con API keys necesarias (sin valores reales)

---

## 🔗 Navegación

[← Semana 09](../week-09-mcp_client_typescript) · [Semana 11 →](../week-11-testing_seguridad_docker)
