pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        withSonarQubeEnv('sonarqube'){
          def scannerHome = tool 'SonarScanner';
          sh "${scannerHome}/bin/sonar-scanner"
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
