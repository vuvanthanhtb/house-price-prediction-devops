pipeline {
  agent any

  environment {
    GIT_REPO    = 'https://github.com/vuvanthanhtb/house-price-prediction-devops.git'
    DOCKER_REPO = 'vuvanthanhtb/house-price-api'
    IMAGE_TAG   = 'latest'
  }

  stages {
    stage('Clone Repository') {
      steps {
        cleanWs()
        git branch: 'main', url: "${GIT_REPO}"
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def fullImage = "${DOCKER_REPO}:${IMAGE_TAG}"
          echo "Building Docker Image: ${fullImage}"
          dockerImage = docker.build(fullImage)
        }
      }
    }

    stage('Login to Docker Hub') {
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

    stage('Deploy with Helm') {
      steps {
        script {
          echo "Deploying image ${DOCKER_REPO}:${IMAGE_TAG} to Kubernetes"
          sh """
            helm upgrade --install house-price ./k8s-chart --set image.repository=${DOCKER_REPO} --set image.tag=${IMAGE_TAG}
          """
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline completed successfully. Deployed: ${DOCKER_REPO}:${IMAGE_TAG}"
    }
    failure {
      echo "Pipeline failed."
    }
  }
}
