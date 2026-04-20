"""
MCP Server — Weather API con httpx y Open-Meteo
Semana 07 — Practica 02

No requiere API key. Open-Meteo es gratis y abierto.
Docs: https://open-meteo.com/en/docs
"""
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context
import httpx
import json

# ---------------------------------------------------------------------------
# API endpoints (public, no key required)
# ---------------------------------------------------------------------------

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


# ---------------------------------------------------------------------------
# Lifespan — shared HTTP client
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Create one shared httpx.AsyncClient for all tool calls."""
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(connect=5.0, read=10.0),
        headers={"User-Agent": "MCP-Weather-Server/1.0"},
        follow_redirects=True,
    ) as http:
        yield {"http": http}


# ---------------------------------------------------------------------------
# MCP Server setup
# ---------------------------------------------------------------------------

mcp = FastMCP("weather-server", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Base tool (already working — observe this)
# ---------------------------------------------------------------------------

@mcp.tool()
async def ping_api(ctx: Context) -> str:
    """Check connectivity to Open-Meteo API.

    Returns API version and status.
    """
    http: httpx.AsyncClient = ctx.request_context.lifespan_context["http"]

    try:
        response = await http.get(
            FORECAST_URL,
            params={
                "latitude": 40.4168,
                "longitude": -3.7038,
                "current_weather": "true",
            },
        )
        response.raise_for_status()
        return json.dumps({"status": "ok", "api": "Open-Meteo", "reachable": True})

    except httpx.RequestError as e:
        return json.dumps({"status": "error", "reachable": False, "detail": str(e)})


# ============================================
# PASO 2: geocode_city (helper function)
# Convierte un nombre de ciudad en coordenadas
# ============================================
print("--- Paso 2: geocode_city helper ---")

# Esta funcion auxiliar no es un tool — la usan los tools de clima.
# Descomenta las siguientes lineas:

# async def geocode_city(http: httpx.AsyncClient, city: str) -> dict:
#     """Convert city name to latitude/longitude coordinates.
#
#     Returns first result from Open-Meteo geocoding API.
#     Raises ValueError if city is not found.
#     """
#     response = await http.get(
#         GEOCODING_URL,
#         params={"name": city, "count": 1, "language": "en"},
#     )
#     response.raise_for_status()
#     data = response.json()
#
#     results = data.get("results", [])
#     if not results:
#         raise ValueError(f"City not found: {city!r}")
#
#     return results[0]  # {"latitude": ..., "longitude": ..., "name": ..., "country": ...}


# ============================================
# PASO 3: get_current_weather
# Clima actual para una ciudad
# ============================================
print("--- Paso 3: get_current_weather ---")

# Descomenta las siguientes lineas:

# @mcp.tool()
# async def get_current_weather(city: str, ctx: Context) -> str:
#     """Get current weather conditions for a city.
#
#     Uses Open-Meteo API — no API key required.
#
#     Args:
#         city: City name (e.g. "Madrid", "London", "Tokyo")
#
#     Returns:
#         JSON with temperature, wind speed, and weather code
#     """
#     http: httpx.AsyncClient = ctx.request_context.lifespan_context["http"]
#
#     try:
#         location = await geocode_city(http, city)
#
#         response = await http.get(
#             FORECAST_URL,
#             params={
#                 "latitude": location["latitude"],
#                 "longitude": location["longitude"],
#                 "current_weather": "true",
#                 "timezone": "auto",
#             },
#         )
#         response.raise_for_status()
#         weather = response.json()
#
#         return json.dumps({
#             "city": location["name"],
#             "country": location.get("country", ""),
#             "latitude": location["latitude"],
#             "longitude": location["longitude"],
#             "temperature_c": weather["current_weather"]["temperature"],
#             "wind_speed_kmh": weather["current_weather"]["windspeed"],
#             "weather_code": weather["current_weather"]["weathercode"],
#             "is_day": weather["current_weather"].get("is_day", 1),
#         }, ensure_ascii=False)
#
#     except ValueError as e:
#         return json.dumps({"error": "city_not_found", "message": str(e)})
#
#     except httpx.HTTPStatusError as e:
#         return json.dumps({"error": "api_error", "status": e.response.status_code})
#
#     except httpx.TimeoutException:
#         return json.dumps({"error": "timeout", "message": "API did not respond in time"})


# ============================================
# PASO 4: get_forecast
# Pronostico para los proximos N dias
# ============================================
print("--- Paso 4: get_forecast ---")

# Descomenta las siguientes lineas:

# @mcp.tool()
# async def get_forecast(city: str, days: int = 3, ctx: Context = None) -> str:
#     """Get weather forecast for the next N days.
#
#     Args:
#         city: City name
#         days: Number of days (1-7, default 3)
#
#     Returns:
#         JSON with daily max/min temperatures and precipitation
#     """
#     if not 1 <= days <= 7:
#         return json.dumps({
#             "error": "invalid_param",
#             "message": "days must be between 1 and 7",
#         })
#
#     http: httpx.AsyncClient = ctx.request_context.lifespan_context["http"]
#
#     try:
#         location = await geocode_city(http, city)
#
#         response = await http.get(
#             FORECAST_URL,
#             params={
#                 "latitude": location["latitude"],
#                 "longitude": location["longitude"],
#                 "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
#                 "timezone": "auto",
#                 "forecast_days": days,
#             },
#         )
#         response.raise_for_status()
#         data = response.json()
#
#         return json.dumps({
#             "city": location["name"],
#             "country": location.get("country", ""),
#             "forecast_days": days,
#             "daily": data["daily"],
#         }, ensure_ascii=False)
#
#     except ValueError as e:
#         return json.dumps({"error": "city_not_found", "message": str(e)})
#
#     except httpx.TimeoutException:
#         return json.dumps({"error": "timeout"})


# ============================================
# PASO 5: get_weather_safe
# Patron completo con manejo de errores
# ============================================
print("--- Paso 5: get_weather_safe (patron robusto) ---")

# Este tool muestra el patron mas completo con todos los casos de error.
# Descomenta las siguientes lineas:

# @mcp.tool()
# async def get_weather_safe(city: str, ctx: Context) -> str:
#     """Get current weather with full error handling.
#
#     Demonstrates the complete error handling pattern for HTTP tools.
#     """
#     http: httpx.AsyncClient = ctx.request_context.lifespan_context["http"]
#
#     try:
#         location = await geocode_city(http, city)
#         response = await http.get(
#             FORECAST_URL,
#             params={
#                 "latitude": location["latitude"],
#                 "longitude": location["longitude"],
#                 "current_weather": "true",
#             },
#         )
#         response.raise_for_status()
#
#         current = response.json()["current_weather"]
#         return json.dumps({
#             "city": location["name"],
#             "temperature_c": current["temperature"],
#             "wind_speed_kmh": current["windspeed"],
#         })
#
#     except ValueError as e:
#         await ctx.warning(f"City not found: {city}")
#         return json.dumps({"error": "city_not_found", "message": str(e)})
#
#     except httpx.HTTPStatusError as e:
#         await ctx.error(f"API error {e.response.status_code} for {city}")
#         return json.dumps({
#             "error": "api_error",
#             "http_status": e.response.status_code,
#         })
#
#     except httpx.TimeoutException:
#         await ctx.error("Open-Meteo API timeout")
#         return json.dumps({"error": "timeout", "retry": "Try again in a moment"})
#
#     except httpx.ConnectError:
#         return json.dumps({"error": "no_connection", "message": "Cannot reach API"})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import mcp.server.stdio
    import asyncio

    asyncio.run(mcp.server.stdio.stdio_server(mcp))
