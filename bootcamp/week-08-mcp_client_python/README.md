# Semana 08 — MCP Client en Python

> **Etapa**: MCP Clients + LLMs (Semanas 8–10) · **Dedicación**: 8 horas · **Lenguajes**: Python

---

## 🎯 Objetivos de Aprendizaje

- ✅ Construir un MCP Client en Python usando el SDK oficial
- ✅ Conectarse a un MCP Server via stdio
- ✅ Listar y descubrir tools, resources y prompts disponibles
- ✅ Invocar tools y procesar sus resultados
- ✅ Manejar errores del client correctamente

---

## 📚 Requisitos Previos

- Semana 07 completada
- MCP Server funcionando (semana 07)
- Python async/await dominado

---

## 🗂️ Estructura de la Semana

```
week-08-mcp_client_python/
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

1. Arquitectura del MCP Client en Python
2. ClientSession y StdioServerParameters
3. Flujo: connect → initialize → discover → call → disconnect
4. Procesamiento de resultados: TextContent, ImageContent
5. Manejo de errores en el client

### 💻 Prácticas ([2-practicas/](2-practicas/README.md))

1. Crear un client Python que se conecte al server de semana 07
2. Listar todos los tools disponibles con list_tools()
3. Invocar un tool y procesar su respuesta
4. Listar resources y leer su contenido
5. Construir un CLI que use el client como interfaz

### 🏗️ Proyecto ([3-proyecto/](3-proyecto/README.md))

MCP Client Python con CLI interactivo que se conecta al server de semana 07

---

## ⏱️ Distribución del Tiempo (8h)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Teoría | 1.5–2h | Lectura y comprensión del material teórico |
| Prácticas | 3–3.5h | Ejercicios guiados con código a descomentar |
| Proyecto | 2–2.5h | Implementación del proyecto integrador |

---

## 📌 Entregables

- [ ] MCP Client Python funcional con conexión a server stdio
- [ ] CLI que permite invocar cualquier tool del server
- [ ] Tests del client con servidor de prueba en memoria
- [ ] README con instrucciones y ejemplos de uso

---

## 🔗 Navegación

[← Semana 07](../week-07-servers_bd_apis_externas) · [Semana 09 →](../week-09-mcp_client_typescript)
