# Week 04 — Practice 02: Type Hints and Auto Schema
# Learn: required vs optional params, list/dict types, Optional/None, Pydantic BaseModel

import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("type-hints-demo")


# ============================================
# SECCIÓN A: Parámetros requeridos vs opcionales
# ============================================
# A parameter WITHOUT a default value is REQUIRED in the JSON Schema.
# A parameter WITH a default value is OPTIONAL (appears only in "properties").
#
# Type hint mapping:
#   str  → {"type": "string"}
#   int  → {"type": "integer"}
#   bool → {"type": "boolean"}

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def search(
#     query: str,                   # Required — no default
#     limit: int = 10,              # Optional — has default
#     case_sensitive: bool = False, # Optional — has default
# ) -> list[str]:
#     """Search for documents matching a query.
#
#     Args:
#         query: The search term to look for.
#         limit: Maximum number of results to return. Defaults to 10.
#         case_sensitive: Whether the search should be case sensitive. Defaults to False.
#     """
#     logger.info(f"Searching for '{query}' (limit={limit}, case={case_sensitive})")
#     # Simulated results
#     results = ["doc1.txt", "report.pdf", "notes.md", "readme.txt", "data.json"]
#     if not case_sensitive:
#         filtered = [r for r in results if query.lower() in r.lower()]
#     else:
#         filtered = [r for r in results if query in r]
#     return filtered[:limit]


# ============================================
# SECCIÓN B: Tipos complejos — list y dict
# ============================================
# list[str]     → {"type": "array", "items": {"type": "string"}}
# dict[str, int] → {"type": "object"}
# Return type dict gets serialized to JSON automatically.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def process_list(
#     items: list[str],
#     separator: str = ", ",
# ) -> dict:
#     """Process a list of strings and return statistics.
#
#     Args:
#         items: List of strings to process.
#         separator: Separator to use when joining. Defaults to comma+space.
#     """
#     return {
#         "count": len(items),
#         "joined": separator.join(items),
#         "longest": max(items, key=len) if items else "",
#         "total_chars": sum(len(item) for item in items),
#     }


# ============================================
# SECCIÓN C: str | None — parámetros verdaderamente opcionales
# ============================================
# str | None = None  means the parameter can be omitted completely
# OR passed as None. It will NOT appear in "required".
# This is the Python 3.10+ syntax (prefer over Optional[str]).

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def get_user(
#     user_id: int,
#     include_email: bool | None = None,   # Truly optional — omittable
#     role_filter: str | None = None,       # Truly optional — omittable
# ) -> dict:
#     """Fetch user data with optional filters.
#
#     Args:
#         user_id: Unique identifier for the user.
#         include_email: Include email address in response. Omit to use default behavior.
#         role_filter: Only return user if they have this role. Omit for no filter.
#     """
#     user = {"id": user_id, "name": "Alice", "role": "admin"}
#     if include_email:
#         user["email"] = f"user{user_id}@example.com"
#     if role_filter and user.get("role") != role_filter:
#         return {}
#     return user


# ============================================
# SECCIÓN D: Pydantic BaseModel como input
# ============================================
# Use BaseModel when a tool has several related parameters.
# Field() adds descriptions and validation constraints to each field.
# FastMCP generates the full JSON Schema from the model automatically.

# Descomenta las siguientes líneas:
# from pydantic import BaseModel, Field
#
# class AnalysisConfig(BaseModel):
#     text: str = Field(..., description="Text to analyze", min_length=1)
#     max_words: int = Field(100, ge=1, le=10000, description="Max words to analyze (1-10000)")
#     include_stats: bool = Field(True, description="Include character and word statistics")
#     language: str = Field("en", description="Language code (e.g. 'en', 'es', 'fr')")
#
# @mcp.tool()
# async def analyze(config: AnalysisConfig) -> dict:
#     """Analyze text using configurable parameters.
#
#     Args:
#         config: Analysis configuration and input text.
#     """
#     words = config.text.split()[:config.max_words]
#     result: dict = {
#         "language": config.language,
#         "word_count": len(words),
#         "truncated": len(config.text.split()) > config.max_words,
#     }
#     if config.include_stats:
#         result["char_count"] = len(config.text)
#         result["avg_word_length"] = (
#             sum(len(w) for w in words) / len(words) if words else 0
#         )
#     return result


if __name__ == "__main__":
    logger.info("Starting type-hints demo server...")
    mcp.run()
