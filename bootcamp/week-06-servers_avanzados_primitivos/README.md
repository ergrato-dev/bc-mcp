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

1. Implementación de Resources: list y read handlers
2. Resource templates: URIs con variables {param}
3. Implementación de Prompts: list y get handlers
4. Combinación de los 3 primitivos en un server completo
5. Gestión de contexto en tools (ctx: Context)

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Agregar resources a un server Python existente
2. Agregar resources al server TypeScript
3. Implementar prompts con argumentos en ambos lenguajes
4. Crear un server completo con los 3 primitivos

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

MCP Server (Python y TypeScript) con tools + resources + prompts sobre un dominio real

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
