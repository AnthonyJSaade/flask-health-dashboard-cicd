# PLAN.md — CI/CD Pipeline for Automated Deployment of a Flask System Health Dashboard

## 1. Project Title

**CI/CD Pipeline for Automated Deployment of a Flask System Health Dashboard Using Jenkins and Docker Compose**

---

## 2. Project Purpose

This project demonstrates a realistic DevOps workflow where a Flask web application is version-controlled in GitHub, built into a Docker image, deployed with Docker Compose, and automated through a Jenkins pipeline.

The application itself is a lightweight **System Health Dashboard**. It gives a simple visual and API-based way to confirm that the deployed system is running correctly after each build. The dashboard can show application status, hostname, Python version, uptime, environment information, and optional request statistics.

The purpose is not to create a complex commercial product. The purpose is to show how multiple workforce tools work together in a real, repeatable software delivery workflow.

---

## 3. Course Requirement Alignment

This project is designed to satisfy the cumulative project requirements:

- Uses **Jenkins**, which is required.
- Uses at least **two additional course tools** beyond Jenkins.
- Includes a working GitHub repository.
- Includes meaningful Jenkins automation rather than simple print statements.
- Produces a working final system that the grader can execute.
- Includes collaboration evidence from all three group members.
- Includes a short report with architecture, tools, setup steps, workflow explanation, and screenshots.

### Tools Used

| Tool | Purpose |
|---|---|
| GitHub | Hosts the project repository and tracks team collaboration |
| Jenkins | Automates checkout, build, verification, and deployment |
| Docker | Packages the Flask application into a repeatable container image |
| Docker Compose | Runs the application stack with a simple deployment command |
| Flask | Provides the working dashboard application |

Minimum required tools: **3**  
Tools used by this project: **5**

---

## 4. Final System Overview

The final system will work like this:

1. A teammate pushes code to GitHub.
2. Jenkins checks out the repository.
3. Jenkins builds the Flask Docker image.
4. Jenkins starts the app using Docker Compose.
5. Jenkins verifies the app using curl commands.
6. The team documents the working dashboard with screenshots.

### High-Level Workflow

```text
Developer Pushes Code
        ↓
GitHub Repository
        ↓
Jenkins Pipeline
        ↓
Docker Image Build
        ↓
Docker Compose Deployment
        ↓
Flask System Health Dashboard
```

---

## 5. Application Purpose and Features

The Flask application will act as a **System Health Dashboard**.

### Required Features

The app should include at least these routes:

| Route | Purpose |
|---|---|
| `/` | Browser dashboard page |
| `/api/health` | Returns basic health status |
| `/api/report` | Returns JSON system/application report |

### Recommended Dashboard Information

The dashboard should display:

- Application name
- App status, such as `running` or `ok`
- Hostname
- Python version
- Application uptime
- Current timestamp
- Environment label, such as `development`, `compose`, or `jenkins`
- Links to API routes

### Optional Feature

If the group has time, add a simple MongoDB-backed request counter. This is optional and should only be added after the main Jenkins + Docker Compose workflow works.

Recommended priority:

1. Flask dashboard working locally
2. Docker image working
3. Docker Compose working
4. Jenkins pipeline working
5. Documentation and screenshots
6. Optional MongoDB enhancement

---

## 6. Recommended Repository Structure

Use this structure:

```text
flask-health-dashboard-cicd/
├── app.py
├── diagnostics.py
├── config.json
├── requirements.txt
├── Dockerfile
├── compose.dashboard.yml
├── Jenkinsfile
├── README.md
├── .gitignore
├── .dockerignore
├── docs/
│   ├── ARCHITECTURE.md
│   ├── REPORT.md
│   └── RUNBOOK.md
├── screenshots/
│   ├── app-browser.png
│   ├── app-health-curl.png
│   ├── compose-ps.png
│   ├── jenkins-pipeline-success.png
│   └── jenkins-console-output.png
└── tests/
    └── test_routes.py
```

### File Purposes

| File | Purpose |
|---|---|
| `app.py` | Main Flask application |
| `diagnostics.py` | Helper functions for system report data |
| `config.json` | App configuration such as name and environment |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Builds the Flask app image |
| `compose.dashboard.yml` | Runs the app with Docker Compose |
| `Jenkinsfile` | Defines Jenkins CI/CD pipeline stages |
| `README.md` | Main project setup and usage guide |
| `PLAN.md` | This planning document |
| `.gitignore` | Prevents local/generated files from being committed |
| `.dockerignore` | Prevents unnecessary files from being sent to Docker build context |
| `docs/ARCHITECTURE.md` | Explains system architecture |
| `docs/REPORT.md` | Final project report draft |
| `docs/RUNBOOK.md` | Step-by-step instructions for running the project |
| `screenshots/` | Stores evidence for report and individual submissions |
| `tests/` | Basic tests or verification scripts |

