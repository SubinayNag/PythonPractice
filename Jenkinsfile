pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        withSonarQubeEnv('sonarqube'){
          sh 'mvn clean package sonar:sonar'
        }
      }
    }
  }
}
