# Week 04 — Practice 05: Multiple Tools with Different Types
# Learn: organizing multiple tools, math/text/datetime types, lifespan history tracking
# This practice consolidates everything from the week.

import sys
import logging
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


# ============================================
# SECCIÓN A: Tools matemáticos
# ============================================
# Math tools demonstrate numeric type hints: int and float.
# int   → {"type": "integer"} in JSON Schema
# float → {"type": "number"} in JSON Schema
# Both types return a numeric value, which FastMCP serializes as a string.

# Descomenta las siguientes líneas:
# @asynccontextmanager
# async def lifespan(server: FastMCP):
#     state = {"call_history": [], "total_calls": 0}
#     yield state
#     logger.info(f"Server done. Total calls: {state['total_calls']}")
#
# mcp = FastMCP("multi-tools", lifespan=lifespan)
#
# @mcp.tool()
# async def add(a: float, b: float) -> float:
#     """Add two numbers.
#
#     Args:
#         a: First number (int or float).
#         b: Second number (int or float).
#     """
#     return a + b
#
# @mcp.tool()
# async def multiply(a: float, b: float) -> float:
#     """Multiply two numbers.
#
#     Args:
#         a: First number.
#         b: Second number.
#     """
#     return a * b
#
# @mcp.tool()
# async def factorial(n: int) -> int:
#     """Compute the factorial of a non-negative integer.
#
#     Args:
#         n: Non-negative integer to compute factorial of (0 <= n <= 20).
#     """
#     if n < 0:
#         raise ValueError("n must be non-negative")
#     if n > 20:
#         raise ValueError("n must be <= 20 to avoid overflow")
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result


# ============================================
# SECCIÓN B: Tools de texto
# ============================================
# Text tools show how to work with strings, lists, and dict return types.
# list[str] → {"type": "array", "items": {"type": "string"}}
# dict      → {"type": "object"} — FastMCP serializes to JSON

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def word_count(text: str) -> dict:
#     """Count words, characters, and sentences in a text.
#
#     Args:
#         text: Text to analyze.
#     """
#     words = text.split()
#     sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
#     return {
#         "words": len(words),
#         "characters": len(text),
#         "characters_no_spaces": len(text.replace(" ", "")),
#         "sentences": len(sentences),
#         "paragraphs": len([p for p in text.split("\n\n") if p.strip()]),
#     }
#
# @mcp.tool()
# async def reverse_text(text: str, word_level: bool = False) -> str:
#     """Reverse a string at character or word level.
#
#     Args:
#         text: Text to reverse.
#         word_level: If True, reverse word order instead of characters. Defaults to False.
#     """
#     if word_level:
#         return " ".join(text.split()[::-1])
#     return text[::-1]
#
# @mcp.tool()
# async def transform_case(text: str, mode: str = "upper") -> str:
#     """Transform text case.
#
#     Args:
#         text: Text to transform.
#         mode: Case mode — 'upper', 'lower', 'title', or 'swap'. Defaults to 'upper'.
#     """
#     modes = {
#         "upper": str.upper,
#         "lower": str.lower,
#         "title": str.title,
#         "swap": str.swapcase,
#     }
#     transform = modes.get(mode, str.upper)
#     return transform(text)


# ============================================
# SECCIÓN C: Tools de fecha y hora
# ============================================
# Datetime tools demonstrate working with Python's stdlib datetime module.
# Always return dates as strings (ISO format) or structured dicts.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def current_datetime(timezone_offset: int = 0) -> dict:
#     """Get the current date and time.
#
#     Args:
#         timezone_offset: UTC offset in hours (e.g. -5 for EST, 1 for CET). Defaults to 0 (UTC).
#     """
#     from datetime import datetime, timezone, timedelta
#     tz = timezone(timedelta(hours=timezone_offset))
#     now = datetime.now(tz)
#     return {
#         "iso": now.isoformat(),
#         "date": now.strftime("%Y-%m-%d"),
#         "time": now.strftime("%H:%M:%S"),
#         "weekday": now.strftime("%A"),
#         "timezone_offset": timezone_offset,
#     }
#
# @mcp.tool()
# async def days_until(target_date: str) -> dict:
#     """Calculate how many days until a target date.
#
#     Args:
#         target_date: Target date in YYYY-MM-DD format (e.g. '2025-12-31').
#     """
#     from datetime import datetime, date
#     try:
#         target = datetime.strptime(target_date, "%Y-%m-%d").date()
#         today = date.today()
#         delta = (target - today).days
#         return {
#             "target_date": target_date,
#             "today": today.isoformat(),
#             "days_until": delta,
#             "is_past": delta < 0,
#             "is_today": delta == 0,
#             "weeks_until": round(delta / 7, 1),
#         }
#     except ValueError:
#         return {"error": f"Invalid date format: '{target_date}'. Use YYYY-MM-DD."}


# ============================================
# SECCIÓN D: Integrar Context en todos los tools
# ============================================
# Add Context to tools to report progress to the LLM client.
# Also adds get_history tool that reads from the lifespan shared state.

# Descomenta las siguientes líneas y agrega ctx: Context a los tools anteriores:
# @mcp.tool()
# async def get_history(ctx: Context) -> dict:
#     """Get the history of tool calls in this session."""
#     state = ctx.request_context.lifespan_context
#     await ctx.info(f"Retrieving history: {state['total_calls']} total calls")
#     return {
#         "total_calls": state["total_calls"],
#         "last_10_calls": state["call_history"][-10:],
#     }
#
# def track_call(tool_name: str, ctx: Context) -> None:
#     """Helper to track tool calls in the lifespan state."""
#     state = ctx.request_context.lifespan_context
#     state["total_calls"] += 1
#     state["call_history"].append({
#         "tool": tool_name,
#         "call_number": state["total_calls"],
#     })


if __name__ == "__main__":
    logger.info("Starting multi-tools server...")
    # mcp.run()   # Uncomment when Section A is uncommented
