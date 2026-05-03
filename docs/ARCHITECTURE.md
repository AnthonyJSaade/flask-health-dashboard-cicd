# Architecture Overview

## System Summary

This project delivers a Flask System Health Dashboard through a fully automated CI/CD pipeline. A developer pushes code to GitHub, Jenkins detects the change, builds a Docker image, deploys it with Docker Compose, and verifies the running application through HTTP checks.

---

## High-Level Workflow

```
Developer Pushes Code
        |
        v
  GitHub Repository
        |
        v
  Jenkins Pipeline
     |       |
     v       v
  Run      Build
  Tests    Docker Image
             |
             v
       Docker Compose
       Deployment
             |
             v
  Flask Health Dashboard
  (running on port 8080)
             |
             v
  Jenkins curl Verification
  /api/health + /api/report
```

---

## Components

### GitHub
- Hosts the source repository.
- Provides the single source of truth for all code.
- Tracks collaboration through commit history and pull requests.

### Jenkins
- Runs the automated pipeline defined in `Jenkinsfile`.
- Job is configured as `Pipeline script from SCM` using the GitHub repository.
- Stages: Checkout → Run Route Tests → Build Docker Image → Deploy with Docker Compose → Verify Deployment → Cleanup.
- Verifies the app is reachable before the pipeline is considered successful.
- On macOS, the Jenkins pipeline includes `/usr/local/bin` in its PATH so Docker is available when the job runs.

### Docker
- Packages the Flask application and its dependencies into a portable image.
- Base image: `python:3.12-slim`.
- Image name: `flask-health-dashboard:latest`.
- Exposes port `8080`.

### Docker Compose
- Manages the application stack as a named service (`app`).
- Maps host port `8080` to container port `8080`.
- Sets `APP_ENV=compose` so the dashboard reports its environment correctly.
- Defined in `compose.dashboard.yml`.

### Flask Application
- Lightweight Python web application.
- Serves a browser dashboard at `/`.
- Exposes `/api/health` and `/api/report` JSON endpoints.
- Reads system information at runtime: hostname, Python version, platform, uptime.
- Configuration loaded from `config.json`, overridable via environment variables.

---

## Port Layout

| Service   | Host Port | Container Port |
|-----------|-----------|----------------|
| Flask app | 8080      | 8080           |

> If Jenkins itself runs on port 8080, reassign the Flask host port to 8088 and update `compose.dashboard.yml` and `Jenkinsfile` accordingly. See `RUNBOOK.md` for details.

---

## Data Flow

1. Browser or curl client sends HTTP request to `localhost:8080`.
2. Docker routes the request to the Flask container on port `8080`.
3. Flask calls `diagnostics.py` helpers to gather system data.
4. Flask returns an HTML page or JSON response.

---

## File Responsibilities

| File                  | Responsibility                              |
|-----------------------|---------------------------------------------|
| `app.py`              | Route definitions and HTML template         |
| `diagnostics.py`      | System data collection helpers              |
| `config.json`         | Default application configuration           |
| `requirements.txt`    | Python dependency list                      |
| `Dockerfile`          | Image build instructions                    |
| `compose.dashboard.yml` | Container orchestration configuration     |
| `Jenkinsfile`         | CI/CD pipeline stage definitions            |
| `tests/test_routes.py`| Unit tests for all three routes             |
