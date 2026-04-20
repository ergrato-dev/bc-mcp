# Práctica 01 — McpServer básico

## 📋 Descripción

Primera práctica con TypeScript. Crearás tu primer MCP Server con `McpServer`,
registrarás un tool `add` usando Zod, y conectarás el servidor con `StdioServerTransport`.

## 🎯 Objetivos

- Importar `McpServer` y `StdioServerTransport` del SDK
- Instanciar `McpServer` con nombre y versión
- Registrar un tool con `server.tool()`
- Conectar el servidor con `await server.connect(transport)`

## ⏱️ Tiempo estimado: 30 min

---

## Paso 0: Setup del entorno

Clona o navega a la carpeta de la práctica y levanta el contenedor:

```bash
cd practica-01-mcpserver-basico
docker compose up --build
```

---

## Paso 1 — Importar dependencias y crear el servidor

**Abre `src/index.ts`** y descomenta la Sección A.

Importarás tres cosas:
- `McpServer` — la clase principal del servidor de alto nivel
- `StdioServerTransport` — el transport que usa stdin/stdout
- `z` de Zod — para definir schemas de validación

Al instanciar `McpServer`, debes pasar `name` y `version`.

```typescript
// Ejemplo del patrón de imports
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "my-server", version: "1.0.0" });
```

Después de descomentar, reconstruye y verifica que no hay errores de compilación:

```bash
docker compose up --build
```

---

## Paso 2 — Registrar el tool `add`

**Descomenta la Sección B** en `src/index.ts`.

`server.tool()` recibe cuatro argumentos:
1. `name` — el nombre del tool (string)
2. `description` — qué hace el tool (string)
3. `schema` — objeto Zod con los parámetros
4. `handler` — función `async` que recibe los parámetros y retorna `{ content: [...] }`

El retorno siempre es un objeto `{ content: [{ type: "text", text: "..." }] }`.

---

## Paso 3 — Conectar el transport

**Descomenta la Sección C** en `src/index.ts`.

Necesitas:
1. Crear una instancia de `StdioServerTransport`
2. Llamar `await server.connect(transport)`

Este `await` es top-level — funciona directamente porque el archivo es ESM y usamos Node.js 22.

---

## Paso 4 — Añadir el tool `greet`

**Descomenta la Sección D** en `src/index.ts`.

El tool `greet` recibe un `name` de tipo `z.string()` y retorna un saludo.
Practca registrar un segundo tool antes del `connect`.

---

## Verificación

Prueba el servidor con el inspector MCP:

```bash
# Dentro del contenedor
docker compose exec server npx @modelcontextprotocol/inspector node dist/index.js
```

O manualmente con JSON-RPC:

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | node dist/index.js
```

Deberías ver los tools `add` y `greet` en la respuesta.
