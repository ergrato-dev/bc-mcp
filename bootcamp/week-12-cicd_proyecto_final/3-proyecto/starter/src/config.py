"""Configuration management using Pydantic Settings.

Reads environment variables from .env file with type validation.
"""

# ============================================
# TODO: Implementar clase Settings con Pydantic
# ============================================
# Importar BaseSettings de pydantic_settings y leer:
# - DB_PATH: str = "/data/library.db"
# - OPENLIBRARY_URL: str = "https://openlibrary.org"
# - MAX_SEARCH_RESULTS: int = 20
#
# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     db_path: str = "/data/library.db"
#     openlibrary_url: str = "https://openlibrary.org"
#     max_search_results: int = 20
#
#     model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}
