pipeline {
    agent any

    environment {
        APP_DIR = "/home/ubuntu/flask-portfolio"
        VENV_DIR = "${APP_DIR}/venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                 git branch: 'main', url: 'https://github.com/amanpandey13/portfolio.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Old Gunicorn') {
            steps {
                sh '''
                pkill gunicorn || true
                '''
            }
        }

        stage('Start Gunicorn') {
            steps {
                sh '''
                source venv/bin/activate
                nohup gunicorn -w 4 -b 0.0.0.0:5001 app:app &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed.'
        }
    }
}
