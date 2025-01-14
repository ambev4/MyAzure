pipeline {
  agent any
  environment {
    registryCredential = 'c71f39e0-4200-4876-850f-9c551f5a45c3'
    imageNameBackend = 'ambev4/lab1:myazure-backend'
    urlTestBackend = 'http://localhost:8000'
  }
  stages {
    stage('Fetch code') {
      steps {
        git branch: 'main', url: 'https://github.com/ambev4/MyAzure.git'
      }
    }
    stage('Build App Image') {
      steps {
        script {
          dockerImage = docker.build(imageNameBackend, '--no-cache ./Docker/Python/')
        }
      }
    }
    stage('Test Image') {
      steps {
        script {
          dockerContainer = docker.image("${imageNameBackend}").run('-d -p 8000:8000')
          def response = httpRequest urlTestBackend
          if (response.status != 200) {
            dockerContainer.stop()
            throw new Exception("ERRO HTTP STATUS DIFERENTE DE 200.")
          }
          dockerContainer.stop()
        }
      }
    }
    stage('Upload App Image') {
      steps{
        script {
          docker.withRegistry('', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Container Image'){
      steps{
        sh'docker image prune -f'
      }
    }
  }
}