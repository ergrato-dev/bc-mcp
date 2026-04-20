# Práctica 04 — CLI Interactivo

## 🎯 Objetivo

Construir un CLI interactivo que mantenga una única sesión MCP abierta
y atienda múltiples comandos del usuario hasta que escriba `quit`.

## 📋 Requisitos previos

- Práctica 03 completada

## 🗂️ Estructura

```
practica-04-cli-interactivo/
├── README.md
└── starter/
    ├── pyproject.toml
    └── client.py
```

---

## Pasos

### Paso 1: PASO 1 — Conectar (ya familiar)

Descomenta `PASO 1`. Igual que las prácticas anteriores, el client se conecta
una sola vez y reutiliza la sesión para todos los comandos.

### Paso 2: PASO 2 — Mostrar el menú de ayuda

Descomenta `PASO 2`.

La función `print_help()` ya está implementada. Solo descomenta la llamada.

### Paso 3: PASO 3 — El bucle interactivo (loop principal)

Descomenta `PASO 3`.

El loop espera input del usuario con `input()`. Dentro de un `async def` se
usa `asyncio.get_event_loop().run_in_executor()` para no bloquear el event loop,
o simplemente `input()` directamente (funciona en scripts simples):

```python
# Leer input desde asyncio (sin bloquear)
loop = asyncio.get_event_loop()
line = await loop.run_in_executor(None, input, ">> ")
```

### Paso 4: PASO 4 — Comando `search`

Descomenta `PASO 4`.

El comando `search <texto>` llama a `search_books` y muestra los resultados.
Si el usuario escribe solo `search` sin texto, muestra un aviso.

### Paso 5: PASO 5 — Comando `stats`

Descomenta `PASO 5`.

El comando `stats` lee el resource `db://books/stats` y muestra las estadísticas.

### Paso 6: Ejecutar

```bash
uv run python client.py
```

Sesión de ejemplo:
```
Biblioteca MCP — CLI Interactivo
Comandos: search <texto> | stats | quit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
>> search python
  [1] Fluent Python — Luciano Ramalho (2022)
  [3] Python Asyncio Jump-Start — Matthew MacDougall (2022)
>> stats
  Total libros: 8
  Con ISBN: 4
  Año promedio: 2016
>> quit
¡Hasta luego!
```

## ✅ Criterio de éxito

- El CLI conecta una vez y reutiliza la sesión para todos los comandos
- `search <texto>` muestra resultados formateados
- `stats` muestra las estadísticas del resource
- `quit` cierra limpiamente la sesión

---

[← Práctica 03](../practica-03-invocar-tools/) | [Proyecto →](../../3-proyecto/)
