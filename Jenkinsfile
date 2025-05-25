pipeline {
    agent any
    environment { 
        venv = "venv"
    }
    stages {
        stage('Checkout git') {
            steps {
                git branch: 'main', url: 'https://github.com/amanpandey13/portfolio'
            }
        }
        stage('Set up the virtual environment') {
            steps {
                sh 'python3 -m venv $venv'
                sh './$venv/bin/pip install --upgrade pip'
                sh './$venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh './$venv/bin/python -m unittest discover -s tests'
            }
        }
    }
}
