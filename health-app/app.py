"""A tiny web app with a /health endpoint.

Run it, then visit http://localhost:8000/health to see a JSON status report.
"""

import os
import platform
import socket
import time
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

# Recorded once, when the app starts, so /health can report uptime.
START_TIME = time.time()


@app.get("/")
def index():
    return jsonify(message="reliability-lab health app. Try /health")


@app.get("/health")
def health():
    return jsonify(
        status="ok",
        service="health-app",
        version=os.environ.get("APP_VERSION", "0.1.0"),
        hostname=socket.gethostname(),
        python=platform.python_version(),
        uptime_seconds=round(time.time() - START_TIME, 1),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    # Development server only. The Docker image uses gunicorn instead.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
