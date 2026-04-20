# Práctica 01 — Tests pytest para el Library Server

## 🎯 Objetivo

Escribir una suite de tests de integración para el Library Server de semana 07
usando `create_connected_server_and_client_session`.

---

## 📋 Requisitos previos

- Semana 07 completada (Library Server con SQLite)
- Material teórico de esta semana leído

---

## 🗂️ Estructura

```
practica-01-tests-pytest/
└── starter/
    ├── pyproject.toml
    ├── conftest.py
    └── tests/
        └── test_library_server.py
```

---

## ⚙️ Setup

```bash
cd starter
uv sync --group test
uv run pytest -v
```

---

## 📝 Pasos

### Paso 1: Fixture de base de datos en memoria

Abre `conftest.py`. Descomenta la sección **PASO 1**.

```python
# El fixture crea una DB SQLite en memoria para cada test.
# Así cada test tiene un estado limpio y predecible.
```

Verifica que pytest puede importar el módulo:

```bash
uv run pytest --collect-only
```

---

### Paso 2: Fixture del client MCP

Descomenta la sección **PASO 2** en `conftest.py`.

```python
# El fixture mcp_client conecta al server en memoria.
# create_connected_server_and_client_session hace toda la magia:
# protocolo MCP completo sin sockets ni procesos externos.
```

Verifica que el fixture funciona:

```bash
uv run pytest -v -k "test_list_tools"
```

---

### Paso 3: Tests de add_book

Descomenta la sección **PASO 3** en `tests/test_library_server.py`.

```python
# Tres tests para add_book:
# - success: retorna id numérico válido
# - crea libro recuperable con get_book
# - title vacío retorna error de validación
```

Ejecuta:

```bash
uv run pytest -v -k "TestAddBook"
```

---

### Paso 4: Tests de search y delete

Descomenta la sección **PASO 4** en `tests/test_library_server.py`.

```python
# Tests para search_books y delete_book:
# - search encuentra libros agregados
# - search retorna vacío cuando no hay resultados
# - delete elimina el libro correctamente
# - delete retorna error para ID inexistente
```

Ejecuta:

```bash
uv run pytest -v -k "TestSearch or TestDelete"
```

---

### Paso 5: Tests de update_book y cobertura

Descomenta la sección **PASO 5** y ejecuta con cobertura:

```bash
uv run pytest --cov=. --cov-report=term-missing -v
```

Objetivo: ver al menos **75% de cobertura**.

---

## ✅ Verificación final

```bash
# Todos los tests deben pasar
uv run pytest -v

# Cobertura ≥ 75%
uv run pytest --cov=. --cov-report=term-missing
```

---

[← Volver a prácticas](../README.md)
