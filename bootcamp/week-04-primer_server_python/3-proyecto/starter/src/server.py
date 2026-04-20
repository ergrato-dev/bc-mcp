# Week 04 — Project: Python Utility MCP Server
# Implement a utility server with 3 tools: calculate, transform_text, date_info
#
# HOW TO COMPLETE THIS PROJECT:
#   1. Read each TODO comment carefully — it describes exactly what to implement
#   2. Implement the logic where marked with "# TODO"
#   3. Run docker compose up --build to verify
#   4. Test with MCP Inspector: npx @modelcontextprotocol/inspector uv run python src/server.py

import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP(
    "utility-server",
    instructions=(
        "A utility server that provides math calculations, "
        "text transformations, and date information."
    ),
)


# ============================================
# TOOL 1: calculate
# ============================================
# Performs basic arithmetic operations on two numbers.
# Must handle: add (+), subtract (-), multiply (*), divide (/)
# Must raise an error for division by zero and unknown operations.

@mcp.tool()
async def calculate(
    operation: str,
    a: float,
    b: float,
    ctx: Context,
) -> float:
    """Perform a basic arithmetic operation on two numbers.

    Args:
        operation: The operation to perform: 'add', 'subtract', 'multiply', or 'divide'.
        a: First operand.
        b: Second operand.
    """
    await ctx.info(f"Calculating: {a} {operation} {b}")
    logger.info(f"calculate(operation={operation!r}, a={a}, b={b})")

    # TODO: Implement the calculation logic
    # 1. Create a mapping of operation names to their implementations
    #    Supported operations: 'add', 'subtract', 'multiply', 'divide'
    # 2. Handle the special case of division by zero for 'divide'
    #    → raise ValueError("Division by zero is not allowed")
    # 3. If the operation is not recognized, raise ValueError with a helpful message
    #    → raise ValueError(f"Unknown operation: '{operation}'. Use: add, subtract, multiply, divide")
    # 4. Return the result of the operation
    pass


# ============================================
# TOOL 2: transform_text
# ============================================
# Applies a text transformation to a string.
# Must support: upper, lower, reverse, title, word_count

@mcp.tool()
async def transform_text(
    text: str,
    operation: str,
    ctx: Context,
) -> str:
    """Apply a transformation to a text string.

    Args:
        text: Input text to transform.
        operation: Transformation to apply: 'upper', 'lower', 'reverse', 'title', or 'word_count'.
    """
    await ctx.info(f"Transforming text with operation: {operation}")
    logger.info(f"transform_text(operation={operation!r}, len={len(text)})")

    # TODO: Implement text transformations
    # 1. Create a mapping of operation names to transformation functions:
    #    - 'upper'      → str.upper (e.g. "hello" → "HELLO")
    #    - 'lower'      → str.lower (e.g. "HELLO" → "hello")
    #    - 'reverse'    → lambda s: s[::-1] (e.g. "hello" → "olleh")
    #    - 'title'      → str.title (e.g. "hello world" → "Hello World")
    #    - 'word_count' → lambda s: str(len(s.split())) (e.g. "hello world" → "2")
    # 2. If the operation is not recognized, raise ValueError with a helpful message
    #    listing all valid operations
    # 3. Apply the transformation and return the result as a string
    # Note: word_count should return a string (e.g. "5 words"), not an int
    pass


# ============================================
# TOOL 3: date_info
# ============================================
# Parses a date string and returns information about it.
# Must return: weekday, days_until, days_since, is_weekend, iso_format

@mcp.tool()
async def date_info(
    date_string: str,
    ctx: Context,
) -> dict:
    """Parse a date and return detailed information about it.

    Args:
        date_string: Date in YYYY-MM-DD format (e.g. '2025-12-31').
    """
    from datetime import datetime, date

    await ctx.info(f"Parsing date: {date_string}")
    logger.info(f"date_info(date_string={date_string!r})")

    # TODO: Implement date parsing and information extraction
    # 1. Parse the date_string using datetime.strptime(date_string, "%Y-%m-%d").date()
    #    If it fails (ValueError), return a dict with key "error" and a descriptive message
    #    e.g. {"error": "Invalid date format: '2025-13-01'. Use YYYY-MM-DD."}
    # 2. Get today's date with date.today()
    # 3. Calculate delta = (target_date - today).days
    # 4. Return a dict with these keys:
    #    - "date"        → the date string as given (date_string)
    #    - "weekday"     → full weekday name (e.g. "Monday") using strftime("%A")
    #    - "iso_format"  → ISO format string (e.g. "2025-12-31") using isoformat()
    #    - "days_until"  → int, positive if future, negative if past, 0 if today
    #    - "days_since"  → int, the negation of days_until (positive if past)
    #    - "is_weekend"  → bool, True if weekday() >= 5 (Saturday=5, Sunday=6)
    #    - "is_today"    → bool, True if delta == 0
    #    - "is_future"   → bool, True if delta > 0
    pass


if __name__ == "__main__":
    logger.info("Starting utility-server...")
    mcp.run()
