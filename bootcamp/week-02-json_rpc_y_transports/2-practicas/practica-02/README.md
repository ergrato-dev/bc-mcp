# Práctica 02 — MCP Server con Transport stdio

## Objetivo

Implementar un MCP Server funcional con transport stdio, tanto en Python
como en TypeScript, y verificarlo con MCP Inspector.

## Tiempo estimado: 60 minutos

---

## Paso 1: Preparar el entorno Python

```bash
cd starter/python/
docker compose up --build
```

Esto construye la imagen con el servidor Python y lo conecta a MCP Inspector.

---

## Paso 2: Completar el servidor Python

**Abre `starter/python/src/server.py`** y descomenta las secciones en orden:

### Sección A — Importaciones y setup del servidor

```python
# Descomenta cuando llegues a la Sección A en server.py
```

### Sección B — Handler list_tools

```python
# Descomenta cuando llegues a la Sección B en server.py
```

### Sección C — Handler call_tool

```python
# Descomenta cuando llegues a la Sección C en server.py
```

### Sección D — Función main y entrada

```python
# Descomenta cuando llegues a la Sección D en server.py
```

Después de cada sección: reinicia el contenedor y verifica en MCP Inspector.

---

## Paso 3: Verificar con MCP Inspector

1. Abre http://localhost:6274
2. Conecta al servidor Python (ya configurado en docker-compose.yml)
3. Navega a la pestaña **Tools**
4. Deberías ver el tool `calculate` listado
5. Prueba el tool con diferentes valores

---

## Paso 4: Completar el servidor TypeScript

**Abre `starter/typescript/src/index.ts`** y repite el proceso para TypeScript:
descomenta sección por sección, reiniciando y verificando con MCP Inspector.

---

## Paso 5: Comparar las dos implementaciones

Abre ambos archivos y responde:

- ¿Qué diferencias sintácticas hay entre Python y TypeScript para definir el mismo tool?
- ¿Cómo difiere el manejo de errores (try/catch vs raise)?
- ¿Qué ocurre si agregas un `print()` en Python o `console.log()` en TypeScript?

---

## Verificación

- [ ] El servidor Python responde a `tools/list` con el tool `calculate`
- [ ] `tools/call` con `{"a": 5, "b": 3, "op": "add"}` retorna `8`
- [ ] El servidor TypeScript hace lo mismo
- [ ] Confirmé que `print()` / `console.log()` rompe la comunicación stdio

---

[← Práctica 01](../practica-01/README.md) | [Práctica 03 →](../practica-03/README.md)
