# Install uv
FROM python:3.12 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Change the working directory to the `app` directory
WORKDIR /astrosky

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

# Copy the project into the intermediate image
ADD . /astrosky

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

FROM python:3.12-slim

# Copy the environment properly
COPY --from=builder --chown=app:app /astrosky/ /astrosky/

# setting up the path properly
ENV PATH="/astrosky/.venv/bin:$PATH"

# Run the application
CMD ["fastapi", "run", "/astrosky/app/main.py", "--port", "8090", "--proxy-headers"]
