---
description: "Genera un ejercicio guiado paso a paso para la sección 2-practicas/ del bootcamp bc-mcp. Formato descomentar — sin TODOs."
mode: "agent"
---

Crea un ejercicio guiado para la sección `2-practicas/` del bootcamp MCP Zero to Hero.

## Regla fundamental

Los ejercicios son **tutoriales guiados**, NO tareas con TODOs.
El estudiante aprende descomentando código ya escrito y verificando que funcione.

❌ **Nunca** usar `# TODO: Implementar` en ejercicios  
✅ **Siempre** código comentado listo para descomentar

## Información necesaria

Si no se especificó en la solicitud, pregunta:

1. **Semana y número del ejercicio** (ej. "Semana 4 — Ejercicio 2")
2. **Concepto a practicar** (ej. "registrar un MCP Tool con parámetros")
3. **Lenguaje(s)**: Python, TypeScript o ambos
4. **Duración estimada**: 30min / 45min / 1h
5. **Prerequisito**: qué debe haber completado el estudiante antes

## Estructura a generar

```
2-practicas/{NN}-{nombre-ejercicio}/
├── README.md          # instrucciones paso a paso
└── starter/
    ├── server.py      # Python (si aplica)
    └── server.ts      # TypeScript (si aplica)
```

> ⚠️ Los ejercicios NO tienen carpeta `solution/`

## README.md del ejercicio

````markdown
# Ejercicio {N}: {Título}

## 🎯 Objetivo

Una oración clara de lo que el estudiante logrará al completar este ejercicio.

## ⏱️ Duración estimada

{N} minutos

## 📚 Prerrequisitos

- Haber completado el ejercicio anterior (si aplica)
- Conocer {concepto previo}

## 📋 Instrucciones

### Paso 1: {Título del paso}

Explicación del concepto con ejemplo de referencia:

```python
# Ejemplo explicativo (NO es el código que debes descomentar)
@mcp.tool()
async def example_tool(param: str) -> str:
    """Descripción del tool."""
    return param.upper()
```
````

**Abre `starter/server.py`** y descomenta la sección `PASO 1`.

Verifica que funciona ejecutando:

```bash
uv run python starter/server.py
```

### Paso 2: {Título del paso}

...

## ✅ ¿Cómo sé que funciona?

Lista de verificación que el estudiante puede comprobar:

- [ ] El servidor arranca sin errores
- [ ] El tool aparece en `tools/list`
- [ ] Al llamar el tool con `{ejemplo}` retorna `{resultado esperado}`

## 💡 ¿Qué aprendiste?

Resumen de los conceptos clave reforzados en este ejercicio.

````

## starter/server.py — formato Python

```python
"""
Ejercicio {N}: {Título}
Semana {N}: {Tema de la semana}
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ejercicio-{n}")


# ============================================
# PASO 1: {Título del paso}
# ============================================
print("--- Paso 1: {descripción breve} ---")

# {Explicación en español de qué hace este código}
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def {tool_name}({params}: {types}) -> {return_type}:
#     """{docstring en inglés para el LLM}"""
#     {implementación}


# ============================================
# PASO 2: {Título del paso}
# ============================================
# ...


if __name__ == "__main__":
    mcp.run()
````

## starter/server.ts — formato TypeScript

```typescript
/**
 * Ejercicio {N}: {Título}
 * Semana {N}: {Tema de la semana}
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new Server({ name: "ejercicio-{n}", version: "1.0.0" });

// ============================================
// PASO 1: {Título del paso}
// ============================================
console.log("--- Paso 1: {descripción breve} ---");

// {Explicación en español de qué hace este código}
// Descomenta las siguientes líneas:
// server.tool(
//   "{tool_name}",
//   { {param}: z.{type}().describe("{description}") },
//   async ({ {param} }) => ({
//     content: [{ type: "text", text: String({result}) }],
//   })
// );

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Reglas de contenido

- Máximo 4-5 pasos por ejercicio — si hay más, dividir en dos ejercicios
- Cada paso debe poder verificarse de forma independiente
- Las instrucciones deben ser lo suficientemente claras para que el estudiante no necesite ayuda externa
- Incluir el comando exacto para ejecutar y verificar cada paso
- Para ejercicios bilingües: el README es único, pero hay un `starter/server.py` Y un `starter/server.ts` separados
