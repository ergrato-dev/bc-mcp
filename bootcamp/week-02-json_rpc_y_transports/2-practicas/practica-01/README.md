# Práctica 01 — Construir Mensajes JSON-RPC Manualmente

## Objetivo

Construir y enviar mensajes JSON-RPC 2.0 a mano para entender la estructura
del protocolo antes de usar los SDKs que lo abstraen.

## Tiempo estimado: 45 minutos

---

## Paso 1: Levantar el entorno

Asegúrate de tener el MCP Inspector de la semana 01 funcionando, o levanta
el de esta práctica:

```bash
cd starter/
docker compose up
```

Abre http://localhost:6274 en tu navegador.

---

## Paso 2: Explorar el archivo de mensajes

Abre el archivo `starter/mensajes.jsonl`. Cada línea es un mensaje JSON-RPC
completo que podrías enviar a un MCP Server.

**Abre `starter/mensajes.jsonl`** y descomenta los mensajes uno a uno en el
orden indicado. Para cada mensaje:
1. Léelo y trata de predecir qué respuesta recibirás
2. Envíalo al servidor usando MCP Inspector
3. Compara tu predicción con la respuesta real

---

## Paso 3: Observar los campos obligatorios

Para cada mensaje que descomentes, verifica que tiene los campos correctos:

**Request válido:**
- `"jsonrpc": "2.0"` ✓
- `"method"` con el nombre del procedimiento ✓
- `"id"` con un número o string único ✓
- `"params"` (opcional, pero necesario si el método lo requiere)

**Notification válida:**
- `"jsonrpc": "2.0"` ✓
- `"method"` ✓
- **Sin** campo `"id"` ✓

---

## Paso 4: Construir mensajes propios

Una vez completados los mensajes del archivo starter, construye tú mismo:

1. Un request para listar los resources del servidor
2. Un request `ping` (sin params)
3. Una notification para enviar al servidor (si el servidor la soporta)

---

## Paso 5: Provocar errores deliberados

Modifica un mensaje para causar cada uno de estos errores:

| Error a provocar | Modificación |
|-----------------|-------------|
| Parse error (-32700) | Romper el JSON (quitar una `"`) |
| Method not found (-32601) | Cambiar `tools/list` por `tools/listar` |
| Invalid params (-32602) | Omitir un campo requerido en `tools/call` |

---

## Verificación

Al terminar esta práctica debes poder responder:

- [ ] ¿Cuál es la diferencia entre un Request y una Notification en JSON-RPC?
- [ ] ¿Qué campo se usa para correlacionar una Response con su Request?
- [ ] ¿Cuándo aparece `"error"` en una Response y cuándo `"result"`?
- [ ] ¿Qué significa el código `-32601`?

---

[← Volver a prácticas](../README.md) | [Práctica 02 →](../practica-02/README.md)
