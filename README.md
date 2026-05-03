# CI/CD Pipeline for Automated Deployment of a Flask System Health Dashboard

## Project Purpose

This project demonstrates a realistic DevOps workflow where a Flask web application is version-controlled in GitHub, built into a Docker image, deployed with Docker Compose, and automated through a Jenkins pipeline.

## Tools Used

| Tool | Purpose |
|------|---------|
| GitHub | Hosts the project repository and tracks team collaboration |
| Jenkins | Automates checkout, build, verification, and deployment |
| Docker | Packages the Flask application into a repeatable container image |
| Docker Compose | Runs the application stack with a simple deployment command |
| Flask | Provides the working dashboard application |

## Quick Start

### Run Locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Run with Docker
```bash
docker build -t flask-health-dashboard:latest .
docker run -d --name flask-health-dashboard -p 8080:8080 flask-health-dashboard:latest
```

### Run with Docker Compose
```bash
docker compose -f compose.dashboard.yml up -d --build
```

### Run with Jenkins
1. Open Jenkins at `http://localhost:8080`.
2. Create a new Pipeline job.
3. Configure the job as:
   - Definition: `Pipeline script from SCM`
   - SCM: `Git`
   - Repository URL: `https://github.com/AnthonyJSaade/flask-health-dashboard-cicd.git`
   - Branches to build: `*/main`
   - Script Path: `Jenkinsfile`
4. Run the job and verify the stages complete successfully.

### Verify
```bash
curl http://localhost:8080/api/health
```

## Team Members

| Member | Role |
|--------|------|
| Cem Tutar | Jenkins and Integration Lead |
| AnthonyJSaade | Flask Application and Testing Lead |
| Deepesh Managuru | Docker, Compose, and Documentation Lead |

## Project Structure

```
├── app.py                    # Main Flask application
├── diagnostics.py            # Helper functions for system report data
├── config.json               # App configuration
├── requirements.txt          # Python dependencies
├── Dockerfile                # Builds the Flask app image
├── compose.dashboard.yml     # Runs the app with Docker Compose
├── Jenkinsfile               # Defines Jenkins CI/CD pipeline stages
├── README.md                 # This file
├── docs/                     # Architecture, report, and runbook
├── screenshots/              # Evidence for report
└── tests/                    # Route verification tests
```
