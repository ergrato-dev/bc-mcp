# Práctica 04 — Configurar Badges de Estado de CI en el README

## 🎯 Objetivo

Añadir badges dinámicos al README de tu proyecto MCP: CI status, cobertura, versión de Python y licencia. Los badges hacen visible a cualquier visitante el estado actual del proyecto.

## 📋 Prerrequisitos

- Práctica 03 completada y pipeline CI pasando en verde
- Haber leído [04-documentacion-profesional-mcp.md](../../1-teoria/04-documentacion-profesional-mcp.md)

## 🗂️ Estructura del ejercicio

```
practica-04-badges-readme/
├── README.md                        # Este archivo
└── starter/
    └── README.md                    # ⭐ README template a completar
```

---

## Paso 1: Badge de CI de GitHub Actions

El badge más importante muestra si el pipeline está pasando.

Sintaxis:

```markdown
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci-python.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci-python.yml)
```

Reemplaza `OWNER` y `REPO` con tu usuario y nombre de repositorio.

---

## Paso 2: Badge de imagen Docker

```markdown
[![Docker](https://img.shields.io/badge/docker-ghcr.io-2496ED?logo=docker&logoColor=white)](https://ghcr.io/OWNER/REPO)
```

---

## Paso 3: Badge de Python version

```markdown
[![Python](https://img.shields.io/badge/python-3.13-3776AB?logo=python&logoColor=white)](https://python.org)
```

---

## Paso 4: Completar el README template

Abre `starter/README.md` — tiene secciones comentadas con `<!-- PASO X -->`.

Descomenta y completa cada sección:
- `<!-- PASO 3 -->` — Badges
- `<!-- PASO 4 -->` — Descripción y arquitectura
- `<!-- PASO 5 -->` — Tabla de tools MCP
- `<!-- PASO 6 -->` — Instalación con Docker
- `<!-- PASO 7 -->` — Variables de entorno

---

## Paso 5: Verificar badges en GitHub

Después de hacer push, ve a `https://github.com/TU_USUARIO/TU_REPO` y verifica que:

1. Los badges se muestran correctamente
2. El badge de CI está en verde (passing)
3. El link del badge lleva a la página de Actions

---

## ✅ Verificación

- [ ] Badge de CI visible en el README
- [ ] Badge de Docker visible en el README
- [ ] Badge de Python versión visible
- [ ] Tabla de tools MCP con parámetros y descripción
- [ ] Instrucciones de instalación con Docker
- [ ] Variables de entorno documentadas

---

[← Práctica 03](../practica-03-docker-ghcr/README.md) | [→ Proyecto Final](../../3-proyecto/README.md)
