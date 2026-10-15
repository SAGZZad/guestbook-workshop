FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync --frozen

COPY . .

C
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
