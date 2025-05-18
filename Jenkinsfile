pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-access')
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/ryleecito/Proyecto-Redes.git'
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                sh 'docker build -t ryleecito/flask-app .'
            }
        }

        stage('Login a Docker Hub') {
            steps {
                sh 'echo "$DOCKER_CREDENTIALS_PSW" | docker login -u "$DOCKER_CREDENTIALS_USR" --password-stdin'
            }
        }

        stage('Push a Docker Hub') {
            steps {
                sh 'docker push ryleecito/flask-app'
            }
        }
    }
}
