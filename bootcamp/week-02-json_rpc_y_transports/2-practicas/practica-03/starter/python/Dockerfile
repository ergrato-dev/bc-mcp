FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  UV_SYSTEM_PYTHON=1
RUN pip install --no-cache-dir uv==0.6.14
WORKDIR /app
COPY pyproject.toml ./
RUN uv sync --no-dev
COPY . .
CMD ["uv", "run", "python", "src/server.py"]
