# Práctica 03 — Tipos de retorno: CallToolResult

## 📋 Descripción

Explorarás las distintas formas de construir el objeto `CallToolResult` que retorna
cada tool en MCP. Aprenderás a retornar texto simple, múltiples bloques de contenido,
JSON serializado como texto, e indicar errores con `isError: true`.

## 🎯 Objetivos

- Retornar texto simple con `{ content: [{ type: "text", text: "..." }] }`
- Retornar múltiples bloques de texto en un mismo `content[]`
- Serializar objetos con `JSON.stringify` para retornar datos estructurados
- Indicar errores de tool con `isError: true` en el CallToolResult

## ⏱️ Tiempo estimado: 35 min

---

## Paso 1 — Setup

**Descomenta la Sección A** en `src/index.ts` (imports y servidor).

---

## Paso 2 — Retorno de texto simple

**Descomenta la Sección B** en `src/index.ts`.

El tool `echo` retorna el texto recibido. La forma más básica de CallToolResult:

```typescript
return {
  content: [{ type: "text", text: "mensaje" }],
};
```

---

## Paso 3 — Múltiples bloques de contenido

**Descomenta la Sección C** en `src/index.ts`.

El tool `multi_info` retorna varios objetos `{ type: "text", text }` en el array `content`.
Cada elemento del array es un bloque separado de contenido.

```typescript
return {
  content: [
    { type: "text", text: "Primera línea" },
    { type: "text", text: "Segunda línea" },
    { type: "text", text: "Tercera línea" },
  ],
};
```

---

## Paso 4 — JSON.stringify para objetos

**Descomenta la Sección D** en `src/index.ts`.

El tool `stats` calcula estadísticas de una lista de números y retorna un objeto
serializado como JSON dentro del campo `text`:

```typescript
const result = { min: 1, max: 10, avg: 5.5, count: 4 };
return {
  content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
};
```

---

## Paso 5 — isError: true

**Descomenta la Sección E** en `src/index.ts`.

El tool `safe_divide` retorna `isError: true` cuando el divisor es cero.
El LLM entiende `isError` como una señal de que el tool falló:

```typescript
if (b === 0) {
  return {
    content: [{ type: "text", text: "Error: division by zero" }],
    isError: true,
  };
}
```

---

## Verificación

Llama al tool `safe_divide` con `b: 0` y verifica que la respuesta incluye `isError: true`.
Llama con valores válidos y verifica que `isError` no está presente (o es `false`).
