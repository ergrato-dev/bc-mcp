# Semana 12 — CI/CD y Proyecto Final Integrador

> **Etapa**: Producción (Semanas 11–12) · **Dedicación**: 8 horas · **Lenguajes**: Python y TypeScript

---

## 🎯 Objetivos de Aprendizaje

- ✅ Configurar un pipeline CI/CD con GitHub Actions
- ✅ Automatizar tests y build de imágenes Docker en CI
- ✅ Construir un sistema MCP completo como proyecto final
- ✅ Documentar el proyecto con READMEs profesionales
- ✅ Presentar el proyecto final con demo funcional

---

## 📚 Requisitos Previos

- Semana 11 completada
- Repositorio en GitHub
- Docker Hub o GHCR disponible

---

## 🗂️ Estructura de la Semana

```
week-12-cicd_proyecto_final/
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

1. GitHub Actions: workflows, jobs, steps y actions
2. CI para MCP: lint → test → build → push imagen
3. Semantic versioning y tags de Docker en CI
4. Documentación profesional de proyectos MCP
5. Patrones de arquitectura para sistemas MCP en producción

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Crear workflow de GitHub Actions para CI del server Python
2. Crear workflow de CI para el server TypeScript
3. Automatizar build y push de imágenes Docker a GHCR
4. Configurar badges de estado de CI en el README

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

Sistema MCP completo: server + client + agente LLM + CI/CD + Docker + documentación

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] Sistema MCP completo con server Python o TypeScript
- [ ] MCP Client + agente LLM funcional
- [ ] Pipeline CI/CD con GitHub Actions pasando en green
- [ ] docker-compose.yml para entorno de producción
- [ ] README profesional con arquitectura, setup y demo
- [ ] Presentación del proyecto (5-10 min demo en vivo)

---

## 🔗 Navegación

[← Semana 11](../week-11-testing_seguridad_docker) · *(fin del bootcamp)*
