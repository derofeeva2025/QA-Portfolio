pipeline {
    agent {
        dockerfile {
            dir 'Automation-Testing/py-plw-pet'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh '''
                    cd Automation-Testing/py-plw-pet
                    pytest --alluredir=allure-results
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'Automation-Testing/py-plw-pet/allure-results/**', allowEmptyArchive: true
        }
    }
}
