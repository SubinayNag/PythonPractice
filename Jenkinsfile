pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        step{
        environment {
                scannerHome = tool 'sonarqube'
            }
        }
        step{
        withSonarQubeEnv('sonarqube'){ 
          sh '${scannerHome}/bin/sonar-scanner'
        }}
      }
    }
    stage('Quality Gate'){
      steps {
              timeout(time: 1, unit: 'HOURS') {
                waitForQualityGate abortPipeline: true
              }
            }
    }
  }
}
