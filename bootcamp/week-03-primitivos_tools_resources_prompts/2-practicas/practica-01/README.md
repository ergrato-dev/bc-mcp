# Práctica 01 — Tools en Python y TypeScript

**Semana 03 — Los Tres Primitivos**

## Objetivo

Implementar un MCP Server con Tools completos en Python y TypeScript.
Aprenderás a declarar `inputSchema`, manejar `isError` y usar `annotations`.

## Prerrequisitos

- Haber leído [01 — Tools: schema, annotations y execution model](../../1-teoria/01-tools-schema-de-inputs-annotations-execu.md)
- Docker y Docker Compose instalados
- Puertos 3000 disponibles

## Estructura

```
practica-01/
├── README.md               ← este archivo
├── docker-compose.yml      ← orquestación
├── python-server/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src/
│       └── server.py       ← código con secciones comentadas
└── ts-server/
    ├── Dockerfile
    ├── package.json
    └── src/
        └── index.ts        ← código con secciones comentadas
```

## Pasos

### Paso 1: Declarar la lista de Tools (`list_tools`)

Abre `python-server/src/server.py` y descomenta la **Sección A**.
Verás cómo se declara un Tool con `name`, `description` e `inputSchema`.

### Paso 2: Implementar el handler (`call_tool`)

Descomenta la **Sección B** para implementar la lógica que ejecuta el tool.
Observa el uso de `arguments.get()` para acceder a los parámetros.

### Paso 3: Manejo de errores con `isError`

Descomenta la **Sección C** para agregar manejo de errores de negocio.
Nota la diferencia entre `isError=True` y lanzar una excepción.

### Paso 4: Agregar `annotations`

Descomenta la **Sección D** para agregar `ToolAnnotations` al Tool.
Experimenta con `readOnlyHint`, `destructiveHint` e `idempotentHint`.

### Paso 5: Repetir en TypeScript

Repite los mismos pasos en `ts-server/src/index.ts`.

## Verificación

```bash
# Construir e iniciar los servidores
docker compose up --build

# En otra terminal: inspeccionar con MCP Inspector
# Ir a http://localhost:5173 y conectar a los servidores
```

Prueba llamar al tool `calculate_discount` con:
```json
{"price": 100.0, "discount_percent": 20}
```

## Resultado esperado

```json
{
  "content": [{"type": "text", "text": "Precio original: $100.00\nDescuento (20%): $20.00\nPrecio final: $80.00"}]
}
```
