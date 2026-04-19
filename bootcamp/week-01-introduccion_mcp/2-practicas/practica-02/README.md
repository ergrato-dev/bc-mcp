# Práctica 02 — Explorar un MCP Server con MCP Inspector

## 🎯 Objetivo

Usar MCP Inspector para explorar el server oficial de ejemplo, entender qué expone
y enviar llamadas a tools de forma manual para ver el protocolo en acción.

## ⏱️ Tiempo estimado: 45 minutos

---

## Prerrequisitos

- Práctica 01 completada (MCP Inspector corriendo en `http://localhost:6274`)

---

## Paso 1: Conectar al server de demo

Con MCP Inspector abierto, conecta al server oficial:

```
npx -y @modelcontextprotocol/server-everything
```

Este server tiene múltiples tools, resources y prompts de ejemplo que representan
todos los tipos de primitivos que ofrece el protocolo.

---

## Paso 2: Explorar los Tools disponibles

En la pestaña **Tools**, verás la lista completa. Para cada tool observa:

- **Nombre**: identificador único del tool
- **Descripción**: qué hace (lo que el LLM leerá para decidir cuándo usarlo)
- **Input Schema**: los parámetros que acepta con sus tipos y si son requeridos

**Responde estas preguntas:**
1. ¿Cuántos tools expone el server?
2. ¿Qué tool crees que es el más útil? ¿Por qué?
3. ¿Algún tool tiene parámetros opcionales? ¿Cómo se diferencian de los requeridos?

---

## Paso 3: Llamar a un Tool manualmente

Selecciona el tool `echo` (o similar) y rellena sus parámetros. Haz clic en **Run**.

Observa en el panel de respuesta:
- La estructura `content: [{ type: "text", text: "..." }]`
- El tiempo de respuesta

Ahora abre `starter/tool-calls.json` y descomenta cada bloque para ver el JSON-RPC
crudo que corresponde a cada llamada.

---

## Paso 4: Explorar los Resources

Ve a la pestaña **Resources** y lista los resources disponibles. Para cada uno:

- Lee la URI — ¿qué esquema usa? (`file://`, `db://`, `https://`)
- Lee el contenido haciendo clic en el resource
- Observa el `mimeType` de la respuesta

**Responde:**
1. ¿Cuál es la diferencia entre un resource con URI fija y uno con URI paramétrica?
2. ¿Qué `mimeType` usan los resources de texto? ¿Y los de JSON?

---

## Paso 5: Explorar los Prompts

Ve a la pestaña **Prompts**. Selecciona un prompt y rellena sus argumentos.

Observa cómo el resultado es un mensaje estructurado (con `role: "user"` o `"assistant"`)
listo para ser enviado al LLM.

---

## ✅ Verificación

- [ ] Conecté al server de demo y vi todos sus tools
- [ ] Ejecuté al menos 3 tools distintos desde MCP Inspector
- [ ] Leí el contenido de al menos 2 resources
- [ ] Probé al menos 1 prompt con argumentos
- [ ] Puedo explicar la diferencia entre Tool, Resource y Prompt con ejemplos concretos

---

[← Práctica 01](../practica-01/README.md) | [Práctica 03 →](../practica-03/README.md)
