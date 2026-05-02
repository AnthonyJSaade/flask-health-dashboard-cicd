pipeline {
  agent any

  environment {
    IMAGE_NAME = 'flask-health-dashboard'
    COMPOSE_FILE = 'compose.dashboard.yml'
    APP_PORT = '8080'
  }

  options {
    ansiColor('xterm')
    timeout(time: 30, unit: 'MINUTES')
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Run Route Tests') {
      steps {
        script {
          // Create a virtual environment and install dependencies
          sh 'python3 -m venv .venv'
          sh '.venv/bin/pip install -r requirements.txt'
          // Run Flask route tests before building the Docker image
          sh '.venv/bin/python -m unittest tests/test_routes.py'
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          sh 'docker build -t ${IMAGE_NAME}:latest .'
        }
      }
    }

    stage('Deploy with Docker Compose') {
      steps {
        script {
          sh 'docker compose -f ${COMPOSE_FILE} up -d --build'
        }
      }
    }

    stage('Verify Deployment') {
      steps {
        script {
          sh 'sleep 5'
          sh 'curl -f http://localhost:${APP_PORT}/api/health'
          sh 'curl -f http://localhost:${APP_PORT}/api/report'
        }
      }
    }

    stage('Show Compose Status') {
      steps {
        script {
          sh 'docker compose -f ${COMPOSE_FILE} ps'
          sh 'docker compose -f ${COMPOSE_FILE} logs --tail=25'
        }
      }
    }

    stage('Cleanup') {
      steps {
        script {
          sh 'docker compose -f ${COMPOSE_FILE} down || true'
        }
      }
    }
  }

  post {
    always {
      script {
        sh 'docker compose -f ${COMPOSE_FILE} down || true'
      }
    }
  }
}
