# Práctica 02 — Resources en Python y TypeScript

**Semana 03 — Los Tres Primitivos**

## Objetivo

Implementar un MCP Server con Resources en Python y TypeScript.
Aprenderás a definir URIs, exponer `list_resources`, implementar `read_resource`
y usar Resource Templates para recursos dinámicos.

## Prerrequisitos

- Haber completado la Práctica 01 (Tools)
- Haber leído [02 — Resources: URI scheme, tipos MIME, resource templates](../../1-teoria/02-resources-uri-scheme-tipos-mime-resource.md)

## Estructura

```
practica-02/
├── README.md
├── docker-compose.yml
├── python-server/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src/
│       └── server.py
└── ts-server/
    ├── Dockerfile
    ├── package.json
    ├── tsconfig.json
    └── src/
        └── index.ts
```

## Pasos

### Paso 1: Declarar resources estáticos (`list_resources`)

Abre `python-server/src/server.py` y descomenta la **Sección A**.
Observa cómo cada Resource tiene `uri`, `name` y `mimeType`.

### Paso 2: Implementar `read_resource`

Descomenta la **Sección B** para retornar datos para cada URI conocida.
Nota el uso de `TextResourceContents` con `mimeType`.

### Paso 3: Resource Templates para URIs dinámicas

Descomenta la **Sección C** para agregar un Resource Template con `{variable}`.
Implementa el handler que parsea la variable desde la URI.

### Paso 4: BlobResourceContents

Descomenta la **Sección D** para ver cómo se retorna contenido binario (base64).

### Paso 5: Repetir en TypeScript

Repite los pasos en `ts-server/src/index.ts`.

## Verificación

```bash
docker compose up --build
```

Verifica que el servidor retorne los siguientes recursos al hacer `resources/list`:
- `config://app/settings`
- `db://schema/products`
- `db://products/{product_id}` (template)
