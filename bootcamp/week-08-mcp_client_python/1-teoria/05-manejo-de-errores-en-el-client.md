# Manejo de Errores en el MCP Client

## 🎯 Objetivos

- Distinguir entre errores de protocolo (`McpError`) y errores de dominio (`isError`)
- Implementar manejo robusto de errores en un client MCP
- Reconocer y manejar errores de transporte (`BrokenPipeError`, `TimeoutError`)
- Diseñar patrones de retry y shutdown graceful

---

## 1. Taxonomía de errores en un MCP Client

Un client MCP puede encontrar errores en tres capas distintas:

```
┌─────────────────────────────────────────────┐
│  Capa 1 — Tu Aplicación                     │
│  • ValueError, RuntimeError, KeyError       │  ← errores de tu código
├─────────────────────────────────────────────┤
│  Capa 2 — Protocolo MCP (ClientSession)     │
│  • McpError (método no existe, params mal)  │  ← excepciones del SDK
│  • result.isError = True (error de dominio) │  ← errores del server
├─────────────────────────────────────────────┤
│  Capa 3 — Transport (stdio)                 │
│  • BrokenPipeError (server crasheó)         │  ← errores de I/O
│  • TimeoutError (server no responde)        │
│  • FileNotFoundError (server no existe)     │
└─────────────────────────────────────────────┘
```

---

## 2. Errores de dominio — result.isError

Ya visto en el archivo anterior. El tool detecta un problema **esperado** de la aplicación y reporta `isError=True`:

```python
result = await session.call_tool("get_book", {"book_id": 9999})

if result.isError:
    # Error de dominio: "Book with id=9999 not found"
    error_message = result.content[0].text if result.content else "Unknown"
    print(f"[DOMAIN ERROR] {error_message}")
    # No es una excepción Python — el flujo continúa normalmente
```

**Cuándo ocurre `isError=True`:**
- El tool lanzó `ValueError`, `KeyError`, `RuntimeError`, etc. y el SDK lo capturó
- El server llamó a `raise McpError(...)` dentro del tool y lo marcó como error
- El tool encontró una condición esperada de "no encontrado" o "datos inválidos"

---

## 3. Errores de protocolo — McpError

`McpError` es una **excepción Python** que salta cuando hay problemas en el nivel del protocolo:

```python
from mcp import McpError
from mcp.types import ErrorCode

try:
    result = await session.call_tool(
        "tool_que_no_existe",
        {},
    )
except McpError as e:
    print(f"[PROTOCOL ERROR] Code: {e.error.code}")
    print(f"[PROTOCOL ERROR] Message: {e.error.message}")
    # e.error.code puede ser:
    # ErrorCode.MethodNotFound (-32601)
    # ErrorCode.InvalidParams  (-32602)
    # ErrorCode.InternalError  (-32603)
```

**Cuándo ocurre `McpError`:**

| Causa | Código JSON-RPC |
|-------|-----------------|
| Tool con nombre incorrecto | `-32601` MethodNotFound |
| Parámetros faltantes o tipos incorrectos | `-32602` InvalidParams |
| Error interno del server no capturado | `-32603` InternalError |
| Método MCP no soportado por el server | `-32601` MethodNotFound |

---

## 4. Errores de transporte

Estos errores ocurren cuando el proceso server falla a nivel de sistema operativo:

### BrokenPipeError — Server crasheó

```python
try:
    result = await session.call_tool("my_tool", {})
except BrokenPipeError:
    print("El proceso server se cerró inesperadamente")
    # El context manager limpiará los recursos
    # Necesitarás reiniciar el client completo
```

**Causa típica**: el server lanzó una excepción no capturada al inicio (import error, DB no existe, etc.).

**Debug**: ejecuta el server directamente en la terminal para ver el error:
```bash
python src/server.py  # verás el traceback
```

### TimeoutError — Server no responde

```python
import asyncio

try:
    result = await asyncio.wait_for(
        session.call_tool("heavy_operation", {}),
        timeout=30.0,
    )
except asyncio.TimeoutError:
    print("El server tardó más de 30 segundos — operación cancelada")
```

### FileNotFoundError — Comando del server no existe

```python
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client

try:
    params = StdioServerParameters(command="comando_que_no_existe", args=[])
    async with stdio_client(params) as (read, write):
        ...
except FileNotFoundError as e:
    print(f"Comando no encontrado: {e}")
    print("Verifica que el server esté instalado y en el PATH")
```

---

## 5. Patrón de manejo completo

Un client robusto maneja los tres niveles:

