# 🤖 Instrucciones para GitHub Copilot

## 📋 Contexto del Bootcamp

Este es un Bootcamp de MCP Zero to Hero estructurado para llevar a estudiantes de cero a héroe en el desarrollo de
servidores y clientes del protocolo MCP (Model Context Protocol), usando Python y JavaScript/TypeScript.

### 📊 Datos del Bootcamp

- **Duración**: 12 semanas (~3 meses)
- **Dedicación semanal**: 8 horas
- **Total de horas**: ~96 horas
- **Nivel de salida**: Desarrollador MCP Junior (Python + TypeScript)
- **Enfoque**: MCP moderno con Python 3.13+ y Node.js 22+
- **Stack**: MCP Python SDK 1.x, @modelcontextprotocol/sdk 1.x, TypeScript 5.x, Docker, uv, pnpm

---

## 🎯 Objetivos de Aprendizaje

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

---

## 📚 Estructura del Bootcamp

### Distribución por Etapas

#### Fundamentos (Semanas 1–3) — 24 horas

- Introducción al protocolo MCP y su arquitectura
- Setup de entornos: Python SDK y TypeScript SDK
- Los tres primitivos: Tools, Resources y Prompts
- JSON-RPC 2.0 y el protocolo de comunicación MCP
- Transports: stdio, HTTP/SSE, WebSocket

#### MCP Servers (Semanas 4–7) — 32 horas

- Primer MCP Server en Python (`mcp` SDK)
- Primer MCP Server en TypeScript (`@modelcontextprotocol/sdk`)
- Servers avanzados: integración con bases de datos (SQLite / PostgreSQL)
- Servers avanzados: APIs externas, file system, web scraping

##### 🏗️ Progresión Arquitectónica (Semanas 4–7)

| Semana | Arquitectura          | Descripción                                  |
| ------ | --------------------- | -------------------------------------------- |
| 04     | Server básico         | Un tool simple, stdio transport, Python      |
| 05     | Server básico         | Un tool simple, stdio transport, TypeScript  |
| 06     | + Resources + Prompts | Los 3 primitivos, conexión a datos reales    |
| 07     | + Integraciones       | DB, APIs externas, múltiples tools complejos |

#### MCP Clients + LLMs (Semanas 8–10) — 24 horas

- MCP Client en Python: conexión a servers, llamadas a tools
- MCP Client en TypeScript/JavaScript: mismo patrón, ecosistema Node.js
- Integración con Claude (Anthropic API) y OpenAI
- Orquestación de múltiples servers desde un client
- Patrones de agentic loop: planning, tool execution, result synthesis

#### Producción (Semanas 11–12) — 16 horas

- Testing de servers y clients MCP (pytest + vitest)
- Seguridad, validación de inputs, manejo de errores
- Docker y docker compose para entornos multi-servicio
- CI/CD con GitHub Actions
- Proyecto final integrador

---

## 🗂️ Estructura de Carpetas

Cada semana sigue esta estructura estándar:

```
bootcamp/week-XX-tema_principal/
├── README.md                 # Descripción y objetivos de la semana
├── rubrica-evaluacion.md     # Criterios de evaluación detallados
├── 0-assets/                 # Imágenes, diagramas y recursos visuales
├── 1-teoria/                 # Material teórico (archivos .md)
├── 2-practicas/              # Ejercicios guiados paso a paso
├── 3-proyecto/               # Proyecto semanal integrador
│   ├── README.md             # Instrucciones del proyecto
│   ├── starter/              # Código inicial para el estudiante
│   └── solution/             # ⚠️ OCULTA - Solo para instructores
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/          # Libros electrónicos gratuitos
│   ├── videografia/          # Videos y tutoriales recomendados
│   └── webgrafia/            # Enlaces y documentación
└── 5-glosario/               # Términos clave de la semana (A-Z)
    └── README.md
```

