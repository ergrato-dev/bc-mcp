# Práctica 01 — Workflow de GitHub Actions para CI del MCP Server Python

## 🎯 Objetivo

Crear un workflow de CI que ejecute lint y tests automáticamente en cada push y pull request al repositorio de tu MCP Server Python.

## 📋 Prerrequisitos

- Repositorio en GitHub con tu MCP Server Python (semana 07 o 11)
- Docker Hub o GHCR disponible
- Haber leído [01-github-actions-workflows.md](../../1-teoria/01-github-actions-workflows.md) y [02-ci-pipeline-mcp.md](../../1-teoria/02-ci-pipeline-mcp.md)

## 🗂️ Estructura del ejercicio

```
practica-01-ci-python/
├── README.md                           # Este archivo
└── starter/
    ├── pyproject.toml                  # Dependencias del server de práctica
    ├── src/
    │   └── server.py                   # MCP Server de ejemplo (completo)
    ├── tests/
    │   ├── conftest.py                 # Fixtures
    │   └── test_tools.py              # Tests a descomentar
    └── .github/
        └── workflows/
            └── ci-python.yml           # ⭐ Workflow a descomentar
```

---

## Paso 1: Explorar el servidor de ejemplo

Abre `starter/src/server.py` — contiene un servidor MCP simple con un tool `add` y un tool `greet`. Es el servidor que vamos a proteger con CI.

Ejecuta los tests localmente para verificar que funcionan:

```bash
cd starter/
pip install --no-cache-dir uv==0.6.6
uv sync --frozen --group test
uv run pytest -v
```

Deberías ver todos los tests pasando.

---

## Paso 2: Estructura del repositorio

Para que GitHub Actions funcione, el workflow debe estar en la ruta exacta:

```
.github/
└── workflows/
    └── ci-python.yml
```

GitHub detecta automáticamente cualquier archivo `.yml` dentro de `.github/workflows/`.

Abre `starter/.github/workflows/ci-python.yml` y observa la estructura comentada.

---

## Paso 3: Descomentar el trigger y el job de lint

En `starter/.github/workflows/ci-python.yml`, descomenta la sección indicada con `PASO 3`.

Verifica que el archivo tiene el trigger correcto para ejecutarse en `push` a `main` y en `pull_request`.

---

## Paso 4: Descomentar el job de tests

Descomenta la sección `PASO 4` en el workflow. Este job usa `needs: lint` para ejecutarse solo si el lint pasa.

Observa el uso de `env: DB_PATH: ":memory:"` para que los tests usen SQLite in-memory en CI.

---

## Paso 5: Subir a GitHub y verificar

```bash
cd starter/
git init
git add .github/ pyproject.toml src/ tests/
git commit -m "feat: add MCP server with CI workflow"
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

Ve a la pestaña **Actions** de tu repositorio en GitHub y verifica que el workflow aparece y pasa en verde.

---

## ✅ Verificación

- [ ] El archivo `.github/workflows/ci-python.yml` está en la ruta correcta
- [ ] El workflow aparece en la pestaña Actions de GitHub
- [ ] Los jobs `lint` y `test` pasan en verde
- [ ] Si introduces un error de sintaxis en `server.py`, el job `lint` falla
- [ ] El job `test` solo corre si `lint` pasa (`needs: lint`)

---

[← Volver a Prácticas](../README.md) | [Práctica 02 →](../practica-02-ci-typescript/README.md)
