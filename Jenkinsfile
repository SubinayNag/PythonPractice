pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        withSonarQubeEnv('sonarqube'){
          
          sh "tool 'SonarScanner'/bin/sonar-scanner"
        }
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
