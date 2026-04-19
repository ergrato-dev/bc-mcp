#!/usr/bin/env python3
"""
scaffold_bootcamp.py
Genera el scaffolding completo del Bootcamp MCP Zero to Hero (12 semanas).
Uso: python3 scripts/scaffold_bootcamp.py
"""

import pathlib

BASE = pathlib.Path(__file__).parent.parent / "bootcamp"


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def mkfile(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {path.relative_to(BASE.parent)}")


def gitkeep(folder: pathlib.Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    (folder / ".gitkeep").write_text("", encoding="utf-8")
    print(f"  ✓ {(folder / '.gitkeep').relative_to(BASE.parent)}")


# ─────────────────────────────────────────────
# Datos de cada semana
# ─────────────────────────────────────────────

WEEKS = [
    {
        "num": "01",
        "slug": "introduccion_mcp",
        "title": "Introducción al Protocolo MCP",
        "stage": "Fundamentos (Semanas 1–3)",
        "langs": "Python y TypeScript",
        "prev": None,
        "next": "02",
        "objectives": [
            "Comprender qué es el Model Context Protocol y por qué fue creado",
            "Identificar los tres componentes principales: Host, Client y Server",
            "Entender el modelo de primitivos: Tools, Resources y Prompts",
            "Diferenciar MCP de otros mecanismos de integración con LLMs",
            "Configurar el entorno de desarrollo con Docker y MCP Inspector",
        ],
        "prereqs": ["Docker y Docker Compose instalados", "Git instalado", "VS Code con extensiones recomendadas"],
        "theory": [
            "¿Qué es MCP? Historia y motivación",
            "Arquitectura MCP: Host, Client y Server",
            "Los tres primitivos: Tools, Resources y Prompts",
            "Casos de uso reales: Claude Desktop, Cursor, VS Code",
            "Comparativa: MCP vs Function Calling vs Plugins",
        ],
        "practice": [
            "Configurar el entorno Docker del bootcamp",
            "Explorar la especificación oficial de MCP",
            "Instalar MCP Inspector y conectar a un server de ejemplo",
            "Analizar mensajes MCP con herramientas de debug",
        ],
        "project": "Mapa conceptual de la arquitectura MCP documentado con un diagrama SVG",
        "deliverables": [
            "Diagrama SVG de la arquitectura MCP (Host / Client / Server / Primitivos)",
            "Documento con análisis de 3 casos de uso reales de MCP",
            "Entorno Docker funcionando con MCP Inspector instalado",
        ],
        "glossary": {
            "Host": "Aplicación que gestiona múltiples MCP Clients (ej. Claude Desktop, Cursor)",
            "LLM": "Large Language Model — modelo de lenguaje de gran escala (Claude, GPT, etc.)",
            "MCP": "Model Context Protocol — protocolo abierto de Anthropic para conectar LLMs con herramientas y datos",
            "MCP Client": "Componente que mantiene una conexión 1:1 con un MCP Server",
            "MCP Server": "Proceso que expone Tools, Resources y Prompts a través del protocolo MCP",
            "Primitivo": "Concepto fundamental del protocolo MCP: Tool, Resource o Prompt",
            "Prompt": "Plantilla de instrucciones reutilizable expuesta por un MCP Server",
            "Protocol": "Conjunto de reglas que define cómo se comunican los componentes de un sistema",
            "Resource": "Dato o fuente de información expuesta por un MCP Server con URI único",
            "Tool": "Función ejecutable expuesta por un MCP Server que un LLM puede invocar",
            "Transport": "Mecanismo de comunicación entre Client y Server (stdio, HTTP/SSE)",
        },
    },
    {
        "num": "02",
        "slug": "json_rpc_y_transports",
        "title": "JSON-RPC 2.0 y Transports",
        "stage": "Fundamentos (Semanas 1–3)",
        "langs": "Python y TypeScript",
        "prev": "01",
        "next": "03",
        "objectives": [
            "Entender la estructura de mensajes JSON-RPC 2.0",
            "Diferenciar requests, responses y notifications en MCP",
            "Comprender el ciclo de vida de una sesión MCP",
            "Conocer los transports disponibles: stdio, HTTP/SSE",
            "Inspeccionar mensajes MCP reales con herramientas de debug",
        ],
        "prereqs": ["Semana 01 completada", "Conocimiento básico de JSON", "Docker funcionando"],
        "theory": [
            "JSON-RPC 2.0: estructura de mensajes",
            "Requests, responses, notifications y batches",
            "Ciclo de vida de una sesión MCP: initialize → use → shutdown",
            "Transport stdio: comunicación por stdin/stdout",
            "Transport HTTP/SSE: Server-Sent Events para streaming",
        ],
        "practice": [
            "Enviar mensajes JSON-RPC manualmente vía stdin",
            "Inspeccionar el handshake MCP con logs detallados",
            "Comparar stdio vs HTTP/SSE en ejemplos reales",
            "Implementar un echo server minimal con JSON-RPC",
        ],
        "project": "Analizador de mensajes MCP que parsea y muestra el ciclo de vida de una sesión",
        "deliverables": [
            "Script que captura y analiza mensajes JSON-RPC de una sesión MCP real",
            "Diagrama del ciclo de vida de sesión MCP (initialize / method calls / shutdown)",
            "Comparativa documentada: stdio vs HTTP/SSE",
        ],
        "glossary": {
            "Batch": "Envío de múltiples requests JSON-RPC en un solo mensaje",
            "HTTP/SSE": "Transport MCP sobre HTTP con Server-Sent Events para streaming de respuestas",
            "initialize": "Primer mensaje de una sesión MCP para negociar capabilities",
            "JSON-RPC 2.0": "Protocolo de llamada a procedimientos remotos basado en JSON",
            "Notification": "Mensaje JSON-RPC sin id — no requiere respuesta",
            "Request": "Mensaje JSON-RPC con id que espera una response del servidor",
            "Response": "Mensaje JSON-RPC de respuesta a un request, con result o error",
            "Sesión MCP": "Conexión completa entre un Client y un Server desde initialize hasta shutdown",
            "shutdown": "Mensaje para terminar ordenadamente una sesión MCP",
            "stdio": "Transport MCP que usa stdin/stdout del proceso para la comunicación",
            "WebSocket": "Protocolo de comunicación bidireccional en tiempo real (transport MCP alternativo)",
        },
    },
    {
        "num": "03",
        "slug": "primitivos_tools_resources_prompts",
        "title": "Los Tres Primitivos: Tools, Resources y Prompts",
        "stage": "Fundamentos (Semanas 1–3)",
        "langs": "Python y TypeScript",
        "prev": "02",
        "next": "04",
        "objectives": [
            "Dominar la definición y uso de Tools con schemas JSON",
            "Entender los Resources: URIs, tipos MIME y contenido",
            "Comprender los Prompts: argumentos y plantillas de mensajes",
            "Saber cuándo usar cada primitivo según el caso de uso",
            "Diseñar interfaces MCP correctas antes de implementarlas",
        ],
        "prereqs": ["Semana 02 completada", "Familiaridad con JSON Schema", "Conceptos básicos de MCP"],
        "theory": [
            "Tools: schema de inputs, annotations, execution model",
            "Resources: URI scheme, tipos MIME, resource templates",
            "Prompts: argumentos, mensajes y role-based content",
            "Cuándo usar Tool vs Resource vs Prompt",
            "Diseño de interfaces MCP: buenas prácticas",
        ],
        "practice": [
            "Definir schemas de tools en JSON (Python y TypeScript)",
            "Diseñar URIs de resources para distintos casos de uso",
            "Crear plantillas de prompts con argumentos variables",
            "Revisar servers MCP de ejemplo y analizar sus primitivos",
        ],
        "project": "Documento de diseño de interfaz MCP para un sistema real (tools + resources + prompts)",
        "deliverables": [
            "Documento de diseño con al menos 5 tools, 3 resources y 2 prompts definidos",
            "JSON Schemas de los tools diseñados (validados)",
            "Diagrama de los primitivos y sus relaciones",
        ],
        "glossary": {
            "Annotation": "Metadato opcional de un Tool que indica su comportamiento (readOnly, destructive, etc.)",
            "Content": "Unidad de contenido MCP: text, image o resource",
            "Input Schema": "JSON Schema que define los parámetros de entrada de un Tool",
            "MIME Type": "Tipo de contenido de un Resource (text/plain, application/json, etc.)",
            "Prompt": "Plantilla de instrucciones con argumentos definidos por el servidor",
            "Prompt Argument": "Parámetro requerido u opcional de un Prompt MCP",
            "Resource": "Fuente de datos expuesta con URI único (db://..., file://..., etc.)",
            "Resource Template": "Patrón de URI con variables para generar resources dinámicos",
            "Tool": "Función con schema de inputs que un LLM puede invocar a través de MCP",
            "URI": "Identificador único de un Resource en formato scheme://path",
        },
    },
    {
        "num": "04",
        "slug": "primer_server_python",
        "title": "Primer MCP Server en Python",
        "stage": "MCP Servers (Semanas 4–7)",
        "langs": "Python",
        "prev": "03",
        "next": "05",
        "objectives": [
            "Crear un MCP Server funcional con FastMCP en Python",
            "Implementar tools con el decorador @mcp.tool()",
            "Gestionar el proyecto Python con uv y pyproject.toml",
            "Ejecutar el server con stdio transport",
            "Probar el server con MCP Inspector",
        ],
        "prereqs": ["Semana 03 completada", "Python 3.13+ (vía Docker)", "uv instalado en contenedor"],
        "theory": [
            "FastMCP: el SDK de Python para MCP",
            "Decorador @mcp.tool(): schema automático con type hints",
            "Ciclo de vida del server: startup, handling, shutdown",
            "pyproject.toml y gestión de dependencias con uv",
            "Debugging de servers Python con logging",
        ],
        "practice": [
            "Crear un server con FastMCP y un tool básico (add)",
            "Agregar type hints y docstrings como schema automático",
            "Gestionar el proyecto con uv sync y pyproject.toml",
            "Conectar MCP Inspector al server stdio",
            "Agregar múltiples tools con distintos tipos de parámetros",
        ],
        "project": "MCP Server Python con mínimo 3 tools útiles (matemáticas, texto, fecha/hora)",
        "deliverables": [
            "MCP Server Python funcional con 3+ tools",
            "pyproject.toml con dependencias exactas",
            "README con instrucciones de ejecución con Docker",
            "Captura de MCP Inspector mostrando los tools",
        ],
        "glossary": {
            "@mcp.tool()": "Decorador de FastMCP que registra una función async como Tool MCP",
            "asyncio": "Librería de Python para programación asíncrona con async/await",
            "FastMCP": "Clase principal del SDK MCP de Python para crear servers de forma declarativa",
            "pyproject.toml": "Archivo de configuración estándar de proyectos Python moderno",
            "stdio transport": "Transport MCP que comunica client y server por stdin/stdout del proceso",
            "type hint": "Anotación de tipo en Python que FastMCP usa para generar el JSON Schema del tool",
            "uv": "Gestor de paquetes y entornos Python ultrarrápido (reemplaza pip/venv)",
            "uv run": "Comando para ejecutar scripts Python en el entorno virtual gestionado por uv",
            "uv sync": "Comando de uv para instalar dependencias exactas del pyproject.toml",
        },
    },
    {
        "num": "05",
        "slug": "primer_server_typescript",
        "title": "Primer MCP Server en TypeScript",
        "stage": "MCP Servers (Semanas 4–7)",
        "langs": "TypeScript",
        "prev": "04",
        "next": "06",
        "objectives": [
            "Crear un MCP Server funcional con el SDK TypeScript de MCP",
            "Implementar tools con server.tool() y validación Zod",
            "Gestionar el proyecto con pnpm y package.json",
            "Compilar y ejecutar el server con Node.js 22+",
            "Probar el server con MCP Inspector",
        ],
        "prereqs": ["Semana 04 completada", "Node.js 22+ (vía Docker)", "pnpm instalado en contenedor", "TypeScript básico"],
        "theory": [
            "McpServer: la clase principal del SDK TypeScript de MCP",
            "server.tool(): registro de tools con nombre y schema Zod",
            "Validación de inputs con Zod — schemas type-safe",
            "package.json, tsconfig.json y compilación con tsc",
            "ESM modules y top-level await en Node.js 22+",
        ],
        "practice": [
            "Crear un server con McpServer y un tool básico (add)",
            "Definir schemas de tools con z.object() y tipos Zod",
            "Configurar pnpm, package.json y tsconfig.json",
            "Compilar con tsc y ejecutar con Node.js",
            "Conectar MCP Inspector al server TypeScript",
        ],
        "project": "MCP Server TypeScript con mínimo 3 tools (equivalentes a los de semana 04)",
        "deliverables": [
            "MCP Server TypeScript funcional con 3+ tools",
            "package.json con dependencias exactas (sin ^)",
            "tsconfig.json correctamente configurado",
            "README con instrucciones de ejecución con Docker",
        ],
        "glossary": {
            "CallToolResult": "Tipo de retorno de un tool MCP en el SDK TypeScript",
            "corepack": "Herramienta de Node.js para gestionar versiones de package managers (pnpm, yarn)",
            "ESM": "ECMAScript Modules — sistema de módulos nativo de Node.js con import/export",
            "McpServer": "Clase principal del SDK TypeScript de MCP para crear servers",
            "pnpm": "Package manager de Node.js ultrarrápido con workspaces y strict hoisting",
            "StdioServerTransport": "Implementación del transport stdio para servers MCP en TypeScript",
            "tsconfig.json": "Archivo de configuración del compilador TypeScript",
            "z.object()": "Función de Zod para definir schemas de objetos con tipos TypeScript",
            "Zod": "Librería de validación de schemas TypeScript-first usada para inputs de tools MCP",
        },
    },
    {
        "num": "06",
        "slug": "servers_avanzados_primitivos",
        "title": "Servers Avanzados — Los 3 Primitivos",
        "stage": "MCP Servers (Semanas 4–7)",
        "langs": "Python y TypeScript",
        "prev": "05",
        "next": "07",
        "objectives": [
            "Implementar Resources con URIs y listado dinámico",
            "Crear Prompts con argumentos y plantillas de mensajes",
            "Combinar Tools + Resources + Prompts en un solo server",
            "Gestionar contexto y estado dentro del server",
            "Implementar resource templates con URIs variables",
        ],
        "prereqs": ["Semana 05 completada", "MCP Server funcional en Python y TypeScript"],
        "theory": [
            "Implementación de Resources: list y read handlers",
            "Resource templates: URIs con variables {param}",
            "Implementación de Prompts: list y get handlers",
            "Combinación de los 3 primitivos en un server completo",
            "Gestión de contexto en tools (ctx: Context)",
        ],
        "practice": [
            "Agregar resources a un server Python existente",
            "Agregar resources al server TypeScript",
            "Implementar prompts con argumentos en ambos lenguajes",
            "Crear un server completo con los 3 primitivos",
        ],
        "project": "MCP Server (Python y TypeScript) con tools + resources + prompts sobre un dominio real",
        "deliverables": [
            "MCP Server Python con 3 tools, 2 resources y 1 prompt",
            "MCP Server TypeScript con los mismos primitivos",
            "Tests básicos verificando que los 3 primitivos responden",
            "README con descripción de cada primitivo expuesto",
        ],
        "glossary": {
            "@mcp.resource()": "Decorador FastMCP para registrar un Resource con URI fijo",
            "@mcp.resource('{param}')": "Decorador FastMCP para resource templates con URI variable",
            "Context": "Objeto disponible en tools de FastMCP con acceso a logging y recursos del server",
            "list_resources": "Handler MCP que devuelve la lista de resources disponibles",
            "list_tools": "Handler MCP que devuelve la lista de tools disponibles",
            "Prompt argument": "Parámetro requerido u opcional de un Prompt (name, description, required)",
            "read_resource": "Handler MCP que devuelve el contenido de un resource por su URI",
            "Resource template": "URI con variables entre llaves que genera resources dinámicos",
            "server.resource()": "Método del SDK TypeScript para registrar un Resource",
        },
    },
    {
        "num": "07",
        "slug": "servers_bd_apis_externas",
        "title": "Servers con BD y APIs Externas",
        "stage": "MCP Servers (Semanas 4–7)",
        "langs": "Python y TypeScript",
        "prev": "06",
        "next": "08",
        "objectives": [
            "Conectar un MCP Server a SQLite con queries async",
            "Integrar APIs externas con httpx (Python) y fetch/axios (TypeScript)",
            "Gestionar variables de entorno de forma segura",
            "Implementar connection pooling para bases de datos",
            "Manejar errores de red y BD correctamente",
        ],
        "prereqs": ["Semana 06 completada", "Conocimiento básico de SQL", "SQLite disponible en Docker"],
        "theory": [
            "Conexiones async a SQLite y PostgreSQL desde Python",
            "HTTP clients async: httpx (Python) y fetch nativo (TypeScript)",
            "Variables de entorno y configuración segura con python-dotenv",
            "Connection pooling: aiosqlite, asyncpg",
            "Manejo de errores: McpError, ToolError y patrones de retry",
        ],
        "practice": [
            "Conectar server Python a SQLite y exponer tools de consulta",
            "Integrar una API REST externa (OpenWeatherMap u otra pública)",
            "Implementar lo mismo en TypeScript",
            "Manejar errores de BD y HTTP con tipos correctos",
        ],
        "project": "MCP Server completo con BD SQLite + API externa (Python y TypeScript)",
        "deliverables": [
            "MCP Server Python conectado a SQLite con 4+ tools CRUD",
            "MCP Server TypeScript con la misma funcionalidad",
            "Integración con al menos una API externa pública",
            ".env.example con todas las variables necesarias",
            "docker-compose.yml para levantar el entorno completo",
        ],
        "glossary": {
            "aiosqlite": "Librería Python para acceso async a SQLite",
            "asyncpg": "Driver async de PostgreSQL para Python",
            "Connection pool": "Conjunto de conexiones reutilizables a una BD para mejorar rendimiento",
            "dotenv": "Herramienta para cargar variables de entorno desde un archivo .env",
            "httpx": "Cliente HTTP async para Python (reemplaza requests en código async)",
            "McpError": "Excepción base del SDK MCP para errores del protocolo",
            "Query parametrizada": "Query SQL con parámetros (?,:name) para prevenir SQL injection",
            "SQL injection": "Vulnerabilidad de seguridad al concatenar inputs del usuario en queries SQL",
            "ToolError": "Excepción para indicar error en la ejecución de un tool MCP",
        },
    },
    {
        "num": "08",
        "slug": "mcp_client_python",
        "title": "MCP Client en Python",
        "stage": "MCP Clients + LLMs (Semanas 8–10)",
        "langs": "Python",
        "prev": "07",
        "next": "09",
        "objectives": [
            "Construir un MCP Client en Python usando el SDK oficial",
            "Conectarse a un MCP Server via stdio",
            "Listar y descubrir tools, resources y prompts disponibles",
            "Invocar tools y procesar sus resultados",
            "Manejar errores del client correctamente",
        ],
        "prereqs": ["Semana 07 completada", "MCP Server funcionando (semana 07)", "Python async/await dominado"],
        "theory": [
            "Arquitectura del MCP Client en Python",
            "ClientSession y StdioServerParameters",
            "Flujo: connect → initialize → discover → call → disconnect",
            "Procesamiento de resultados: TextContent, ImageContent",
            "Manejo de errores en el client",
        ],
        "practice": [
            "Crear un client Python que se conecte al server de semana 07",
            "Listar todos los tools disponibles con list_tools()",
            "Invocar un tool y procesar su respuesta",
            "Listar resources y leer su contenido",
            "Construir un CLI que use el client como interfaz",
        ],
        "project": "MCP Client Python con CLI interactivo que se conecta al server de semana 07",
        "deliverables": [
            "MCP Client Python funcional con conexión a server stdio",
            "CLI que permite invocar cualquier tool del server",
            "Tests del client con servidor de prueba en memoria",
            "README con instrucciones y ejemplos de uso",
        ],
        "glossary": {
            "CallToolResult": "Respuesta de la invocación de un tool — incluye content y isError",
            "ClientSession": "Clase del SDK MCP Python que representa la sesión de un client",
            "connect()": "Método que inicia la conexión y el handshake con el server",
            "ImageContent": "Tipo de contenido MCP para datos de imagen en base64",
            "list_resources()": "Método del client para obtener resources disponibles en el server",
            "list_tools()": "Método del client para obtener la lista de tools disponibles en el server",
            "StdioServerParameters": "Configuración del client para conectarse a un server via stdio",
            "TextContent": "Tipo de contenido MCP para texto plano",
            "tool_result.content": "Lista de contenidos devueltos por un tool (TextContent, ImageContent)",
        },
    },
    {
        "num": "09",
        "slug": "mcp_client_typescript",
        "title": "MCP Client en TypeScript",
        "stage": "MCP Clients + LLMs (Semanas 8–10)",
        "langs": "TypeScript",
        "prev": "08",
        "next": "10",
        "objectives": [
            "Construir un MCP Client en TypeScript usando el SDK oficial",
            "Conectarse a un MCP Server via stdio desde Node.js",
            "Listar y descubrir tools, resources y prompts",
            "Invocar tools y tipar correctamente sus resultados",
            "Comparar la experiencia de cliente en Python vs TypeScript",
        ],
        "prereqs": ["Semana 08 completada", "MCP Client Python dominado", "TypeScript async/await dominado"],
        "theory": [
            "Client class del SDK TypeScript de MCP",
            "StdioClientTransport: configuración y conexión",
            "Tipado de resultados con interfaces TypeScript",
            "Manejo de errores y timeouts en el client TS",
            "Comparativa Python SDK vs TypeScript SDK",
        ],
        "practice": [
            "Crear un client TypeScript que se conecte al server de semana 07",
            "Listar tools con client.listTools()",
            "Invocar tools con client.callTool() y tipar resultados",
            "Listar y leer resources con client.listResources()",
            "Construir un CLI TypeScript equivalente al de semana 08",
        ],
        "project": "MCP Client TypeScript con CLI que se conecta al server de semana 07",
        "deliverables": [
            "MCP Client TypeScript funcional con conexión a server stdio",
            "CLI TypeScript que permite invocar cualquier tool del server",
            "Tests del client con InMemoryTransport",
            "README con comparativa Python vs TypeScript client",
        ],
        "glossary": {
            "callTool()": "Método del Client TypeScript para invocar un tool en el server",
            "Client": "Clase del SDK TypeScript de MCP que representa el client",
            "connect()": "Método del Client TypeScript para iniciar la conexión con el server",
            "InMemoryTransport": "Transport en memoria para testing — no requiere proceso externo",
            "listResources()": "Método del Client TypeScript para obtener resources del server",
            "listTools()": "Método del Client TypeScript para obtener la lista de tools del server",
            "StdioClientTransport": "Implementación del transport stdio para clients MCP en TypeScript",
            "Tool[]": "Array de tools devuelto por listTools() con name, description e inputSchema",
        },
    },
    {
        "num": "10",
        "slug": "integracion_claude_openai",
        "title": "Integración con Claude y OpenAI",
        "stage": "MCP Clients + LLMs (Semanas 8–10)",
        "langs": "Python y TypeScript",
        "prev": "09",
        "next": "11",
        "objectives": [
            "Integrar un MCP Client con la API de Claude (Anthropic)",
            "Integrar un MCP Client con la API de OpenAI (function calling)",
            "Implementar el agentic loop completo: planning → tool call → result → synthesis",
            "Orquestar múltiples MCP Servers desde un solo client",
            "Construir un agente funcional que use LLM + MCP tools",
        ],
        "prereqs": ["Semana 09 completada", "API keys de Anthropic y/o OpenAI", "MCP Client en Python y TypeScript dominado"],
        "theory": [
            "Agentic loop: cómo un LLM decide qué tool usar",
            "Anthropic API: tool_use, tool_result y conversación multi-turn",
            "OpenAI API: function_calling y messages con tool results",
            "Conversión de MCP tool schemas a formatos de LLM",
            "Orquestación multi-server: conectar N servers desde 1 client",
        ],
        "practice": [
            "Conectar Claude a un MCP Server y ejecutar tool calls",
            "Implementar el loop completo con Anthropic SDK",
            "Replicar con OpenAI SDK (function calling)",
            "Orquestar 2 servers desde un agente Claude",
        ],
        "project": "Agente LLM (Claude o OpenAI) que usa MCP tools del server de semana 07",
        "deliverables": [
            "Agente Python con Claude + MCP Server funcionando",
            "Agente TypeScript equivalente",
            "Demo del agentic loop con 3+ tool calls encadenados",
            ".env.example con API keys necesarias (sin valores reales)",
        ],
        "glossary": {
            "Agentic loop": "Ciclo de razonamiento del LLM: recibir input → decidir tool → ejecutar → sintetizar",
            "Anthropic SDK": "Librería oficial de Anthropic para interactuar con Claude API",
            "Function calling": "Mecanismo de OpenAI para que el LLM invoque funciones definidas por el usuario",
            "Multi-turn": "Conversación con múltiples rondas de mensajes entre usuario y LLM",
            "OpenAI SDK": "Librería oficial de OpenAI para interactuar con sus modelos (GPT-4, etc.)",
            "Tool result": "Respuesta de la ejecución de un tool que se devuelve al LLM en el siguiente turno",
            "tool_use": "Bloque de respuesta de Claude que indica que quiere invocar un tool",
        },
    },
    {
        "num": "11",
        "slug": "testing_seguridad_docker",
        "title": "Testing, Seguridad y Docker",
        "stage": "Producción (Semanas 11–12)",
        "langs": "Python y TypeScript",
        "prev": "10",
        "next": "12",
        "objectives": [
            "Escribir tests unitarios y de integración para MCP Servers",
            "Testear MCP Clients con transports en memoria",
            "Aplicar validación de inputs y manejo de errores",
            "Identificar y corregir vulnerabilidades de seguridad en tools",
            "Containerizar servers MCP con Docker y docker compose",
        ],
        "prereqs": ["Semana 10 completada", "Conocimiento básico de pytest y vitest", "Docker Compose dominado"],
        "theory": [
            "Testing de MCP Servers con create_connected_server_and_client_session",
            "Testing de MCP Clients con InMemoryTransport (TypeScript)",
            "Validación de inputs: Pydantic (Python) y Zod (TypeScript)",
            "Seguridad en tools: SQL injection, path traversal, rate limiting",
            "Dockerfiles para Python (uv) y TypeScript (pnpm) en producción",
        ],
        "practice": [
            "Escribir tests pytest para el server de semana 07",
            "Escribir tests vitest para el server TypeScript",
            "Agregar validación Pydantic a inputs de tools",
            "Revisar y corregir vulnerabilidades en tools existentes",
            "Crear Dockerfile y docker-compose.yml para el proyecto",
        ],
        "project": "Server de semana 07 con suite de tests completa, validación de inputs y Docker",
        "deliverables": [
            "Suite pytest con 80%+ de cobertura del server Python",
            "Suite vitest con 80%+ de cobertura del server TypeScript",
            "Dockerfile.python y Dockerfile.node optimizados",
            "docker-compose.yml para entorno completo",
            "Informe de seguridad con vulnerabilidades corregidas",
        ],
        "glossary": {
            "create_connected_server_and_client_session": "Helper del SDK MCP Python para crear pares server/client en memoria para tests",
            "Coverage": "Porcentaje de código ejecutado durante los tests",
            "Fixture": "Objeto de pytest reutilizable para setup/teardown de tests",
            "InMemoryTransport": "Transport del SDK TypeScript en memoria para tests sin E/S real",
            "Path traversal": "Vulnerabilidad que permite acceder a archivos fuera del directorio permitido",
            "pytest-asyncio": "Plugin de pytest para testear código async con async/await",
            "Rate limiting": "Técnica para limitar la cantidad de requests por unidad de tiempo",
            "SQL injection": "Ataque que inyecta SQL malicioso en queries construidas con concatenación",
            "vitest": "Framework de testing para TypeScript/JavaScript moderno y rápido",
        },
    },
    {
        "num": "12",
        "slug": "cicd_proyecto_final",
        "title": "CI/CD y Proyecto Final Integrador",
        "stage": "Producción (Semanas 11–12)",
        "langs": "Python y TypeScript",
        "prev": "11",
        "next": None,
        "objectives": [
            "Configurar un pipeline CI/CD con GitHub Actions",
            "Automatizar tests y build de imágenes Docker en CI",
            "Construir un sistema MCP completo como proyecto final",
            "Documentar el proyecto con READMEs profesionales",
            "Presentar el proyecto final con demo funcional",
        ],
        "prereqs": ["Semana 11 completada", "Repositorio en GitHub", "Docker Hub o GHCR disponible"],
        "theory": [
            "GitHub Actions: workflows, jobs, steps y actions",
            "CI para MCP: lint → test → build → push imagen",
            "Semantic versioning y tags de Docker en CI",
            "Documentación profesional de proyectos MCP",
            "Patrones de arquitectura para sistemas MCP en producción",
        ],
        "practice": [
            "Crear workflow de GitHub Actions para CI del server Python",
            "Crear workflow de CI para el server TypeScript",
            "Automatizar build y push de imágenes Docker a GHCR",
            "Configurar badges de estado de CI en el README",
        ],
        "project": "Sistema MCP completo: server + client + agente LLM + CI/CD + Docker + documentación",
        "deliverables": [
            "Sistema MCP completo con server Python o TypeScript",
            "MCP Client + agente LLM funcional",
            "Pipeline CI/CD con GitHub Actions pasando en green",
            "docker-compose.yml para entorno de producción",
            "README profesional con arquitectura, setup y demo",
            "Presentación del proyecto (5-10 min demo en vivo)",
        ],
        "glossary": {
            "Action": "Unidad reutilizable de GitHub Actions (ej. actions/checkout)",
            "Artifact": "Archivo generado por un job de CI y almacenado temporalmente",
            "CI/CD": "Continuous Integration / Continuous Delivery — automatización de build, test y deploy",
            "GHCR": "GitHub Container Registry — registro de imágenes Docker de GitHub",
            "GitHub Actions": "Plataforma de CI/CD integrada en GitHub con workflows YAML",
            "Job": "Grupo de steps en un workflow de GitHub Actions que se ejecutan en un runner",
            "Runner": "Máquina virtual que ejecuta los jobs de GitHub Actions (ubuntu-latest, etc.)",
            "Semantic versioning": "Esquema de versiones MAJOR.MINOR.PATCH para software",
            "Workflow": "Archivo YAML en .github/workflows/ que define el pipeline de CI/CD",
        },
    },
]


# ─────────────────────────────────────────────
# Templates
# ─────────────────────────────────────────────

def week_readme(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    stage = w["stage"]
    langs = w["langs"]
    prev_link = f"[← Semana {w['prev']}](../week-{w['prev']}-{WEEK_SLUGS[w['prev']]})" if w["prev"] else "*(inicio del bootcamp)*"
    next_link = f"[Semana {w['next']} →](../week-{w['next']}-{WEEK_SLUGS[w['next']]})" if w["next"] else "*(fin del bootcamp)*"
    objectives = "\n".join(f"- ✅ {o}" for o in w["objectives"])
    prereqs = "\n".join(f"- {p}" for p in w["prereqs"])
    theory_items = "\n".join(f"{i+1}. {t}" for i, t in enumerate(w["theory"]))
    practice_items = "\n".join(f"{i+1}. {p}" for i, p in enumerate(w["practice"]))
    deliverables = "\n".join(f"- [ ] {d}" for d in w["deliverables"])

    return f"""# Semana {num} — {title}

> **Etapa**: {stage} · **Dedicación**: 8 horas · **Lenguajes**: {langs}

---

## 🎯 Objetivos de Aprendizaje

{objectives}

---

## 📚 Requisitos Previos

{prereqs}

---

## 🗂️ Estructura de la Semana

```
week-{num}-{w['slug']}/
├── README.md                 # Este archivo
├── rubrica-evaluacion.md     # Criterios de evaluación
├── 0-assets/                 # Diagramas SVG
├── 1-teoria/                 # Material teórico
│   └── README.md
├── 2-practicas/              # Ejercicios guiados
│   └── README.md
├── 3-proyecto/               # Proyecto semanal
│   ├── README.md
│   └── starter/
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### 📖 Teoría ([1-teoria/](1-teoria/README.md))

{theory_items}

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

{practice_items}

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

{w['project']}

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

{deliverables}

---

## 🔗 Navegación

{prev_link} · {next_link}
"""


def teoria_readme(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    items = "\n".join(
        f"- [0{i+1}-{t.lower().replace(' ', '-').replace('/', '').replace(':', '').replace('(', '').replace(')', '').replace(',', '').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n').replace('¿','')[:40]}.md]"
        f"(0{i+1}-{t.lower().replace(' ', '-').replace('/', '').replace(':', '').replace('(', '').replace(')', '').replace(',', '').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n').replace('¿','')[:40]}.md) — {t}"
        for i, t in enumerate(w["theory"])
    )
    return f"""# Teoría — Semana {num}: {title}

## Archivos de Teoría

{items}

> 📌 Cada archivo de teoría debe referenciar al menos un SVG de `../0-assets/`
> para reforzar visualmente el concepto principal.

---

[← Volver al README de la semana](../README.md)
"""


def practicas_readme(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    items = "\n".join(
        f"- [practica-0{i+1}/](practica-0{i+1}/) — {p}"
        for i, p in enumerate(w["practice"])
    )
    return f"""# Prácticas — Semana {num}: {title}

## Ejercicios Guiados

{items}

> 📌 Los ejercicios usan el formato **descomentar código** (NO TODOs).
> El estudiante aprende descomentando las secciones indicadas en el `README.md`
> de cada práctica y verificando que el código funcione correctamente.

---

[← Volver al README de la semana](../README.md)
"""


def proyecto_readme(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    deliverables = "\n".join(f"- [ ] {d}" for d in w["deliverables"])
    return f"""# Proyecto — Semana {num}: {title}

## 🎯 Descripción

{w['project']}

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/README.md) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/README.md) como preparación
3. Trabaja en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Usa Docker para ejecutar tu solución (`docker compose up --build`)
5. Verifica que todos los entregables estén completos antes de la entrega

## 📌 Entregables

{deliverables}

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md          # Este archivo
└── starter/           # Tu código va aquí
    └── README.md      # Instrucciones de setup
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
"""


def starter_readme(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    return f"""# Starter — Semana {num}: {title}

## Setup

```bash
# Clonar y navegar al directorio
cd bootcamp/week-{num}-{w['slug']}/3-proyecto/starter

# Levantar el entorno con Docker
docker compose up --build
```

## Estructura Esperada

Implementa el proyecto según las instrucciones en [`../README.md`](../README.md).

## TODO

Implementa los entregables descritos en [`../README.md`](../README.md#-entregables).

---

[← Volver al proyecto](../README.md)
"""


def rubrica(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    return f"""# Rúbrica de Evaluación — Semana {num}: {title}

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
| Funcionalidad | Todos los entregables funcionan correctamente con Docker | Los entregables principales funcionan | Los entregables no funcionan o están incompletos |
| Documentación | README claro con instrucciones completas y ejemplos | README básico con instrucciones de setup | Sin README o instrucciones insuficientes |
| Entregables completos | Todos los ítems del checklist marcados | 70%+ de los ítems completados | Menos del 70% completado |

---

## 📝 Notas del Evaluador

_Espacio para comentarios personalizados del instructor._

---

**Evaluado por**: _________________ · **Fecha**: _________________ · **Puntuación total**: _____ / 100
"""


def glosario_readme(w: dict) -> str:
    num = w["num"]
    title = w["title"]
    terms = "\n\n".join(
        f"### {term}\n\n{definition}"
        for term, definition in sorted(w["glossary"].items())
    )
    return f"""# Glosario — Semana {num}: {title}

Términos clave de esta semana, ordenados alfabéticamente.

---

{terms}

---

[← Volver al README de la semana](../README.md)
"""


# ─────────────────────────────────────────────
# Build slug lookup map
# ─────────────────────────────────────────────

WEEK_SLUGS = {w["num"]: w["slug"] for w in WEEKS}


# ─────────────────────────────────────────────
# Main generation
# ─────────────────────────────────────────────

def generate():
    print(f"\n🚀 Generando scaffolding en: {BASE}\n")
    for w in WEEKS:
        num = w["num"]
        slug = w["slug"]
        week_dir = BASE / f"week-{num}-{slug}"
        print(f"\n📁 Semana {num}: {w['title']}")

        # README principal
        mkfile(week_dir / "README.md", week_readme(w))

        # Rúbrica
        mkfile(week_dir / "rubrica-evaluacion.md", rubrica(w))

        # 0-assets
        gitkeep(week_dir / "0-assets")

        # 1-teoria
        mkfile(week_dir / "1-teoria" / "README.md", teoria_readme(w))

        # 2-practicas
        mkfile(week_dir / "2-practicas" / "README.md", practicas_readme(w))

        # 3-proyecto
        mkfile(week_dir / "3-proyecto" / "README.md", proyecto_readme(w))
        mkfile(week_dir / "3-proyecto" / "starter" / "README.md", starter_readme(w))

        # 4-recursos
        gitkeep(week_dir / "4-recursos" / "ebooks-free")
        gitkeep(week_dir / "4-recursos" / "videografia")
        gitkeep(week_dir / "4-recursos" / "webgrafia")

        # 5-glosario
        mkfile(week_dir / "5-glosario" / "README.md", glosario_readme(w))

    print(f"\n✅ Scaffolding completo — {len(WEEKS)} semanas generadas.\n")


if __name__ == "__main__":
    generate()
