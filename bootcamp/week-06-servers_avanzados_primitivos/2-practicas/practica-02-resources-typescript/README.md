# Práctica 02 — Resources en TypeScript

## 🎯 Objetivo

Implementar **Resources** en un servidor MCP TypeScript usando los handlers
`ListResourcesRequestSchema` y `ReadResourceRequestSchema`.

## 📋 Prerrequisitos

- Semana 05 completada (primer server TypeScript)
- Docker instalado y funcionando

## 🚀 Pasos

### Paso 1: Levantar el entorno

```bash
docker compose up --build
```

### Paso 2: Verificar que el server compila y arranca

```bash
docker compose logs server
```

Deberías ver: servidor MCP iniciado sin errores.

### Paso 3: Handler de resources/list

Abre `src/index.ts` y descomenta la **Sección 1**.

El handler `ListResourcesRequestSchema` registra los resources estáticos disponibles.
Cada resource necesita: `uri`, `name`, y opcionalmente `mimeType`.

### Paso 4: Handler de resources/read

Descomenta la **Sección 2**.

El handler `ReadResourceRequestSchema` recibe la URI solicitada y devuelve el contenido.
La respuesta siempre tiene la forma:

```typescript
{
  contents: [
    { uri: string, mimeType: string, text: string }
  ]
}
```

### Paso 5: Resource template con regex

Descomenta la **Sección 3**.

Los resource templates en TypeScript requieren matching manual con regex:

```typescript
const match = uri.match(/^books:\/\/isbn\/(.+)$/);
if (match) {
  const isbn = match[1];
  // ...
}
```

### Paso 6: Verificar en MCP Inspector

```bash
npx @modelcontextprotocol/inspector docker compose exec server node dist/index.js
```

→ Resources → List Resources → deberías ver los 2 resources estáticos
→ Prueba `books://isbn/978-0-13-110362-7` → datos del libro específico

---

## 📁 Estructura

```
practica-02-resources-typescript/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── package.json
├── tsconfig.json
└── src/
    └── index.ts
```
