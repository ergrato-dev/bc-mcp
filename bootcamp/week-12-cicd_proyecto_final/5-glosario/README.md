# Glosario — Semana 12: CI/CD y Proyecto Final Integrador

Términos clave de esta semana, ordenados alfabéticamente.

---

### Action

Unidad reutilizable de GitHub Actions (ej. `actions/checkout@v4`, `docker/build-push-action@v6`). Se reutiliza desde el Marketplace o desde el mismo repositorio.

### Agentic loop

Patrón de ejecución LLM donde el modelo decide qué tool llamar, recibe el resultado y decide si continuar llamando más tools o dar la respuesta final. Termina cuando `stop_reason == "end_turn"`.

### Artifact

Archivo generado por un job de CI (ej. reporte de cobertura `coverage.xml`) y almacenado temporalmente con `actions/upload-artifact`. Otro job puede descargarlo con `actions/download-artifact`.

### Badge

Imagen dinámica en el README que muestra el estado del CI, cobertura, versión de Python, licencia, etc. Se genera con shields.io o directamente por GitHub Actions.

### Build context

Conjunto de archivos enviados al daemon de Docker al ejecutar `docker build`. Se controla con `.dockerignore` para excluir archivos innecesarios y reducir el tamaño del contexto.

### Cache layer

Capa de imagen Docker almacenada en caché para evitar reinstalar dependencias en cada build. En GitHub Actions, se usa `cache-from: type=gha` con `docker/build-push-action`.

### CI/CD

Continuous Integration / Continuous Delivery — automatización del ciclo: commit → lint → test → build → push → deploy. CI verifica que el código no rompe nada; CD entrega la versión al entorno destino.

### Conventional Commits

Especificación de formato de commits: `type(scope): description`. Permite generar CHANGELOG automático. Tipos principales: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `ci`.

### GHCR

GitHub Container Registry (`ghcr.io`) — registro de imágenes Docker integrado con GitHub. La autenticación usa `GITHUB_TOKEN` sin configuración extra.

### GitHub Actions

Plataforma de CI/CD integrada en GitHub con workflows YAML en `.github/workflows/`. Ofrece runners gratuitos (ubuntu, windows, macOS) y 2000 min/mes en repos públicos.

### HTTP + SSE

Transport de MCP para producción (en lugar de stdio). El servidor expone un endpoint HTTP SSE en `/sse` y el cliente usa `sse_client()` para conectarse. Permite múltiples clientes concurrentes.

### if:

Condición en GitHub Actions que controla si un step o job se ejecuta. Ejemplo: `if: github.event_name == 'push' && github.ref == 'refs/heads/main'` (solo en push a main, no en PRs).

### Job

Grupo de steps en un workflow de GitHub Actions que se ejecutan secuencialmente en un runner. Los jobs se pueden paralelizar o secuenciar con `needs:`.

### MAJOR.MINOR.PATCH

Los tres componentes de Semantic Versioning: MAJOR (cambio incompatible), MINOR (nueva funcionalidad compatible), PATCH (fix compatible). Ejemplo: `2.4.1`.

### Metadata action

`docker/metadata-action@v5` — genera automáticamente tags y labels Docker a partir de eventos de GitHub (ramas, tags `v*`, SHA de commit). Evita escribir los tags manualmente.

### Multi-stage build

Técnica Docker para separar el proceso de compilación/instalación (builder) de la imagen final de producción (runtime). Reduce drásticamente el tamaño de la imagen final.

### needs:

Palabra clave en GitHub Actions que define dependencias entre jobs. `needs: lint` hace que el job espere a que `lint` termine con éxito antes de ejecutarse.

### Pre-release

Versión con sufijo: `1.0.0-alpha.1`, `2.0.0-beta.3`, `3.0.0-rc.1`. En SemVer, indica que no es una versión estable para producción.

### Release

Versión publicada con tag `vX.Y.Z` en GitHub. Puede incluir release notes, CHANGELOG y artefactos descargables. Dispara workflows con `on: push: tags: ["v*"]`.

### Runner

Máquina virtual que ejecuta los jobs de GitHub Actions. Los más usados: `ubuntu-latest` (Linux), `windows-latest`, `macos-latest`. También hay self-hosted runners.

### Semantic versioning

Esquema de versiones MAJOR.MINOR.PATCH definido en semver.org. Permite comunicar el impacto de una actualización: un MAJOR indica breaking changes, MINOR nuevas features, PATCH solo fixes.

### Step

Unidad mínima de un job en GitHub Actions. Puede ser una action (`uses:`) o un comando shell (`run:`). Los steps se ejecutan secuencialmente en el mismo runner.

### Supply chain attack

Ataque que inyecta código malicioso a través de dependencias o actions de terceros. Se mitiga fijando versiones exactas (sin `^`, `~`, `>=`) y usando `sha256` en actions críticas.

### Trigger

Evento que inicia un workflow de GitHub Actions. Los más comunes: `push`, `pull_request`, `schedule`, `workflow_dispatch` (manual), `release`.

### Workflow

Archivo YAML en `.github/workflows/` que define el pipeline de CI/CD. Contiene triggers (`on:`), jobs y steps. Un repositorio puede tener múltiples workflows independientes.

### workflow_dispatch

Trigger especial que permite ejecutar un workflow manualmente desde la UI de GitHub o via API. Útil para deploys manuales o tareas de mantenimiento.

---

[← Volver al README de la semana](../README.md)
