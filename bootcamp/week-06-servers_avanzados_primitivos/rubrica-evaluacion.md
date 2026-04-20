# Rúbrica de Evaluación — Semana 06: Servers Avanzados — Los 3 Primitivos

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
| Comprensión de Resources | Explica la diferencia entre resource estático y template, protocolo list/read | Explica el concepto principal con algún error menor | No distingue resources de tools |
| Comprensión de Prompts | Explica prompts/list vs prompts/get, argumentos requeridos/opcionales | Explica el concepto pero confunde algunos detalles | No comprende la diferencia con un tool |
| Terminología MCP | Usa correctamente: URI scheme, resource template, prompt argument, Context, state | Usa la mayoría de los términos correctamente | Confunde o no usa la terminología |
| Casos de uso | Justifica cuándo usar tool vs resource vs prompt con criterio técnico | Identifica los casos de uso principales | No puede justificar la elección de primitivo |

### Preguntas de evaluación oral (conocimiento)

1. ¿Cuándo usarías un Resource en lugar de un Tool para exponer datos?
2. ¿Qué diferencia hay entre `@mcp.resource("tasks://all")` y `@mcp.resource("tasks://{id}")`?
3. ¿Qué retorna `prompts/get`? ¿En qué formato?
4. ¿Por qué los Resources deben ser solo lectura?
5. ¿Qué es el objeto `Context` en FastMCP y para qué se usa?

---

## 💪 Desempeño (40 pts)

| Criterio | Excelente (40) | Satisfactorio (28) | Insuficiente (<28) |
|----------|---------------|--------------------|--------------------|
| Prácticas completadas | Completa las 4 prácticas con código correcto y sin errores | Completa 3 de 4 prácticas | Completa menos de 2 prácticas |
| Resources correctos | Resources estáticos y templates funcionan, mimeType correcto | Resources estáticos funcionan, templates con errores menores | Resources no responden o retornan formato incorrecto |
| Prompts correctos | Prompts con argumentos funcionan, mensajes bien formados | Prompts sin argumentos funcionan | Prompts no registrados o mensajes mal formados |
| Calidad del código Python | Type hints, async, nombres snake_case, docstrings en tools/resources | Código funcional con mejoras menores | Sin type hints o código síncrono en I/O |
| Calidad del código TypeScript | Tipos estrictos, ESM imports, manejo correcto de `as const` | Código funcional con mejoras menores | `any` generalizado o errores de tipos |

### Checklist de desempeño

- [ ] practica-01: `books://all`, `books://available`, `books://{isbn}` funcionan en Python
- [ ] practica-02: `books://all`, `books://available`, `books://isbn/{isbn}` funcionan en TypeScript
- [ ] practica-03: Prompts con y sin argumentos funcionan en Python y TypeScript
- [ ] practica-04: Server completo con tools + resources + prompts en ambos lenguajes
- [ ] Cada práctica arranca con `docker compose up --build` sin errores

---

## 📦 Producto (30 pts)

| Criterio | Excelente (30) | Satisfactorio (21) | Insuficiente (<21) |
|----------|---------------|--------------------|--------------------|
| Server Python funcional | Tools, Resources (estáticos + template) y Prompts funcionan en MCP Inspector | Los 3 primitivos están registrados pero algún detalle falla | El server no arranca o falta algún primitivo |
| Server TypeScript funcional | Tools, Resources (estáticos + template) y Prompts funcionan en MCP Inspector | Los 3 primitivos están registrados pero algún detalle falla | El server no arranca o falta algún primitivo |
| Estado compartido | Tools y Resources usan el mismo estado (crear una tarea → aparece en el resource) | El estado es compartido pero con inconsistencias menores | Estado duplicado o separado entre primitivos |
| Docker correcto | `docker compose up --build` levanta ambos servers sin advertencias | Levanta con advertencias menores | No levanta o requiere pasos manuales |

### Checklist de producto

- [ ] `python-server`: `create_task` + `complete_task` + `list_tasks` + `get_task_stats` funcionan
- [ ] `python-server`: `tasks://all`, `tasks://pending`, `tasks://done`, `tasks://{id}` funcionan
- [ ] `python-server`: `daily_review(date)` + `productivity_report()` retornan mensajes correctos
- [ ] `ts-server`: misma funcionalidad que el Python server
- [ ] Verificado en MCP Inspector (screenshots o log de pruebas)

---

## 📝 Notas del Evaluador

_Espacio para comentarios personalizados del instructor._

---

**Evaluado por**: _________________ · **Fecha**: _________________ · **Puntuación total**: _____ / 100
