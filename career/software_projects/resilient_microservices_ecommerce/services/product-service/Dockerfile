# syntax=docker/dockerfile:1
FROM python:3.13-slim

# Don't write .pyc, unbuffered stdout for real-time logs in k8s.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DB_PATH=/data/product.db

WORKDIR /app

# Install deps first for better layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Persist the SQLite file on a writable volume.
RUN mkdir -p /data

# Run as an unprivileged user (security best practice).
RUN useradd -m appuser && chown -R appuser /data /app
USER appuser

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/healthz').status==200 else 1)"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