### 📁 Carpetas Raíz

- `assets/`: Recursos visuales globales (logos, headers, etc.)
- `docs/`: Documentación general que aplica a todo el bootcamp
- `scripts/`: Scripts de automatización y utilidades
- `bootcamp/`: Contenido semanal del bootcamp

---

## 🎓 Componentes de Cada Semana

### 1. Teoría (1-teoria/)

- Archivos markdown con explicaciones conceptuales
- Ejemplos de código con comentarios claros en Python y/o TypeScript
- Diagramas y visualizaciones de arquitectura MCP
- Referencias a la documentación oficial de MCP

### 2. Prácticas (2-practicas/)

- Ejercicios guiados paso a paso
- Incremento progresivo de dificultad
- Soluciones comentadas
- Casos de uso del mundo real con LLMs y tools

#### 📋 Formato de Ejercicios

Los ejercicios son tutoriales guiados, NO tareas con TODOs. El estudiante aprende descomentando código:

README.md del ejercicio:

````markdown
### Paso 1: Crear un tool básico en Python

Explicación del concepto con ejemplo:

```python
# Ejemplo explicativo
@mcp.tool()
async def add(a: int, b: int) -> int:
    """Suma dos números."""
    return a + b
```
````

**Abre `starter/server.py`** y descomenta la sección correspondiente.

````

starter/server.py (Python):

```python
# ============================================
# PASO 1: Crear un tool básico
# ============================================
print("--- Paso 1: Tool básico ---")

# Este tool recibe dos enteros y retorna su suma
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def add(a: int, b: int) -> int:
#     """Suma dos números."""
#     return a + b
````

starter/server.ts (TypeScript):

```typescript
// ============================================
// PASO 1: Crear un tool básico
// ============================================

// Este tool recibe dos enteros y retorna su suma
// Descomenta las siguientes líneas:
// server.tool("add", { a: z.number(), b: z.number() }, async ({ a, b }) => ({
//   content: [{ type: "text", text: String(a + b) }],
// }));
```

> ⚠️ **IMPORTANTE**: Los ejercicios NO tienen carpeta `solution/`. El estudiante aprende descomentando el código y verificando que funcione correctamente.

#### ❌ NO usar este formato en ejercicios:

```python
# ❌ INCORRECTO - Este formato es para PROYECTOS, no ejercicios
@mcp.tool()
async def add(a: int, b: int) -> int:
    result = None  # TODO: Implementar
    return result
```

#### ✅ Usar este formato en ejercicios:

```python
# ✅ CORRECTO - Código comentado para descomentar
# Descomenta las siguientes líneas:
# @mcp.tool()
# async def add(a: int, b: int) -> int:
#     """Suma dos números."""
#     return a + b
```

### 3. Proyecto (3-proyecto/)

- Proyecto integrador que consolida lo aprendido
- README.md con instrucciones claras
- Código inicial en `starter/`
- Carpeta `solution/` oculta (en `.gitignore`) solo para instructores
- Criterios de evaluación específicos

#### 📋 Formato de Proyecto (con TODOs)

A diferencia de los ejercicios, el proyecto SÍ usa TODOs para que el estudiante implemente desde cero:

starter/server.py:

```python
# ============================================
# TOOL: search_products
# Busca productos en la base de datos por nombre
# ============================================

@mcp.tool()
async def search_products(query: str) -> list[dict]:
    """
    Busca productos por nombre o descripción.

    Args:
        query: Texto a buscar

    Returns:
        Lista de productos que coinciden con la búsqueda
    """
    # TODO: Implementar lógica de búsqueda
    # 1. Conectar a la base de datos
    # 2. Ejecutar query con LIKE o full-text search
    # 3. Retornar lista de productos
    pass
