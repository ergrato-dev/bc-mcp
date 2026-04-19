# Glosario — Semana 02: JSON-RPC 2.0 y Transports

Términos clave de esta semana, ordenados alfabéticamente.

---

### Batch

Envío de múltiples requests JSON-RPC en un solo mensaje

### HTTP/SSE

Transport MCP sobre HTTP con Server-Sent Events para streaming de respuestas

### JSON-RPC 2.0

Protocolo de llamada a procedimientos remotos basado en JSON

### Notification

Mensaje JSON-RPC sin id — no requiere respuesta

### Request

Mensaje JSON-RPC con id que espera una response del servidor

### Response

Mensaje JSON-RPC de respuesta a un request, con result o error

### Sesión MCP

Conexión completa entre un Client y un Server desde initialize hasta shutdown

### WebSocket

Protocolo de comunicación bidireccional en tiempo real (transport MCP alternativo)

### initialize

Primer mensaje de una sesión MCP para negociar capabilities

### shutdown

Mensaje para terminar ordenadamente una sesión MCP

### stdio

Transport MCP que usa stdin/stdout del proceso para la comunicación

---

[← Volver al README de la semana](../README.md)
