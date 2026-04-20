# Práctica 04 — Context, Logging y MCP Inspector

## 🎯 Objetivo

Usar el objeto `Context` para enviar logs al cliente LLM, implementar el patrón `lifespan`
para recursos compartidos, y explorar el servidor con MCP Inspector.

## 📋 Prerrequisitos

- Haber completado la Práctica 02
- Haber leído [03-ciclo-de-vida-del-server-startup-handlin.md](../../1-teoria/03-ciclo-de-vida-del-server-startup-handlin.md)
- Haber leído [05-debugging-de-servers-python-con-logging.md](../../1-teoria/05-debugging-de-servers-python-con-logging.md)

## 🗂️ Estructura

```
practica-04/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py        ← Código a descomentar
```

## ⏱️ Tiempo estimado: 50 minutos

---

## Paso 1: ctx.info() en un tool

El objeto `Context` (parámetro `ctx: Context`) permite enviar mensajes al cliente LLM.
Estos mensajes aparecen en Claude como progreso en tiempo real.

**Abre `src/server.py`** y descomenta la **Sección A**.

```python
@mcp.tool()
async def process(data: str, ctx: Context) -> str:
    await ctx.info("Starting processing...")
    # ... lógica
    await ctx.info("Done!")
    return result
```

## Paso 2: Lifespan context manager

El `lifespan` inicializa recursos al arranque y los limpia al cerrar.
El dict que se pasa con `yield` queda disponible en todos los tools.

**Descomenta la Sección B** para implementar un lifespan que mantiene un contador de requests.

## Paso 3: Acceder al lifespan context desde tools

Una vez que el lifespan está activo, cualquier tool puede acceder a su contexto
con `ctx.request_context.lifespan_context`.

**Descomenta la Sección C** para crear tools que usan el contexto compartido.

## Paso 4: Python logging a stderr

Configura `logging` correctamente para ver los mensajes internos del servidor
en `docker compose logs`, separados del protocolo MCP.

**Descomenta la Sección D**.

## Verificación con MCP Inspector

```bash
# Ejecutar localmente para conectar MCP Inspector
npx @modelcontextprotocol/inspector uv run python src/server.py
```

En MCP Inspector, en el panel "Notifications", verás los mensajes de `ctx.info()`.

---

## ✅ Criterios de Completitud

- [ ] Los tools usan `await ctx.info()` para reportar progreso
- [ ] El lifespan inicializa un dict de estado compartido
- [ ] Los tools leen del lifespan context con `ctx.request_context.lifespan_context`
- [ ] Los logs Python van a stderr (no stdout)
- [ ] Las notificaciones son visibles en MCP Inspector
