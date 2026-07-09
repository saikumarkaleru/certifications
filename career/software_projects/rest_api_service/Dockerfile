# Production-style image: slim base, non-root user, no cache bloat.
FROM python:3.13-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first for better layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code.
COPY app ./app

# Run as an unprivileged user.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# Uvicorn ASGI server.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
