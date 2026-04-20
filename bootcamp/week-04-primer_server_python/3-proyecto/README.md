# Proyecto — Semana 04: Utility MCP Server en Python

## 🎯 Descripción

Construir un **MCP Server en Python** con FastMCP que exponga 3 tools de utilidad real:

| Tool | Descripción | Parámetros |
|------|-------------|------------|
| `calculate` | Operaciones matemáticas básicas | `operation`, `a`, `b` |
| `transform_text` | Transformaciones de texto | `text`, `operation` |
| `date_info` | Información sobre una fecha | `date_string` |

El proyecto integra todo lo aprendido en la semana: FastMCP, type hints, Context, logging y Docker.

---

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/) como preparación
3. Trabaja en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Implementa la lógica en `starter/src/server.py` donde indican los `# TODO`
5. Usa Docker para ejecutar tu solución: `docker compose up --build`
6. Verifica con MCP Inspector: `npx @modelcontextprotocol/inspector uv run python src/server.py`

---

## 📌 Entregables

- [ ] `src/server.py` con los 3 tools implementados y funcionando
- [ ] `docker compose up --build` sin errores
- [ ] MCP Inspector muestra los 3 tools con sus schemas correctos
- [ ] Captura de pantalla del Inspector con al menos 2 tools ejecutados exitosamente
- [ ] Manejo correcto de errores (división por cero, operación desconocida, fecha inválida)

---

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md              ← Este archivo (instrucciones)
└── starter/               ← Tu código va aquí
    ├── README.md          ← Setup e instrucciones de ejecución
    ├── Dockerfile
    ├── docker-compose.yml
    ├── pyproject.toml
    └── src/
        └── server.py      ← ⭐ Archivo principal — aquí implementas los TODOs
```

---

## 🧪 Cómo probar

```bash
# Desde starter/
docker compose up --build

# En otra terminal: probar con MCP Inspector
npx @modelcontextprotocol/inspector uv run python src/server.py

# Ejemplos de uso en el Inspector:
# calculate: operation="add", a=10, b=5       → 15.0
# calculate: operation="divide", a=10, b=0    → error descriptivo
# transform_text: text="hello", operation="upper" → "HELLO"
# transform_text: text="hello world", operation="word_count" → "2 words"
# date_info: date_string="2025-01-01"         → dict con weekday, days_until, etc.
```

---

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para el detalle completo.

| Criterio | Peso | Descripción |
|----------|------|-------------|
| Tools funcionan correctamente | 40% | Los 3 tools retornan resultados correctos |
| Manejo de errores | 20% | Errores claros para inputs inválidos |
| Código limpio y type hints | 20% | Type hints completos, docstrings descriptivos |
| Docker funciona | 20% | `docker compose up --build` sin errores |

---

[← Volver al README de la semana](../README.md)

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
