pipeline {
  agent any

  environment {
    GIT_REPO = 'https://github.com/vuvanthanhtb/house-price-prediction-devops.git'
    DOCKER_REPO = 'vuvanthanhtb/house-price-api'
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
          def TIMESTAMP = new Date().format("yyyyMMddHHmmss")
          def IMAGE_TAG = "${DOCKER_REPO}:${TIMESTAMP}"
          env.IMAGE_TAG = IMAGE_TAG
          echo "Building image: ${IMAGE_TAG}"
          dockerImage = docker.build(IMAGE_TAG)
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

    stage('Deploy to Kubernetes') {
      steps {
        script {
          sh '''
            echo "Deploying to Kubernetes..."

            # Replace image in deployment YAML dynamically (if using static file)
            sed -i "s|image: .*|image: ${IMAGE_TAG}|" deployment/deployment.yaml

            # Apply Kubernetes manifests
            kubectl apply -f deployment/deployment.yaml
            kubectl apply -f deployment/service.yaml
          '''
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline completed successfully. Image: ${env.IMAGE_TAG}"
    }
    failure {
      echo "Pipeline failed."
    }
  }
}
