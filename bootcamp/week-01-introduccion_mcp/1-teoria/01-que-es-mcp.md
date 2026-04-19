# ¿Qué es el Model Context Protocol (MCP)?

![Arquitectura MCP: Host, Client y Server](../0-assets/01-mcp-architecture.svg)

## 🎯 Objetivos

- Comprender el origen y motivación del protocolo MCP
- Identificar el problema que MCP resuelve en el ecosistema de LLMs
- Conocer quién creó MCP y cómo se convirtió en estándar abierto
- Entender la diferencia entre un LLM aislado y un LLM con contexto externo

---

## 📋 Contenido

### 1. El Problema: LLMs sin Contexto

Los modelos de lenguaje grande (LLMs) como Claude o GPT son sistemas extraordinariamente
capaces, pero tienen una limitación fundamental: **solo saben lo que estaba en su
entrenamiento**. No pueden acceder a:

- Tu base de datos de producción
- Los archivos de tu proyecto
- Una API externa en tiempo real
- El estado actual de tu sistema

Antes de MCP, cada equipo resolvía esto de manera diferente: algunos usaban function calling
de OpenAI, otros construían integraciones ad-hoc con REST, otros usaban plugins propietarios.
El resultado era un ecosistema fragmentado donde **cada solución era incompatible con las demás**.

### 2. La Solución: Un Protocolo Estándar

En noviembre de 2024, **Anthropic** publicó el Model Context Protocol (MCP) como estándar
abierto bajo licencia MIT. La idea central es simple:

> MCP es un protocolo universal que define cómo los LLMs pueden conectarse de forma
> segura y estandarizada a herramientas, datos y capacidades externas.

Piénsalo como **USB-C para los LLMs**: un conector estándar que funciona igual sin importar
qué LLM usas (Claude, GPT, Gemini) o qué herramienta quieres conectar (base de datos,
sistema de archivos, API externa).

### 3. Historia y Adopción

| Fecha | Hito |
|-------|------|
| Nov 2024 | Anthropic publica MCP como open source |
| Dic 2024 | Claude Desktop integra MCP nativamente |
| Ene 2025 | Cursor IDE adopta MCP para herramientas de coding |
| Feb 2025 | VS Code (Copilot) agrega soporte MCP |
| Mar 2025 | OpenAI anuncia compatibilidad con MCP |
| 2025–2026 | Más de 1000 MCP servers públicos disponibles |

La adopción fue extraordinariamente rápida porque el protocolo resolvía un dolor real y
universal en la industria.

### 4. Los Tres Actores Principales

MCP define tres roles claramente separados:

**Host**
El Host es la aplicación que el usuario final utiliza directamente. Claude Desktop, Cursor,
VS Code con Copilot son ejemplos de Hosts. El Host gestiona múltiples conexiones a MCP Servers
a través de MCP Clients internos.

**MCP Client**
El Client es un componente interno del Host que mantiene una conexión 1:1 con un MCP Server.
El usuario nunca interactúa directamente con el Client — es infraestructura interna.

**MCP Server**
El Server es el proceso que expone capacidades concretas al LLM: herramientas que puede
ejecutar, datos que puede leer, plantillas que puede usar. Tú, como desarrollador, construyes
MCP Servers.

```
Host (Claude Desktop)
  └── MCP Client ──── JSON-RPC 2.0 ────► MCP Server (tu código)
                                              ├── Tools
                                              ├── Resources
                                              └── Prompts
```

### 5. Los Tres Primitivos

MCP define tres tipos de capacidades que un server puede exponer:

**Tools** (Herramientas)
Son acciones que el LLM puede ejecutar. Tienen inputs validados y retornan outputs.
Ejemplo: `search_files(pattern: str)`, `send_email(to: str, body: str)`.

**Resources** (Recursos)
Son datos que el LLM puede leer como contexto. Se identifican por una URI.
Ejemplo: `db://schema`, `file://README.md`.

**Prompts** (Plantillas)
Son plantillas de mensajes reutilizables con argumentos dinámicos.
Ejemplo: `code_review(language: str, code: str)`.

### 6. ¿Por Qué MCP Sobre Otras Alternativas?

```
LLM con MCP:
  LLM ←→ MCP Client ←→ MCP Server ←→ Cualquier herramienta
                         (estándar abierto, multi-LLM)

LLM sin MCP:
  LLM ←→ Function Calling (solo ese LLM)
  LLM ←→ Plugin propietario (solo esa plataforma)
  LLM ←→ REST ad-hoc (sin estándar, sin estado)
```

