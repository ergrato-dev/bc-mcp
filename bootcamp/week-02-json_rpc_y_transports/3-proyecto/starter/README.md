# Setup — Proyecto Semana 02

## Entorno requerido

- Python 3.13+
- Docker + Docker Compose
- Haber completado las prácticas 01, 02 y 03

## Instalar dependencias

```bash
# Con uv (recomendado)
uv run python session-analyzer.py session-log.jsonl
```

## Archivos incluidos

- `session-log.jsonl` — sesión de ejemplo con mensajes MCP reales
- `session-analyzer.py` — script a completar con los TODOs indicados

## Capturar tu propia sesión (opcional)

1. Levanta el servidor stdio de practica-02 y redirige stderr a un archivo
2. Usa MCP Inspector y guarda la actividad de red como JSONL
3. Analiza ese JSONL con tu script

## Cómo ejecutar

```bash
python session-analyzer.py session-log.jsonl
```

## Estructura Esperada

Implementa el proyecto según las instrucciones en [`../README.md`](../README.md).

## TODO

Implementa los entregables descritos en [`../README.md`](../README.md#-entregables).

---

[← Volver al proyecto](../README.md)
