# Glosario — Semana 05: Primer MCP Server en TypeScript

Términos clave de esta semana, ordenados alfabéticamente.

---

### CallToolResult

Tipo TypeScript que representa la respuesta de un tool MCP. Siempre tiene la forma:
`{ content: Array<{ type: "text", text: string }>, isError?: boolean }`.

---

### corepack

Herramienta integrada en Node.js que gestiona versiones de package managers (pnpm, yarn).
Permite fijar la versión exacta de pnpm con `corepack prepare pnpm@X.Y.Z --activate`.

---

### ESM (ECMAScript Modules)

Sistema de módulos nativo de JavaScript/Node.js. Usa `import`/`export` en lugar de
`require`/`module.exports`. Se activa en Node.js con `"type": "module"` en `package.json`.

---

### isError

Campo opcional del `CallToolResult`. Cuando es `true`, indica al LLM que el tool
falló. El LLM puede reintentar o informar el error al usuario.

---

### McpServer

Clase principal de alto nivel del SDK TypeScript (`@modelcontextprotocol/sdk`).
Equivalente a `FastMCP` en Python. Registra tools con el método `server.tool()`.

---

### module: "Node16"

Opción de `tsconfig.json` que activa el sistema de módulos ESM compatible con Node.js.
Requiere extensiones `.js` en imports locales y habilita top-level `await`.

---

### pnpm

Package manager rápido y eficiente para Node.js. Usa un store compartido de módulos
para ahorrar espacio. En este bootcamp se usa siempre en lugar de `npm` o `yarn`.

---

### StdioServerTransport

Clase del SDK TypeScript que implementa el transport MCP sobre stdin/stdout.
Se crea con `new StdioServerTransport()` y se pasa a `server.connect(transport)`.

---

### top-level await

Feature de Node.js ESM que permite usar `await` directamente en el nivel raíz del módulo,
sin necesitar un wrapper `async function main()`.

---

### tsconfig.json

Archivo de configuración de TypeScript. Define opciones del compilador (`target`, `module`,
`outDir`), archivos a incluir y excluir.

---

### tsc

Compilador oficial de TypeScript. Transforma archivos `.ts` en `.js`.
Se ejecuta con `pnpm build` (o directamente con `npx tsc`).

---

### tsx

Herramienta que ejecuta archivos TypeScript directamente sin compilar.
Útil para desarrollo rápido: `tsx src/index.ts`. No se usa en producción.

---

### "type": "module"

Campo en `package.json` que indica a Node.js que los archivos `.js` del proyecto
son módulos ESM (no CommonJS). Obligatorio para usar `import`/`export`.

---

### z.enum()

Validador Zod que restringe un parámetro a un conjunto fijo de valores string.
Ejemplo: `z.enum(["add", "subtract", "multiply", "divide"])`.
Genera una validación tanto en TypeScript (tipos) como en runtime (Zod).

---

### Zod

Librería TypeScript de validación y parsing de schemas. En MCP se usa para definir
el schema de inputs de cada tool. El SDK convierte los schemas Zod a JSON Schema automáticamente.


Implementación del transport stdio para servers MCP en TypeScript

### Zod

Librería de validación de schemas TypeScript-first usada para inputs de tools MCP

### corepack

Herramienta de Node.js para gestionar versiones de package managers (pnpm, yarn)

### pnpm

Package manager de Node.js ultrarrápido con workspaces y strict hoisting

### tsconfig.json

Archivo de configuración del compilador TypeScript

### z.object()

Función de Zod para definir schemas de objetos con tipos TypeScript

---

[← Volver al README de la semana](../README.md)
