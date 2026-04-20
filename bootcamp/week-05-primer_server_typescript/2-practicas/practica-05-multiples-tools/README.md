# Práctica 05 — Servidor con Múltiples Tools

## 📋 Descripción

Construirás un servidor completo con tres grupos de tools: matemáticas, texto y fechas.
Esta práctica consolida todos los patrones aprendidos en la semana y produce un servidor
listo para ser integrado con Claude u otro LLM.

## 🎯 Objetivos

- Organizar un servidor con múltiples tools de distintas categorías
- Combinar todos los patrones de Zod vistos en la semana
- Gestionar errores correctamente en todos los tools
- Verificar el servidor completo con el inspector MCP

## ⏱️ Tiempo estimado: 45 min

---

## Paso 1 — Setup

**Descomenta la Sección A** en `src/index.ts` (imports y servidor).

---

## Paso 2 — Tools matemáticos

**Descomenta la Sección B** en `src/index.ts`.

Tres tools:
- `add(a, b)` → suma
- `multiply(a, b)` → producto
- `power(base, exponent)` → potencia (con validación de exponent ≥ 0)

---

## Paso 3 — Tools de texto

**Descomenta la Sección C** en `src/index.ts`.

Dos tools:
- `word_count(text)` → cuenta palabras, caracteres y líneas
- `reverse_text(text)` → invierte el string

---

## Paso 4 — Tool de fechas

**Descomenta la Sección D** en `src/index.ts`.

Un tool completo:
- `date_info(date_string)` → retorna día de semana, si es fin de semana,
  días hasta esa fecha, y si ya pasó

---

## Paso 5 — Conectar y probar

**Descomenta la Sección E** en `src/index.ts` (transport + connect).

Construye y prueba todos los tools:

```bash
docker compose up --build
```

Verifica con el inspector que aparecen **6 tools** en la lista.

---

## Verificación

```bash
# Listar todos los tools
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | node dist/index.js

# Probar add
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"add","arguments":{"a":5,"b":3}}}' | node dist/index.js

# Probar date_info
echo '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"date_info","arguments":{"date_string":"2025-12-25"}}}' | node dist/index.js
```