```

📁 Estructura del proyecto:

```
3-proyecto/
├── README.md          # Instrucciones del proyecto
├── starter/           # Código inicial para el estudiante
└── solution/          # ⚠️ OCULTA - Solo para instructores
```

La carpeta `solution/` está en `.gitignore` y NO se sube al repositorio público.

### 4. Recursos (4-recursos/)

- `ebooks-free/`: Libros gratuitos relevantes
- `videografia/`: Videos tutoriales complementarios
- `webgrafia/`: Enlaces a documentación y artículos

### 5. Glosario (5-glosario/)

- Términos técnicos ordenados alfabéticamente
- Definiciones claras y concisas
- Ejemplos de código cuando aplique

---

## 📝 Convenciones de Código

### Python Moderno (3.13+)

```python
# ✅ BIEN - type hints obligatorios
async def search_files(pattern: str, directory: str = ".") -> list[str]:
    """Busca archivos que coincidan con el patrón."""
    return [str(p) for p in Path(directory).rglob(pattern)]

# ✅ BIEN - async para operaciones I/O
@mcp.tool()
async def fetch_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

# ✅ BIEN - dataclasses / Pydantic para estructuras
from pydantic import BaseModel

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

# ❌ MAL - sin type hints
def search_files(pattern, directory):
    return [str(p) for p in Path(directory).rglob(pattern)]

# ❌ MAL - sync en operaciones I/O
@mcp.tool()
def fetch_url(url: str) -> str:
    return requests.get(url).text
```

### TypeScript Moderno (Node.js 22+)

```typescript
// ✅ BIEN - tipos estrictos con Zod
import { z } from "zod";

server.tool(
  "search_files",
  {
    pattern: z.string().describe("Glob pattern to search"),
    directory: z.string().optional().default("."),
  },
  async ({ pattern, directory }): Promise<CallToolResult> => {
    const files = await glob(pattern, { cwd: directory });
    return {
      content: [{ type: "text", text: files.join("\n") }],
    };
  },
);

// ❌ MAL - sin tipado
server.tool("search_files", {}, async (args) => {
  const files = glob.sync(args.pattern);
  return { content: [{ type: "text", text: files.join("\n") }] };
});
```

### Nomenclatura

- Variables y funciones Python: `snake_case`
- Variables y funciones TypeScript: `camelCase`
- Constantes globales: `UPPER_SNAKE_CASE`
- Clases: `PascalCase`
- Archivos Python: `snake_case.py`
- Archivos TypeScript: `kebab-case.ts` o `camelCase.ts`
- Nombres de tools MCP: `snake_case` (ej. `search_files`, `get_weather`)
- Nombres de resources MCP: URI estilo `scheme://path` (ej. `db://users`, `file://docs`)
- Idioma: inglés para código, español para documentación

### Estructura de Proyecto MCP Server (Python)

```
src/
├── server.py            # Punto de entrada del servidor MCP
├── config.py            # Configuración (env vars, etc.)
├── tools/               # Implementación de tools
│   ├── __init__.py
│   └── search.py
├── resources/           # Implementación de resources
│   ├── __init__.py
│   └── database.py
├── prompts/             # Implementación de prompts
│   ├── __init__.py
│   └── templates.py
└── utils/               # Utilidades compartidas
    ├── __init__.py
    └── db.py
```

### Estructura de Proyecto MCP Server (TypeScript)

```
src/
├── index.ts             # Punto de entrada del servidor MCP
├── config.ts            # Configuración
├── tools/               # Implementación de tools
│   └── search.ts
├── resources/           # Implementación de resources
│   └── database.ts
├── prompts/             # Implementación de prompts
│   └── templates.ts
└── utils/               # Utilidades compartidas
    └── db.ts
```

---

## 🧪 Testing

El bootcamp enseña testing con **pytest** (Python) y **vitest** (TypeScript).

### Tests Python (pytest)

