# Prácticas — Semana 04: Primer MCP Server en Python

## Ejercicios Guiados

Todos los ejercicios son Python puro con FastMCP. El formato es **descomentar código** (NO TODOs).
Abrir el `src/server.py` de cada práctica y descomentar las secciones indicadas en el README.

| Práctica | Tema | Secciones | Herramientas |
|----------|------|-----------|--------------|
| [practica-01](practica-01/) | FastMCP básico — primer tool `add` | A, B, C, D | mcp, FastMCP, mcp.run() |
| [practica-02](practica-02/) | Type hints y schema automático | A, B, C, D | type hints, Optional, Pydantic |
| [practica-03](practica-03/) | Dependencias externas con uv + httpx | A, B, C, D | uv add, httpx, async client |
| [practica-04](practica-04/) | Context y lifespan | A, B, C, D | ctx: Context, @asynccontextmanager |
| [practica-05](practica-05/) | Múltiples tools con tipos variados | A, B, C, D | math, text, datetime, ctx |

---

## Flujo de trabajo recomendado

1. Leer el `README.md` de la práctica para entender el objetivo
2. Abrir `src/server.py` y leer todos los comentarios sin descomentar nada
3. Descomentar la **Sección A** y levantar el server con `docker compose up --build`
4. Probar con MCP Inspector antes de continuar con la Sección B
5. Repetir hasta completar todas las secciones
6. Comparar el resultado con lo esperado en el README

---

> 📌 Los ejercicios usan el formato **descomentar código** (NO TODOs).
> El estudiante aprende descomentando las secciones indicadas en el `README.md`
> de cada práctica y verificando que el código funcione correctamente.

---

[← Volver al README de la semana](../README.md)
