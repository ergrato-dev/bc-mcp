# Glosario — Semana 09: MCP Client en TypeScript

Términos clave de esta semana, ordenados alfabéticamente.

---

## C

**`CallToolResult`**
Tipo de retorno de `client.callTool()`. Contiene `content: ContentItem[]` e `isError?: boolean`. Si `isError` es `true`, el tool retornó un error de dominio (no una excepción de red).

**`Client`** (clase del SDK TypeScript)
Clase principal del SDK MCP en TypeScript para el lado cliente. Se instancia con `new Client({ name, version })` y requiere un `Transport` para establecer la conexión.

**`connect(transport)`**
Método async de `Client` que establece la sesión MCP. Hasta que se resuelve esta promesa, el client no puede enviar requests.

**`ContentItem`**
Elemento del array `content` de `CallToolResult`. Union discriminada: `{ type: "text", text: string }` | `{ type: "image", data: string, mimeType: string }` | `{ type: "resource", resource: EmbeddedResource }`.

## D

**Discriminated Union**
Patrón de TypeScript donde un campo literal (como `type`) diferencia variantes de un tipo. En MCP, `content[0].type` puede ser `"text"`, `"image"` o `"resource"`. El narrowing (`if (x.type === "text")`) da acceso seguro al campo específico.

## E

**`EmbeddedResource`**
Variante de `ContentItem` con `type: "resource"`. Contiene un resource embebido directamente en la respuesta del tool.

**ESM (ECMAScript Modules)**
Sistema de módulos estándar de JavaScript. Se habilita con `"type": "module"` en `package.json`. Los imports deben incluir la extensión `.js` (aunque el archivo sea `.ts`): `import { Client } from "@modelcontextprotocol/sdk/client/index.js"`.

## G

**`getServerVersion()`**
Método síncrono de `Client` que retorna `ServerVersion | undefined` con `name` y `version` del servidor. Disponible después de `connect()`.

## I

**`InMemoryTransport`**
Transport en memoria para testing: no requiere proceso externo. Se crea con `InMemoryTransport.createLinkedPair()` que retorna un par `[clientTransport, serverTransport]`.

**`isError`**
Campo booleano de `CallToolResult`. Cuando es `true`, indica que el servidor procesó la request pero el tool falló con un error de dominio. Diferente de `McpError`, que indica fallo de protocolo.

## L

**`ListPromptsResult`**
Tipo retornado por `client.listPrompts()`. Contiene `prompts: Prompt[]`.

**`ListResourcesResult`**
Tipo retornado por `client.listResources()`. Contiene `resources: Resource[]` con la lista de resources disponibles.

**`ListToolsResult`**
Tipo retornado por `client.listTools()`. Contiene `tools: Tool[]` con la lista de tools disponibles y sus schemas.

## M

**`McpError`**
Error de protocolo del SDK MCP. Se lanza cuando la sesión falla (timeout, process crash, JSON inválido). Se distingue de `isError`, que es un error de dominio del tool.

**Module Resolution — NodeNext**
Configuración de TypeScript (`"moduleResolution": "NodeNext"`) que respeta las reglas de resolución de módulos de Node.js 22. Requiere extensión `.js` en imports y `"type": "module"` en `package.json`.

## N

**NDJSON (Newline-Delimited JSON)**
Formato de framing usado por el transport stdio. Cada mensaje JSON-RPC se serializa en una línea terminada con `\n`. `StdioClientTransport` y `StdioServerTransport` lo implementan internamente.

## P

**pnpm**
Package manager de Node.js con workspaces y modo offline. Recomendado en este bootcamp. Instalar paquetes con versión exacta: `pnpm add @modelcontextprotocol/sdk@1.10.2` (sin `^` ni `~`).

## R

**`ReadResourceResult`**
Tipo retornado por `client.readResource({ uri })`. Contiene `contents: ResourceContents[]` donde cada elemento puede tener `text` (si es texto) o `blob` (si es binario) más `uri` y `mimeType`.

## S

**`StdioClientTransport`**
Implementación de Transport para stdio. Lanza el proceso servidor con `child_process.spawn()` y establece comunicación NDJSON a través de `stdin`/`stdout`. Se configura con `{ command, args, env }`.

**`stdio`** (transport)
Mecanismo de transport donde cliente y servidor se comunican a través de `stdin`/`stdout`. Ideal para integración con Claude Desktop, Cursor y VS Code. El cliente lanza el servidor como proceso hijo.

## T

**Transport** (interfaz)
Interfaz del SDK que abstrae el canal de comunicación. `StdioClientTransport` es la implementación principal para clients TypeScript. Existen también `SSEClientTransport` y `WebSocketClientTransport`.

**tsx**
Herramienta que ejecuta TypeScript directamente con Node.js sin compilación previa. Equivalente a `ts-node` pero moderno y compatible con ESM. Usado en scripts `"dev": "tsx src/client.ts"`.

---

[← Volver al README de la semana](../README.md)
