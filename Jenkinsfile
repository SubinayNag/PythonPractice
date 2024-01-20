pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        withSonarQubeEnv('sonar'){
          sh 'mvn clean package sonar:sonar'
        }
      }
    }
  }
}
