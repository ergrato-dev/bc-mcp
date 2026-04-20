# Práctica 05 — Dockerfile multi-stage para el Library Server

## 🎯 Objetivo

Crear un Dockerfile multi-stage para el Library Server Python
y un `docker-compose.yml` para orquestar el servicio completo.

---

## 🗂️ Estructura

```
practica-05-dockerfile-multistage/
└── starter/
    ├── Dockerfile.python      ← stages a descomentar
    ├── docker-compose.yml     ← servicios a descomentar
    ├── .dockerignore
    ├── pyproject.toml
    └── src/
        └── server.py          ← server de demo
```

---

## ⚙️ Prerrequisitos

```bash
docker --version    # Docker 24+
docker compose version
```

---

## 📝 Pasos

### Paso 1: Stage builder en el Dockerfile

Abre `Dockerfile.python`. Descomenta la sección **PASO 1**.

```dockerfile
# El stage builder instala uv y las dependencias de producción.
# No instala dev deps (tests, linters) — imagen más pequeña.
```

Construye solo el stage builder para verificar:

```bash
docker build --target builder -f Dockerfile.python -t test-builder .
docker run --rm test-builder python -c "import mcp; print('deps OK')"
```

---

### Paso 2: Stage runtime en el Dockerfile

Descomenta la sección **PASO 2**.

```dockerfile
# El stage runtime copia solo lo necesario del builder.
# Crea usuario no-root para seguridad.
```

Construye la imagen completa:

```bash
docker build -f Dockerfile.python -t library-server:latest .
docker images | grep library-server
```

Compara el tamaño con y sin multi-stage.

---

### Paso 3: .dockerignore

Revisa el `.dockerignore` incluido. Verifica que excluye:
- `__pycache__/`
- `.env`
- `tests/`
- `.git`

---

### Paso 4: docker-compose.yml

Descomenta la sección **PASO 4** en `docker-compose.yml`.

```yaml
# El servicio monta un volumen para persistir la DB SQLite.
# Las variables de entorno se pasan desde el .env del host.
```

Levanta el servicio:

```bash
docker compose up --build
```

---

### Paso 5: Verificación completa

```bash
# Ver el size de la imagen
docker images library-server:latest

# Verificar que el proceso corre como usuario no-root
docker compose exec python-server whoami

# Ver los logs
docker compose logs -f python-server

# Parar los servicios
docker compose down
```

---

## ✅ Verificación

- [ ] Imagen construye sin errores
- [ ] Tamaño de imagen < 300 MB
- [ ] El proceso corre como usuario `mcpuser` (no root)
- [ ] `docker compose up` levanta el servicio correctamente
- [ ] El volumen `library-data` persiste la DB entre reinicios

[← Volver a prácticas](../README.md)
