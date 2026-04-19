# Semana 03 — Los Tres Primitivos: Tools, Resources y Prompts

> **Etapa**: Fundamentos (Semanas 1–3) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Dominar la definición y uso de Tools con schemas JSON
- ✅ Entender los Resources: URIs, tipos MIME y contenido
- ✅ Comprender los Prompts: argumentos y plantillas de mensajes
- ✅ Saber cuándo usar cada primitivo según el caso de uso
- ✅ Diseñar interfaces MCP correctas antes de implementarlas

---

## 📚 Requisitos Previos

- Semana 02 completada
- Familiaridad con JSON Schema
- Conceptos básicos de MCP

---

## 🗂️ Estructura de la Semana

```
week-03-primitivos_tools_resources_prompts/
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

1. Tools: schema de inputs, annotations, execution model
2. Resources: URI scheme, tipos MIME, resource templates
3. Prompts: argumentos, mensajes y role-based content
4. Cuándo usar Tool vs Resource vs Prompt
5. Diseño de interfaces MCP: buenas prácticas

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Definir schemas de tools en JSON (Python y TypeScript)
2. Diseñar URIs de resources para distintos casos de uso
3. Crear plantillas de prompts con argumentos variables
4. Revisar servers MCP de ejemplo y analizar sus primitivos

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

Documento de diseño de interfaz MCP para un sistema real (tools + resources + prompts)

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] Documento de diseño con al menos 5 tools, 3 resources y 2 prompts definidos
- [ ] JSON Schemas de los tools diseñados (validados)
- [ ] Diagrama de los primitivos y sus relaciones

---

## 🔗 Navegación

[← Semana 02](../week-02-json_rpc_y_transports) · [Semana 04 →](../week-04-primer_server_python)
