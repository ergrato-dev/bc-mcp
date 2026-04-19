# Glosario — Semana 01: Introducción al Protocolo MCP

Términos clave de esta semana, ordenados alfabéticamente.

---

### Function Calling

Mecanismo propietario de proveedores de LLMs (OpenAI, Anthropic) que permite al modelo
declarar que quiere ejecutar una función con argumentos específicos. A diferencia de MCP,
está atado al proveedor y no es portátil entre LLMs.

---

### Host

Aplicación que el usuario final utiliza directamente y que gestiona múltiples MCP Clients.
Ejemplos: Claude Desktop, Cursor, VS Code con Copilot. El Host controla qué servers puede
usar el LLM y con qué permisos.

---

### JSON-RPC 2.0

Protocolo de llamada a procedimientos remotos basado en JSON. Define la estructura de
mensajes de solicitud (`method`, `params`, `id`) y respuesta (`result` o `error`).
Es el protocolo de transporte de mensajes que usa MCP.

---

### LLM

Large Language Model. Modelo de lenguaje de gran escala entrenado con grandes volúmenes
de texto. Ejemplos: Claude (Anthropic), GPT-4 (OpenAI), Gemini (Google). En MCP,
el LLM vive dentro del Host y usa los tools/resources expuestos por los MCP Servers.

---

### MCP

Model Context Protocol. Protocolo abierto publicado por Anthropic en noviembre de 2024
que define cómo los LLMs pueden conectarse de forma estandarizada a herramientas, datos
y capacidades externas. Licencia MIT.

---

### MCP Client

Componente interno del Host que mantiene una conexión 1:1 con un MCP Server. Gestiona
el handshake de inicialización, serializa solicitudes a JSON-RPC y retorna respuestas
al LLM. No es una aplicación separada — vive dentro del Host.

---

### MCP Server

Proceso que expone Tools, Resources y Prompts al ecosistema MCP a través de un transport.
Es el componente que los desarrolladores construyen. Puede ser un script Python, un
binario Node.js, un contenedor Docker, etc.

---

### Primitivo

Uno de los tres tipos fundamentales de capacidad que un MCP Server puede exponer:
**Tool** (acción ejecutable), **Resource** (dato legible por URI) o **Prompt** (plantilla
de mensaje con argumentos dinámicos).

---

### Prompt (MCP)

Plantilla de mensaje reutilizable con argumentos dinámicos que un MCP Server expone.
Permite al Host cargar conversaciones pre-estructuradas para tareas específicas.
No confundir con un mensaje que el usuario escribe al LLM.

---

### Resource

Primitivo MCP que representa un dato que el LLM puede leer como contexto. Se identifica
por una URI con scheme propio (`db://schema`, `file://docs`). Ideal para datos
semi-estáticos como esquemas de BD o documentación.

---

### stdio

Transport MCP que usa la entrada estándar (`stdin`) y salida estándar (`stdout`) del
proceso para intercambiar mensajes JSON-RPC. Es el transport más simple y el recomendado
para desarrollo local e integración con Claude Desktop / Cursor.

---

### Tool

Primitivo MCP que representa una acción ejecutable con inputs validados y outputs
tipados. El LLM decide cuándo y con qué argumentos ejecutar un tool. Equivalente
a una función en el servidor expuesta al LLM.

---

### Transport

Mecanismo físico por el que viajan los mensajes JSON-RPC entre el MCP Client y el
MCP Server. Los tres transports principales son `stdio`, `HTTP/SSE` y `WebSocket`.
El protocolo (JSON-RPC) es siempre el mismo; solo cambia el canal.

---

[← Volver al README de la semana](../README.md)


### Prompt

Plantilla de instrucciones reutilizable expuesta por un MCP Server

### Protocol

Conjunto de reglas que define cómo se comunican los componentes de un sistema

### Resource

Dato o fuente de información expuesta por un MCP Server con URI único

### Tool

Función ejecutable expuesta por un MCP Server que un LLM puede invocar

### Transport

Mecanismo de comunicación entre Client y Server (stdio, HTTP/SSE)

---

[← Volver al README de la semana](../README.md)
