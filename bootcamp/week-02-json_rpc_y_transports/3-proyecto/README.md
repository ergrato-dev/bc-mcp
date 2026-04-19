# Proyecto Semana 02 — Analizador de Sesiones MCP

## 🎯 Descripción

Construirás un **analizador de sesiones MCP** que:

1. Captura todos los mensajes JSON-RPC intercambiados en una sesión real
2. Los parsea e identifica cada tipo (request / response / notification / error)
3. Genera un reporte que documenta el ciclo de vida completo de la sesión
4. Compara el comportamiento entre transports stdio y HTTP/SSE

## 📋 Prerrequisitos

- Completar las prácticas 01, 02 y 03 de esta semana
- Leer el material teórico de `1-teoria/` (especialmente `05-mensajes-mcp.md`)

## 📌 Entregables

- [ ] `session-analyzer.py` — script que analiza un archivo `.jsonl` de sesión
- [ ] `session-stdio.jsonl` — sesión capturada con transport stdio
- [ ] `session-sse.jsonl` — sesión capturada con transport HTTP/SSE (opcional +10%)
- [ ] `reporte.md` — análisis documentado con conclusiones

## 🏗️ Estructura

```
3-proyecto/
├── README.md          # Este archivo
└── starter/           # Tu código va aquí
    ├── README.md      # Instrucciones de setup
    ├── session-log.jsonl         # Sesión de ejemplo para analizar
    └── session-analyzer.py      # Script a completar (TODOs)
```

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| El analizador parsea correctamente requests vs responses | 25 |
| Identifica y muestra el handshake initialize/initialized | 25 |
| Genera estadísticas (total mensajes, tiempo, métodos llamados) | 25 |
| Documentación clara en `reporte.md` | 25 |
| Análisis de sesión SSE (bonus) | +10 |

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
