pipeline {
     agent any

     stages{
          stage('Checkout complete'){
              steps {
                  echo 'Source code checked out from Github'
              }
          }
          stage('Run Python App'){
              steps {
                 bat '"C:\\Users\\DanduNitheshVardhan\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" --version'
                 bat 'python main.py'
              }
          }
          stage('Run Unit Tests'){
              steps {
                  bat 'python -m unittest -v test_main'
              }
          }
     }

     post {
         success {
              echo 'SUCCESS: Application and tests passed!'
         }
         failure {
              echo 'FAILURE: Checkout the Jenkins console output.'}
         }

     }
