pipeline {
  agent any

  parameters {
    choice(name: 'BRANCH', choices: getGitBranches(), description: 'Chọn nhánh Git để build')
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
        git branch: "${params.BRANCH}", url: "${env.GIT_REPO}"
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def fullImage = "${DOCKER_REPO}:${IMAGE_TAG}"
          dockerImage = docker.build(fullImage)
        }
      }
    }

    stage('Login to Docker Hub') {
      steps {
        withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
          sh 'echo $DOCKERHUB_TOKEN | docker login -u vuvanthanhtb --password-stdin'
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
        sh """
          helm upgrade --install house-price ./k8s-chart \\
            --set image.repository=${DOCKER_REPO} \\
            --set image.tag=${IMAGE_TAG}
        """
      }
    }
  }
}

def getGitBranches() {
  def proc = ['git', 'ls-remote', '--heads', 'https://github.com/vuvanthanhtb/house-price-prediction-devops.git'].execute()
  proc.waitFor()
  return proc.in.text.readLines()
      .collect { it.replaceAll(/^.*refs\/heads\//, '') }
      .unique()
      .sort()
}
