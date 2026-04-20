# Práctica 02 — Workflow de CI para el MCP Server TypeScript

## 🎯 Objetivo

Crear un workflow de GitHub Actions que ejecute lint, type check y tests para un MCP Server TypeScript con Node.js 22 y pnpm.

## 📋 Prerrequisitos

- Práctica 01 completada
- Haber leído [02-ci-pipeline-mcp.md](../../1-teoria/02-ci-pipeline-mcp.md)

## 🗂️ Estructura del ejercicio

```
practica-02-ci-typescript/
├── README.md
└── starter/
    ├── package.json
    ├── tsconfig.json
    ├── src/
    │   └── server.ts              # MCP Server TypeScript de ejemplo
    ├── tests/
    │   ├── helpers/
    │   │   └── test-setup.ts      # Helper para crear client de test
    │   └── server.test.ts         # Tests a descomentar
    └── .github/
        └── workflows/
            └── ci-typescript.yml  # ⭐ Workflow a descomentar
```

---

## Paso 1: Instalar dependencias y ejecutar tests

```bash
cd starter/
corepack enable && corepack prepare pnpm@10.7.0 --activate
pnpm install --frozen-lockfile
pnpm test
pnpm exec tsc --noEmit    # Type check
```

---

## Paso 2: Diferencias con el workflow de Python

El workflow TypeScript usa:
- `actions/setup-node@v4` en vez de `setup-python`
- `corepack enable` para habilitar pnpm
- `pnpm install --frozen-lockfile` (equivalente a `uv sync --frozen`)
- `pnpm exec tsc --noEmit` para type check
- `pnpm test` para vitest

---

## Paso 3: Descomentar trigger y job de lint

Abre `starter/.github/workflows/ci-typescript.yml` y descomenta la sección `PASO 3`.

Verifica que incluye:
- `corepack enable && corepack prepare pnpm@10.7.0 --activate`
- `actions/cache@v4` con path `~/.local/share/pnpm/store`
- `pnpm install --frozen-lockfile`
- `pnpm exec tsc --noEmit`

---

## Paso 4: Descomentar el job de tests

Descomenta la sección `PASO 4`. Observa que:
- `needs: lint` encadena los jobs
- El caché de pnpm se reutiliza entre jobs

---

## Paso 5: Subir a GitHub y verificar

Sube el código a GitHub y verifica que el workflow aparece en la pestaña **Actions** y pasa en verde.

---

## ✅ Verificación

- [ ] Workflow `ci-typescript.yml` creado en `.github/workflows/`
- [ ] Jobs `lint` y `test` pasan en verde en GitHub Actions
- [ ] `pnpm exec tsc --noEmit` sin errores
- [ ] Caché de pnpm configurado correctamente

---

[← Práctica 01](../practica-01-ci-python/README.md) | [Práctica 03 →](../practica-03-docker-ghcr/README.md)
