# Rúbrica de Evaluación — Semana 07: Servers con BD y APIs Externas

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
| Comprensión conceptual | Explica todos los conceptos con precisión y puede relacionarlos | Explica los conceptos principales con algunos errores menores | No comprende los conceptos clave de la semana |
| Terminología MCP | Usa correctamente toda la terminología del glosario | Usa la mayoría de los términos correctamente | Confunde o no usa la terminología del protocolo |
| Casos de uso | Identifica y justifica múltiples casos de uso con criterio técnico | Identifica los casos de uso principales | No logra justificar los casos de uso |

---

## 💪 Desempeño (40 pts)

| Criterio | Excelente (40) | Satisfactorio (28) | Insuficiente (<28) |
|----------|---------------|--------------------|--------------------|
| Ejercicios completados | Completa todos los ejercicios correctamente | Completa 70%+ de los ejercicios | Completa menos del 70% |
| Calidad del código | Código limpio, type hints, async correcto, sin warnings | Código funcional con mejoras menores posibles | Código con errores o malas prácticas |
| Comprensión del proceso | Puede explicar cada paso que realizó | Puede explicar la mayoría de los pasos | No puede explicar lo que hizo |

---

## 📦 Producto (30 pts)

| Criterio | Excelente (30) | Satisfactorio (21) | Insuficiente (<21) |
|----------|---------------|--------------------|--------------------|
| Funcionalidad | Todos los 7 tools del Library Manager funcionan correctamente | Al menos 5/7 tools funcionan, incluyendo CRUD básico | Menos de 4 tools funcionan |
| Integración BD + API | SQLite CRUD y Open Library API integrados, manejo de errores correcto | SQLite funciona; API externa con manejo de errores básico | No implementa alguna de las dos integraciones |
| Variables de entorno | `.env.example` completo; `.env` no committed; `DB_PATH`, `OPENLIBRARY_URL`, `MAX_SEARCH_RESULTS` configurables | Variables principales configuradas | Credenciales hardcodeadas en el código |
| Docker | `docker compose up --build` levanta ambos servidores sin errores | Al menos un servidor levanta correctamente con Docker | Docker no funciona |
| Documentación | README claro con instrucciones completas, tabla de tools y ejemplos de uso | README básico con instrucciones de setup | Sin README o instrucciones insuficientes |

---

## ✅ Checklist de Entregables

### Python Server
- [ ] `lifespan` con `aiosqlite.connect()` + `httpx.AsyncClient()` combinados
- [ ] Tool `search_books` con LIKE en título y autor
- [ ] Tool `get_book` retorna error `not_found` si el ID no existe
- [ ] Tool `add_book` guarda en SQLite con commit
- [ ] Tool `update_book` actualiza solo los campos provistos
- [ ] Tool `delete_book` verifica `rowcount > 0` antes de confirmar
- [ ] Tool `search_openlibrary` usa `raise_for_status()` y maneja timeout
- [ ] Tool `enrich_book` combina datos locales + API

### TypeScript Server
- [ ] `better-sqlite3` con schema inicializado
- [ ] Todos los 7 tools implementados con Zod validation
- [ ] Errores de "not found" devuelven `isError: true`
- [ ] `fetch` nativo con `AbortSignal.timeout()`

### Configuración
- [ ] `.env.example` con todas las variables documentadas
- [ ] `docker-compose.yml` con dos servicios
- [ ] `pyproject.toml` con dependencias exactas (sin `^` ni `~`)
- [ ] `package.json` con dependencias exactas

---

## 📝 Notas del Evaluador

_Espacio para comentarios personalizados del instructor._

---

**Evaluado por**: _________________ · **Fecha**: _________________ · **Puntuación total**: _____ / 100
