# Práctica 02 — Zod Schemas: tipos y validación

## 📋 Descripción

Explorarás los tipos Zod más usados en MCP: `z.string()`, `z.number()`, `z.boolean()`,
`z.enum()`, `.optional()`, `.default()`, y `.describe()`. Cada sección añade un tool
que demuestra un patrón de validación distinto.

## 🎯 Objetivos

- Usar los tipos básicos de Zod en schemas MCP
- Añadir restricciones con `.min()`, `.max()`, `.email()`
- Usar `.optional()` y `.default()` para parámetros opcionales
- Documentar parámetros con `.describe()`
- Usar `z.object()` para parámetros anidados

## ⏱️ Tiempo estimado: 40 min

---

## Paso 1 — Setup e imports

**Descomenta la Sección A** en `src/index.ts`.

Misma base que la práctica 01: imports, `McpServer`, `StdioServerTransport`, `z`.

---

## Paso 2 — Tipos básicos: string, number, boolean

**Descomenta la Sección B** en `src/index.ts`.

El tool `validate_types` recibe un `text` (string), `count` (number) y `active` (boolean).
Observa cómo Zod valida automáticamente que cada parámetro tenga el tipo correcto.

```typescript
// Tipos básicos Zod
z.string()    // cualquier string
z.number()    // cualquier número (int o float)
z.boolean()   // true o false
```

---

## Paso 3 — z.enum(), .optional() y .default()

**Descomenta la Sección C** en `src/index.ts`.

El tool `format_text` demuestra tres features:
- `z.enum(["upper", "lower", "title"])` — limita los valores posibles
- `.optional()` — parámetro puede no enviarse
- `.default("upper")` — valor por defecto si no se envía

```typescript
// enum: solo valores permitidos
format: z.enum(["upper", "lower", "title"])

// opcional sin default
suffix: z.string().optional()

// con default
format: z.enum(["upper", "lower"]).default("upper")
```

---

## Paso 4 — .describe() para documentar

**Descomenta la Sección D** en `src/index.ts`.

El tool `search_items` usa `.describe()` en todos los parámetros.
Las descripciones aparecen en el JSON Schema y el LLM las usa para
entender qué valor enviar a cada parámetro.

---

## Paso 5 — z.object() anidado

**Descomenta la Sección E** en `src/index.ts`.

El tool `create_profile` recibe un `address` como `z.object()` anidado:

```typescript
{
  name: z.string(),
  age: z.number().min(0).max(150),
  address: z.object({
    city: z.string(),
    country: z.string().default("Spain"),
  }),
}
```

---

## Verificación

Prueba los tools con el inspector o JSON-RPC y verifica que la validación rechaza
parámetros incorrectos (tipo wrong, enum inválido, etc.).
