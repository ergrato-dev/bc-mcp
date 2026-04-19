# Práctica 03 — Leer e Interpretar Mensajes JSON-RPC de MCP

## 🎯 Objetivo

Entender la estructura exacta de los mensajes que viajan entre el MCP Client y el
MCP Server analizando logs reales del protocolo.

## ⏱️ Tiempo estimado: 30 minutos

---

## Prerrequisitos

- Práctica 02 completada
- MCP Inspector corriendo y conectado al server de demo

---

## Paso 1: Activar logs detallados en MCP Inspector

En MCP Inspector, activa el modo verbose/debug si está disponible, o abre las
**DevTools del navegador** (F12) → pestaña **Network** → filtra por `WS` o `Fetch`.

Esto te permitirá ver los mensajes JSON-RPC exactos que se intercambian.

---

## Paso 2: Analizar el handshake de inicialización

Abre `starter/mensajes-protocolo.md` y descomenta la sección **Paso 1**.

Lee el mensaje `initialize` y responde:
- ¿Qué campos son obligatorios en toda solicitud JSON-RPC?
- ¿Qué información comunica el Client sobre sí mismo al Server?
- ¿Qué responde el Server con sus capacidades?

---

## Paso 3: Analizar una llamada a Tool

Desde MCP Inspector, ejecuta el tool `add` (si existe) con `a=5, b=3`.

Descomenta la sección **Paso 2** en `starter/mensajes-protocolo.md` y compara
con lo que ves en los DevTools.

Identifica:
- El campo `method` de la solicitud
- Cómo se pasan los argumentos en `params.arguments`
- La estructura de `result.content` en la respuesta

---

## Paso 4: Analizar un error del protocolo

En MCP Inspector, intenta llamar a un tool con un parámetro incorrecto (por ejemplo,
pasar un string donde se espera un número).

Descomenta la sección **Paso 3** en `starter/mensajes-protocolo.md`.

Observa:
- El código de error (`code`) — ¿qué significado tiene -32602?
- El campo `message` — ¿es útil para el LLM?
- ¿Hay campo `data` con detalles adicionales?

---

## Paso 5: Reflexión sobre el protocolo

Descomenta la sección **Paso 4** en `starter/mensajes-protocolo.md` y responde
las preguntas de reflexión.

---

## ✅ Verificación

- [ ] Identifiqué los 4 campos de toda solicitud JSON-RPC (jsonrpc, id, method, params)
- [ ] Entendí la diferencia entre `result` y `error` en una respuesta
- [ ] Vi el handshake initialize/initialized completo
- [ ] Analicé al menos un mensaje de error con su código numérico
- [ ] Puedo explicar por qué `id` es importante para correlacionar request/response

---

[← Práctica 02](../practica-02/README.md) | [Práctica 04 →](../practica-04/README.md)
