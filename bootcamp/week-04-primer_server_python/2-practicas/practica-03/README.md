# Práctica 03 — Gestión de Proyecto con uv y pyproject.toml

## 🎯 Objetivo

Comprender el flujo de trabajo con `uv`: cómo se definen dependencias en `pyproject.toml`,
cómo `uv.lock` garantiza reproducibilidad, y cómo agregar una nueva dependencia externa
(`httpx`) para enriquecer los tools del servidor.

## 📋 Prerrequisitos

- Haber completado la Práctica 02
- Haber leído [04-pyproject.toml-y-gestion-de-dependencias.md](../../1-teoria/04-pyproject.toml-y-gestion-de-dependencias.md)

## 🗂️ Estructura

```
practica-03/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml        ← Aquí agregarás httpx
└── src/
    └── server.py         ← Código a descomentar
```

## ⏱️ Tiempo estimado: 45 minutos

---

## Paso 1: Servidor base sin dependencias externas

Comenzamos con un servidor que solo usa la stdlib de Python, sin dependencias extras.

**Abre `src/server.py`** y descomenta la **Sección A**.

## Paso 2: Agregar httpx como dependencia

`httpx` es un cliente HTTP asíncrono moderno para Python. Para agregarlo:

1. Modifica `pyproject.toml` — agrega `"httpx==0.28.1"` a `dependencies`
2. Ejecuta `uv sync` para actualizar `uv.lock`:

```bash
# Opción A: con uv instalado localmente
uv add httpx==0.28.1

# Opción B: editar pyproject.toml a mano y luego
uv lock && uv sync
```

Luego reconstruye el contenedor:

```bash
docker compose build
```

**Descomenta la Sección B** para usar httpx en un tool.

## Paso 3: Manejo de errores HTTP

Las redes fallan. Un buen tool MCP maneja errores y retorna información útil.

**Descomenta la Sección C** para agregar manejo de errores.

## Paso 4: Timeout y headers

Configura timeouts y headers personalizados para hacer el cliente HTTP más robusto.

**Descomenta la Sección D**.

## Conceptos Clave

```
pyproject.toml  →  define qué versiones quieres
uv.lock         →  registra exactamente qué se instaló (incluye transitive deps)
uv sync --frozen →  instala EXACTAMENTE lo del lockfile (fail si hay diff)
```

## Verificación

```bash
docker compose up --build
```

Prueba el tool `fetch_url` con una URL real en MCP Inspector.

---

## ✅ Criterios de Completitud

- [ ] `pyproject.toml` tiene `httpx==0.28.1` en dependencies
- [ ] `uv.lock` está actualizado (ejecutar `uv lock` si es necesario)
- [ ] El tool `fetch_metadata` hace una petición HTTP real
- [ ] Los errores de red se manejan con `try/except`
- [ ] El timeout está configurado a ≤10 segundos
