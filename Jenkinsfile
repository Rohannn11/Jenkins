pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create and activate virtual environment
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate.bat
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest tests/
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        start /B streamlit run src/app.py
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Cleaning up...'
            bat 'if exist venv rmdir /s /q venv'
        }
    }
}