# reliability-lab

A hands-on lab for Site Reliability Engineering experiments, built in public.

I'm an SRE with 14+ years in enterprise reliability. This repo is where I practice modern tooling (containers, Python, and AI-assisted development) and turn that practice into small, working reliability projects. Each lab is meant to be something you can clone, build, and run in a few minutes.

## What's inside

| File | Purpose |
| --- | --- |
| `Dockerfile` | A minimal Ubuntu image with `curl` installed, used as a clean, disposable shell for testing and troubleshooting. |
| `health-app/` | A tiny Python (Flask) web app with a `/health` endpoint, runnable with a venv or Docker. See [health-app/README.md](health-app/README.md). |
| `README.md` | This file. |

The current image:

- Starts from `ubuntu:latest`
- Installs `curl` and cleans up the apt cache to keep the image small
- Drops you into a `bash` shell when it starts

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or any Docker Engine), running
- [Git](https://git-scm.com/)

Tested on macOS with Apple Silicon. Docker automatically pulls the ARM64 version of Ubuntu on Apple Silicon and the AMD64 version on Intel machines, so no extra flags are needed.

## Quick start

Clone the repo:

```bash
git clone https://github.com/andrewleec2/reliability-lab.git
cd reliability-lab
```

Build the image:

```bash
docker build -t my-ubuntu .
```

Run an interactive shell inside a container (the container is removed when you exit):

```bash
docker run -it --rm my-ubuntu
```

Try it out from inside the container:

```bash
curl -I https://example.com
exit
```

## Useful commands

```bash
docker images                 # list images you have built
docker ps -a                  # list containers, including stopped ones
docker rmi my-ubuntu          # delete the image
docker system prune           # clean up stopped containers and unused data
```

## Roadmap

Planned labs, roughly in order. Each one will live in its own folder with its own README.

- [x] **Docker basics:** a minimal Ubuntu troubleshooting container
- [x] **Health check app:** a Python web app with a JSON `/health` endpoint, packaged with Docker
- [ ] **Log parser:** a Python CLI that loads application logs into SQLite and reports the top errors by service
- [ ] **Alert triage bot:** an LLM-powered assistant that reads an alert and returns severity, likely component, and three first checks, measured with a scored evaluation set
- [ ] **Runbook search:** retrieval over a small set of runbooks so answers come with citations
- [ ] **Incident assistant:** an agent that searches runbooks, checks (mock) service status, and drafts a postmortem
- [ ] **Production hardening:** deployment, latency and cost metrics, guardrails, and CI checks that fail when evaluation accuracy drops

## Why this repo exists

Reliability work is about judgment: knowing what can fail, how to detect it, and how to recover. AI tools make it faster to build things, but they still need someone who thinks about failure modes, observability, and safe rollouts. This lab is where I combine the two.

## License

No license has been chosen yet. Until one is added, all rights are reserved.
