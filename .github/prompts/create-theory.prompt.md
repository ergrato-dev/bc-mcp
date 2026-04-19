---
description: "Genera el material teórico completo de un tema MCP para la sección 1-teoria/ de una semana del bootcamp."
mode: "agent"
---

Crea el material teórico para un tema del bootcamp MCP Zero to Hero.

## Información necesaria

Si no se especificó en la solicitud, pregunta:

1. **Semana y tema** (ej. "Semana 3 — Los tres primitivos: Tools, Resources y Prompts")
2. **Lenguaje(s)**: Python, TypeScript o ambos
3. **Nivel de los estudiantes** en ese punto del bootcamp (qué ya saben)
4. **Conceptos clave** a cubrir
5. **¿Incluir diagrama SVG?** — si sí, describir qué debe mostrar el diagrama

## Archivos a generar en `1-teoria/`

Para un tema principal, generar uno o varios archivos `.md`:

```
1-teoria/
├── README.md                     # índice de la teoría de la semana
├── 01-{concepto-principal}.md    # concepto más importante
├── 02-{concepto-secundario}.md   # (si el tema es amplio)
└── 03-ejemplos-practicos.md      # (opcional — ejemplos integrados)
```

## Estructura de cada archivo de teoría

````markdown
# {Título del Concepto}

## 🎯 Objetivos

Al finalizar esta sección serás capaz de:

- Objetivo concreto y medible 1
- Objetivo concreto y medible 2

## 📋 ¿Qué es {concepto}?

Explicación clara en lenguaje accesible.
Usar analogías con tecnologías conocidas cuando sea útil.
(ej. "Un MCP Tool es como un endpoint REST que un LLM puede llamar automáticamente")

## 🏗️ Arquitectura / Cómo funciona

Diagrama o descripción del flujo.
Si hay SVG disponible en `../0-assets/`, referenciar aquí:

![Diagrama de {concepto}](../0-assets/{nombre}.svg)

## 💻 Implementación en Python

Explicación paso a paso con código comentado y funcional.

```python
# Comentarios educativos que expliquen el "por qué"
# de cada decisión, no solo el "qué"
```
````

## 💻 Implementación en TypeScript

(Si aplica — mismos conceptos, sintaxis diferente)

```typescript
// Equivalente TypeScript al ejemplo Python anterior
```

## ⚡ Casos de uso reales

Ejemplos de cuándo y por qué usar este concepto en proyectos reales con LLMs.

## ⚠️ Errores comunes

Lista de los 3-5 errores más frecuentes de principiantes en este tema, con cómo evitarlos.

## ✅ Checklist de verificación

- [ ] Entiendo qué es {concepto} y cuándo usarlo
- [ ] Puedo implementar {concepto} en Python
- [ ] Puedo implementar {concepto} en TypeScript
- [ ] Entiendo la diferencia entre {concepto} y {concepto relacionado}

## 📚 Recursos adicionales

- [Documentación oficial MCP](https://modelcontextprotocol.io/docs)
- Enlace 2

```

## Reglas de contenido

- **Analogías**: usar comparaciones con tecnologías conocidas (REST APIs, funciones, endpoints)
- **Bilingüismo**: si cubre Python Y TypeScript, ambos ejemplos deben ser completos e independientes — no escribir "ver ejemplo Python" en la sección TypeScript
- **Progresión**: de lo simple a lo complejo dentro de cada archivo
- **Ejemplos reales**: preferir ejemplos útiles (weather API, file search, DB query) sobre ejemplos abstractos (foo/bar)
- **Errores comunes**: siempre incluir al menos 3 errores frecuentes específicos del protocolo MCP
- **Longitud**: un archivo de teoría bien hecho tiene entre 200-400 líneas; si supera 400 líneas, dividir en varios archivos

## Sobre los diagramas SVG

Si el tema requiere un diagrama (arquitectura, flujo de datos, secuencia de mensajes):
- Describir qué debe mostrar el diagrama con detalle
- El diagrama SVG se creará por separado en `0-assets/`
- Dejar el placeholder en el markdown: `![Descripción](../0-assets/nombre-descriptivo.svg)`
- Paleta: tema oscuro, morado `#6B4FBB`, fuente sans-serif, sin degradés
```
