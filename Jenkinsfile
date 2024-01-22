pipeline {
  agent any
  stages {
    stage('Scan'){
      steps {
        withSonarQubeEnv('sonarqube'){ 
          sh '/var/lib/jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonarqube/bin/sonar-scanner -Dsonar.host.url=http://192.168.153.132:9000/ -Dsonar.projectKey=python-project -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/scripted-pipeline'
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
