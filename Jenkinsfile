pipeline {
  agent any

  parameters {
    string(name: 'BRANCH', defaultValue: 'main', description: 'Git branch to build')
  }

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
        git branch: "${params.BRANCH}", url: "${env.GIT_REPO}"
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

    // stage('Run Ansible Playbook') {
    //   steps {
    //     sh '''
    //       ansible-playbook -i ansible/inventory ansible/playbook.yml
    //     '''
    //   }
    // }

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
          sh '''
            helm upgrade --install house-price ./k8s-chart/
          '''
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline completed successfully. Deployed: ${DOCKER_REPO}:${IMAGE_TAG}"
    }
    failure {
      echo 'Pipeline failed.'
    }
  }
}
