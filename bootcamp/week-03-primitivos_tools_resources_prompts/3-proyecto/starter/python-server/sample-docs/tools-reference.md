# MCP Tools Reference

## Overview

A **Tool** is an MCP primitive that represents an executable function.
The LLM calls tools to take actions or retrieve computed data.

## inputSchema

Every tool must declare a JSON Schema for its inputs:

```json
{
  "type": "object",
  "properties": {
    "query": { "type": "string", "description": "Search text" }
  },
  "required": ["query"],
  "additionalProperties": false
}
```

Setting `additionalProperties: false` prevents unexpected fields.

## ToolAnnotations

Annotations let the client understand the tool's behavior:

- `readOnlyHint`: the tool does not modify state
- `destructiveHint`: the tool may delete or overwrite data
- `idempotentHint`: calling with the same arguments always produces the same result

## isError

When a tool execution fails logically (not a crash), return `isError: true`:

```python
return types.CallToolResult(
    content=[types.TextContent(type="text", text="Item not found")],
    isError=True
)
```
