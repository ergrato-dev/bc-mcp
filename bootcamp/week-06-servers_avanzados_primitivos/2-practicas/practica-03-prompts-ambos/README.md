# Práctica 03 — Prompts en Python y TypeScript

## 🎯 Objetivo

Implementar **Prompts** MCP (handlers `list` y `get`) en Python y TypeScript.
Los prompts generan mensajes de conversación a partir de argumentos.

## 📋 Prerrequisitos

- Prácticas 01 y 02 completadas (Resources)
- Docker instalado y funcionando

## 🚀 Pasos

### Paso 1: Levantar ambos servidores

```bash
docker compose up --build
```

Esto levanta:
- `python-server` — FastMCP con prompts en Python
- `ts-server` — SDK TypeScript con prompts

### Paso 2 (Python): Prompt simple sin argumentos

Abre `python-server/src/server.py` y descomenta la **Sección 1**.

El decorador `@mcp.prompt()` registra el prompt en `prompts/list`.
La función retorna `list[Message]`.

```python
# Estructura de un mensaje:
# Message(role="user", content=TextContent(type="text", text="..."))
```

### Paso 3 (Python): Prompt con argumento obligatorio

Descomenta la **Sección 2**.

Los argumentos del prompt se declaran como parámetros de la función Python.
FastMCP los publica automáticamente en `prompts/list`.

### Paso 4 (Python): Prompt con múltiples mensajes

Descomenta la **Sección 3**.

Un prompt puede retornar una conversación multi-turno con mensajes `user` y `assistant`.

### Paso 5 (TypeScript): Handler prompts/list

Abre `ts-server/src/index.ts` y descomenta la **Sección 1 TS**.

El handler `ListPromptsRequestSchema` declara los prompts disponibles y sus argumentos.

### Paso 6 (TypeScript): Handler prompts/get

Descomenta la **Sección 2 TS**.

El handler `GetPromptRequestSchema` recibe `name` y `arguments`, y retorna los mensajes.

### Paso 7: Verificar en MCP Inspector

```bash
# Python
npx @modelcontextprotocol/inspector docker compose exec python-server uv run python src/server.py

# TypeScript
npx @modelcontextprotocol/inspector docker compose exec ts-server node dist/index.js
```

→ Pestaña **Prompts** → List Prompts → verás los prompts registrados
→ Selecciona uno, llena los argumentos → **Get Prompt**

---

## 📁 Estructura

```
practica-03-prompts-ambos/
├── README.md
├── docker-compose.yml
├── python-server/
│   ├── Dockerfile.python
│   ├── pyproject.toml
│   └── src/
│       └── server.py
└── ts-server/
    ├── Dockerfile.node
    ├── package.json
    ├── tsconfig.json
    └── src/
        └── index.ts
```
