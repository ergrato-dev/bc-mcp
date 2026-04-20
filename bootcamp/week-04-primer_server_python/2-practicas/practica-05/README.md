# Práctica 05 — Múltiples Tools con Distintos Tipos

## 🎯 Objetivo

Construir un servidor MCP completo con múltiples tools de distintas categorías
(matemáticas, texto, fechas), consolidando todo lo aprendido en la semana.

## 📋 Prerrequisitos

- Haber completado las Prácticas 01–04
- Entender type hints, docstrings, Context y estructura de proyecto

## 🗂️ Estructura

```
practica-05/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py        ← Código a descomentar
```

## ⏱️ Tiempo estimado: 50 minutos

---

## Paso 1: Tools matemáticos

Implementa tools de cálculo: `add`, `multiply` y `factorial`.
Observa cómo distintos tipos numéricos (`int` vs `float`) generan schemas distintos.

**Abre `src/server.py`** y descomenta la **Sección A**.

## Paso 2: Tools de texto

Implementa tools de manipulación de strings: `word_count`, `reverse_text` y `to_uppercase`.
Observa cómo `list[str]` y `dict` se usan como tipos de retorno.

**Descomenta la Sección B**.

## Paso 3: Tools de fecha y hora

Implementa tools con la stdlib `datetime`: `current_datetime` y `days_until`.
Aprende a retornar tipos estructurados (`dict`) con datos temporales.

**Descomenta la Sección C**.

## Paso 4: Integrar Context en todos los tools

Agrega `ctx: Context` a todos los tools para reportar progreso,
y configura un lifespan que registre el historial de llamadas.

**Descomenta la Sección D**.

## Verificación

```bash
docker compose up --build
```

Prueba todos los tools con MCP Inspector. Verifica:
- Los schemas correctos en el panel "Tools"
- Las notificaciones en "Notifications"
- El historial de llamadas en el tool `get_history`

---

## ✅ Criterios de Completitud

- [ ] 3 tools matemáticos funcionando
- [ ] 3 tools de texto funcionando con tipos de retorno correctos
- [ ] 2 tools de fecha/hora con `datetime`
- [ ] Al menos 5 tools usan `ctx.info()` para reportar progreso
- [ ] El lifespan registra el historial de tools llamados
