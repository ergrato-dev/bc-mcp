"""
Analizador de sesiones MCP.

Lee un archivo .jsonl con mensajes JSON-RPC y genera un reporte
del ciclo de vida de la sesión MCP.

Uso:
    python session-analyzer.py session-log.jsonl
"""

import json
import sys
from pathlib import Path


def load_messages(filepath: str) -> list[dict]:
    """
    Carga mensajes JSON-RPC desde un archivo .jsonl.

    Cada línea del archivo es un objeto JSON independiente.
    Las líneas vacías se ignoran.

    Args:
        filepath: Ruta al archivo .jsonl

    Returns:
        Lista de objetos JSON (dicts)
    """
    # TODO: Implementar la carga del archivo
    # 1. Abrir el archivo con Path(filepath).read_text()
    # 2. Separar por líneas y filtrar líneas vacías
    # 3. Parsear cada línea con json.loads()
    # 4. Retornar la lista de mensajes
    pass


def classify_message(msg: dict) -> str:
    """
    Clasifica un mensaje JSON-RPC según su tipo.

    Tipos posibles:
    - "request"      → tiene "method" y "id"
    - "response"     → tiene "result" o "error" y "id" (sin "method")
    - "notification" → tiene "method" pero NO tiene "id"
    - "error"        → tiene "error" (sin "result")
    - "unknown"      → no encaja en ninguna categoría

    Args:
        msg: Objeto JSON del mensaje

    Returns:
        String con el tipo de mensaje
    """
    # TODO: Implementar la clasificación
    # Pistas:
    #   - Un request tiene "method" y "id"
    #   - Una notification tiene "method" pero NO tiene "id"
    #   - Una response tiene "result" (y puede tener "id")
    #   - Un error tiene "error" (en lugar de "result")
    pass


def extract_handshake(messages: list[dict]) -> dict | None:
    """
    Extrae la información del handshake MCP de la lista de mensajes.

    El handshake consiste en:
    1. Request "initialize" (del cliente)
    2. Response con "result" que incluye serverInfo y capabilities
    3. Notification "notifications/initialized"

    Args:
        messages: Lista completa de mensajes de la sesión

    Returns:
        Dict con {"request": ..., "response": ..., "initialized": bool}
        o None si no se encontró handshake
    """
    # TODO: Implementar la extracción del handshake
    # 1. Buscar el mensaje con method == "initialize"
    # 2. Buscar la response correspondiente (mismo id)
    # 3. Buscar la notification "notifications/initialized"
    pass


def generate_report(filepath: str, messages: list[dict]) -> str:
    """
    Genera un reporte completo de la sesión MCP.

    El reporte debe incluir:
    - Total de mensajes
    - Conteo por tipo (requests, responses, notifications, errors)
    - Detalles del handshake
    - Lista de métodos llamados con frecuencia
    - Cualquier error encontrado

    Args:
        filepath: Ruta al archivo analizado (para el encabezado)
        messages: Lista de mensajes de la sesión

    Returns:
        String con el reporte formateado
    """
    # TODO: Implementar la generación del reporte
    # Estructura sugerida:
    #
    # === Análisis de Sesión MCP ===
    # Archivo: <filepath>
    # Total de mensajes: N
    #
    # Tipos:
    #   Requests:       N
    #   Responses:      N
    #   Notifications:  N
    #   Errors:         N
    #
    # Handshake:
    #   protocolVersion: ...
    #   serverName: ...
    #   capabilities: ...
    #
    # Métodos llamados:
    #   <method>: N veces
    pass


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python session-analyzer.py <archivo.jsonl>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not Path(filepath).exists():
        print(f"Error: archivo no encontrado: {filepath}")
        sys.exit(1)

    # TODO: Llamar a load_messages() y generate_report()
    # 1. Cargar mensajes con load_messages()
    # 2. Generar reporte con generate_report()
    # 3. Imprimir el reporte
    pass


if __name__ == "__main__":
    main()
