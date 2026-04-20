# Práctica 01 — Primer Client MCP en Python

## 🎯 Objetivo

Conectarte al MCP Server de la semana 07 desde un script Python, completar
el handshake del protocolo e imprimir la información del server.

## 📋 Requisitos previos

- Semana 07 completada (el server de la biblioteca debe funcionar)
- Python 3.13+ con `uv` instalado

## 🗂️ Estructura

```
practica-01-primer-client/
├── README.md
└── starter/
    ├── pyproject.toml
    └── client.py
```

---

## Pasos

### Paso 1: Configurar el entorno

Instala las dependencias:

```bash
cd practica-01-primer-client/starter
uv sync
```

### Paso 2: Entender el boilerplate

Abre `starter/client.py`. El archivo ya tiene imports y la función `main()` esquematizada.

Tu tarea es descomentar cada sección numerada en orden.

### Paso 3: PASO 1 — Crear StdioServerParameters

En `client.py`, descomenta la sección `PASO 1`.

`StdioServerParameters` describe **cómo lanzar el proceso server**:

```python
# Ejemplo explicativo
params = StdioServerParameters(
    command="python",
    args=["ruta/al/server.py"],
    env={**os.environ, "DB_PATH": "./data/library.db"},
)
```

Ajusta `SERVER_PATH` al servidor de tu semana 07.

### Paso 4: PASO 2 — Abrir el canal de comunicación

Descomenta la sección `PASO 2`.

`stdio_client(params)` lanza el proceso como subprocess y crea los pipes `stdin`/`stdout`.
Los streams `read` y `write` son pasados a `ClientSession`.

### Paso 5: PASO 3 — Crear la sesión e inicializar

Descomenta la sección `PASO 3`.

`session.initialize()` realiza el handshake MCP. Sin este paso, cualquier llamada
posterior lanzará un error. El resultado contiene nombre, versión y capabilities.

### Paso 6: PASO 4 — Imprimir la información

Descomenta la sección `PASO 4`.

Accede a `info.serverInfo.name`, `info.serverInfo.version` y `info.capabilities`.

### Paso 7: Ejecutar

```bash
uv run python client.py
```

Salida esperada:
```
✓ Conectado al server MCP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Server:  Library Manager MCP Server
Version: 0.1.0
Tools:   ✓
Resources: ✓
Prompts: ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Sesión cerrada correctamente
```

## ✅ Criterio de éxito

- El script se conecta sin errores
- Imprime el nombre y versión del server
- Muestra correctamente qué capabilities tiene el server

---

[← Teoría](../../1-teoria/) | [Práctica 02 →](../practica-02-descubrir-capacidades/)