---

## 7. Team Roles for 3 Members

Each student must contribute to Jenkins and at least one other technical area. To make that visible, every member should touch the Jenkins workflow in some way, even if one person leads it.

### Member 1 — Jenkins and Integration Lead

Responsibilities:

- Install and configure Jenkins locally.
- Create the Jenkins pipeline job.
- Write or lead the `Jenkinsfile`.
- Make sure Jenkins can run Docker and Docker Compose commands.
- Capture Jenkins screenshots.
- Help merge final branches and verify the full workflow.

Deliverables:

- `Jenkinsfile`
- Jenkins successful build screenshot
- Jenkins console output screenshot
- Contribution statement explaining Jenkins and integration work

Suggested commits:

```bash
git commit -m "feat: add Jenkins deployment pipeline"
git commit -m "docs: add Jenkins setup evidence"
```

---

### Member 2 — Flask Application and Testing Lead

Responsibilities:

- Build or adapt the Flask dashboard.
- Implement `/`, `/api/health`, and `/api/report`.
- Add `diagnostics.py` if used.
- Add simple tests or verification scripts.
- Capture browser and curl screenshots.

Deliverables:

- `app.py`
- `diagnostics.py`
- `requirements.txt`
- `tests/test_routes.py` or documented curl checks
- Flask browser screenshot
- API route screenshots
- Contribution statement explaining Flask and verification work

Suggested commits:

```bash
git commit -m "feat: add Flask health dashboard"
git commit -m "test: add route verification tests"
```

---

### Member 3 — Docker, Compose, and Documentation Lead

Responsibilities:

- Write the `Dockerfile`.
- Write `compose.dashboard.yml`.
- Add `.dockerignore`.
- Confirm the app runs through Docker Compose.
- Write setup steps in `README.md` and `docs/RUNBOOK.md`.
- Capture Docker and Compose screenshots.

Deliverables:

- `Dockerfile`
- `compose.dashboard.yml`
- `.dockerignore`
- Docker build screenshot
- Docker Compose `ps` screenshot
- Runbook documentation
- Contribution statement explaining Docker/Compose/docs work

Suggested commits:

```bash
git commit -m "feat: containerize Flask dashboard"
git commit -m "feat: run dashboard with Docker Compose"
git commit -m "docs: add project runbook"
```

---

## 8. Branching Plan

Use branches so each member has visible contribution evidence.

### Recommended Branches

```text
main
├── feature/flask-dashboard
├── feature/docker-compose
├── feature/jenkins-pipeline
└── docs/final-report
```

### Workflow

Each member should:

1. Create a branch.
2. Make changes.
3. Commit with professional commit messages.
4. Push branch to GitHub.
5. Open a pull request.
6. Get at least one teammate to review or comment.
7. Merge into `main`.

### Commit Message Prefixes

Use these prefixes:

- `feat:` for new functionality
- `fix:` for bug fixes
- `docs:` for documentation
- `chore:` for setup or maintenance
- `test:` for test-related work

Examples:

```bash
git commit -m "feat: add Flask health dashboard"
git commit -m "feat: add Docker Compose deployment"
git commit -m "feat: add Jenkins pipeline stages"
git commit -m "docs: add architecture overview"
git commit -m "test: add health route verification"
```

---

## 9. Implementation Phases

## Phase 1 — Repository Setup

Goal: Create a clean GitHub repository with a professional layout.

Tasks:

- Create GitHub repository.
- Clone locally.
- Add `.gitignore`.
- Add base folders: `docs/`, `screenshots/`, `tests/`.
- Add this `PLAN.md`.
- Push initial commit.

Suggested `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.env.*
.DS_Store
.vscode/
.idea/
*.log
```

Suggested commands:

```bash
git clone <repo-url>
cd flask-health-dashboard-cicd
mkdir docs screenshots tests
touch README.md PLAN.md .gitignore
git add .
git commit -m "chore: initialize project repository"
git push origin main
```

Acceptance criteria:

- Repository exists on GitHub.
- Main project folders exist.
- `.gitignore` is committed.
- All group members have access.

---

## Phase 2 — Flask Dashboard

Goal: Build a working Flask app that can be tested locally.

Tasks:

- Add `requirements.txt`.
- Add `config.json`.
- Add `diagnostics.py`.
- Add `app.py`.
- Run locally.
- Verify browser page and API routes.

Suggested local commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Suggested routes to verify:

```bash
curl http://localhost:8080/
curl http://localhost:8080/api/health
curl http://localhost:8080/api/report
```

Acceptance criteria:

- App runs locally on port `8080`.
- `/` loads in browser.
- `/api/health` returns JSON status.
- `/api/report` returns useful system information.

