pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-access')
        IMAGE_NAME = 'ryleecito/flask-app'
        KUBECONFIG = '/home/azureuser/.kube/config'
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/ryleecito/Proyecto-Redes.git'
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login a Docker Hub') {
            steps {
                sh 'echo "$DOCKER_CREDENTIALS_PSW" | docker login -u "$DOCKER_CREDENTIALS_USR" --password-stdin'
            }
        }

        stage('Push a Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Desplegar en Kubernetes') {
            steps {
              sh 'kubectl apply -f k8s/flask-app.yaml'
            }
        }
    }
}