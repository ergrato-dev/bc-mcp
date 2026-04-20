# Práctica 03 — Validación de inputs con Pydantic

## 🎯 Objetivo

Agregar validación robusta de inputs a las tools del Library Server
usando modelos Pydantic v2.

---

## 🗂️ Estructura

```
practica-03-validacion-pydantic/
└── starter/
    ├── pyproject.toml
    └── src/
        ├── validators.py    ← modelos Pydantic a descomentar
        └── server_demo.py   ← server de demo con validación
```

---

## ⚙️ Setup

```bash
cd starter
uv sync
uv run python src/server_demo.py
```

---

## 📝 Pasos

### Paso 1: Modelo AddBookInput

Abre `src/validators.py`. Descomenta la sección **PASO 1**.

```python
# AddBookInput valida título, autor, año e ISBN.
# Field(...) define límites y patrones de forma declarativa.
```

Prueba en Python interactivo:

```bash
uv run python -c "from src.validators import AddBookInput; print(AddBookInput(title='  Dune  ', author='Herbert', year=1965))"
```

Debes ver el título sin espacios extra: `title='Dune'`.

---

### Paso 2: Modelo SearchBooksInput

Descomenta la sección **PASO 2** en `src/validators.py`.

```python
# SearchBooksInput limita el tamaño del query y el resultado máximo.
# Previene queries muy largos que podrían indicar un ataque DoS.
```

---

### Paso 3: Integración en una tool

Descomenta la sección **PASO 3** en `src/server_demo.py`.

```python
# La tool add_book_validated usa AddBookInput para validar antes de
# hacer cualquier operación con la base de datos.
# Si la validación falla, retorna un error descriptivo al LLM.
```

---

### Paso 4: Manejo de errores de validación

Descomenta la sección **PASO 4** y prueba casos de error:

```bash
# En el Inspector MCP, enviar:
# add_book_validated(title="", author="x", year=1965)
# → debe retornar error de validación
```

---

## ✅ Verificación

```bash
uv run python -c "
from src.validators import AddBookInput, SearchBooksInput
# Test AddBookInput
book = AddBookInput(title='  Clean Code  ', author='Martin', year=2008)
assert book.title == 'Clean Code'  # strip aplicado

# Test límites
try:
    AddBookInput(title='', author='x', year=2008)
    assert False, 'Debe lanzar ValidationError'
except Exception as e:
    print('✅ Validación OK:', type(e).__name__)

# Test SearchBooksInput
search = SearchBooksInput(query='python', limit=5)
assert search.limit == 5
print('✅ Todos los modelos válidos')
"
```

[← Volver a prácticas](../README.md)
