# Práctica 04 — Seguridad: hardening del Library Server

## 🎯 Objetivo

Identificar y corregir vulnerabilidades de seguridad en un server MCP
intencialmente inseguro: SQL injection, manejo de secretos y timeout.

---

## 🗂️ Estructura

```
practica-04-seguridad-hardening/
└── starter/
    ├── pyproject.toml
    └── src/
        └── server_secure.py  ← server a corregir, descomentar en orden
```

---

## ⚙️ Setup

```bash
cd starter
uv sync
uv run python src/server_secure.py
```

---

## 📝 Pasos

### Paso 1: Fix SQL Injection en search_books

Abre `src/server_secure.py`. Descomenta la sección **PASO 1**.

```python
# La versión vulnerable usa f-string en el SQL.
# La versión segura usa parámetros con ? y una tupla.
```

Verifica visualmente la diferencia entre ambas versiones.

---

### Paso 2: Fix de secretos hardcoded

Descomenta la sección **PASO 2**.

```python
# Los API keys nunca deben estar en el código fuente.
# Usar os.environ[] en lugar de strings literales.
```

---

### Paso 3: Timeout en llamadas externas

Descomenta la sección **PASO 3**.

```python
# asyncio.timeout(10.0) previene que el server quede
# bloqueado indefinidamente si la API externa no responde.
```

Prueba el comportamiento con timeout simulado.

---

### Paso 4: Mensajes de error seguros

Descomenta la sección **PASO 4**.

```python
# Los errores deben ser genéricos — no exponer internos del server.
# El LLM recibe información útil sin detalles de implementación.
```

---

## ✅ Verificación

Con el Inspector MCP de Claude Desktop, probar:

1. `search_books(query="x' OR '1'='1")` — debe no romper la DB
2. Ver en logs que los secretos se leen de variables de entorno
3. Simular timeout de API — el server debe responder con error en < 15s

[← Volver a prácticas](../README.md)
