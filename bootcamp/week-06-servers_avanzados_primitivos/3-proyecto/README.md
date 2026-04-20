# Proyecto — Task Manager MCP (Semana 06)

## 🎯 Descripción

Construye un **Task Manager** con los 3 primitivos MCP:

- **Tools**: crear, completar, eliminar y buscar tareas
- **Resources**: leer tareas por estado y por ID
- **Prompts**: generar conversaciones contextuales de revisión y planificación

Implementa el server en **Python** y **TypeScript** siguiendo los archivos `starter/`.

## 📋 Entregables

1. `python-server/src/server.py` — todos los TODOs implementados
2. `ts-server/src/index.ts` — todos los TODOs implementados
3. Evidencia de pruebas con MCP Inspector (screenshots o texto)

## ✅ Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

## 🚀 Instrucciones

1. Navega a `starter/`
2. Lee los comentarios `TODO` en cada archivo fuente
3. Implementa cada TODO
4. Levanta con `docker compose up --build`
5. Verifica con MCP Inspector

## 📁 Estructura

```
3-proyecto/
├── README.md
└── starter/
    ├── docker-compose.yml
    ├── .env.example
    ├── python-server/
    │   ├── Dockerfile.python
    │   ├── pyproject.toml
    │   └── src/
    │       └── server.py
    └── ts-server/
        ├── Dockerfile.node
        ├── package.json
        ├── tsconfig.json
        └── src/
            └── index.ts
```

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/README.md) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/README.md) como preparación
3. Trabaja en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Usa Docker para ejecutar tu solución (`docker compose up --build`)
5. Verifica que todos los entregables estén completos antes de la entrega

## 📌 Entregables

- [ ] MCP Server Python con 3 tools, 2 resources y 1 prompt
- [ ] MCP Server TypeScript con los mismos primitivos
- [ ] Tests básicos verificando que los 3 primitivos responden
- [ ] README con descripción de cada primitivo expuesto

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md          # Este archivo
└── starter/           # Tu código va aquí
    └── README.md      # Instrucciones de setup
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
