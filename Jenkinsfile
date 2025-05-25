pipeline{
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
        stage('set up the env'){
            steps {
                bat  "python -m venv %{venv}"
                bat "%venv%\\Scripts\\pythion -m pip install --upgrade pip"
                bat "%venv%\\Scripts\\pip install -r requirements.txt"
            }
        }
        stage('Run tests') {
            steps {
                bat "%venv%\\Scripts\\python -m unittest discover -s tests"
            }
        }
    }
}