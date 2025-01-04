pipeline {
  agent any
  environment {
    // registryCredential = 'ecr:us-east-1:awscreds'
    imageNameBackend = 'ambev4/lab1:myazure-backend'
    imageNameFrontend = 'ambev4/lab1:myazure-nginx'
    urlTestBackend = 'http://localhost:8000'
    // vprofileRegistry = "https://716657688884.dkr.ecr.us-east-1.amazonaws.com"
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
    // stage('Upload App Image') {
    //   steps{
    //     script {
    //       docker.withRegistry( vprofileRegistry, registryCredential ) {
    //         dockerImage.push("$BUILD_NUMBER")
    //         dockerImage.push('latest')
    //       }
    //     }
    //   }
    // }

    // stage('Remove Container Images'){
    //     steps{
    //         sh 'docker rmi -f $(docker images -a -q)'
    //     }
    // }
  }
}