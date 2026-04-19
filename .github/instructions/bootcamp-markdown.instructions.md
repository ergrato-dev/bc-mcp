---
applyTo: "bootcamp/**/*.md"
---

# Convenciones de contenido Markdown — bc-mcp

## Idioma

- Documentación, READMEs, teoría y guías: **español**
- Código, variables, nombres de tools/resources: **inglés**
- Comentarios educativos en español cuando expliquen conceptos del protocolo MCP

## Estructura de README semanal

Todo `bootcamp/week-XX-*/README.md` debe incluir estas secciones en orden:

1. Header con imagen SVG del asset de semana
2. `## 🎯 Objetivos de aprendizaje` — lista de lo que el estudiante logrará
3. `## 📚 Requisitos previos` — semanas o conocimientos previos necesarios
4. `## 🗂️ Estructura de la semana` — listado de archivos/carpetas con descripción
5. `## 📝 Contenido` — enlaces a teoría y prácticas
6. `## ⏱️ Distribución del tiempo` — tabla con 8 horas desglosadas
7. `## 📌 Entregables` — qué debe entregar el estudiante
8. `## 🔗 Navegación` — links a semana anterior y siguiente

```markdown
[← Semana 01](../week-01-introduccion_mcp/README.md) | [Semana 03 →](../week-03-primitivos_mcp/README.md)
```

## Archivos de teoría (1-teoria/)

Estructura obligatoria:

```markdown
# Título del Tema

## 🎯 Objetivos

- Objetivo 1
- Objetivo 2

## 📋 Contenido

### 1. Introducción

### 2. Conceptos Clave

### 3. Ejemplos Prácticos

### 4. Ejercicios

## 📚 Recursos Adicionales

## ✅ Checklist de Verificación
```

## Diagramas y assets SVG

- ❌ NO usar ASCII art para diagramas de arquitectura- ✅ Cada archivo de teoría debe referenciar **al menos un SVG** de `0-assets/` que refuerce visualmente el concepto principal del archivo- ✅ Referenciar SVGs en `0-assets/` con descripción accesible
- Paleta: tema oscuro, morado MCP `#6B4FBB`, sin degradés

```markdown
![Diagrama de arquitectura MCP client-server](../0-assets/mcp-architecture.svg)
```

## Bloques de código

- Especificar siempre el lenguaje: ` ```python `, ` ```typescript `, ` ```bash `
- Para ejercicios (2-practicas/): código **comentado** para descomentar, sin TODOs
- Para proyectos (3-proyecto/): código con **TODOs** explícitos y numerados

````markdown
<!-- Ejercicio: código comentado -->

```python
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def add(a: int, b: int) -> int:
#     return a + b
```
````

<!-- Proyecto: TODOs -->

```python
# TODO: Implementar lógica de búsqueda
# 1. Conectar a la base de datos
# 2. Ejecutar query con LIKE
# 3. Retornar resultados
pass
```

```

## Semanas bilingües

Cuando una semana introduce un concepto nuevo de MCP, **siempre** incluir ejemplo funcional en Python Y TypeScript. No usar "ver ejemplo Python" en la sección TypeScript — cada lenguaje tiene su propio código completo.

## Glosario (5-glosario/README.md)

- Términos ordenados alfabéticamente
- Formato: `**Término**: Definición clara en una o dos oraciones.`
- Incluir ejemplo de código mínimo cuando ayude a clarificar

## Rúbrica de evaluación

Cada `rubrica-evaluacion.md` debe incluir las tres dimensiones:
- **Conocimiento 🧠 (30%)**: preguntas teóricas sobre el protocolo MCP
- **Desempeño 💪 (40%)**: criterios de las prácticas implementadas
- **Producto 📦 (30%)**: criterios del proyecto semanal entregable
```
