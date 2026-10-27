# health-app

A tiny Python web app with a `/health` endpoint that returns JSON. Health endpoints are how load balancers, Kubernetes, and monitoring tools ask a service "are you alive?", so this is the smallest useful building block for later labs.

## What each file does

| File | Purpose |
| --- | --- |
| `app.py` | The web app, written with [Flask](https://flask.palletsprojects.com/). It has two routes: `/` and `/health`. |
| `requirements.txt` | The Python packages the app needs, pinned to exact versions so every install is the same. |
| `Dockerfile` | Instructions to package the app into a container image. It runs the app with gunicorn as a non-root user and includes a Docker `HEALTHCHECK`. |
| `.dockerignore` / `.gitignore` | Keep the local virtual environment and Python cache files out of the image and out of git. |

## Example response

```bash
curl -s http://localhost:8000/health
```

```json
{
  "status": "ok",
  "service": "health-app",
  "version": "0.1.0",
  "hostname": "my-macbook",
  "python": "3.13.1",
  "uptime_seconds": 12.4,
  "timestamp": "2026-10-27T07:00:00+00:00"
}
```

## Option 1: run with a Python virtual environment

A virtual environment (venv) is a private folder of Python packages for this project, so it does not touch the rest of your Mac.

```bash
cd health-app
python3 -m venv .venv            # create the venv (once)
source .venv/bin/activate        # turn it on for this terminal
pip install -r requirements.txt  # install Flask and gunicorn into it
python app.py                    # start the app on port 8000
```

In a second terminal tab:

```bash
curl -s http://localhost:8000/health
```

Stop the app with `Ctrl+C`, and leave the venv with `deactivate`.

## Option 2: run with Docker

```bash
cd health-app
docker build -t health-app .
docker run -d --rm --name health-app -p 8000:8000 health-app
curl -s http://localhost:8000/health
docker ps                         # after ~30s STATUS shows (healthy)
docker stop health-app
```

`-p 8000:8000` connects port 8000 on your Mac to port 8000 inside the container. `-d` runs it in the background and `--rm` deletes the container when it stops.

If port 8000 is already in use, pick another one on the Mac side, for example `-p 8080:8000`, then curl `localhost:8080`.
