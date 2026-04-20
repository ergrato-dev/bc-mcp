# Semana 11 — Proyecto Integrador: Library Server con Tests, Seguridad y Docker

## 🎯 Descripción

Refactoriza el Library Server de semana 07 para llevarlo a producción:
- Tests de integración completos con pytest
- Validación de inputs con Pydantic v2
- Seguridad aplicada: queries parametrizadas, timeout, errores seguros
- Dockerfile multi-stage para Python + docker-compose.yml

---

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/) como preparación
3. Trabaja en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Ejecuta los tests con `uv run pytest -v` antes de dockerizar
5. Verifica que todos los entregables estén completos antes de la entrega

---

## 🗂️ Estructura del proyecto

```
3-proyecto/
├── README.md
└── starter/
    ├── pyproject.toml          ← deps + grupo test
    ├── .env.example
    ├── Dockerfile.python       ← multi-stage a completar
    ├── docker-compose.yml      ← orquestación a completar
    ├── src/
    │   ├── server.py           ← server con validación a implementar
    │   └── validators.py       ← modelos Pydantic a implementar
    └── tests/
        ├── conftest.py         ← fixtures a implementar
        └── test_tools.py       ← suite completa a implementar
```

---

## 📌 Entregables y criterios

| Entregable | Criterio de éxito |
|-----------|-------------------|
| `src/validators.py` | 3 modelos Pydantic: AddBookInput, SearchBooksInput, UpdateBookInput |
| `src/server.py` | Tools usan validación, SQL parametrizado, timeout en APIs externas |
| `tests/conftest.py` | Fixtures `db` y `mcp_client` con DB en memoria |
| `tests/test_tools.py` | ≥ 10 tests, ≥ 75% de cobertura |
| `Dockerfile.python` | Multi-stage, usuario no-root, imagen < 300 MB |
| `docker-compose.yml` | Levanta el servicio correctamente |

---

## ⚙️ Setup

```bash
cd starter

# Instalar dependencias de producción y test
uv sync --group test

# Ejecutar tests
uv run pytest -v

# Ejecutar con cobertura
uv run pytest --cov=src --cov-report=term-missing -v

# Construir y levantar con Docker
docker compose up --build
```

---

## 🔗 Recursos

- [Teoría: Testing pytest](../1-teoria/01-testing-mcp-servers-pytest.md)
- [Teoría: Validación Pydantic](../1-teoria/03-validacion-pydantic-zod.md)
- [Teoría: Seguridad OWASP](../1-teoria/04-seguridad-owasp-mcp-tools.md)
- [Teoría: Docker multi-stage](../1-teoria/05-docker-produccion-mcp.md)
- [Server original: semana 07](../../week-07-servers_bd_apis_externas/3-proyecto/starter/python-server/src/server.py)

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
