# Semana 04 — Primer MCP Server en Python

> **Etapa**: MCP Servers (Semanas 4–7) · **Dedicación**: 8 horas · **Lenguajes**: Python

---

## 🎯 Objetivos de Aprendizaje

- ✅ Crear un MCP Server funcional con FastMCP en Python
- ✅ Implementar tools con el decorador @mcp.tool()
- ✅ Gestionar el proyecto Python con uv y pyproject.toml
- ✅ Ejecutar el server con stdio transport
- ✅ Probar el server con MCP Inspector

---

## 📚 Requisitos Previos

- Semana 03 completada
- Python 3.13+ (vía Docker)
- uv instalado en contenedor

---

## 🗂️ Estructura de la Semana

```
week-04-primer_server_python/
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

1. FastMCP: el SDK de Python para MCP
2. Decorador @mcp.tool(): schema automático con type hints
3. Ciclo de vida del server: startup, handling, shutdown
4. pyproject.toml y gestión de dependencias con uv
5. Debugging de servers Python con logging

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Crear un server con FastMCP y un tool básico (add)
2. Agregar type hints y docstrings como schema automático
3. Gestionar el proyecto con uv sync y pyproject.toml
4. Conectar MCP Inspector al server stdio
5. Agregar múltiples tools con distintos tipos de parámetros

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

MCP Server Python con mínimo 3 tools útiles (matemáticas, texto, fecha/hora)

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] MCP Server Python funcional con 3+ tools
- [ ] pyproject.toml con dependencias exactas
- [ ] README con instrucciones de ejecución con Docker
- [ ] Captura de MCP Inspector mostrando los tools

---

## 🔗 Navegación

[← Semana 03](../week-03-primitivos_tools_resources_prompts) · [Semana 05 →](../week-05-primer_server_typescript)