```python
# tests/test_tools.py
import pytest
from mcp.shared.memory import create_connected_server_and_client_session

@pytest.mark.asyncio
async def test_add_tool():
    async with create_connected_server_and_client_session(server) as (_, client):
        result = await client.call_tool("add", {"a": 2, "b": 3})
        assert result.content[0].text == "5"

@pytest.mark.asyncio
async def test_search_tool_empty():
    async with create_connected_server_and_client_session(server) as (_, client):
        result = await client.call_tool("search_files", {"pattern": "*.xyz"})
        assert result.content[0].text == ""
```

### Tests TypeScript (vitest)

```typescript
// tests/tools.test.ts
import { describe, it, expect } from "vitest";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";

describe("add tool", () => {
  it("should sum two numbers", async () => {
    const [clientTransport, serverTransport] =
      InMemoryTransport.createLinkedPair();
    // ... setup server and client
    const result = await client.callTool({
      name: "add",
      arguments: { a: 2, b: 3 },
    });
    expect((result.content[0] as { text: string }).text).toBe("5");
  });
});
```

---

## 📖 Documentación

### README.md de Semana

Debe incluir:

1. Título y descripción
2. 🎯 Objetivos de aprendizaje
3. 📚 Requisitos previos
4. 🗂️ Estructura de la semana
5. 📝 Contenidos (con enlaces a teoría/prácticas)
6. ⏱️ Distribución del tiempo (8 horas)
7. 📌 Entregables
8. 🔗 Navegación (anterior/siguiente semana)

### Archivos de Teoría

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

---

## 🎨 Recursos Visuales y Estándares de Diseño

### Formato de Assets

- ✅ Preferir SVG para todos los diagramas, iconos y gráficos
- ❌ NO usar ASCII art para diagramas o visualizaciones
- ✅ Usar PNG/JPG solo para screenshots o fotografías
- ✅ Optimizar imágenes antes de incluirlas

### Criterio para Assets SVG por Semana

Los assets SVG en `0-assets/` de cada semana tienen un propósito educativo específico:

- ✅ Apoyo visual para comprensión de conceptos teóricos
- ✅ Diagramas de arquitectura MCP (flujo client/server, primitivos, transports)
- ✅ Visualización de procesos (tool execution, resource fetch, prompt flow)
- ✅ Headers de semana para identificación visual

Reglas de vinculación:

1. Todo SVG debe estar vinculado en al menos un archivo de teoría o práctica
2. Usar sintaxis markdown: `![Descripción](../0-assets/nombre.svg)`
3. Incluir texto alternativo descriptivo para accesibilidad
4. Nombrar archivos descriptivamente: `mcp-architecture.svg`, `tool-execution-flow.svg`

```markdown
<!-- Ejemplo de vinculación correcta en teoría -->

## Flujo de Ejecución de un Tool

![Diagrama del flujo de ejecución de un MCP tool](../0-assets/tool-execution-flow.svg)

Como se observa en el diagrama, el client envía una solicitud `tools/call`...
```

### Tema Visual

- 🌙 Tema dark para todos los assets visuales
- ❌ Sin degradés (gradients) en diseños
- ✅ Colores sólidos y contrastes claros
- ✅ Paleta consistente basada en el morado MCP (`#6B4FBB`) y blanco/gris oscuro

### Tipografía

- ✅ Fuentes sans-serif exclusivamente
- ✅ Recomendadas: Inter, Roboto, Open Sans, System UI
- ❌ NO usar fuentes serif (Times, Georgia, etc.)
- ✅ Mantener jerarquía visual clara

---

## 🌐 Idioma y Nomenclatura

### Código y Comentarios Técnicos

- ✅ Nomenclatura en inglés (variables, funciones, clases, nombres de tools/resources)
- ✅ Comentarios de código en inglés
- ✅ Usar términos técnicos estándar de la industria