Las ventajas clave de MCP son:

- **Portabilidad**: el mismo server funciona con Claude, GPT, Gemini y cualquier LLM compatible
- **Bidireccionalidad**: el server puede enviar notificaciones al client, no solo responder
- **Estandarización**: un solo protocolo para todos los tipos de integración
- **Seguridad**: el protocolo define claramente qué puede y no puede hacer el server
- **Local/On-premise**: funciona sin necesidad de internet o servicios en la nube

### 7. Casos de Uso Reales

**Claude Desktop + MCP Server de Sistema de Archivos**
El usuario le pide a Claude que analice todos los archivos `.py` de su proyecto. Claude usa
el MCP Server de filesystem para listar y leer los archivos, los analiza, y sugiere
mejoras — todo sin que el usuario tenga que copiar y pegar código manualmente.

**Cursor IDE + MCP Server de Base de Datos**
El desarrollador le pide a Cursor que escriba una query para su esquema de PostgreSQL. Cursor
consulta el MCP Server de BD para obtener el esquema actual y genera SQL correcto para ese
esquema específico.

**VS Code Copilot + MCP Server de Jira**
El desarrollador le pide a Copilot que implemente el ticket PROJ-123. Copilot usa el MCP
Server de Jira para leer la descripción del ticket, los criterios de aceptación y los
comentarios, y genera el código correspondiente.

---

## 4. Errores Comunes

**Error: Confundir MCP Server con un servidor web**
Un MCP Server no es necesariamente un servidor HTTP. El transport más común para desarrollo
local es `stdio` (entrada/salida estándar), que no requiere puertos ni HTTP.

**Error: Creer que MCP solo funciona con Claude**
MCP es un estándar abierto. OpenAI, Google y docenas de herramientas ya tienen compatibilidad.
El protocolo es independiente del LLM.

**Error: Pensar que MCP reemplaza las APIs REST**
MCP no reemplaza las APIs de tus sistemas — las usa. Un MCP Server puede internamente llamar
a tu API REST existente y exponer esa funcionalidad al LLM de forma estandarizada.

**Error: Implementar tools síncronas para operaciones I/O**
Todas las operaciones de red, disco y BD deben ser `async`. Un tool síncrono que hace I/O
bloqueará el event loop del server.

```python
# ❌ MAL — bloqueante
@mcp.tool()
def get_user(user_id: int) -> dict:
    return requests.get(f"/api/users/{user_id}").json()

# ✅ BIEN — async
@mcp.tool()
async def get_user(user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"/api/users/{user_id}")
        return response.json()
```

---

## 5. Ejercicios de Comprensión

1. ¿Cuál es la diferencia entre un Host y un MCP Client? ¿Puede un usuario interactuar
   directamente con un MCP Client?

2. Si tienes un MCP Server de base de datos y quieres usarlo tanto con Claude Desktop como
   con un cliente Python personalizado, ¿necesitas modificar el server? ¿Por qué?

3. Un compañero dice: "Prefiero function calling de OpenAI porque ya conozco la API".
   ¿Qué ventajas concretas le darías como argumento para adoptar MCP?

4. Lista tres casos de uso de tu trabajo o proyectos actuales donde un MCP Server aportaría
   valor. Para cada uno, identifica qué primitivo usarías (Tool, Resource o Prompt).

---

## 📚 Recursos Adicionales

- [Especificación oficial MCP](https://spec.modelcontextprotocol.io/)
- [Blog Anthropic: Introducing MCP](https://www.anthropic.com/news/model-context-protocol)
- [MCP Python SDK — GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK — GitHub](https://github.com/modelcontextprotocol/typescript-sdk)
- [Lista de MCP Servers disponibles](https://modelcontextprotocol.io/examples)

---

## ✅ Checklist de Verificación

- [ ] Puedo explicar qué problema resuelve MCP en mis propias palabras
- [ ] Identifico los tres roles: Host, Client y Server
- [ ] Conozco los tres primitivos: Tool, Resource y Prompt
- [ ] Sé por qué MCP es superior a function calling ad-hoc para proyectos grandes
- [ ] Puedo nombrar al menos 3 Hosts que implementan MCP nativamente
- [ ] Entiendo que MCP usa JSON-RPC 2.0 como protocolo de comunicación

---

[← Volver al índice de teoría](README.md) | [02 — Arquitectura →](02-arquitectura.md)
