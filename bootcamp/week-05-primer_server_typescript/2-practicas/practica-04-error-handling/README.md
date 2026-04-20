# Práctica 04 — Error Handling en MCP Tools

## 📋 Descripción

Aprenderás a manejar errores en tools TypeScript: validación con `z.enum()` para
restricciones en compile-time y runtime, `try/catch` para capturar excepciones,
y el patrón `isError` para comunicar fallos al LLM.

## 🎯 Objetivos

- Usar `z.enum()` para restringir valores posibles
- Implementar `try/catch` en handlers de tools
- Retornar `isError: true` para errores de dominio
- Distinguir entre errores de validación (Zod) y errores de runtime

## ⏱️ Tiempo estimado: 35 min

---

## Paso 1 — Setup

**Descomenta la Sección A** en `src/index.ts`.

---

## Paso 2 — Happy path: z.enum() básico

**Descomenta la Sección B** en `src/index.ts`.

El tool `get_weekday` recibe un `lang: z.enum(["en", "es", "fr"])`.
Si el LLM intenta pasar un valor que no está en el enum (como `"de"`),
Zod rechaza la llamada antes de que llegue al handler.

---

## Paso 3 — z.enum() con operaciones aritméticas

**Descomenta la Sección C** en `src/index.ts`.

El tool `calculate` usa `z.enum(["add", "subtract", "multiply", "divide"])`.
La operación `"divide"` puede fallar si `b === 0` — hay que manejarlo.

---

## Paso 4 — try/catch en el handler

**Descomenta la Sección D** en `src/index.ts`.

El tool `parse_json` intenta parsear un string como JSON.
Si el string no es JSON válido, `JSON.parse` lanza una excepción.
El `try/catch` la captura y retorna un `isError: true`:

```typescript
async ({ json_string }) => {
  try {
    const parsed = JSON.parse(json_string);
    return { content: [{ type: "text", text: JSON.stringify(parsed, null, 2) }] };
  } catch (error) {
    return {
      content: [{ type: "text", text: `Parse error: ${String(error)}` }],
      isError: true,
    };
  }
}
```

---

## Paso 5 — isError por validación de dominio

**Descomenta la Sección E** en `src/index.ts`.

El tool `get_user` simula una búsqueda de usuario. Si el ID no existe,
retorna `isError: true` aunque no haya excepción (es un error de dominio).

---

## Verificación

1. Llama a `calculate` con `op: "divide"` y `b: 0` → debe retornar `isError: true`
2. Llama a `parse_json` con `json_string: "no-es-json"` → debe retornar `isError: true`
3. Llama a `get_user` con `id: 999` → debe retornar `isError: true`
4. Llama con valores válidos → debe funcionar correctamente