```python
# ✅ CORRECTO - inglés
@mcp.tool()
async def get_weather(city: str, units: str = "metric") -> dict:
    # Fetch current weather from external API
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/weather", params={"q": city, "units": units})
        return response.json()

# ❌ INCORRECTO - español en código
@mcp.tool()
async def obtener_clima(ciudad: str) -> dict:
    # Obtener clima actual de la API externa
    ...
```

### Documentación

- ✅ Documentación en español (READMEs, teoría, guías)
- ✅ Explicaciones y tutoriales en español
- ✅ Comentarios educativos en español cuando expliquen conceptos

```python
# ✅ CORRECTO - código en inglés, explicación en español
@mcp.tool()
async def search_database(query: str, limit: int = 10) -> list[dict]:
    # Execute parameterized query to avoid SQL injection
    # Usamos queries parametrizadas para evitar inyección SQL
    async with get_db_connection() as db:
        rows = await db.fetch_all(
            "SELECT * FROM items WHERE name ILIKE :q LIMIT :limit",
            {"q": f"%{query}%", "limit": limit},
        )
    return [dict(row) for row in rows]
```

---

## 🔐 Mejores Prácticas

### Código Limpio

- Nombres descriptivos y significativos para tools y resources
- Funciones pequeñas con una sola responsabilidad
- Comentarios solo cuando sea necesario explicar el "por qué"
- Evitar anidamiento profundo
- Usar early returns

### Seguridad

- Validar TODOS los inputs con Pydantic (Python) o Zod (TypeScript)
- Nunca exponer credenciales, API keys ni tokens en el código
- Sanitizar parámetros antes de usarlos en queries SQL o comandos del sistema
- Limitar el scope de file system access a directorios específicos
- Implementar rate limiting en tools que llamen a APIs externas
- No exponer información sensible en mensajes de error

### Rendimiento

- Usar `async/await` para todas las operaciones I/O
- Cachear respuestas de APIs externas cuando sea apropiado
- Usar connection pooling para bases de datos
- Paginar resultados en tools que retornen listas grandes

---

## 📊 Evaluación

Cada semana incluye tres tipos de evidencias:

1. **Conocimiento 🧠 (30%)**: Evaluaciones teóricas, cuestionarios sobre el protocolo MCP
2. **Desempeño 💪 (40%)**: Ejercicios prácticos de implementación de tools/resources/prompts
3. **Producto 📦 (30%)**: Proyecto entregable funcional (server o client MCP operativo)

### Criterios de Aprobación

- Mínimo 70% en cada tipo de evidencia
- Entrega puntual de proyectos
- Código funcional y bien documentado
- Tests pasando (cuando aplique)
- Server/Client MCP que responda correctamente al protocolo

---

## 🚀 Metodología de Aprendizaje

### Estrategias Didácticas

- **Aprendizaje Basado en Proyectos (ABP)**: Proyectos semanales integradores
- **Práctica Deliberada**: Ejercicios incrementales en dos lenguajes
- **MCP Challenges**: Problemas del mundo real con LLMs y tools
- **Code Review**: Revisión de código entre estudiantes
- **Live Coding**: Sesiones en vivo de programación

### Distribución del Tiempo (8h/semana)

- Teoría: 1.5–2 horas
- Prácticas: 3–3.5 horas
- Proyecto: 2–2.5 horas

---

## 🤖 Instrucciones para Copilot

Cuando trabajes en este proyecto:

### Límites de Respuesta

1. **Divide respuestas largas**
   - ❌ NUNCA generar respuestas que superen los límites de tokens
   - ✅ SIEMPRE dividir contenido extenso en múltiples entregas
   - ✅ Crear contenido por secciones, esperar confirmación del usuario
   - ✅ Priorizar calidad sobre cantidad en cada entrega
   - Razón: Evitar pérdida de contenido y garantizar completitud

2. **Estrategia de División**
   - Para semanas completas: dividir por carpetas (`teoria` → `practicas` → `proyecto`)
   - Para archivos grandes: dividir por secciones lógicas
   - Siempre indicar claramente qué parte se entrega y qué falta
   - Esperar confirmación del usuario antes de continuar

