# Práctica 03 — Prompts en Python y TypeScript

**Semana 03 — Los Tres Primitivos**

## Objetivo

Implementar un MCP Server con Prompts en Python y TypeScript.
Aprenderás a declarar `PromptArgument`, construir el `messages` array
con `TextContent` y usar `EmbeddedResource` dentro de mensajes.

## Prerrequisitos

- Haber completado Práctica 01 y 02
- Haber leído [03 — Prompts: argumentos, mensajes y role-based content](../../1-teoria/03-prompts-argumentos-mensajes-y-role-based.md)

## Pasos

### Paso 1: Declarar la lista de Prompts (`list_prompts`)

Abre `python-server/src/server.py` y descomenta la **Sección A**.
Observa la diferencia entre argumentos `required=True` y `required=False`.

### Paso 2: Implementar `get_prompt`

Descomenta la **Sección B** para generar mensajes a partir de los argumentos.
Nota cómo `arguments or {}` evita el caso `None`.

### Paso 3: Multi-turn con role `assistant`

Descomenta la **Sección C** para agregar un mensaje `assistant` seed.
Este mensaje "pre-orienta" la respuesta del LLM.

### Paso 4: EmbeddedResource en mensajes

Descomenta la **Sección D** para incluir un Resource directamente en el Prompt.

### Paso 5: Repetir en TypeScript

Repite los pasos en `ts-server/src/index.ts`.

## Verificación

```bash
docker compose up --build
```

Llama a `prompts/get` con:
```json
{"name": "code_review", "arguments": {"language": "python", "code": "def add(a, b): return a+b"}}
```
