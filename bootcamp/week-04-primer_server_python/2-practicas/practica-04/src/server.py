# Week 04 — Practice 04: Context, Logging, and MCP Inspector
# Learn: ctx.info/warning, lifespan pattern, ctx.request_context.lifespan_context,
#        Python logging to stderr, MCP_LOG_LEVEL

import sys
import logging

# Python logging must go to stderr, NOT stdout.
# stdout is reserved exclusively for the MCP JSON-RPC protocol.
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stderr,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ============================================
# SECCIÓN A: ctx.info() en un tool
# ============================================
# Context provides methods to send log notifications to the LLM client.
# These appear in MCP Inspector under "Notifications" and in Claude as progress messages.
#
# ctx methods (all require await):
#   await ctx.debug(msg)    — detailed debug info
#   await ctx.info(msg)     — normal progress messages
#   await ctx.warning(msg)  — unusual but non-critical situations
#
# ctx is NOT part of the tool's JSON Schema — FastMCP injects it automatically.

# Descomenta las siguientes líneas:
# from mcp.server.fastmcp import FastMCP, Context
#
# mcp = FastMCP("context-demo")
#
# @mcp.tool()
# async def analyze_text(text: str, ctx: Context) -> dict:
#     """Analyze text and return statistics with progress logging.
#
#     Args:
#         text: Text to analyze.
#     """
#     logger.debug(f"analyze_text called, input length: {len(text)}")
#     await ctx.info(f"Analyzing {len(text)} characters...")
#
#     words = text.split()
#     await ctx.info(f"Found {len(words)} words, counting sentences...")
#
#     sentences = [s.strip() for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
#
#     if len(text) > 1000:
#         await ctx.warning("Large text input, results may take a moment")
#
#     result = {
#         "char_count": len(text),
#         "word_count": len(words),
#         "sentence_count": len(sentences),
#         "avg_word_length": round(sum(len(w) for w in words) / len(words), 2) if words else 0,
#     }
#     await ctx.info("Analysis complete!")
#     logger.info(f"analyze_text result: {result}")
#     return result


# ============================================
# SECCIÓN B: Lifespan context manager
# ============================================
# The lifespan is an async generator that:
#   - Runs BEFORE the server starts accepting requests (STARTUP)
#   - Yields a dict that becomes available to all tools
#   - Resumes AFTER stdin closes (SHUTDOWN)
#
# Use it to: initialize DB connections, load ML models, configure caches, etc.

# Descomenta las siguientes líneas:
# from contextlib import asynccontextmanager
#
# @asynccontextmanager
# async def lifespan(server: FastMCP):
#     # ---- STARTUP ----
#     logger.info("Server lifespan: STARTUP")
#     shared_state = {
#         "request_count": 0,
#         "start_time": __import__("time").time(),
#         "server_name": "context-demo",
#     }
#     logger.info(f"Shared state initialized: {list(shared_state.keys())}")
#
#     yield shared_state   # This dict is available via ctx.request_context.lifespan_context
#
#     # ---- SHUTDOWN ----
#     logger.info(
#         f"Server lifespan: SHUTDOWN after {shared_state['request_count']} requests"
#     )
#
# # IMPORTANT: Pass lifespan to FastMCP constructor
# mcp = FastMCP("context-demo", lifespan=lifespan)


# ============================================
# SECCIÓN C: Acceder al lifespan context desde tools
# ============================================
# ctx.request_context.lifespan_context gives access to the dict from yield.
# Any tool can read AND write to the shared state dict.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def get_server_stats(ctx: Context) -> dict:
#     """Return server runtime statistics from the lifespan context."""
#     import time
#     state = ctx.request_context.lifespan_context
#     state["request_count"] += 1
#     await ctx.info(f"Stats request #{state['request_count']}")
#     return {
#         "server_name": state["server_name"],
#         "total_requests": state["request_count"],
#         "uptime_seconds": round(time.time() - state["start_time"], 1),
#     }
#
# @mcp.tool()
# async def increment_counter(amount: int = 1, ctx: Context = None) -> int:
#     """Increment the request counter by a given amount.
#
#     Args:
#         amount: How much to increment the counter by. Defaults to 1.
#     """
#     state = ctx.request_context.lifespan_context
#     state["request_count"] += amount
#     if ctx:
#         await ctx.info(f"Counter incremented by {amount}, now: {state['request_count']}")
#     return state["request_count"]


# ============================================
# SECCIÓN D: Logging diferenciado
# ============================================
# Compare how Python logging (stderr) and ctx logging (LLM notifications) work together.
# Use Python logging for internal developer debugging.
# Use ctx logging for progress that the LLM/user should see.

# Descomenta las siguientes líneas:
# @mcp.tool()
# async def process_items(items: list[str], ctx: Context) -> dict:
#     """Process a list of items with detailed logging.
#
#     Args:
#         items: List of strings to process.
#     """
#     # Python logging — goes to stderr, visible in docker compose logs
#     logger.info(f"process_items called with {len(items)} items")
#     logger.debug(f"Items: {items}")
#
#     # ctx logging — goes to LLM client as notifications/message
#     await ctx.info(f"Processing {len(items)} items...")
#
#     results = []
#     for i, item in enumerate(items):
#         processed = item.strip().title()
#         results.append(processed)
#         logger.debug(f"  [{i+1}/{len(items)}] '{item}' → '{processed}'")
#
#     # ctx warning if items were empty strings
#     empty_count = sum(1 for item in items if not item.strip())
#     if empty_count > 0:
#         await ctx.warning(f"{empty_count} empty items were skipped")
#
#     await ctx.info("Processing complete!")
#     logger.info(f"process_items done, {len(results)} results")
#
#     return {"processed": results, "count": len(results), "empty_skipped": empty_count}


if __name__ == "__main__":
    logger.info("Starting context-demo server...")
    # mcp.run()   # Uncomment when Sections A and B are uncommented
