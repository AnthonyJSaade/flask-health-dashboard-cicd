# Runbook — Flask Health Dashboard

## Prerequisites

Ensure the following are installed before running anything:

| Tool          | Minimum Version | Check Command          |
|---------------|-----------------|------------------------|
| Python        | 3.10+           | `python3 --version`    |
| pip           | any             | `pip --version`        |
| Docker        | 24+             | `docker --version`     |
| Docker Compose| v2 (plugin)     | `docker compose version` |
| Git           | any             | `git --version`        |
| curl          | any             | `curl --version`       |

---

## 1. Clone the Repository

```bash
git clone https://github.com/AnthonyJSaade/flask-health-dashboard-cicd.git
cd flask-health-dashboard-cicd
```

---

## 2. Run Locally (no Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Verify:
```bash
curl http://localhost:8080/api/health
curl http://localhost:8080/api/report
```

Open `http://localhost:8080` in a browser to see the dashboard.

Stop: `Ctrl+C`

---

## 3. Build and Run with Docker

```bash
docker build -t flask-health-dashboard:latest .
docker run -d --name flask-health-dashboard -p 8080:8080 flask-health-dashboard:latest
```

Verify:
```bash
curl http://localhost:8080/api/health
```

Stop and remove:
```bash
docker stop flask-health-dashboard
docker rm flask-health-dashboard
```

---

## 4. Run with Docker Compose

```bash
docker compose -f compose.dashboard.yml up -d --build
```

Check status:
```bash
docker compose -f compose.dashboard.yml ps
docker compose -f compose.dashboard.yml logs --tail=25
```

Verify:
```bash
curl http://localhost:8080/api/health
curl http://localhost:8080/api/report
```

Open `http://localhost:8080` in a browser.

Stop:
```bash
docker compose -f compose.dashboard.yml down
```

---

## 5. Run the Tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest tests/test_routes.py
```

Expected output: 3 tests passing with `OK`.

---

## 6. Jenkins Pipeline

Jenkins must have access to:
- Git (to run `checkout scm`)
- Python 3 with venv support (to run route tests)
- Docker (to build the image)
- Docker Compose v2 (to deploy and teardown)

### Pipeline Stages

| Stage                  | What It Does                                         |
|------------------------|------------------------------------------------------|
| Checkout               | Clones the repo from GitHub                          |
| Run Route Tests        | Creates a venv, installs deps, runs unittest         |
| Build Docker Image     | Runs `docker build`                                  |
| Deploy with Docker Compose | Runs `docker compose up -d --build`            |
| Verify Deployment      | Waits 5 seconds, then curls `/api/health` and `/api/report` |
| Cleanup                | Runs `docker compose down`                           |

### Trigger the Pipeline

1. Open Jenkins in a browser (default: `http://localhost:8080`).
2. Navigate to the pipeline job.
3. Click **Build Now**.
4. Monitor progress in **Stage View** or **Console Output**.

---

## 7. Jenkins Job Setup

If Jenkins is not yet configured, create the pipeline job using these settings:

- Definition: `Pipeline script from SCM`
- SCM: `Git`
- Repository URL: `https://github.com/AnthonyJSaade/flask-health-dashboard-cicd.git`
- Branches to build: `*/main`
- Script Path: `Jenkinsfile`

Then save and build the job.

---

## 8. Jenkins PATH Fix

On macOS, Jenkins may run with a limited PATH and fail to locate Docker. If the job reports `docker: command not found`, update the pipeline environment or the Jenkins agent configuration so `/usr/local/bin` is included.

Example pipeline environment setting:
```groovy
environment {
  PATH = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
}
```

---

## 9. Troubleshooting

### Port 8080 already in use
Jenkins itself often runs on 8080. If so, remap the Flask host port:

In `compose.dashboard.yml`, change:
```yaml
ports:
  - "8080:8080"
```
to:
```yaml
ports:
  - "8088:8080"
```

Update `APP_PORT` in `Jenkinsfile` to `8088` and verify with `curl http://localhost:8088/api/health`.

### Docker permission denied in Jenkins
The Jenkins process user may not be in the `docker` group. On Linux:
```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

### Compose command not found
Ensure Docker Compose v2 (plugin) is installed — use `docker compose` (with a space), not `docker-compose`.

### Tests fail — ModuleNotFoundError: flask
The venv must be created and activated before running tests. Make sure `pip install -r requirements.txt` runs inside the venv.