### Generación de Código

1. **Usa sintaxis moderna en ambos lenguajes**
   - Python 3.13+: type hints obligatorios, `async/await`, `|` para unions, genéricos nativos
   - TypeScript 5.x: tipos estrictos, Zod para validación de inputs, ESM modules
   - Node.js 22+: `import/export` nativo, top-level await cuando aplique

2. **Entorno de Desarrollo con Docker**
   - ✅ USAR Docker para evitar problemas de versiones múltiples
   - ✅ `docker compose` para orquestar servicios (server MCP, DB, etc.)
   - ✅ Crear archivos `.env` para configuración de entorno
   - Razón: Entorno consistente y reproducible para todos los estudiantes
   - Estructura recomendada:

   ```
   proyecto/
   ├── docker-compose.yml    # Orquestación de servicios
   ├── Dockerfile.python     # Imagen del server Python
   ├── Dockerfile.node       # Imagen del server TypeScript
   ├── .env.example          # Variables de entorno (template)
   ├── .env                  # Variables de entorno (ignorado en git)
   ├── python-server/        # Código fuente Python
   └── ts-server/            # Código fuente TypeScript
   ```

   - Comandos esenciales:

   ```bash
   # Construir y levantar servicios
   docker compose up --build

   # Levantar en background
   docker compose up -d

   # Ver logs
   docker compose logs -f server

   # Ejecutar comandos dentro del contenedor Python
   docker compose exec python-server bash

   # Detener servicios
   docker compose down

   # Limpiar todo (incluye volúmenes)
   docker compose down -v
   ```

3. **Gestión de Paquetes**
   - Python (dentro de Docker): usar **`uv`** exclusivamente, NUNCA `pip` directamente
   - JavaScript/TypeScript: usar **`pnpm`** exclusivamente, NUNCA `npm` ni `yarn`
   - Razón: Mejor resolución de dependencias, reproducibilidad, velocidad
   - Versiones de dependencias: **SIEMPRE exactas**, sin `^`, `~`, `>=` ni `*`

   Python con `uv`:

   ```dockerfile
   FROM python:3.13-slim
   ENV PYTHONDONTWRITEBYTECODE=1 \
       PYTHONUNBUFFERED=1 \
       UV_SYSTEM_PYTHON=1
   RUN pip install --no-cache-dir uv
   WORKDIR /app
   COPY pyproject.toml uv.lock* ./
   RUN uv sync --frozen --no-dev
   COPY . .
   CMD ["uv", "run", "python", "src/server.py"]
   ```

   TypeScript con `pnpm`:

   ```dockerfile
   FROM node:22-slim
   RUN corepack enable && corepack prepare pnpm@latest --activate
   WORKDIR /app
   COPY package.json pnpm-lock.yaml ./
   RUN pnpm install --frozen-lockfile --prod
   COPY . .
   RUN pnpm build
   CMD ["node", "dist/index.js"]
   ```

4. **Transports MCP**
   - `stdio`: para integración con Claude Desktop, Cursor, VS Code
   - `http` + `SSE`: para servers accesibles via HTTP (producción)
   - Usar `stdio` en semanas 4–9, introducir HTTP/SSE en semana 10+

5. **Comenta el código de manera educativa**
   - Explica conceptos del protocolo MCP para principiantes
   - Incluye referencias a la documentación oficial cuando sea útil
   - Usa comentarios que enseñen, no solo describan

6. **Proporciona ejemplos completos y funcionales**
   - Código que se pueda copiar y ejecutar
   - Incluye casos de uso realistas con LLMs
   - Muestra tanto lo que se debe hacer como lo que se debe evitar

### Creación de Contenido

1. **Estructura clara y progresiva**
   - De lo simple a lo complejo
   - Conceptos construidos sobre conocimientos previos
   - Repetición espaciada: tools → resources → prompts → client → LLM

