# Semana 11 — Testing, Seguridad y Docker

> **Etapa**: Producción (Semanas 11–12) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Escribir tests unitarios y de integración para MCP Servers
- ✅ Testear MCP Clients con transports en memoria
- ✅ Aplicar validación de inputs y manejo de errores
- ✅ Identificar y corregir vulnerabilidades de seguridad en tools
- ✅ Containerizar servers MCP con Docker y docker compose

---

## 📚 Requisitos Previos

- Semana 10 completada
- Conocimiento básico de pytest y vitest
- Docker Compose dominado

---

## 🗂️ Estructura de la Semana

```
week-11-testing_seguridad_docker/
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

1. Testing de MCP Servers con create_connected_server_and_client_session
2. Testing de MCP Clients con InMemoryTransport (TypeScript)
3. Validación de inputs: Pydantic (Python) y Zod (TypeScript)
4. Seguridad en tools: SQL injection, path traversal, rate limiting
5. Dockerfiles para Python (uv) y TypeScript (pnpm) en producción

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Escribir tests pytest para el server de semana 07
2. Escribir tests vitest para el server TypeScript
3. Agregar validación Pydantic a inputs de tools
4. Revisar y corregir vulnerabilidades en tools existentes
5. Crear Dockerfile y docker-compose.yml para el proyecto

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

Server de semana 07 con suite de tests completa, validación de inputs y Docker

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] Suite pytest con 80%+ de cobertura del server Python
- [ ] Suite vitest con 80%+ de cobertura del server TypeScript
- [ ] Dockerfile.python y Dockerfile.node optimizados
- [ ] docker-compose.yml para entorno completo
- [ ] Informe de seguridad con vulnerabilidades corregidas

---

## 🔗 Navegación

[← Semana 10](../week-10-integracion_claude_openai) · [Semana 12 →](../week-12-cicd_proyecto_final)
