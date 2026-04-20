# 📚 MCP Library Server

<!-- PASO 3: Añade los badges aquí -->
<!-- Reemplaza OWNER y REPO con tu usuario y nombre de repositorio de GitHub -->

<!-- Badge de CI: muestra si el pipeline pasa -->
<!-- [![CI](https://github.com/OWNER/REPO/actions/workflows/ci-python.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci-python.yml) -->

<!-- Badge de Docker: enlaza a la imagen en GHCR -->
<!-- [![Docker](https://img.shields.io/badge/docker-ghcr.io-2496ED?logo=docker&logoColor=white)](https://ghcr.io/OWNER/REPO) -->

<!-- Badge de Python versión -->
<!-- [![Python](https://img.shields.io/badge/python-3.13-3776AB?logo=python&logoColor=white)](https://python.org) -->

<!-- Badge de licencia -->
<!-- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) -->

---

<!-- PASO 4: Descripción del proyecto -->
<!-- Explica en 2-3 líneas qué hace tu MCP Server, qué problema resuelve y qué tecnologías usa -->

<!-- > Servidor MCP para gestión de biblioteca con integración a OpenLibrary API. -->
<!-- > Construido con Python 3.13, FastMCP y SQLite. Incluye client LLM con Claude. -->

---

<!-- PASO 4 (continuación): Diagrama de arquitectura -->
<!-- Añade un SVG o imagen del sistema -->

<!-- ## 🏗️ Arquitectura -->

<!-- ![Arquitectura del Sistema](docs/architecture.svg) -->

---

<!-- PASO 5: Tabla de tools MCP disponibles -->
<!-- Lista todos los tools del servidor con parámetros y descripción -->

<!-- ## ✨ Tools disponibles -->

<!-- | Tool | Descripción | Parámetros | -->
<!-- |------|-------------|----------| -->
<!-- | `search_books` | Busca libros por título o autor | `query: str`, `limit: int = 10` | -->
<!-- | `get_book` | Obtiene un libro por ID | `book_id: int` | -->
<!-- | `add_book` | Añade un nuevo libro | `title: str`, `author: str`, `year: int` | -->
<!-- | `update_book` | Actualiza un libro | `book_id: int`, `title?: str`, `author?: str` | -->
<!-- | `delete_book` | Elimina un libro | `book_id: int` | -->
<!-- | `search_openlibrary` | Busca en OpenLibrary.org | `title: str` | -->
<!-- | `enrich_book` | Enriquece con datos externos | `book_id: int` | -->

---

<!-- PASO 6: Instalación con Docker -->

<!-- ## 🚀 Instalación rápida -->

<!-- ```bash -->
<!-- git clone https://github.com/OWNER/REPO.git -->
<!-- cd REPO -->
<!-- cp .env.example .env -->
<!-- # Editar .env: añadir ANTHROPIC_API_KEY -->
<!-- docker compose up --build -->
<!-- ``` -->

---

<!-- PASO 7: Variables de entorno -->

<!-- ## 🔧 Variables de entorno -->

<!-- | Variable | Descripción | Requerida | Por defecto | -->
<!-- |----------|-------------|-----------|-------------| -->
<!-- | `ANTHROPIC_API_KEY` | API key de Anthropic | Sí | — | -->
<!-- | `DB_PATH` | Ruta a la base de datos SQLite | No | `./library.db` | -->
<!-- | `OPENLIBRARY_URL` | URL base de OpenLibrary | No | `https://openlibrary.org` | -->
<!-- | `MAX_SEARCH_RESULTS` | Máximo de resultados | No | `20` | -->

---

## 🧪 Desarrollo

```bash
pip install --no-cache-dir uv==0.6.6
uv sync --frozen --group test
uv run pytest --cov=src
uv run ruff check .
```

---

## 📄 Licencia

MIT — ver [LICENSE](LICENSE)
