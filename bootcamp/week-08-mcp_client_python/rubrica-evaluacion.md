# Rúbrica de Evaluación — Semana 08: MCP Client en Python

## 📊 Distribución de Puntos

| Tipo de Evidencia | Peso | Puntos |
|-------------------|------|--------|
| Conocimiento 🧠   | 30%  | 30 pts |
| Desempeño 💪      | 40%  | 40 pts |
| Producto 📦       | 30%  | 30 pts |

**Criterio de aprobación**: Mínimo **70 puntos** (70%) en total,
con mínimo **21 pts** en cada tipo de evidencia.

---

## 🧠 Conocimiento (30 pts)

| Criterio | Excelente (30) | Satisfactorio (21) | Insuficiente (<21) |
|----------|---------------|--------------------|--------------------|
| Arquitectura client/server | Explica con precisión qué hace cada capa: App, ClientSession, StdioTransport | Explica las capas con errores menores | Confunde el rol del client con el del server |
| Ciclo de vida de la sesión | Describe correctamente: launch → connect → initialize → use → close | Describe los pasos principales con algún error | No puede describir el ciclo de vida |
| Tipos de contenido | Distingue TextContent, ImageContent y EmbeddedResource y cómo procesarlos | Conoce TextContent; confunde los otros dos | No conoce los tipos o no sabe cómo procesarlos |
| isError vs McpError | Explica la diferencia: dominio vs protocolo, con ejemplos | Distingue ambos casos con algún error | Confunde ambos tipos de error |

---

## 💪 Desempeño (40 pts)

### Prácticas (20 pts)

| Práctica | Completa (5 pts) | Parcial (3 pts) | Incompleta (0 pts) |
|----------|-----------------|-----------------|-------------------|
| P01 — Primer client | Se conecta e imprime serverInfo y capabilities | Se conecta pero sin datos completos | No conecta |
| P02 — Descubrir capacidades | Lista tools con schema, resources y prompts | Lista tools sin schema | No lista nada |
| P03 — Invocar tools | call_tool + JSON + isError + read_resource | Solo call_tool sin isError | No funciona |
| P04 — CLI interactivo | Loop completo con search, stats, quit | Loop básico sin stats | No funciona |

### Calidad de código (20 pts)

| Criterio | Excelente (20) | Satisfactorio (14) | Insuficiente (<14) |
|----------|---------------|--------------------|--------------------|
| Type hints | Todas las funciones tienen type hints correctos | La mayoría tiene type hints | Sin type hints |
| async/await | Uso correcto de `async with`, `await`, `run_in_executor` | Mayormente correcto con errores menores | Mezcla sync/async incorrectamente |
| Manejo de errores | `isError`, `McpError`, `BrokenPipeError` manejados | Al menos `isError` manejado | Sin manejo de errores |
| Patrón `async with` | Usa los dos `async with` anidados correctamente | Usa solo uno o incorrectamente | No usa context managers |

---

## 📦 Producto (30 pts)

### Funcionalidad del CLI (20 pts)

| Entregable | Completo (pts) | Descripción |
|-----------|---------------|-------------|
| `connect_to_server()` | 4 pts | StdioServerParameters + stdio_client + ClientSession + initialize |
| `list_available_tools()` | 2 pts | Imprime nombre y descripción de cada tool |
| `search_books()` | 4 pts | call_tool + JSON + isError → lista de dicts |
| `add_book()` | 4 pts | call_tool con args opcionales + isError → dict con ID |
| `search_openlibrary()` | 3 pts | call_tool API externa + isError → lista |
| `interactive_loop()` | 3 pts | Loop con 5+ comandos y shutdown graceful |

### Calidad del proyecto (10 pts)

| Criterio | Excelente (10) | Satisfactorio (7) | Insuficiente (<7) |
|----------|---------------|-------------------|-------------------|
| `.env.example` completo | Todas las variables documentadas con comentarios | Variables presentes sin comentarios | Faltan variables esenciales |
| `pyproject.toml` correcto | Versiones exactas (sin ^, ~), Python 3.13+ | Versiones exactas pero sin pinning de Python | Versiones flotantes (^, ~, *) |
| `Dockerfile.python` funcional | Construye y corre correctamente con `docker compose` | Construye pero falla al ejecutar | No construye |
| `config.py` robusto | Valida variables requeridas con mensaje de error claro | Lee variables sin validación | No usa config.py |

---

## 📝 Notas del Evaluador

_Espacio para comentarios personalizados del instructor._

---

**Evaluado por**: _________________ · **Fecha**: _________________ · **Puntuación total**: _____ / 100
