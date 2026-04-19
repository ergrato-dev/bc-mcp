<p align="center">
  <img src="assets/bootcamp-header.svg" alt="Bootcamp MCP Zero to Hero" width="800">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="License CC BY-NC-SA 4.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/semanas-12-yellow.svg" alt="12 Semanas"></a>
  <a href="#"><img src="https://img.shields.io/badge/horas-96-orange.svg" alt="96 Horas"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript"></a>
</p>

<p align="center">
  <a href="README_EN.md"><img src="https://img.shields.io/badge/🇺🇸_English-0969DA?style=for-the-badge&logoColor=white" alt="English Version"></a>
</p>

---

## 📋 Descripción

Bootcamp intensivo de **12 semanas (~3 meses)** enfocado en el dominio del **Model Context Protocol (MCP)** y el desarrollo de servidores y clientes MCP modernos con Python y TypeScript. Diseñado para llevar a estudiantes de cero a **Desarrollador MCP Junior**, con énfasis en código limpio, mejores prácticas y proyectos del mundo real listos para integrarse con LLMs (Claude, OpenAI).

### 🎯 Objetivos

Al finalizar el bootcamp, los estudiantes serán capaces de:

- ✅ Dominar el protocolo MCP: arquitectura, primitivos y transports
- ✅ Construir MCP Servers completos en Python y TypeScript
- ✅ Implementar los tres primitivos: Tools, Resources y Prompts
- ✅ Desarrollar MCP Clients en Python y JavaScript
- ✅ Integrar servidores MCP con LLMs (Claude, OpenAI)
- ✅ Conectar MCP Servers con bases de datos y APIs externas
- ✅ Escribir tests automatizados para servers y clients MCP
- ✅ Desplegar aplicaciones MCP con Docker y CI/CD
- ✅ Aplicar clean code, patrones de diseño y mejores prácticas
- ✅ Construir proyectos completos listos para producción

### 🚀 ¿Por qué MCP?

> **MCP moderno desde el día 1** — Sin código legacy, solo las mejores prácticas actuales.

El Model Context Protocol (MCP) es el estándar abierto de Anthropic para conectar LLMs con herramientas, datos y sistemas externos. Este bootcamp se enfoca en MCP con Python 3.13+ y Node.js 22+, enseñando los mismos conceptos en dos ecosistemas. Los estudiantes aprenden directamente las herramientas que usarán para construir agentes e integraciones con LLMs en el mundo profesional.

---

## 🗓️ Estructura del Bootcamp

| Etapa | Semanas | Horas | Temas Principales |
| :-------------------: | :-----: | :---: | ------------------------------------------------------ |
| **Fundamentos**       |   1–3   |  24h  | Protocolo MCP, arquitectura, primitivos, JSON-RPC 2.0, transports |
| **MCP Servers**       |   4–7   |  32h  | Servers Python y TypeScript, bases de datos, APIs externas |
| **MCP Clients + LLMs**|  8–10   |  24h  | Clients Python y JS, Claude, OpenAI, agentic loop |
| **Producción**        |  11–12  |  16h  | Testing, Docker, CI/CD, proyecto final |

**Total: 12 semanas** | **96 horas** de formación intensiva

---

## 📚 Contenido por Semana

Cada semana incluye:

```
bootcamp/week-XX-tema_principal/
├── README.md                 # Descripción y objetivos
├── rubrica-evaluacion.md     # Criterios de evaluación
├── 0-assets/                 # Imágenes y diagramas SVG
├── 1-teoria/                 # Material teórico
├── 2-practicas/              # Ejercicios guiados
├── 3-proyecto/               # Proyecto semanal
│   ├── README.md
│   ├── starter/
│   └── solution/             # ⚠️ Solo para instructores
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/               # Términos clave
```

### 🔑 Componentes Clave

- 📖 **Teoría**: Conceptos del protocolo MCP con ejemplos en Python y TypeScript
- 💻 **Práctica**: Ejercicios guiados con código a descomentar (sin TODOs)
- 🏗️ **Proyecto**: Integrador semanal con código inicial y criterios de evaluación
- 📝 **Evaluación**: Evidencias de conocimiento, desempeño y producto
- 🎓 **Recursos**: Glosarios, referencias y material complementario

---

## 🗺️ Hoja de Ruta por Semana

| Semana | Tema | Python | TypeScript |
|:------:|------|:------:|:----------:|
| 01 | Introducción al protocolo MCP | ✅ | ✅ |
| 02 | JSON-RPC 2.0 y transports | ✅ | ✅ |
| 03 | Los tres primitivos: Tools, Resources y Prompts | ✅ | ✅ |
| 04 | Primer MCP Server en Python | ✅ | — |
| 05 | Primer MCP Server en TypeScript | — | ✅ |
| 06 | Servers avanzados: los 3 primitivos | ✅ | ✅ |
| 07 | Servers con BD y APIs externas | ✅ | ✅ |
| 08 | MCP Client en Python | ✅ | — |
| 09 | MCP Client en TypeScript | — | ✅ |
| 10 | Integración con Claude y OpenAI | ✅ | ✅ |
| 11 | Testing, seguridad y Docker | ✅ | ✅ |
| 12 | CI/CD y proyecto final integrador | ✅ | ✅ |

