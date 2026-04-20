# Proyecto Semana 05 — Servidor Utilitario TypeScript

## 🎯 Descripción

Implementarás un MCP Server completo en TypeScript con tres tools utilitarios:
`calculate`, `transform_text` y `date_info`. Es el equivalente TypeScript del
servidor Python que construiste en la semana 04.

## 📋 Instrucciones

1. Lee el material teórico de [`1-teoria/`](../1-teoria/) antes de comenzar
2. Completa las prácticas de [`2-practicas/`](../2-practicas/) como preparación
3. Trabaja en el directorio `starter/` — **no modifiques** archivos fuera de él
4. Implementa los tres tools con las instrucciones en los comentarios `TODO`
5. Usa Docker para ejecutar tu solución: `docker compose up --build`
6. Verifica con el inspector MCP que los tres tools funcionan correctamente

## 🛠️ Tools a implementar

### `calculate(operation, a, b)`

Operaciones: `add`, `subtract`, `multiply`, `divide`

Requisitos:
- Usar `z.enum()` para validar la operación
- Retornar `isError: true` si se divide por cero
- El resultado debe ser un número como texto

### `transform_text(text, operation)`

Operaciones: `upper`, `lower`, `reverse`, `title`, `word_count`

Requisitos:
- Usar `z.enum()` para validar la operación
- `word_count` debe retornar JSON con `{ words, characters, lines }`
- `title` capitaliza la primera letra de cada palabra

### `date_info(date_string)`

Formato esperado: `YYYY-MM-DD`

Requisitos:
- Validar que la fecha sea válida — `isError: true` si no lo es
- Retornar JSON con `{ date, weekday, is_weekend, days_until, is_past }`

## 📌 Entregables

- [ ] `starter/src/index.ts` con los tres tools implementados
- [ ] `pnpm build` compila sin errores TypeScript
- [ ] `docker compose up --build` arranca el servidor
- [ ] `tools/list` devuelve los tres tools
- [ ] Cada tool retorna el resultado correcto con valores válidos
- [ ] `calculate` con `b=0` y `divide` retorna `isError: true`
- [ ] `date_info` con fecha inválida retorna `isError: true`

## 🏗️ Estructura del proyecto

```
3-proyecto/
├── README.md          ← este archivo
└── starter/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── package.json
    ├── tsconfig.json
    └── src/
        └── index.ts   ← implementa los TODOs aquí
```

## 🚀 Comandos

```bash
cd starter

# Opción A — Docker (recomendado)
docker compose up --build

# Opción B — Local
pnpm install
pnpm build
pnpm start

# Probar manualmente
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | node dist/index.js
```

> ⚠️ La carpeta `solution/` es solo para instructores y está en `.gitignore`.

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) para los criterios detallados.

---

[← Volver al README de la semana](../README.md)