Screenshots to capture:

- Browser dashboard
- curl output for `/api/health`
- curl output for `/api/report`

---

## Phase 3 — Dockerfile

Goal: Package the Flask app into a Docker image.

Tasks:

- Add `Dockerfile`.
- Add `.dockerignore`.
- Build image.
- Run container manually.
- Verify routes with curl.

Recommended `Dockerfile` requirements:

- Use `python:3.12-slim`.
- Set `WORKDIR /app`.
- Copy `requirements.txt` first.
- Install dependencies with `pip`.
- Copy the rest of the app.
- Expose port `8080`.
- Run `python app.py`.

Suggested commands:

```bash
docker build -t flask-health-dashboard:latest .
docker run -d --name flask-health-dashboard -p 8080:8080 flask-health-dashboard:latest
curl http://localhost:8080/api/health
docker stop flask-health-dashboard
docker rm flask-health-dashboard
```

Acceptance criteria:

- Docker image builds successfully.
- Container starts successfully.
- App is reachable at `http://localhost:8080`.

Screenshots to capture:

- Docker build output
- Running container with `docker ps`
- curl verification output

---

## Phase 4 — Docker Compose

Goal: Run the app using Docker Compose so deployment is repeatable.

Tasks:

- Add `compose.dashboard.yml`.
- Configure service name as `app`.
- Build current repository.
- Map host port `8080` to container port `8080`.
- Start stack.
- Verify stack and routes.
- Stop stack.

Suggested commands:

```bash
docker compose -f compose.dashboard.yml up -d --build
docker compose -f compose.dashboard.yml ps
docker compose -f compose.dashboard.yml logs --tail=25
curl http://localhost:8080/api/health
curl http://localhost:8080/api/report
docker compose -f compose.dashboard.yml down
```

Acceptance criteria:

- Compose starts the dashboard.
- `docker compose ps` shows service running.
- Compose logs show Flask app started.
- App routes work through `localhost:8080`.

Screenshots to capture:

- `docker compose ps`
- Last 25 log entries
- Browser dashboard through Compose
- curl route verification

---

## Phase 5 — Jenkins Setup

Goal: Install Jenkins and prepare it to run the project pipeline.

Tasks:

- Install Jenkins locally.
- Confirm Jenkins is accessible in the browser.
- Install recommended plugins.
- Make sure Jenkins can access Git.
- Make sure Jenkins can run Docker commands.
- Create a Pipeline job.
- Connect job to the GitHub repository.

Important Jenkins requirement:

Jenkins must do meaningful automation. It should not simply print messages. The pipeline should check out code, build the Docker image, deploy with Compose, and verify the app.

Potential Jenkins setup issue:

The Jenkins user may not have permission to run Docker. If Docker commands fail in Jenkins, the team may need to add the Jenkins user to the Docker group or use the correct local setup for the operating system.

Acceptance criteria:

- Jenkins opens in browser.
- Jenkins has a Pipeline job for this project.
- Jenkins can read the GitHub repository.
- Jenkins can run Docker commands.

Screenshots to capture:

- Jenkins dashboard
- Pipeline job configuration
- Jenkins build history

---

## Phase 6 — Jenkinsfile Pipeline

Goal: Automate the full workflow through Jenkins.

Recommended pipeline stages:

1. **Checkout**
2. **Build Docker Image**
3. **Start Compose Stack**
4. **Verify Application**
5. **Show Logs**
6. **Cleanup Old Containers** or controlled cleanup behavior

Important note:

For the final demo, the group may want the Compose stack to stay running after the pipeline finishes so the grader can open the dashboard. If cleanup is included, make it clear when and how cleanup happens.

Suggested Jenkins stages:

```text
Checkout
Build
Deploy
Verify
Logs
Post Actions
```

Acceptance criteria:

- Jenkins pipeline completes successfully.
- Docker image is built by Jenkins.
- Docker Compose deployment is started by Jenkins.
- Jenkins verifies routes using curl.
- Console output shows meaningful automation.

Screenshots to capture:

- Successful Jenkins pipeline stage view
- Jenkins console output showing Docker build
- Jenkins console output showing Compose deployment
- Jenkins console output showing curl verification

---

## Phase 7 — Documentation

Goal: Make the project understandable and reproducible.

Required documentation:

### `README.md`

Should include:

- Project title
- Project purpose
- Tools used
- How to run locally
- How to run with Docker
- How to run with Docker Compose
- How Jenkins pipeline works
- Team members and roles

### `docs/ARCHITECTURE.md`

Should include:

- Architecture diagram
- Explanation of each component
- Data/control flow

### `docs/RUNBOOK.md`

Should include:

- Prerequisites
- Setup commands
- Build commands
- Deployment commands
- Verification commands
- Troubleshooting notes

