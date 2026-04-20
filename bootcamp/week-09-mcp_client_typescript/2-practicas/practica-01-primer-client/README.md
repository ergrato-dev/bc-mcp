# Práctica 01 — Primer Client TypeScript

## 🎯 Objetivo

Crear el primer MCP Client en TypeScript: configurar `StdioClientTransport`, instanciar
`Client`, conectar al servidor de semana 07 e imprimir sus metadatos.

## 📋 Prerequisitos

- Semana 07 completada (servidor Python de Library Manager disponible)
- Node.js 22+ instalado
- pnpm instalado

## 🛠️ Setup

```bash
cd starter
pnpm install
```

---

## Paso a Paso

### Paso 1: Importar módulos del SDK

Abre `starter/src/client.ts` y descomenta la sección **PASO 1**.

Los módulos necesarios son:
- `Client` de `@modelcontextprotocol/sdk/client/index.js`
- `StdioClientTransport` de `@modelcontextprotocol/sdk/client/stdio.js`
- `"dotenv/config"` para cargar variables de entorno desde `.env`

### Paso 2: Crear el StdioClientTransport

Descomenta la sección **PASO 2**. El transport se crea con:

```typescript
const transport = new StdioClientTransport({
  command: process.env.SERVER_COMMAND ?? "python",
  args: [process.env.SERVER_PATH ?? "server.py"],
  env: { ...process.env },
});
```

### Paso 3: Instanciar el Client y conectar

Descomenta la sección **PASO 3**. El client se crea con nombre y versión, y se conecta
con `await client.connect(transport)`. Recuerda el patrón `try/finally` para garantizar
el cierre:

```typescript
const client = new Client({ name: "library-client", version: "1.0.0" });
try {
  await client.connect(transport);
  // ... usar el client
} finally {
  await client.close();
}
```

### Paso 4: Imprimir información del servidor

Descomenta la sección **PASO 4**. Tras conectar, el SDK expone los metadatos del servidor:

```typescript
const serverInfo = client.getServerVersion();
```

`getServerVersion()` retorna `{ name, version }` — los metadatos que el servidor declaró
en su `McpServer({ name, version })`.

---

## ▶️ Ejecutar

Crea el archivo `.env` (copia de `.env.example`) y ajusta la ruta al servidor:

```bash
cp .env.example .env
# Edita .env con la ruta correcta al server.py de semana 07
pnpm dev
```

## ✅ Salida Esperada

```
🔌 Conectando al servidor MCP...
✅ Conectado exitosamente

📋 Información del Servidor:
   Nombre:  library-manager
   Versión: 1.0.0

🔒 Cerrando conexión...
✅ Listo
```

---

[← Volver a Prácticas](../README.md)
