# Semana 05 — Primer MCP Server en TypeScript

> **Etapa**: MCP Servers (Semanas 4–7) · **Dedicación**: 8 horas · **Lenguajes**: TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Crear un MCP Server funcional con el SDK TypeScript de MCP
- ✅ Implementar tools con server.tool() y validación Zod
- ✅ Gestionar el proyecto con pnpm y package.json
- ✅ Compilar y ejecutar el server con Node.js 22+
- ✅ Probar el server con MCP Inspector

---

## 📚 Requisitos Previos

- Semana 04 completada
- Node.js 22+ (vía Docker)
- pnpm instalado en contenedor
- TypeScript básico

---

## 🗂️ Estructura de la Semana

```
week-05-primer_server_typescript/
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

1. McpServer: la clase principal del SDK TypeScript de MCP
2. server.tool(): registro de tools con nombre y schema Zod
3. Validación de inputs con Zod — schemas type-safe
4. package.json, tsconfig.json y compilación con tsc
5. ESM modules y top-level await en Node.js 22+

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Crear un server con McpServer y un tool básico (add)
2. Definir schemas de tools con z.object() y tipos Zod
3. Configurar pnpm, package.json y tsconfig.json
4. Compilar con tsc y ejecutar con Node.js
5. Conectar MCP Inspector al server TypeScript

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

MCP Server TypeScript con mínimo 3 tools (equivalentes a los de semana 04)

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] MCP Server TypeScript funcional con 3+ tools
- [ ] package.json con dependencias exactas (sin ^)
- [ ] tsconfig.json correctamente configurado
- [ ] README con instrucciones de ejecución con Docker

---

## 🔗 Navegación

[← Semana 04](../week-04-primer_server_python) · [Semana 06 →](../week-06-servers_avanzados_primitivos)
