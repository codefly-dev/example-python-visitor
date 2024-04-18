# The builder image, used to build the virtual environment
FROM codeflydev/python-poetry:0.0.1 as builder

WORKDIR /app

COPY src/pyproject.toml src/poetry.lock ./

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

WORKDIR /app

COPY src/pyproject.toml src/poetry.lock ./

RUN poetry install --without dev --no-root


# Runner
FROM python:3.11-slim-buster as runtime

RUN apt-get update



RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
# Set up a non-root user
RUN adduser appuser
USER appuser

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY --chown=appuser service.codefly.yaml .

# We go be smarter here

COPY --chown=appuser service.codefly.yaml service.codefly.yaml

COPY --chown=appuser src src




WORKDIR /app/src
# Standards port for REST is 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
