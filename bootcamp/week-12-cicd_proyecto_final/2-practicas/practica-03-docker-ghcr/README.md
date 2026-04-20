# Práctica 03 — Automatizar Build y Push de Imagen Docker a GHCR

## 🎯 Objetivo

Añadir un job al pipeline de CI que construya la imagen Docker del MCP Server y la publique en GitHub Container Registry (GHCR) al hacer push a `main`.

## 📋 Prerrequisitos

- Prácticas 01 y 02 completadas
- Repositorio en GitHub con acceso a `packages`
- Haber leído [02-ci-pipeline-mcp.md](../../1-teoria/02-ci-pipeline-mcp.md) y [03-semantic-versioning-docker-tags.md](../../1-teoria/03-semantic-versioning-docker-tags.md)

## 🗂️ Estructura del ejercicio

```
practica-03-docker-ghcr/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── src/server.py              # El mismo server de práctica 01
    ├── Dockerfile.python          # ⭐ Dockerfile multi-stage a descomentar
    ├── .dockerignore
    └── .github/
        └── workflows/
            └── docker-build-push.yml   # ⭐ Workflow a descomentar
```

---

## Paso 1: Dockerfile multi-stage

Abre `starter/Dockerfile.python` — tiene dos stages comentados:

- **PASO 3**: Stage `builder` con `uv` para instalar dependencias
- **PASO 4**: Stage `runtime` con usuario no-root para seguridad

---

## Paso 2: Construir la imagen localmente

```bash
cd starter/
docker build -f Dockerfile.python -t mcp-server-test .
docker run --rm mcp-server-test python -c "print('OK')"
```

---

## Paso 3: Descomentar el Dockerfile — stage builder

En `starter/Dockerfile.python`, descomenta la sección `PASO 3`.

El stage builder debe:
- Partir de `python:3.13-slim AS builder`
- Instalar `uv`
- Copiar `pyproject.toml` y `uv.lock`
- Ejecutar `uv sync --frozen --no-dev`

---

## Paso 4: Descomentar el Dockerfile — stage runtime

Descomenta la sección `PASO 4`:

- Partir de `python:3.13-slim` (imagen final más pequeña)
- Crear usuario no-root `appuser`
- Copiar solo el virtual env del stage builder
- No copiar código de tests ni __pycache__

---

## Paso 5: Descomentar el workflow de Docker

En `starter/.github/workflows/docker-build-push.yml`, descomenta las secciones indicadas.

Observa cómo:
- El job `docker` tiene `needs: test` para solo buildear si los tests pasan
- `if: github.event_name == 'push' && github.ref == 'refs/heads/main'` evita push en PRs
- `docker/metadata-action@v5` genera el tag `:latest` y `:sha-xxxxxxx` automáticamente
- `docker/build-push-action@v6` sube la imagen con `push: true`

---

## Paso 6: Verificar en GHCR

Después del push a `main`, ve a:

```
https://github.com/TU_USUARIO/TU_REPO/pkgs/container/TU_REPO
```

La imagen debe aparecer con el tag `latest`.

```bash
# Probar la imagen publicada
docker pull ghcr.io/TU_USUARIO/TU_REPO:latest
docker run --rm ghcr.io/TU_USUARIO/TU_REPO:latest
```

---

## ✅ Verificación

- [ ] `Dockerfile.python` con 2 stages (builder + runtime)
- [ ] Imagen construida correctamente en local
- [ ] Workflow `docker-build-push.yml` con job `docker` después de `test`
- [ ] Imagen publicada en GHCR con tag `latest`
- [ ] La imagen NO se publica en Pull Requests (solo en push a main)

---

[← Práctica 02](../practica-02-ci-typescript/README.md) | [Práctica 04 →](../practica-04-badges-readme/README.md)
