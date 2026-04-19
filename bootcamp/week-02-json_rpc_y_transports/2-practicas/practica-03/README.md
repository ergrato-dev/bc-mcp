# Práctica 03 — MCP Server con Transport HTTP/SSE

## Objetivo

Implementar el mismo servidor de calculadora del Paso 02, pero con transport
HTTP/SSE para hacerlo accesible por red y soportar múltiples clientes.

## Tiempo estimado: 60 minutos

---

## Paso 1: Levantar el entorno

```bash
cd starter/
docker compose up --build
```

Verifica que el servidor HTTP esté corriendo:

```bash
curl http://localhost:8000/health
# Esperado: {"status":"ok"}
```

---

## Paso 2: Completar el servidor Python con SSE

**Abre `starter/python/src/server.py`** y descomenta las secciones en orden:

### Sección A — Importaciones y setup de FastAPI + MCP
### Sección B — Tools (igual que práctica-02)
### Sección C — Endpoint SSE (`GET /sse`)
### Sección D — Endpoint de mensajes (`POST /message`)
### Sección E — Endpoint de health check y arranque

---

## Paso 3: Conectar desde MCP Inspector

1. Abre http://localhost:6274
2. Selecciona transport: **SSE**
3. URL: `http://localhost:8000/sse`
4. Haz clic en **Connect**

¿Ves la lista de tools? ¿Funciona `tools/call`?

---

## Paso 4: Conectar múltiples clientes simultáneos

Abre dos pestañas del navegador apuntando a http://localhost:6274.
En cada una, conecta al servidor SSE. Ambas deben poder:
- Listar tools independientemente
- Llamar al tool `calculate` sin interferirse

Observa el log del servidor: ¿cuántas sesiones activas aparecen?

---

## Paso 5: Completar el servidor TypeScript

**Abre `starter/typescript/src/index.ts`** y repite el proceso descomentando
sección por sección.

---

## Paso 6: Comparar stdio vs HTTP/SSE

| Aspecto | stdio (práctica-02) | HTTP/SSE (esta práctica) |
|---------|--------------------|-----------------------|
| Puerto | N/A | 8000 |
| Número de clientes | 1 | Múltiples |
| Debuggeable con curl | ❌ | ✅ |
| Necesita HTTP server | ❌ | ✅ (FastAPI / Express) |

---

## Verificación

- [ ] `curl http://localhost:8000/health` retorna `{"status":"ok"}`
- [ ] MCP Inspector conecta vía SSE y lista el tool `calculate`
- [ ] `tools/call` con `{"a":10,"b":4,"op":"mul"}` retorna `40`
- [ ] Dos instancias de Inspector conectan simultáneamente sin errores

---

[← Práctica 02](../practica-02/README.md) | [← Volver a prácticas](../README.md)
