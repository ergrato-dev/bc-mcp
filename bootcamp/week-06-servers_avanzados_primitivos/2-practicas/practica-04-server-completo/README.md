# Práctica 04 — Server Completo con los 3 Primitivos

## 🎯 Objetivo

Integrar **Tools + Resources + Prompts** en un único servidor MCP funcional,
implementado en Python y TypeScript. Ambos servers usan el dominio de notas.

## 📋 Prerrequisitos

- Prácticas 01, 02 y 03 completadas
- Docker instalado y funcionando

## 🚀 Pasos

### Paso 1: Levantar el entorno

```bash
docker compose up --build
```

### Paso 2 (Python): Agregar Tools

Abre `python-server/src/server.py` y descomenta la **Sección 1 — Tools**.

El server empieza con el estado `NOTES` y los tools para crear, buscar y eliminar notas.

### Paso 3 (Python): Agregar Resources

Descomenta la **Sección 2 — Resources**.

Los resources leen el mismo estado `NOTES` que los tools mutaron.
Verifica que crear una nota con un tool → actualiza el resource `notes://all`.

### Paso 4 (Python): Agregar Prompts

Descomenta la **Sección 3 — Prompts**.

Los prompts generan mensajes contextuales usando el estado actual de `NOTES`.

### Paso 5 (TypeScript): Repetir el proceso

Repite los pasos 2–4 para `ts-server/src/index.ts`:
- Descomenta **Sección 1 TS** (Tools handlers)
- Descomenta **Sección 2 TS** (Resources handlers)
- Descomenta **Sección 3 TS** (Prompts handlers)

### Paso 6: Verificar integración

Usa MCP Inspector para verificar la integración:

1. **Tools** → `create_note` → crea una nota
2. **Resources** → `notes://all` → verifica que la nota aparece
3. **Prompts** → `summarize_notes` → genera el mensaje con las notas actuales

---

## 📁 Estructura

```
practica-04-server-completo/
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
