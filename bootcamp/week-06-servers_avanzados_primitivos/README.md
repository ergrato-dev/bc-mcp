# Semana 06 — Servers Avanzados — Los 3 Primitivos

> **Etapa**: MCP Servers (Semanas 4–7) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Implementar Resources con URIs y listado dinámico
- ✅ Crear Prompts con argumentos y plantillas de mensajes
- ✅ Combinar Tools + Resources + Prompts en un solo server
- ✅ Gestionar contexto y estado dentro del server
- ✅ Implementar resource templates con URIs variables

---

## 📚 Requisitos Previos

- Semana 05 completada
- MCP Server funcional en Python y TypeScript

---

## 🗂️ Estructura de la Semana

```
week-06-servers_avanzados_primitivos/
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

1. [Resources: list y read handlers](1-teoria/01-resources-list-y-read.md)
2. [Resource templates: URIs con variables {param}](1-teoria/02-resource-templates-uris-variables.md)
3. [Prompts: list y get handlers con argumentos](1-teoria/03-prompts-argumentos-y-plantillas.md)
4. [Combinando los 3 primitivos en un server](1-teoria/04-combinando-los-tres-primitivos.md)
5. [Context object y gestión de estado](1-teoria/05-context-y-estado-en-mcp.md)

### 💻 Prácticas ([2-practicas/](2-practicas/))

1. [practica-01](2-practicas/practica-01-resources-python/) — Resources en Python (FastMCP)
2. [practica-02](2-practicas/practica-02-resources-typescript/) — Resources en TypeScript
3. [practica-03](2-practicas/practica-03-prompts-ambos/) — Prompts en Python y TypeScript
4. [practica-04](2-practicas/practica-04-server-completo/) — Server completo con los 3 primitivos

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

Task Manager MCP con Tools + Resources + Prompts en Python y TypeScript

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] MCP Server Python con 3 tools, 2 resources y 1 prompt
- [ ] MCP Server TypeScript con los mismos primitivos
- [ ] Tests básicos verificando que los 3 primitivos responden
- [ ] README con descripción de cada primitivo expuesto

---

## 🔗 Navegación

[← Semana 05](../week-05-primer_server_typescript) · [Semana 07 →](../week-07-servers_bd_apis_externas)
