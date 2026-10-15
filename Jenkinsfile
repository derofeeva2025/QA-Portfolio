pipeline {
    agent {
        dockerfile {
            dir 'Automation-Testing/py-plw-pet'
        }
    }
    triggers {
        pollSCM('H/5 * * * *')
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
