"""
config.py — Carga y valida la configuración del agente desde variables de entorno.

TODO: Implementar este módulo para que el agente pueda leer sus ajustes desde .env
"""
# TODO 1: Importar os y load_dotenv de python-dotenv
#   - Importar os
#   - Importar load_dotenv desde dotenv
#   - Llamar a load_dotenv() para cargar el archivo .env

# TODO 2: Definir las constantes de configuración
#   Las variables que debes leer del entorno son:
#
#   ANTHROPIC_API_KEY  — requerida, debe lanzar error si no existe
#   MODEL              — opcional, default "claude-opus-4-5"
#   MAX_TOKENS         — opcional, default 4096 (convertir a int)
#   MAX_ITERATIONS     — opcional, default 10 (convertir a int)
#   SERVER_SCRIPT      — ruta al script del MCP Server (requerida)
#   DB_PATH            — ruta a la base de datos SQLite (opcional)
#
#   Ejemplo de cómo leer una variable requerida:
#   ANTHROPIC_API_KEY: str = os.environ["ANTHROPIC_API_KEY"]
#
#   Ejemplo de cómo leer una variable opcional con default:
#   MODEL: str = os.getenv("MODEL", "claude-opus-4-5")

# TODO 3: Agregar un bloque de validación que imprima las variables cargadas
#   (solo en modo debug, sin imprimir la API key completa)
#
#   Sugerencia:
#   if __name__ == "__main__":
#       print(f"Model: {MODEL}")
#       print(f"API key presente: {'Sí' if ANTHROPIC_API_KEY else 'No'}")
#       print(f"Server script: {SERVER_SCRIPT}")
