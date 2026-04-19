# Práctica 04 — Identificar Primitivos en un MCP Server Real

## 🎯 Objetivo

Analizar un MCP Server público real y clasificar correctamente cada primitivo que expone,
aplicando el criterio de decisión Tool / Resource / Prompt aprendido en teoría.

## ⏱️ Tiempo estimado: 30 minutos

---

## Prerrequisitos

- Teoría 03 (Los Tres Primitivos) completada
- MCP Inspector corriendo

---

## Paso 1: Conectar al server de filesystem

En MCP Inspector, conecta al server oficial de filesystem:

```
npx -y @modelcontextprotocol/server-filesystem /tmp
```

Este server expone acceso al directorio `/tmp` de tu sistema.

Descomenta la sección **Paso 1** en `starter/clasificacion-primitivos.md`.

---

## Paso 2: Listar y clasificar todos los primitivos

Para cada tool, resource y prompt que encuentres, descomenta la fila correspondiente
en `starter/clasificacion-primitivos.md` y completa:

- Nombre del primitivo
- Tipo (Tool / Resource / Prompt)
- ¿Por qué es ese tipo y no otro?

---

## Paso 3: Conectar al server de memory

Desconecta del server de filesystem y conecta al server de memory:

```
npx -y @modelcontextprotocol/server-memory
```

Repite la clasificación para este server en la sección **Paso 3**.

---

## Paso 4: Diseñar tu propio server (en papel)

Sin escribir código todavía, diseña los primitivos de un MCP Server para un sistema
de gestión de tareas (tipo Todoist simplificado).

Descomenta la sección **Paso 4** en `starter/clasificacion-primitivos.md` y completa
la tabla de diseño.

---

## ✅ Verificación

- [ ] Clasifiqué correctamente todos los primitivos del server de filesystem
- [ ] Clasifiqué correctamente todos los primitivos del server de memory
- [ ] Diseñé al menos 4 Tools, 2 Resources y 1 Prompt para mi server de tareas
- [ ] Puedo justificar cada decisión Tool vs Resource vs Prompt

---

[← Práctica 03](../practica-03/README.md) | [← Volver a Prácticas](../README.md)
