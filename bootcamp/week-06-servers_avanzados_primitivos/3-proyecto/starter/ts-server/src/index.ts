/**
 * Task Manager MCP Server — TypeScript starter.
 * Semana 06 — Proyecto integrador: Tools + Resources + Prompts
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// =============================================
// ESTADO COMPARTIDO
// =============================================
interface Task {
  id: number;
  title: string;
  done: boolean;
  priority: "high" | "medium" | "low";
}

const tasksDb: Task[] = [
  { id: 1, title: "Aprender MCP Resources", done: false, priority: "high" },
  { id: 2, title: "Implementar Prompts", done: false, priority: "high" },
  { id: 3, title: "Leer teoría semana 06", done: true, priority: "medium" },
];
let nextId = 4;

const server = new Server({ name: "task-manager", version: "1.0.0" });

// =============================================
// TOOLS — handlers
// =============================================
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "create_task",
      description: "Creates a new task",
      inputSchema: {
        type: "object",
        properties: {
          title: { type: "string", description: "Task title" },
          priority: {
            type: "string",
            enum: ["high", "medium", "low"],
            description: "Task priority",
          },
        },
        required: ["title"],
      },
    },
    {
      name: "complete_task",
      description: "Marks a task as completed",
      inputSchema: {
        type: "object",
        properties: { task_id: { type: "number", description: "Task ID" } },
        required: ["task_id"],
      },
    },
    {
      name: "delete_task",
      description: "Deletes a task by ID",
      inputSchema: {
        type: "object",
        properties: { task_id: { type: "number" } },
        required: ["task_id"],
      },
    },
    {
      name: "get_task_stats",
      description: "Returns task statistics",
      inputSchema: { type: "object", properties: {} },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "create_task") {
    // TODO: Extraer title y priority (default "medium") de args
    // Validar que priority sea "high" | "medium" | "low"
    // Si no es válido, retornar isError: true con el mensaje de error
    // Crear task: { id: nextId++, title, done: false, priority }
    // Agregar a tasksDb, retornar { content: [{ type: "text", text: JSON.stringify({ created: task }) }] }
    throw new Error("TODO: implement create_task");
  }

  if (name === "complete_task") {
    // TODO: Extraer task_id de args (number)
    // Buscar task en tasksDb
    // Si no existe, retornar isError: true
    // Si existe, marcar task.done = true, retornar { completed: task }
    throw new Error("TODO: implement complete_task");
  }

  if (name === "delete_task") {
    // TODO: Extraer task_id, buscar índice en tasksDb
    // Si no existe, retornar isError: true
    // Usar tasksDb.splice(idx, 1) para eliminar
    // Retornar { deleted: task }
    throw new Error("TODO: implement delete_task");
  }

  if (name === "get_task_stats") {
    // TODO: Calcular total, done, pending y completion_rate
    // Retornar como JSON en content[0].text
    throw new Error("TODO: implement get_task_stats");
  }

  throw new Error(`Unknown tool: ${name}`);
});

// =============================================
// RESOURCES — handlers
// =============================================
server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: [
    { uri: "tasks://all", name: "All Tasks", mimeType: "application/json" },
    { uri: "tasks://pending", name: "Pending Tasks", mimeType: "application/json" },
    { uri: "tasks://done", name: "Completed Tasks", mimeType: "application/json" },
  ],
}));

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  if (uri === "tasks://all") {
    // TODO: Retornar todos los tasksDb como JSON
    // Formato: { contents: [{ uri, mimeType: "application/json", text: JSON.stringify(tasksDb) }] }
    throw new Error("TODO: implement tasks://all resource");
  }

  if (uri === "tasks://pending") {
    // TODO: Filtrar tasksDb donde !task.done y retornar como JSON
    throw new Error("TODO: implement tasks://pending resource");
  }

  if (uri === "tasks://done") {
    // TODO: Filtrar tasksDb donde task.done y retornar como JSON
    throw new Error("TODO: implement tasks://done resource");
  }

  // Template: tasks://{id}
  const templateMatch = uri.match(/^tasks:\/\/(\d+)$/);
  if (templateMatch) {
    // TODO: Extraer id con parseInt(templateMatch[1], 10)
    // Buscar task en tasksDb
    // Retornar task o { error: "Task not found" }
    throw new Error("TODO: implement tasks://{id} template resource");
  }

  throw new Error(`Resource not found: ${uri}`);
});

// =============================================
// PROMPTS — handlers
// =============================================
server.setRequestHandler(ListPromptsRequestSchema, async () => ({
  prompts: [
    {
      name: "daily_review",
      description: "Daily task review conversation starter",
      arguments: [
        { name: "date", description: "Review date (YYYY-MM-DD)", required: true },
      ],
    },
    {
      name: "productivity_report",
      description: "Productivity report conversation starter",
      arguments: [],
    },
  ],
}));

server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "daily_review") {
    // TODO: Extraer date de args
    // Calcular pendingCount = tasksDb.filter(!done).length
    // Calcular highPriorityTitles = tasksDb filtrado por priority==="high" && !done
    // Retornar { description, messages: [{ role: "user", content: { type: "text", text: "..." } }] }
    // El texto debe incluir fecha, pendingCount, highPriorityTitles y solicitar un plan de trabajo
    throw new Error("TODO: implement daily_review prompt");
  }

  if (name === "productivity_report") {
    // TODO: Calcular total, done, pending, completionRate
    // Retornar mensaje que incluya las estadísticas y solicite análisis + recomendaciones
    throw new Error("TODO: implement productivity_report prompt");
  }

  throw new Error(`Unknown prompt: ${name}`);
});

const transport = new StdioServerTransport();
await server.connect(transport);