2. **Ejemplos del mundo real**
   - Tools útiles: búsqueda de archivos, consulta de DB, llamadas a APIs
   - Resources: esquemas de DB, documentación, configuración
   - Proyectos que los estudiantes puedan mostrar en portfolios

3. **Enfoque moderno**
   - No mencionar características obsoletas del SDK
   - Enfocarse en las mejores prácticas del protocolo MCP actual
   - Usar herramientas y patrones modernos del ecosistema LLM

### Respuestas y Ayuda

1. **Explicaciones claras**
   - Lenguaje simple y directo
   - Evitar jerga innecesaria
   - Proporcionar analogías (ej. "un tool MCP es como un endpoint REST que un LLM puede llamar")

2. **Código comentado**
   - Explicar cada paso importante del protocolo
   - Destacar conceptos clave: tool schema, resource URI, prompt arguments
   - Señalar posibles errores comunes (transport incorrecto, schema inválido)

3. **Recursos adicionales**
   - Referencias a la documentación oficial de MCP
   - Enlace a los SDKs oficiales
   - Artículos y ejemplos de la comunidad

---

## 📚 Referencias Oficiales

- MCP Specification: <https://spec.modelcontextprotocol.io/>
- MCP Python SDK: <https://github.com/modelcontextprotocol/python-sdk>
- MCP TypeScript SDK: <https://github.com/modelcontextprotocol/typescript-sdk>
- MCP Docs: <https://modelcontextprotocol.io/docs>
- Anthropic Claude API: <https://docs.anthropic.com/>
- OpenAI API: <https://platform.openai.com/docs>
- Python Documentation: <https://docs.python.org/3/>
- Node.js Documentation: <https://nodejs.org/docs/>
- Zod Documentation: <https://zod.dev/>
- pytest Documentation: <https://docs.pytest.org/>
- vitest Documentation: <https://vitest.dev/>

---

## 🔗 Enlaces Importantes

- Repositorio: <https://github.com/ergrato-dev/bc-mcp>
- Documentación general: [docs/README.md](../docs/README.md)
- Primera semana: [bootcamp/week-01-introduccion_mcp/README.md](../bootcamp/week-01-introduccion_mcp/README.md)

---

## ✅ Checklist para Nuevas Semanas

Cuando crees contenido para una nueva semana:

- [ ] Crear estructura de carpetas completa
- [ ] README.md con objetivos y estructura
- [ ] Assets SVG en `0-assets/`: mínimo un SVG por cada archivo de teoría que refuerce visualmente el concepto principal
- [ ] Material teórico en `1-teoria/` — cada archivo debe referenciar su SVG correspondiente de `0-assets/`
- [ ] Ejercicios prácticos en `2-practicas/` (formato descomentar, NO TODOs)
- [ ] Proyecto integrador en `3-proyecto/` (formato TODOs, con `starter/` y `solution/`)
- [ ] Recursos adicionales en `4-recursos/`
- [ ] Glosario de términos en `5-glosario/`
- [ ] Rúbrica de evaluación
- [ ] Verificar coherencia con semanas anteriores
- [ ] Revisar progresión de dificultad
- [ ] Probar código de ejemplos en Python y TypeScript
- [ ] Asegurar que `solution/` está en `.gitignore`

---

## 💡 Notas Finales

- **Prioridad**: Claridad sobre brevedad
- **Enfoque**: Aprendizaje práctico sobre teoría abstracta
- **Objetivo**: Preparar desarrolladores MCP listos para integrar LLMs en producción
- **Filosofía**: Dos lenguajes desde el día 1 — mismos conceptos, dos ecosistemas
- **Bilingüismo técnico**: cada semana que introduzca un concepto nuevo lo implementa en Python Y TypeScript

_Última actualización: Abril 2026 — Versión: 1.0_
