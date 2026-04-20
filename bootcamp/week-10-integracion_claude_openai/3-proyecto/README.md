# Proyecto Semana 10 — Agente Claude con MCP

## 🎯 Objetivo

Construir desde cero un agente autónomo que conecte a un MCP Server (Library Server),
convierta sus tools al formato de Anthropic y ejecute un agentic loop completo que
razone, llame herramientas y devuelva una respuesta final.

---

## 📋 Descripción

El agente debe:

1. Conectar al Library Server (semana 07) via stdio
2. Listar y convertir todas sus tools al formato de Anthropic
3. Recibir un prompt del usuario (argumento CLI o constante)
4. Ejecutar el agentic loop: llamar a Claude, despachar tool calls, acumular mensajes
5. Imprimir la respuesta final cuando `stop_reason == "end_turn"`

---

## 🗂️ Estructura del proyecto

```
starter/python-agent/
├── pyproject.toml          # dependencias del proyecto
├── .env.example            # variables de entorno necesarias
└── src/
    ├── config.py           # ← implementar: carga de configuración
    ├── tools.py            # ← implementar: conversión de tools
    └── agent.py            # ← implementar: conexión, loop y main
```

---

## ✅ Requerimientos funcionales

| # | Requerimiento | Criterio de aceptación |
|---|--------------|------------------------|
| 1 | Conectar al MCP Server | `session.initialize()` sin errores |
| 2 | Listar tools | Al menos 6 tools del Library Server |
| 3 | Convertir tools | Formato correcto con `input_schema` |
| 4 | Agentic loop | Múltiples iteraciones hasta `end_turn` |
| 5 | Despachar tool calls | Cada tool_use se ejecuta via MCP |
| 6 | Respuesta final | Texto coherente relacionado con el prompt |
| 7 | Límite de seguridad | Loop no supera `MAX_ITERATIONS` |
| 8 | Config desde `.env` | Sin credenciales hardcodeadas en el código |

---

## 📦 Entregables

- Carpeta `starter/python-agent/src/` con los tres archivos implementados
- `.env` con credenciales reales (no se sube al repo)
- Captura o log de la ejecución mostrando al menos 2 iteraciones del loop

---

## 🚀 Ejecución esperada

```bash
cd starter/python-agent
uv sync
cp .env.example .env
# Edita .env con tu ANTHROPIC_API_KEY y la ruta al Library Server

uv run python src/agent.py
```

Salida esperada:

```
✓ Conectado a Library Server (7 tools)
✓ Tools convertidas para Anthropic

[Iteración 1] stop_reason: tool_use
  → search_books({'query': 'Python'})
  ← 3 libros encontrados

[Iteración 2] stop_reason: end_turn

============================================================
RESPUESTA FINAL:
Encontré 3 libros de Python en la base de datos: ...
============================================================
```

---

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/README.md) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/README.md) como preparación
3. Trabaja en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Verifica que todos los entregables estén completos antes de la entrega

---

## 📌 Entregables

- [ ] `src/config.py` implementado (carga de env vars con validación)
- [ ] `src/tools.py` implementado (conversión MCP → Anthropic + dispatch)
- [ ] `src/agent.py` implementado (loop completo funcional)
- [ ] `.env` configurado con tu API key real
- [ ] Log de ejecución con al menos 2 iteraciones del loop

---

## 📊 Criterios de evaluación

Ver `rubrica-evaluacion.md` para el detalle completo.

| Criterio | Peso |
|---------|------|
| Conexión MCP funcional | 20% |
| Conversión correcta de tools | 20% |
| Agentic loop completo | 30% |
| Despacho y acumulación de mensajes | 20% |
| Configuración segura (sin credenciales hardcodeadas) | 10% |

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
