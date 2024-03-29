# The builder image, used to build the virtual environment
FROM codeflydev/python-poetry:0.0.1 as builder

WORKDIR /app

COPY src/pyproject.toml src/poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# Runner
FROM python:3.11-slim-buster as runtime

RUN apt-get update


RUN apt-get install -y libpq5


RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
# Set up a non-root user
RUN adduser appuser
USER appuser
ENV VIRTUAL_ENV=/venv \
    PATH="/venv/bin:$PATH"

COPY --chown=appuser --from=builder /venv /venv
COPY --chown=appuser service.codefly.yaml .

# We go be smarter here

COPY --chown=appuser service.codefly.yaml service.codefly.yaml

COPY --chown=appuser src src


EXPOSE 8080



WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
