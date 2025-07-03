DOCKER_IMAGE=vuvanthanhtb/jenkins:lts
JENKINS_DIR=jenkins

.PHONY: jenkins-build jenkins-push jenkins-up jenkins-all

jenkins-build:
	docker build -t $(DOCKER_IMAGE) $(JENKINS_DIR)

jenkins-push:
	docker push $(DOCKER_IMAGE)

jenkins-up:
	docker-compose -f $(JENKINS_DIR)/docker-compose.yaml up -d


jenkins-all: jenkins-build jenkins-push jenkins-up