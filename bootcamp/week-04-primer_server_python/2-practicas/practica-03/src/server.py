# Week 04 — Practice 03: pyproject.toml and uv Dependency Management
# Learn: adding external deps, uv add/sync/lock workflow, httpx async client

import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("uv-deps-demo")


# ============================================
# SECCIÓN A: Tools sin dependencias externas
# ============================================
# These tools use only Python stdlib — no external packages needed.
# pyproject.toml only needs "mcp==1.9.0" for these to work.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def url_info(url: str) -> dict:
#     """Extract basic info from a URL string without making a network request.
#
#     Args:
#         url: The URL to parse.
#     """
#     from urllib.parse import urlparse
#     parsed = urlparse(url)
#     return {
#         "scheme": parsed.scheme,
#         "host": parsed.netloc,
#         "path": parsed.path,
#         "query": parsed.query,
#         "is_https": parsed.scheme == "https",
#     }
#
# @mcp.tool()
# async def encode_url(text: str) -> str:
#     """URL-encode a string.
#
#     Args:
#         text: Text to URL-encode.
#     """
#     from urllib.parse import quote
#     return quote(text, safe="")


# ============================================
# SECCIÓN B: Tool con httpx — fetch de URL
# ============================================
# httpx is an async HTTP client. To use it, add it to pyproject.toml:
#   dependencies = ["mcp==1.9.0", "httpx==0.28.1"]
# Then run: uv lock && uv sync (or docker compose build)
#
# httpx.AsyncClient() is the async version of requests.Session().
# Always use async with to ensure the client is properly closed.

# Descomenta las siguientes líneas:
# import httpx
#
# @mcp.tool()
# async def fetch_metadata(url: str) -> dict:
#     """Fetch HTTP metadata from a URL (headers and status only, no body parsing).
#
#     Args:
#         url: URL to fetch metadata from (must start with http:// or https://).
#     """
#     logger.info(f"Fetching metadata for: {url}")
#     async with httpx.AsyncClient() as client:
#         response = await client.head(url, follow_redirects=True)
#         return {
#             "url": str(response.url),
#             "status_code": response.status_code,
#             "content_type": response.headers.get("content-type", "unknown"),
#             "content_length": response.headers.get("content-length", "unknown"),
#             "server": response.headers.get("server", "unknown"),
#         }


# ============================================
# SECCIÓN C: Manejo de errores de red
# ============================================
# Network operations can fail: timeouts, DNS errors, HTTP errors.
# A good MCP tool handles these gracefully and returns useful error info.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def check_url(url: str) -> dict:
#     """Check if a URL is reachable and return its status.
#
#     Args:
#         url: URL to check for availability.
#     """
#     logger.info(f"Checking URL: {url}")
#     try:
#         async with httpx.AsyncClient(timeout=5.0) as client:
#             response = await client.head(url, follow_redirects=True)
#             return {
#                 "reachable": True,
#                 "status_code": response.status_code,
#                 "ok": response.is_success,
#                 "final_url": str(response.url),
#             }
#     except httpx.TimeoutException:
#         logger.warning(f"Timeout checking {url}")
#         return {"reachable": False, "error": "timeout", "url": url}
#     except httpx.ConnectError as e:
#         logger.warning(f"Connection error for {url}: {e}")
#         return {"reachable": False, "error": "connection_failed", "url": url}
#     except httpx.RequestError as e:
#         logger.error(f"Request error for {url}: {e}")
#         return {"reachable": False, "error": str(e), "url": url}


# ============================================
# SECCIÓN D: Timeout y headers personalizados
# ============================================
# Configure timeouts to avoid hanging indefinitely.
# Add custom headers (e.g., User-Agent) to identify your requests.
# httpx.Timeout allows per-phase timeouts: connect, read, write, pool.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def fetch_with_options(
#     url: str,
#     timeout_seconds: float = 10.0,
#     follow_redirects: bool = True,
# ) -> dict:
#     """Fetch a URL with configurable timeout and redirect behavior.
#
#     Args:
#         url: URL to fetch.
#         timeout_seconds: Request timeout in seconds. Defaults to 10.
#         follow_redirects: Whether to follow HTTP redirects. Defaults to True.
#     """
#     headers = {
#         "User-Agent": "MCP-Server/1.0 (bootcamp-week04)",
#         "Accept": "text/html,application/json,*/*",
#     }
#     timeout = httpx.Timeout(timeout_seconds, connect=5.0)
#     try:
#         async with httpx.AsyncClient(headers=headers, timeout=timeout) as client:
#             response = await client.get(url, follow_redirects=follow_redirects)
#             return {
#                 "status_code": response.status_code,
#                 "final_url": str(response.url),
#                 "content_type": response.headers.get("content-type", ""),
#                 "body_preview": response.text[:200] if response.is_success else "",
#                 "redirect_count": len(response.history),
#             }
#     except httpx.TimeoutException:
#         return {"error": f"Request timed out after {timeout_seconds}s", "url": url}
#     except httpx.RequestError as e:
#         return {"error": str(e), "url": url}


if __name__ == "__main__":
    logger.info("Starting uv-deps-demo server...")
    mcp.run()