### `docs/REPORT.md`

Should include:

- Architecture summary
- Tools used
- Setup steps
- Jenkins workflow explanation
- Screenshots
- Collaboration evidence
- Lessons learned

Acceptance criteria:

- A grader can follow the README or runbook.
- The report explains what the system does and why each tool was used.
- Screenshots support the claims.

---

## Phase 8 — Collaboration Evidence

Goal: Prove that all three group members contributed.

Evidence options:

- Git commit history
- Pull requests
- GitHub issues
- GitHub project board
- Screenshots of task assignments
- Slack or Teams messages if used
- Jenkins screenshots
- Docker/Compose screenshots

Recommended GitHub Issues:

Create issues like:

1. Build Flask dashboard routes
2. Add Dockerfile
3. Add Docker Compose configuration
4. Install and configure Jenkins
5. Create Jenkinsfile pipeline
6. Write README and runbook
7. Capture screenshots for report
8. Prepare final report

Each issue should be assigned to a teammate.

Acceptance criteria:

- Every group member appears in the repository history or collaboration evidence.
- Every group member has at least one meaningful technical contribution.
- Every group member can write an individual contribution statement with evidence.

---

## 10. Suggested Timeline

### Day 1 — Planning and Repository Setup

- Agree on project purpose.
- Create GitHub repository.
- Add folder structure.
- Add `PLAN.md`.
- Assign roles.
- Create GitHub issues.

### Day 2 — Flask App

- Build dashboard routes.
- Run locally.
- Capture local app screenshots.

### Day 3 — Docker and Compose

- Add Dockerfile.
- Add Compose file.
- Verify app runs through Compose.
- Capture Docker/Compose screenshots.

### Day 4 — Jenkins

- Install Jenkins.
- Create Jenkins pipeline job.
- Add `Jenkinsfile`.
- Debug Docker/Jenkins permission issues.
- Capture Jenkins screenshots.

### Day 5 — Documentation and Final Testing

- Complete README.
- Complete report.
- Verify clean setup from scratch.
- Make sure screenshots match final system.
- Write individual contribution statements.

---

## 11. Screenshot Checklist

The final report should include screenshots of:

### Application

- Flask dashboard in browser
- `/api/health` curl output
- `/api/report` curl output

### Docker

- Docker image build success
- Running container or Compose service

### Docker Compose

- `docker compose -f compose.dashboard.yml ps`
- `docker compose -f compose.dashboard.yml logs --tail=25`
- Browser dashboard running through Compose

### Jenkins

- Jenkins pipeline job page
- Successful pipeline run
- Console output showing checkout
- Console output showing Docker build
- Console output showing Compose deployment
- Console output showing route verification

### Collaboration

- GitHub commit history
- Pull requests or branches
- GitHub issues or task board
- Optional team communication screenshot

---

## 12. Minimum Viable Product

The group should consider the project successful when this works:

- GitHub repository exists.
- Flask dashboard runs locally.
- Docker image builds.
- Docker Compose runs the app.
- Jenkins pipeline builds and deploys the app.
- Jenkins verifies the app with curl.
- Screenshots and documentation are complete.
- Each teammate has visible contribution evidence.

Do not add optional features until this minimum version works.

---


## 13. Risk Management

### Risk 1 — Jenkins cannot run Docker

Possible cause:

- Jenkins user lacks Docker permissions.

Mitigation:

- Test Docker commands outside Jenkins first.
- Research OS-specific Jenkins Docker setup.
- Document the fix in `docs/RUNBOOK.md`.

### Risk 2 — Port 8080 already in use

Possible cause:

- Jenkins or another app uses port 8080.

Mitigation:

- Jenkins often runs on port 8080. If so, run the Flask app on `8088` instead.
- Update Dockerfile, Compose, README, and Jenkinsfile consistently.

Recommended adjustment:

If Jenkins uses `localhost:8080`, use this for Flask:

```text
Flask app: http://localhost:8088
Container port: 8080
Host port: 8088
```

Compose mapping:

```yaml
ports:
  - "8088:8080"
```

### Risk 3 — Teammates overwrite each other’s work

Mitigation:

- Use branches.
- Use pull requests.
- Pull latest `main` before starting work.

### Risk 4 — Project gets too complicated

Mitigation:

- Focus on the minimum viable project.
- Do not add MongoDB until Jenkins + Compose works.

---

## 14. Definition of Done

The project is done when:

- The GitHub repository is complete and public or accessible to the grader.
- The Flask dashboard works.
- Docker builds the image.
- Docker Compose runs the app.
- Jenkins performs real automation.
- Jenkins pipeline completes successfully.
- The app can be opened in the browser.
- The report includes architecture, setup steps, workflow explanation, screenshots, and collaboration evidence.
- Each student has an individual contribution statement.

---
