"""
Task Manager MCP Server — Python starter.
Semana 06 — Proyecto integrador: Tools + Resources + Prompts
"""

import json
from mcp.server.fastmcp import FastMCP
from mcp.types import Message, TextContent

mcp = FastMCP("task-manager")

# =============================================
# ESTADO COMPARTIDO
# =============================================
TASKS: list[dict] = [
    {"id": 1, "title": "Aprender MCP Resources", "done": False, "priority": "high"},
    {"id": 2, "title": "Implementar Prompts", "done": False, "priority": "high"},
    {"id": 3, "title": "Leer teoría semana 06", "done": True, "priority": "medium"},
]
_next_id = 4


# =============================================
# TOOLS
# =============================================

@mcp.tool()
async def create_task(title: str, priority: str = "medium") -> dict:
    """Creates a new task.

    Args:
        title: Task title.
        priority: Priority level: high, medium, or low.
    """
    global _next_id
    # TODO: Validar que priority sea "high", "medium" o "low"
    # Si no es válido, retornar {"error": "Invalid priority: <priority>"}

    # TODO: Crear el task con id=_next_id, title=title, done=False, priority=priority
    # Agregar a TASKS, incrementar _next_id
    # Retornar {"created": task}
    pass


@mcp.tool()
async def complete_task(task_id: int) -> dict:
    """Marks a task as completed.

    Args:
        task_id: The numeric ID of the task.
    """
    # TODO: Buscar el task con id == task_id en TASKS
    # Si no existe, retornar {"error": f"Task {task_id} not found"}
    # Si existe, marcar task["done"] = True
    # Retornar {"completed": task}
    pass


@mcp.tool()
async def delete_task(task_id: int) -> dict:
    """Deletes a task by ID.

    Args:
        task_id: The numeric ID of the task to delete.
    """
    global TASKS
    # TODO: Buscar el task con id == task_id
    # Si no existe, retornar {"error": f"Task {task_id} not found"}
    # Si existe, eliminar de TASKS y retornar {"deleted": task}
    pass


@mcp.tool()
async def get_task_stats() -> dict:
    """Returns task statistics: total, done, pending counts and completion rate."""
    # TODO: Calcular:
    # total = len(TASKS)
    # done = cantidad de tasks con done=True
    # pending = total - done
    # completion_rate = done / total * 100 (redondeado a 1 decimal), o 0 si total==0
    # Retornar dict con esos 4 valores
    pass


# =============================================
# RESOURCES
# =============================================

@mcp.resource("tasks://all")
async def resource_all_tasks() -> str:
    """Returns all tasks as JSON."""
    # TODO: Retornar json.dumps(TASKS, ensure_ascii=False)
    pass


@mcp.resource("tasks://pending")
async def resource_pending_tasks() -> str:
    """Returns only pending (not done) tasks as JSON."""
    # TODO: Filtrar TASKS donde done==False y retornar como JSON
    pass


@mcp.resource("tasks://done")
async def resource_done_tasks() -> str:
    """Returns only completed tasks as JSON."""
    # TODO: Filtrar TASKS donde done==True y retornar como JSON
    pass


@mcp.resource("tasks://{task_id}")
async def resource_task_by_id(task_id: str) -> str:
    """Returns a specific task by ID.

    Args:
        task_id: Numeric task ID extracted from the URI template.
    """
    # TODO: Validar que task_id.isdigit()
    # Si no, retornar json.dumps({"error": "task_id must be a positive integer"})
    # Buscar task con id == int(task_id)
    # Si no existe, retornar json.dumps({"error": f"Task {task_id} not found"})
    # Si existe, retornar json.dumps(task, ensure_ascii=False)
    pass


# =============================================
# PROMPTS
# =============================================

@mcp.prompt()
async def daily_review(date: str) -> list[Message]:
    """Generates a daily task review conversation starter.

    Args:
        date: Review date in YYYY-MM-DD format.
    """
    # TODO:
    # Calcular pending_count = cantidad de tasks con done==False
    # Calcular high_priority = lista de titles con priority=="high" y done==False
    # Retornar list[Message] con un mensaje "user" que incluya:
    # - La fecha (date)
    # - Cuántas tareas pendientes hay
    # - Las tareas de alta prioridad
    # - Una petición de plan de trabajo para el día
    pass


@mcp.prompt()
async def productivity_report() -> list[Message]:
    """Generates a productivity report conversation starter."""
    # TODO:
    # Calcular las estadísticas: total, done, pending, completion_rate
    # Retornar list[Message] con un mensaje "user" que incluya las estadísticas
    # y solicite un análisis de productividad con recomendaciones
    pass


if __name__ == "__main__":
    mcp.run()
