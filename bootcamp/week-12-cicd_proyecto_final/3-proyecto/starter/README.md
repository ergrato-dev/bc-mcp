# 📚 MCP Library Server — Proyecto Final

[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-2496ED?logo=docker&logoColor=white)](https://ghcr.io/OWNER/REPO)
[![Python](https://img.shields.io/badge/python-3.13-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Proyecto final del Bootcamp MCP Zero to Hero — Semana 12.
> Sistema MCP completo: server Python con 7 tools + client LLM con Claude + CI/CD + Docker.

## 🏗️ Arquitectura

```
┌────────────────────────────────────────────────────┐
│                  docker compose                    │
│                                                    │
│  ┌─────────────────┐    MCP     ┌───────────────┐ │
│  │   MCP Server    │◄──────────►│  MCP Client   │ │
│  │   Python 3.13   │  HTTP+SSE  │  + Claude LLM │ │
│  │   :8000/sse     │            │               │ │
│  └────────┬────────┘            └───────────────┘ │
│           │                                        │
│  ┌────────▼────────┐   ┌───────────────────────┐  │
│  │    SQLite DB    │   │    OpenLibrary API     │  │
│  │  /data/lib.db   │   │  openlibrary.org       │  │
│  └─────────────────┘   └───────────────────────┘  │
└────────────────────────────────────────────────────┘
```

## ✨ Tools MCP disponibles

| Tool | Descripción | Parámetros |
|------|-------------|-----------|
| `search_books` | Busca libros por título o autor | `query: str`, `limit: int = 10` |
| `get_book` | Obtiene un libro por ID | `book_id: int` |
| `add_book` | Añade un libro a la biblioteca | `title: str`, `author: str`, `year: int` |
| `update_book` | Actualiza campos de un libro | `book_id: int`, `title?: str`, `author?: str`, `year?: int` |
| `delete_book` | Elimina un libro | `book_id: int` |
| `search_openlibrary` | Busca en OpenLibrary.org | `title: str` |
| `enrich_book` | Enriquece un libro con datos externos | `book_id: int` |

## 🚀 Setup

```bash
# Clonar y navegar al directorio
cd bootcamp/week-12-cicd_proyecto_final/3-proyecto/starter

# Copiar y configurar variables de entorno
cp .env.example .env
# Editar .env: añadir ANTHROPIC_API_KEY

# Levantar el entorno con Docker
docker compose up --build
```

## Estructura Esperada

Implementa el proyecto según las instrucciones en [`../README.md`](../README.md).

## TODO

Implementa los entregables descritos en [`../README.md`](../README.md#-entregables).

---

[← Volver al proyecto](../README.md)
