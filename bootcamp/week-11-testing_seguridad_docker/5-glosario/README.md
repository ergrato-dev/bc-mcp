# Glosario — Semana 11: Testing, Seguridad y Docker

Términos clave de esta semana, ordenados alfabéticamente.

---

### .dockerignore

Archivo que lista los archivos y directorios a excluir al construir una imagen Docker.
Equivalente al `.gitignore` pero para el contexto de build de Docker.

### AAA (Arrange-Act-Assert)

Patrón de organización de tests en tres fases: Arrange (preparar datos),
Act (ejecutar la acción), Assert (verificar el resultado esperado).

### asyncio.timeout()

Gestor de contexto de Python 3.11+ que cancela una operación async si supera
el tiempo límite. Previene que el server quede bloqueado esperando una API externa.

### Bandit

Herramienta de análisis estático de seguridad para Python. Detecta patrones
de código potencialmente inseguros (SQL injection, hardcoded passwords, etc.).

### Builder stage

Primera etapa de un Dockerfile multi-stage. Instala dependencias de build y
compilación. Su contenido no se incluye en la imagen final de runtime.

### Coverage

Porcentaje de código fuente ejecutado durante la ejecución de los tests.
Se mide con `pytest-cov` (Python) o `@vitest/coverage-v8` (TypeScript).

### create_connected_server_and_client_session

Función del MCP Python SDK que crea un par servidor-cliente conectados en
memoria. Permite tests de integración sin abrir sockets ni procesos externos.

### Docker Scout

Herramienta de Docker para escanear imágenes en busca de CVEs (vulnerabilidades
conocidas) en las dependencias instaladas.

### DoS (Denial of Service)

Ataque que busca agotar recursos del servidor (CPU, memoria, conexiones) para
dejarlo inoperativo. En MCP, puede ocurrir si un LLM llama a una tool infinitamente.

### Field (Pydantic)

Función de Pydantic v2 para configurar validaciones de un campo de modelo:
`min_length`, `max_length`, `ge`, `le`, `pattern`, `default`, etc.

### field_validator

Decorador de Pydantic v2 para definir validadores personalizados que se ejecutan
antes (`mode="before"`) o después de la validación estándar.

### Fixture

En pytest, función decorada con `@pytest.fixture` que provee recursos reutilizables
a los tests. Se usa para setup/teardown de DB, clients MCP, mocks, etc.

### InMemoryTransport

Transport del MCP TypeScript SDK que opera completamente en memoria.
`InMemoryTransport.createLinkedPair()` crea dos extremos conectados para tests.

### Multi-stage build

Técnica de Dockerfile que usa múltiples instrucciones `FROM`. Cada stage puede
copiar artefactos de stages anteriores con `COPY --from=<stage>`. Reduce el
tamaño de la imagen final.

### OWASP

Open Web Application Security Project. Organización sin fines de lucro que
publica guías de seguridad, incluyendo el OWASP Top 10 (vulnerabilidades más comunes).

### Parameterized query

Query SQL que usa marcadores `?` en lugar de concatenar valores directamente.
El driver de DB sanitiza los parámetros, eliminando el riesgo de SQL injection.

### Path traversal

Vulnerabilidad que permite acceder a archivos fuera del directorio permitido
usando secuencias como `../../etc/passwd`. Se mitiga con `Path.resolve()` +
`is_relative_to()` en Python.

### pip-audit

Herramienta que audita las dependencias Python instaladas contra bases de datos
de CVEs conocidos. Equivalente a `pnpm audit` para el ecosistema Python.

### Prompt injection

Ataque donde instrucciones maliciosas en el contenido procesado por el LLM
intentan modificar el comportamiento del sistema. Difícil de eliminar
completamente; se mitiga con separación clara de roles.

### Rate limiting

Técnica para limitar la cantidad de llamadas a un endpoint o función por
unidad de tiempo. Previene abuso de APIs externas y ataques DoS.

### Runtime stage

Segunda etapa de un Dockerfile multi-stage. Contiene solo lo necesario para
ejecutar la aplicación: código y dependencias de producción.

### SQL injection

Ataque que inyecta SQL malicioso en queries construidas con concatenación de
strings. Siempre usar queries parametrizadas (`?` en SQLite, `$1` en PostgreSQL).

### uv

Gestor de paquetes Python ultrarrápido escrito en Rust. Reemplaza a pip/pipenv/poetry.
En Docker: `pip install uv` en el builder, luego `uv sync --frozen --no-dev`.

### ValidationError

Excepción de Pydantic v2 lanzada cuando los datos no cumplen con el schema.
Contiene una lista de errores con campo, tipo y mensaje descriptivo.

### vitest

Test runner moderno para TypeScript/JavaScript, compatible con la API de Jest.
Soporta ESM nativo, TypeScript sin transpilación y watch mode integrado.

### create_connected_server_and_client_session

Helper del SDK MCP Python para crear pares server/client en memoria para tests

### pytest-asyncio

Plugin de pytest para testear código async con async/await

### vitest

Framework de testing para TypeScript/JavaScript moderno y rápido

---

[← Volver al README de la semana](../README.md)
