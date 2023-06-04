FROM python:3.10.11-slim AS base

WORKDIR /app

EXPOSE 8501

RUN apt-get update && apt-get install libgomp1

COPY pyproject.toml .
RUN pip install poetry

FROM base AS dependencies
RUN poetry install --no-dev

FROM base AS development
RUN poetry install
COPY . .

FROM dependencies AS production
COPY app app
COPY alembic /app/alembic
COPY run.py .
COPY settings.toml .
COPY alembic.ini .
