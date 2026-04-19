# Clasificación de Primitivos MCP

Descomenta cada sección según las instrucciones del README.

---

## Paso 1: Server `@modelcontextprotocol/server-filesystem`

<!-- Descomenta la tabla y completa las columnas vacías: -->

<!--
| Nombre | Tipo | ¿Por qué es ese tipo? |
|--------|------|-----------------------|
| read_file | Tool | Ejecuta una acción: lee un archivo del sistema de archivos |
| read_multiple_files | Tool | |
| write_file | Tool | |
| edit_file | Tool | |
| create_directory | Tool | |
| list_directory | Tool | |
| directory_tree | Tool | |
| move_file | Tool | |
| search_files | Tool | |
| get_file_info | Tool | |
-->

**Reflexión:** ¿Por qué este server NO tiene Resources ni Prompts?
¿Sería correcto exponer el contenido de un archivo como Resource en lugar de Tool?

<!-- Tu respuesta: -->

---

## Paso 2: ¿Podrían ser Resources?

<!-- Descomenta y responde: -->

<!--
El tool `read_file` podría haberse implementado como Resource con URI `file://ruta`.
Analiza las diferencias:

| Aspecto | Como Tool (actual) | Como Resource |
|---------|-------------------|---------------|
| Acceso | El LLM llama explícitamente | El LLM puede leerlo como contexto |
| Parámetros | `path: str` en arguments | Ruta en la URI |
| Cuándo usar | Cuando el LLM decide qué leer | Cuando el Host pre-carga el contexto |
| Ejemplo de uso | "Lee el archivo X y dime..." | "Aquí está el contenido de X para que lo uses" |

¿Cuál diseño prefieres para un server de filesystem? ¿Por qué?

Tu respuesta:
-->

---

## Paso 3: Server `@modelcontextprotocol/server-memory`

<!-- Descomenta la tabla y completa las columnas vacías: -->

<!--
| Nombre | Tipo | ¿Por qué es ese tipo? |
|--------|------|-----------------------|
| create_entities | Tool | Acción con efecto: crea entidades en el grafo de memoria |
| create_relations | Tool | |
| add_observations | Tool | |
| delete_entities | Tool | |
| delete_observations | Tool | |
| delete_relations | Tool | |
| read_graph | Tool | |
| search_nodes | Tool | |
| open_nodes | Tool | |
-->

---

## Paso 4: Diseñar un Server de Gestión de Tareas

<!-- Descomenta y completa la tabla: -->

<!--
### Tools (acciones que el LLM puede ejecutar)

| Nombre | Parámetros | ¿Qué hace? |
|--------|-----------|------------|
| create_task | title: str, priority: str | |
| update_task | task_id: str, status: str | |
| delete_task | task_id: str | |
| list_tasks | status: str \| None | |
| (añade más aquí) | | |

### Resources (datos que el LLM puede leer)

| URI | ¿Qué expone? |
|-----|-------------|
| tasks://schema | |
| tasks://stats | |
| (añade más aquí) | |

### Prompts (plantillas reutilizables)

| Nombre | Argumentos | ¿Para qué sirve? |
|--------|-----------|-----------------|
| daily_review | date: str | |
| (añade más aquí) | | |
-->
