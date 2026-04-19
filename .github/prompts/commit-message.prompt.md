---
description: "Genera un mensaje de commit siguiendo Conventional Commits con el formato What/For/Impact adaptado a bc-mcp."
mode: "agent"
---

Genera un mensaje de commit para los cambios actuales del repositorio bc-mcp.

## Proceso

1. Ejecuta `git diff --staged --stat` para ver los archivos en staging
2. Ejecuta `git diff --staged` para ver los cambios en detalle
3. Si no hay nada en staging, ejecuta `git diff --stat` para ver cambios no staged

## Formato obligatorio

```
<tipo>(<scope>): <descripción concisa en imperativo, máx 72 chars>

What?   <qué cambios se hicieron>
For?    <por qué era necesario — motivación o contexto>
Impact? <qué habilita o afecta este cambio>

Changes: X archivos modificados (+adiciones -eliminaciones)
```

## Tipos válidos

| Tipo       | Cuándo usarlo                                                |
| ---------- | ------------------------------------------------------------ |
| `feat`     | Nuevo contenido de semana, nueva práctica, nuevo server/tool |
| `fix`      | Corrección de código de ejemplo, error en instrucciones      |
| `docs`     | Cambios en README, teoría, glosario                          |
| `chore`    | Estructura de carpetas, assets, configuración                |
| `refactor` | Reorganización de contenido sin cambio funcional             |
| `test`     | Añadir o corregir tests de ejemplos                          |
| `ci`       | GitHub Actions, workflows                                    |
| `style`    | Formato de código, sin cambios de lógica                     |

## Scopes recomendados

- `week-{NN}` — contenido de una semana específica (ej. `week-04`)
- `server` — código de un MCP server de ejemplo
- `tools` — tools MCP
- `resources` — resources MCP
- `prompts` — prompts MCP (primitivo)
- `client` — código de un MCP client
- `deps` — dependencias
- `ci` — integración continua
- `docs` — documentación global
- `assets` — recursos visuales SVG

## Ejemplos

```
feat(week-04): add complete Python MCP server week content

What?   Added theory, 3 guided practices and project starter for week 04
For?    Week 04 introduces students to their first Python MCP server
Impact? Students can now build and run a basic MCP server with stdio transport

Changes: 18 archivos modificados (+842 -0)
```

```
fix(week-06): correct SQL injection in search_database tool example

What?   Replace f-string interpolation with parameterized query in example
For?    Example had a SQL injection vulnerability visible to students
Impact? Students learn the secure pattern from the start

Changes: 2 archivos modificados (+4 -4)
```

```
chore(deps): pin all Python dependencies to exact versions

What?   Replace >= and ^ ranges with exact versions in all pyproject.toml files
For?    Floating ranges can install vulnerable versions automatically
Impact? Reproducible builds across all student environments

Changes: 7 archivos modificados (+35 -35)
```

## Reglas

- Siempre en **inglés**
- Descripción principal en **imperativo** ("add", "fix", "update" — no "added", "fixes")
- Máximo 72 caracteres en la primera línea
- Si los cambios afectan múltiples semanas, usar scope `bootcamp`
- No mencionar detalles de implementación obvios — explicar el "por qué"
