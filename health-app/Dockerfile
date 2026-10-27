# Small official Python image (works on Apple Silicon and Intel).
FROM python:3.13-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer between builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Run as a non-root user, a basic container hardening step.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# Docker marks the container healthy or unhealthy based on this check.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# gunicorn is a production-grade server for Python web apps.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
