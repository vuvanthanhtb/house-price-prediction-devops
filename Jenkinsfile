pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'vuvanthanhtb/house-price-api:v1.0'
    GIT_REPO = 'https://github.com/vuvanthanhtb/house-price-prediction-devops.git'
  }

  stages {
    stage('Clone Repository') {
      steps {
        git branch: 'main', url: "${env.GIT_REPO}"
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("${env.DOCKER_IMAGE}")
        }
      }
    }

    stage('Login to Docker Hub with Token') {
      steps {
        withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
          sh '''
            echo $DOCKERHUB_TOKEN | docker login -u vuvanthanhtb --password-stdin
          '''
        }
      }
    }

    stage('Push Docker Image') {
      steps {
        script {
          dockerImage.push()
        }
      }
    }
  }

  post {
    success {
      echo 'Pipeline completed successfully.'
    }
    failure {
      echo 'Pipeline failed.'
    }
  }
}
