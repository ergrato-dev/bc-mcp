# Library CLI — Starter

## Requisitos

- Python 3.13+ y `uv` instalado, O Docker + Docker Compose
- Week-07 Library Manager Server (starter o solution)

## Setup local (sin Docker)

```bash
# 1. Copiar variables de entorno
cp .env.example .env

# 2. Editar .env — ajustar SERVER_PATH a tu ruta del server semana 07
#    SERVER_PATH=../../../week-07-servers_bd_apis_externas/3-proyecto/starter/python-server/src/server.py

# 3. Instalar dependencias del client
cd python-client
uv sync

# 4. Ejecutar el CLI
uv run python src/client.py
```

## Setup con Docker

```bash
# 1. Copiar variables de entorno
cp .env.example .env

# 2. Construir y ejecutar (modo interactivo)
docker compose run --rm library-client
```

## Verificar que funciona

Al ejecutar correctamente verás:

```
Library CLI — MCP Client
Conectando a Library Manager MCP Server...
✓ Conectado — 7 tools disponibles

Comandos: search | add | openlibrary | tools | stats | quit
>> 
```

## Implementar los TODOs

Abre `python-client/src/client.py` y completa las 6 funciones marcadas con `TODO`.
Implementa en orden — cada función usa la anterior.

---

[← Volver al proyecto](../README.md)
