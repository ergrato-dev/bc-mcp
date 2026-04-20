"""
config.py — Load and validate settings from environment variables.

All configuration comes from .env (loaded by python-dotenv in client.py).
Using os.environ directly (no third-party config library) to keep it simple.
"""

import os
from pathlib import Path


def _require(key: str) -> str:
    """Return the value of an env var; raise if missing or empty."""
    value = os.environ.get(key, "").strip()
    if not value:
        raise EnvironmentError(
            f"Required environment variable '{key}' is not set. "
            "Copy .env.example to .env and fill in the values."
        )
    return value


# Command used to launch the MCP server process (e.g. "python", "uv")
SERVER_COMMAND: str = os.environ.get("SERVER_COMMAND", "python")

# Path to the server entry point (passed as first argument to SERVER_COMMAND)
SERVER_PATH: str = _require("SERVER_PATH")

# Path to the SQLite database (forwarded to the server as env var)
DB_PATH: str = os.environ.get("DB_PATH", "./data/library.db")

# Ensure the data directory exists (needed when running locally)
Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

# Maximum seconds to wait for a single tool call
TOOL_TIMEOUT: float = float(os.environ.get("TOOL_TIMEOUT_SECONDS", "30"))