```python
import asyncio
import json
from mcp import ClientSession, McpError, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

async def safe_call_tool(
    session: ClientSession,
    tool_name: str,
    args: dict,
) -> dict | None:
    """Llama a un tool con manejo completo de errores."""

    try:
        result = await asyncio.wait_for(
            session.call_tool(tool_name, args),
            timeout=30.0,
        )

        # Nivel 2a — error de dominio
        if result.isError:
            error_text = result.content[0].text if result.content else "Unknown"
            print(f"[DOMAIN] {tool_name} reportó error: {error_text}")
            return None

        # Procesar resultado exitoso
        if result.content and isinstance(result.content[0], TextContent):
            return json.loads(result.content[0].text)

        return None

    # Nivel 2b — error de protocolo MCP
    except McpError as e:
        print(f"[PROTOCOL] {tool_name}: {e.error.code} — {e.error.message}")
        return None

    # Nivel 3 — errores de transporte
    except BrokenPipeError:
        print(f"[TRANSPORT] Server cerrado inesperadamente en '{tool_name}'")
        raise  # re-lanzar: el caller debe reiniciar el client

    except asyncio.TimeoutError:
        print(f"[TIMEOUT] '{tool_name}' tardó más de 30 segundos")
        return None

    # Errores de tu código (siempre deja pasar)
    except Exception as e:
        print(f"[UNEXPECTED] {tool_name}: {type(e).__name__}: {e}")
        raise
```

---

## 6. Estado de error en la sesión

![Ciclo de vida con estado de error](../0-assets/02-clientsession-ciclo-de-vida.svg)

Cuando ocurre un `McpError` o error de dominio (`isError=True`), la sesión **sigue funcionando**. Puedes seguir llamando otros tools.

Cuando ocurre un `BrokenPipeError` o `ConnectionResetError`, la sesión está **muerta**. Debes salir del `async with` y crear una nueva sesión:

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_with_retry(command: str, args_list: list[str], max_retries: int = 3):
    """Reintenta la conexión al server hasta max_retries veces."""

    for attempt in range(1, max_retries + 1):
        try:
            params = StdioServerParameters(command=command, args=args_list)
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    await do_work(session)
            return  # éxito

        except BrokenPipeError:
            if attempt < max_retries:
                wait = 2 ** attempt  # backoff exponencial: 2s, 4s, 8s
                print(f"Intento {attempt} falló. Reintentando en {wait}s...")
                await asyncio.sleep(wait)
            else:
                print("Máximo de reintentos alcanzado")
                raise
```

---

## 7. Shutdown graceful

Cuando recibes SIGINT (Ctrl+C) u otras señales, el `async with` cierra la sesión correctamente:

```python
import asyncio
import signal

async def main():
    params = StdioServerParameters(command="python", args=["src/server.py"])

    try:
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                # Loop interactivo
                while True:
                    cmd = input(">> ").strip()
                    if cmd == "quit":
                        break
                    result = await session.call_tool("execute", {"cmd": cmd})
                    print(result.content[0].text)

    except KeyboardInterrupt:
        # El async with ya cerró los recursos
        print("\nCerrando cliente...")
    except BrokenPipeError:
        print("El server se cerró inesperadamente")
```

---

## 8. Logging recomendado

Para debug y producción, agrega logging estructurado:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
)
logger = logging.getLogger("mcp.client")

# Uso
logger.info("Conectando a server: %s %s", command, args)
logger.debug("call_tool(%s, %s)", tool_name, args)
logger.warning("Server reportó error de dominio: %s", error_text)
logger.error("McpError en %s: %s", tool_name, e.error.message)
```

Para habilitar logs del SDK:
```python
logging.getLogger("mcp").setLevel(logging.DEBUG)  # ver mensajes raw JSON-RPC
```

---

## 9. Checklist de errores antes de deploy

```python
# ✅ Test de conexión exitosa
async with create_client("python", ["src/server.py"]) as session:
    info = await session.initialize()
    assert info.serverInfo.name, "Server debe tener nombre"

# ✅ Test de tool no encontrado
try:
    await session.call_tool("nonexistent", {})
    assert False, "Debería haber lanzado McpError"
except McpError as e:
    assert e.error.code == -32601  # MethodNotFound

# ✅ Test de error de dominio
result = await session.call_tool("get_book", {"book_id": -1})
assert result.isError, "ID inválido debería retornar isError=True"

# ✅ Test de timeout
try:
    await asyncio.wait_for(
        session.call_tool("fast_tool", {}),
        timeout=5.0,
    )
except asyncio.TimeoutError:
    pass  # OK si el server es lento, ajusta timeout
```

---

## ✅ Checklist de Verificación

- [ ] Distingo `McpError` (protocolo) de `isError=True` (dominio)
- [ ] Distingo `BrokenPipeError` (server caído) de `TimeoutError` (server lento)
- [ ] Uso `asyncio.wait_for()` para operaciones que pueden bloquearse
- [ ] Sé cuándo la sesión puede recuperarse y cuándo hay que reiniciarla
- [ ] Implemento logging para debug sin exponer datos sensibles
- [ ] Mi client maneja `KeyboardInterrupt` con cleanup correcto

## 📚 Recursos Adicionales

- [JSON-RPC 2.0 Error Codes](https://www.jsonrpc.org/specification#error_object)
- [Python asyncio.TimeoutError](https://docs.python.org/3/library/asyncio-exceptions.html)
- [MCP Spec — Error Handling](https://spec.modelcontextprotocol.io/specification/server/tools/#error-handling)
