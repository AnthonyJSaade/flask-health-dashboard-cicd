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
