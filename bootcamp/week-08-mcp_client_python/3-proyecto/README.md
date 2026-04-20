# Proyecto — Semana 08: Library CLI

## 🎯 Descripción

Construirás un **MCP Client Python** con interfaz de línea de comandos
interactiva que se conecta al Library Manager MCP Server de la semana 07.
El client permite buscar libros, agregar nuevos títulos, consultar la API de
Open Library y ver estadísticas de la biblioteca, todo desde un único CLI.

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/README.md) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/README.md) como preparación
3. Trabaja en el directorio `starter/python-client/` — **no modifiques** archivos fuera de él
4. Implementa los TODOs en `src/client.py` en orden numérico
5. Ejecuta con `uv run python src/client.py` o con Docker

## 📌 Entregables

- [ ] `connect_to_server()` — StdioServerParameters + stdio_client + ClientSession + initialize
- [ ] `list_available_tools()` — listar e imprimir tools con su descripción
- [ ] `search_books(query)` — call_tool + parsear TextContent JSON
- [ ] `add_book(title, author, year)` — call_tool + verificar isError
- [ ] `search_openlibrary(title)` — call_tool + parsear resultados de la API externa
- [ ] `interactive_loop()` — bucle de comandos: search, add, openlibrary, tools, stats, quit

## 🏗️ Estructura del Proyecto

```
starter/
├── README.md                 # Setup e instrucciones
├── .env.example              # Variables de entorno
├── docker-compose.yml        # Orquestación con Docker
└── python-client/
    ├── Dockerfile.python     # Imagen del client
    ├── pyproject.toml        # Dependencias
    └── src/
        ├── config.py         # Configuración desde .env
        └── client.py         # ← Tu código (TODOs aquí)
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
