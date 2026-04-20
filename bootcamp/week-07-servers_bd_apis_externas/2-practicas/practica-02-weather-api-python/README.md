# Practica 02 — Weather API con Python y httpx

## 🎯 Objetivo

Integrar la API de clima Open-Meteo en un MCP Server Python usando `httpx`.
Open-Meteo es completamente gratuita — sin registro ni API key.

## 📋 Que aprenderás

- Usar `httpx.AsyncClient` para llamadas HTTP asíncronas
- Encadenar dos llamadas API: geocoding → forecast
- Manejar errores de red: timeouts, ciudades no encontradas, 5xx
- Compartir un cliente HTTP via lifespan pattern

## 🗂️ Estructura

```
practica-02-weather-api-python/
├── README.md
├── Dockerfile.python
├── docker-compose.yml
├── pyproject.toml
└── src/
    └── server.py       ← archivo principal (descomentar secciones)
```

## ⚙️ Setup

```bash
cd practica-02-weather-api-python
docker compose up --build
```

## 🌐 APIs utilizadas (sin API key)

- **Geocoding**: `https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1`
- **Forecast**: `https://api.open-meteo.com/v1/forecast?latitude=...&longitude=...`

## 📝 Instrucciones

### Paso 1 — Explorar el servidor base

Abre `src/server.py` y observa el lifespan que crea el `httpx.AsyncClient`.
El server ya tiene un tool `ping_api` que verifica la conectividad.

### Paso 2 — Activar geocode_city (helper)

La funcion auxiliar `geocode_city` convierte un nombre de ciudad en coordenadas.
Descomenta la seccion `# PASO 2` — esta funcion es requerida por los tools siguientes.

### Paso 3 — Activar get_current_weather

Descomenta la seccion `# PASO 3`.
El tool usa `geocode_city` y luego llama al forecast de Open-Meteo.

Prueba con ciudades como: "Madrid", "London", "Tokyo", "Buenos Aires".

### Paso 4 — Activar get_forecast

Descomenta la seccion `# PASO 4`.
El tool retorna el pronostico para los proximos N dias (1-7).

Observa como el parametro `daily` cambia el formato de la respuesta.

### Paso 5 — Manejo de errores

Descomenta la seccion `# PASO 5`.
El tool `get_weather_safe` muestra el patron completo con manejo de errores.

Prueba con: una ciudad inexistente, un nombre con tildes, una ciudad con espacios.

## ✅ Criterios de éxito

- [ ] `ping_api` confirma conectividad con Open-Meteo
- [ ] `get_current_weather` retorna temperatura y velocidad del viento
- [ ] `get_forecast` retorna pronostico de N dias
- [ ] Ciudades inexistentes retornan un error descriptivo
- [ ] Los timeouts se manejan correctamente
