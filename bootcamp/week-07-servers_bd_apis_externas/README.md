# Semana 07 — Servers con BD y APIs Externas

> **Etapa**: MCP Servers (Semanas 4–7) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Conectar un MCP Server a SQLite con queries async
- ✅ Integrar APIs externas con httpx (Python) y fetch/axios (TypeScript)
- ✅ Gestionar variables de entorno de forma segura
- ✅ Implementar connection pooling para bases de datos
- ✅ Manejar errores de red y BD correctamente

---

## 📚 Requisitos Previos

- Semana 06 completada
- Conocimiento básico de SQL
- SQLite disponible en Docker

---

## 🗂️ Estructura de la Semana

```
week-07-servers_bd_apis_externas/
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

1. Conexiones async a SQLite y PostgreSQL desde Python
2. HTTP clients async: httpx (Python) y fetch nativo (TypeScript)
3. Variables de entorno y configuración segura con python-dotenv
4. Connection pooling: aiosqlite, asyncpg
5. Manejo de errores: McpError, ToolError y patrones de retry

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Conectar server Python a SQLite y exponer tools de consulta
2. Integrar una API REST externa (OpenWeatherMap u otra pública)
3. Implementar lo mismo en TypeScript
4. Manejar errores de BD y HTTP con tipos correctos

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

MCP Server completo con BD SQLite + API externa (Python y TypeScript)

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] MCP Server Python conectado a SQLite con 4+ tools CRUD
- [ ] MCP Server TypeScript con la misma funcionalidad
- [ ] Integración con al menos una API externa pública
- [ ] .env.example con todas las variables necesarias
- [ ] docker-compose.yml para levantar el entorno completo

---

## 🔗 Navegación

[← Semana 06](../week-06-servers_avanzados_primitivos) · [Semana 08 →](../week-08-mcp_client_python)
