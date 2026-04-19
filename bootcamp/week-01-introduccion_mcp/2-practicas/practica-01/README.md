# Práctica 01 — Configurar el Entorno con Docker

## 🎯 Objetivo

Levantar el entorno Docker del bootcamp y verificar que MCP Inspector está disponible
para explorar servers MCP en las próximas prácticas.

## ⏱️ Tiempo estimado: 45 minutos

---

## Prerrequisitos

- Docker y Docker Compose instalados ([docs/setup/docker.md](../../../../../docs/setup/docker.md))
- Git instalado
- Repositorio clonado localmente

---

## Paso 1: Crear el archivo `docker-compose.yml`

Abre `starter/docker-compose.yml` y descomenta la configuración completa.

**Explicación:** Este compose levanta el servicio `mcp-inspector` que es una herramienta
web para explorar e interactuar con cualquier MCP Server de forma visual.

---

## Paso 2: Crear el archivo `.env`

Abre `starter/.env.example` y crea una copia llamada `.env` en la misma carpeta.

```bash
cp starter/.env.example starter/.env
```

Por ahora no necesitas modificar ningún valor.

---

## Paso 3: Levantar el entorno

```bash
cd starter/
docker compose up --build
```

Deberías ver en la terminal:
```
mcp-inspector  | MCP Inspector running on http://localhost:6274
```

---

## Paso 4: Verificar que funciona

Abre tu navegador en `http://localhost:6274`. Deberías ver la interfaz de MCP Inspector.

**¿Qué ves?**
- Un campo para ingresar el comando de un MCP Server
- Una sección de Tools, Resources y Prompts (vacía por ahora)
- Logs de conexión en el panel inferior

---

## Paso 5: Conectar al server de demo

En el campo "Command" de MCP Inspector, ingresa:

```
npx -y @modelcontextprotocol/server-everything
```

Haz clic en "Connect". Deberías ver los tools y resources del server de demo oficial.

---

## ✅ Verificación

- [ ] Docker Compose levantó sin errores
- [ ] MCP Inspector es accesible en `http://localhost:6274`
- [ ] Pudiste conectar al server `@modelcontextprotocol/server-everything`
- [ ] Ves al menos 5 tools listados en la sección Tools

---

[← Volver a Prácticas](../README.md) | [Práctica 02 →](../practica-02/README.md)
