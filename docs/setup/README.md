# Guía de Setup — Bootcamp MCP Zero to Hero

Elige el método que mejor se adapte a tu entorno:

| Método | Recomendado | Requisitos | Guía |
|--------|:-----------:|------------|------|
| **Docker** ✅ | Sí — método oficial | Docker Desktop o Docker Engine | [setup con Docker](docker.md) |
| **Local** | Solo si no puedes usar Docker | Python 3.13+ y/o Node.js 22+ instalados manualmente | [setup local](local.md) |

> ⚠️ El bootcamp está diseñado y probado con Docker. El setup local es un fallback no oficial
> y puede requerir ajustes según tu sistema operativo.

---

## ¿Por qué Docker?

- ✅ Entorno idéntico al de producción y al de los demás estudiantes
- ✅ No contaminas tu sistema con versiones de Python/Node.js adicionales
- ✅ Un solo comando para levantar cualquier semana: `docker compose up --build`
- ✅ Fácil limpieza: `docker compose down -v`

---

[← Volver al README principal](../../README.md)