---

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python | **3.13+** | Lenguaje principal (MCP Servers y Clients) |
| Node.js | **22+** | Runtime TypeScript |
| TypeScript | **5.x** | Lenguaje secundario (MCP Servers y Clients) |
| MCP Python SDK | **1.x** | SDK oficial MCP para Python |
| MCP TypeScript SDK | **1.x** | SDK oficial MCP para TypeScript |
| Pydantic | **2.x** | Validación de datos en Python |
| Zod | **3.x** | Validación de schemas en TypeScript |
| uv | **0.6+** | Gestión de paquetes Python |
| pnpm | **9+** | Gestión de paquetes Node.js |
| pytest | **8.x** | Testing Python |
| vitest | **2.x** | Testing TypeScript |
| Docker | **27+** | Containerización |
| Docker Compose | **2.x** | Orquestación de servicios |

**Entorno de desarrollo**: Docker + docker compose (❌ NO instalar Python ni Node.js localmente)

---

## 🚀 Inicio Rápido

### Prerrequisitos

- **Docker** y **Docker Compose** instalados ([Bootcamp Docker](https://github.com/ergrato-dev/bc-docker))
- **Git** para control de versiones
- **VS Code** (recomendado) con extensiones incluidas
- Navegador moderno (Chrome, Firefox, Edge)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/ergrato-dev/bc-mcp.git
cd bc-mcp
```

### 2. Instalar Extensiones de VS Code

```bash
# Abrir en VS Code
code .

# Las extensiones recomendadas aparecerán automáticamente
# O ejecutar:
# Ctrl+Shift+P → "Extensions: Show Recommended Extensions"
```

### 3. Navegar a la Semana Actual

```bash
cd bootcamp/week-01-introduccion_mcp
```

### 4. Seguir las Instrucciones

Cada semana contiene un `README.md` con instrucciones detalladas y los comandos Docker necesarios para ejecutar los ejemplos.

---

## 📊 Metodología de Aprendizaje

### Estrategias Didácticas

- 🎯 **Aprendizaje Basado en Proyectos (ABP)**: Proyectos semanales integradores
- 🧩 **Práctica Deliberada**: Ejercicios incrementales en dos lenguajes
- 🔄 **MCP Challenges**: Problemas del mundo real con LLMs y tools
- 👥 **Code Review entre pares**
- 🎮 **Live Coding**

### Distribución del Tiempo (8h/semana)

- **Teoría**: 1.5–2 horas
- **Prácticas**: 3–3.5 horas
- **Proyecto**: 2–2.5 horas

### Evaluación

Cada semana incluye tres tipos de evidencias:

1. **Conocimiento 🧠** (30%): Cuestionarios y evaluaciones teóricas sobre el protocolo MCP
2. **Desempeño 💪** (40%): Ejercicios prácticos de implementación de tools/resources/prompts
3. **Producto 📦** (30%): Entregables funcionales (MCP Server o Client operativo)

**Criterio de aprobación**: Mínimo 70% en cada tipo de evidencia

---

## 📞 Soporte

- 💬 **Discussions**: [GitHub Discussions](https://github.com/ergrato-dev/bc-mcp/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/ergrato-dev/bc-mcp/issues)

---

## ⚠️ Exención de Responsabilidad

Este repositorio es un recurso **educativo** creado con fines de aprendizaje. Al utilizarlo, aceptas los siguientes términos:

- **Solo fines educativos**: El contenido, los ejemplos de código y los proyectos están diseñados exclusivamente para la enseñanza y el aprendizaje. No constituyen asesoramiento profesional, legal ni de seguridad.
- **Sin garantías**: El material se proporciona **"tal cual"**, sin garantías de ningún tipo, expresas o implícitas, incluyendo idoneidad para un propósito particular o ausencia de errores.
- **Código en producción**: Los ejemplos de código son ilustrativos. Antes de usarlos en entornos productivos, debes realizar revisiones de seguridad, rendimiento y adaptación a tu contexto específico.
- **Versiones de software**: Las versiones de librerías y herramientas mencionadas pueden quedar desactualizadas. Siempre consulta la documentación oficial más reciente.
- **Limitación de responsabilidad**: Los autores y contribuidores no se responsabilizan por pérdidas de datos, daños directos o indirectos, interrupciones de servicio ni cualquier otro perjuicio derivado del uso de este material.
- **Responsabilidad del estudiante**: Cada estudiante es responsable de sus propias implementaciones, entornos de desarrollo y decisiones técnicas.

---

## 📄 Licencia

Este proyecto está bajo la licencia **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)** (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International).

**Puedes:** compartir y adaptar el material, incluso crear forks educativos.<br>
**No puedes:** usar este material con fines comerciales.<br>
**Debes:** dar crédito apropiado y distribuir las adaptaciones bajo la misma licencia.

Ver el archivo [LICENSE](LICENSE) para el texto completo.

---

## 🏆 Agradecimientos

- [Anthropic](https://www.anthropic.com/) — Por crear el Model Context Protocol y Claude
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) — SDK oficial para Python
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — SDK oficial para TypeScript
- Comunidad Python y Node.js — Por los recursos y ejemplos
- Todos los contribuidores

---

## 📚 Documentación Adicional

- [🤖 Instrucciones de Copilot](.github/copilot-instructions.md)
- [📜 Código de Conducta](CODE_OF_CONDUCT.md)
- [🔒 Política de Seguridad](SECURITY.md)

---

<p align="center">
  <strong>🎓 Bootcamp MCP — Zero to Hero</strong><br>
  <em>De cero a desarrollador MCP en 3 meses</em>
</p>

<p align="center">
  <a href="bootcamp/week-01-introduccion_mcp">Comenzar Semana 1</a> •
  <a href="docs">Ver Documentación</a> •
  <a href="https://github.com/ergrato-dev/bc-mcp/issues">Reportar Issue</a>
</p>

<p align="center">
  Hecho con ❤️ para la comunidad de desarrolladores
</p>
