# Rúbrica de Evaluación — Semana 09: MCP Client en TypeScript

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

### Prácticas (20 pts — 5 pts cada una)

| Práctica | 5 pts (excelente) | 3-4 pts (satisfactorio) | 0-2 pts (insuficiente) |
|----------|-------------------|-------------------------|------------------------|
| P01 — Primer client | Descomenta y ejecuta los 4 PASOs. El server conecta e imprime nombre y versión | Completa 3 de 4 PASOs. El client conecta | No conecta o menos de 3 PASOs |
| P02 — Descubrir capacidades | Imprime tools (con params requeridos marcados), resources y prompts | Imprime tools y resources. Prompts incompleto | Solo imprime tools |
| P03 — Invocar tools | Completa los 5 PASOs: search, isError, add, readResource | 3-4 PASOs completos | Menos de 3 PASOs |
| P04 — CLI interactivo | Bucle readline funcional con search, tools, stats y quit | search y stats funcionan. quit funciona | Solo se conecta |

### Calidad del código (20 pts)

| Criterio | Excelente (20) | Satisfactorio (14) | Insuficiente (<14) |
|----------|---------------|--------------------|--------------------|
| Tipado TypeScript | Discriminated unions correctas, sin `any`, tipos inferidos | Usa types en la mayoría de casos, `any` mínimo | Uso frecuente de `any`, tipos incorrectos |
| `isError` handling | Siempre verifica `isError` antes de parsear content | Verifica en la mayoría de los casos | No verifica `isError` — posibles crashes |
| Async/await | Correcto uso de `await`, try/finally con `client.close()` | Await presente pero falta finally en algún caso | Mezcla sync/async o falta cierre del client |

---

## 📦 Producto (30 pts)

### TODOs del proyecto (18 pts — 3 pts cada TODO)

| TODO | 3 pts | 1-2 pts | 0 pts |
|------|-------|---------|-------|
| TODO 1 — `connectToServer()` | Crea transport con `...process.env`, conecta y retorna client | Conecta pero sin env o sin try/finally | No implementado o no conecta |
| TODO 2 — `listAvailableTools()` | Lista nombre + descripción de todos los tools | Lista solo nombres | No implementado |
| TODO 3 — `searchBooks()` | `callTool` → `isError` check → `JSON.parse as Book[]` | Parsea pero sin verificar `isError` | No implementado |
| TODO 4 — `addBook()` | `callTool` → `isError` → parsea Book con id asignado | Llama al tool pero no parsea correctamente | No implementado |
| TODO 5 — `searchOpenLibrary()` | `callTool` → parsea `OpenLibraryResult[]` | Llama al tool pero retorna `any[]` | No implementado |
| TODO 6 — `interactiveLoop()` | Bucle con search/add/ol/stats/quit. readline cerrado en finally | Al menos 4 comandos funcionan | Menos de 4 comandos |

### Calidad general del producto (12 pts)

| Criterio | Excelente (12) | Satisfactorio (8) | Insuficiente (<8) |
|----------|---------------|--------------------|--------------------|
| Funcionalidad end-to-end | El CLI se conecta al server de semana 07 y ejecuta todos los comandos | Los comandos principales (search, stats) funcionan | No conecta o crashes frecuentes |
| Entregables completos | Todos los TODOs marcados como implementados | 4-5 TODOs implementados | Menos de 4 TODOs |

---

## 📝 Notas del Evaluador

_Espacio para comentarios personalizados del instructor._

---

**Evaluado por**: _________________ · **Fecha**: _________________ · **Puntuación total**: _____ / 100
