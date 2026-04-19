---
description: "Crea la estructura completa de una nueva semana del bootcamp bc-mcp con todas sus carpetas y archivos base."
mode: "agent"
---

Crea la estructura completa de una nueva semana del bootcamp MCP Zero to Hero.

## Información necesaria

Si no se especificó en la solicitud, pregunta:

1. **Número de semana** (ej. `04`)
2. **Nombre del tema** en `snake_case` (ej. `primer_server_python`)
3. **Título legible** (ej. "Primer MCP Server en Python")
4. **Lenguaje principal** de la semana: Python, TypeScript, o ambos
5. **Semana anterior** y **semana siguiente** (para navegación)

## Estructura a crear

```
bootcamp/week-{NN}-{tema}/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
│   └── .gitkeep
├── 1-teoria/
│   └── README.md
├── 2-practicas/
│   └── README.md
├── 3-proyecto/
│   ├── README.md
│   └── starter/
│       └── README.md
├── 4-recursos/
│   ├── ebooks-free/
│   │   └── .gitkeep
│   ├── videografia/
│   │   └── README.md
│   └── webgrafia/
│       └── README.md
└── 5-glosario/
    └── README.md
```

> ⚠️ NO crear la carpeta `solution/` — está en `.gitignore` y el instructor la crea localmente.

## Contenido de cada archivo

### README.md (raíz de semana)

Debe contener:

- Encabezado con referencia al SVG de assets (pendiente de crear)
- Tabla con distribución de 8 horas (teoría 1.5-2h, prácticas 3-3.5h, proyecto 2-2.5h)
- Objetivos de aprendizaje concretos y medibles
- Requisitos previos (semana anterior)
- Estructura de carpetas con descripción de cada una
- Entregables claros
- Navegación a semana anterior y siguiente

### rubrica-evaluacion.md

Tabla con tres dimensiones:

- Conocimiento 🧠 (30%) — preguntas teóricas sobre el tema
- Desempeño 💪 (40%) — criterios de las prácticas
- Producto 📦 (30%) — criterios del proyecto

### 1-teoria/README.md

Índice de los archivos de teoría de la semana con descripción breve de cada uno.

### 2-practicas/README.md

Índice de las prácticas con descripción, duración estimada y objetivo de cada una.

### 3-proyecto/README.md

- Descripción del proyecto semanal
- Objetivos de aprendizaje del proyecto
- Instrucciones paso a paso para el estudiante
- Criterios de aceptación
- Cómo verificar que funciona correctamente

### 3-proyecto/starter/README.md

Instrucciones de setup del proyecto starter: qué archivos hay, cómo correrlo, qué debe implementar el estudiante.

### 4-recursos/videografia/README.md y webgrafia/README.md

Listas con recursos recomendados relevantes para el tema de la semana.

### 5-glosario/README.md

Lista de 5-10 términos clave de la semana definidos en español, ordenados alfabéticamente. Incluir ejemplos de código mínimos donde ayude.

## Validación final

Después de crear todos los archivos:

1. Confirmar que la estructura coincide con `bootcamp/week-XX-tema/` esperado
2. Verificar que los links de navegación en README.md apuntan a las semanas correctas
3. Confirmar que NO se creó carpeta `solution/`
