# MCP Resources Reference

## Overview

A **Resource** is an MCP primitive for exposing read-only data via a URI.
Resources are fetched by the client, not invoked like tools.

## URI Design

Resources use a scheme-based URI:

```
db://users/42          # Database record
file://logs/app.log    # File system
config://app/settings  # Configuration
api://github/repos     # External API data
```

## Resource Types

### TextResourceContents

For text data (JSON, Markdown, plain text):

```python
types.TextResourceContents(
    uri="db://users/42",
    text='{"id": 42, "name": "Alice"}',
    mimeType="application/json"
)
```

### BlobResourceContents

For binary data (images, PDFs) encoded in base64:

```python
types.BlobResourceContents(
    uri="file://logo.png",
    blob=base64.b64encode(image_bytes).decode(),
    mimeType="image/png"
)
```

## ResourceTemplates

Templates allow parameterized URIs using RFC 6570 syntax:

```
docs://files/{filename}
db://users/{user_id}
```
