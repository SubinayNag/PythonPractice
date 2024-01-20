pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        withSonarQubeEnv('sonarqube'){ 
          sh "sonar-scanner \
  -Dsonar.projectKey=python-validation \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://192.168.153.129:9000 \
  -Dsonar.login=08c9973661158200a5d5d88db50779a21ed8e352"
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
