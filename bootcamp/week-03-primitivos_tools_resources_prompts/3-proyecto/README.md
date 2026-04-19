# Proyecto — Semana 03: Knowledge Base MCP Server

## 🎯 Descripción

Construirás un servidor MCP completo para una base de conocimientos de documentación técnica.
El servidor expone los **tres primitivos** del protocolo MCP:

- **Tool** `search_docs` — busca en los documentos por texto
- **Resource** `docs://catalog` — lista todos los documentos disponibles
- **Resource** `docs://files/{filename}` — retorna el contenido de un documento (template)
- **Prompt** `summarize_doc` — genera un prompt con el documento embebido para que el LLM lo resuma

## 📋 Instrucciones

1. Lee el material teórico en [`1-teoria/`](../1-teoria/README.md) antes de comenzar
2. Completa las prácticas 01–04 en [`2-practicas/`](../2-practicas/README.md) como preparación
3. Trabaja únicamente en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Implementa los TODOs en `starter/src/server.py` (Python) y `starter/src/index.ts` (TypeScript)
5. Verifica tu solución con Docker: `docker compose up --build`
6. Prueba en MCP Inspector que los 3 primitivos respondan correctamente

## 📌 Entregables

- [ ] `starter/src/server.py` — todos los TODOs implementados
- [ ] `starter/src/index.ts` — todos los TODOs implementados
- [ ] `docker compose up --build` sin errores
- [ ] MCP Inspector: `tools/call search_docs` retorna resultados
- [ ] MCP Inspector: `resources/read docs://catalog` retorna lista de documentos
- [ ] MCP Inspector: `resources/read docs://files/intro.md` retorna contenido
- [ ] MCP Inspector: `prompts/get summarize_doc` retorna mensajes con EmbeddedResource

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md              # Este archivo
└── starter/
    ├── README.md          # Instrucciones de setup
    ├── docker-compose.yml
    ├── python-server/
    │   ├── Dockerfile
    │   ├── pyproject.toml
    │   ├── sample-docs/   # Documentos de ejemplo (no modificar)
    │   └── src/
    │       └── server.py  # ← Implementa los TODOs aquí
    └── ts-server/
        ├── Dockerfile
        ├── package.json
        ├── tsconfig.json
        └── src/
            └── index.ts   # ← Implementa los TODOs aquí
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
