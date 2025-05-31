// pipeline {
//     agent any

//     environment {
//         APP_DIR = "/var/lib/jenkins/workspace/flask-portfolio"
//         VENV_DIR = "${APP_DIR}/venv"
//     }

//     stages {
//         stage('Install System Dependencies') {
//             steps {
//                 sh '''
//                 sudo apt-get update
//                 sudo apt-get install -y python3-venv
//                 '''
//             }
//         }

//         stage('Clone Repo') {
//             steps {
//                 sh '''
//                 rm -rf $APP_DIR
//                 git clone -b main https://github.com/amanpandey13/portfolio.git $APP_DIR
//                 '''
//             }
//         }

//         stage('Install Python Dependencies') {
//             steps {
//                 sh '''
//                 cd $APP_DIR
//                 python3 -m venv venv
//                 source venv/bin/activate
//                 pip install --upgrade pip
//                 pip install -r requirements.txt
//                 pip install gunicorn
//                 '''
//             }
//         }

//         stage('Stop Old Gunicorn') {
//             steps {
//                 sh 'pkill gunicorn || true'
//             }
//         }

//         stage('Start Gunicorn') {
//             steps {
//                 sh '''
//                 cd $APP_DIR
//                 source venv/bin/activate
//                 nohup gunicorn -w 4 -b 0.0.0.0:5001 app:app &
//                 '''
//             }
//         }
//     }

//     post {
//         success {
//             echo '✅ Deployment Successful!'
//         }
//         failure {
//             echo '❌ Deployment Failed.'
//         }
//     }
// }

// ####################################################

pipeline {
    agent any

    environment {
    APP_DIR = "/var/lib/jenkins/workspace/flask-portfolio"
    VENV_DIR = "$APP_DIR/venv"
}

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'demo', url: 'https://github.com/amanpandey13/portfolio.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Gunicorn Server') {
            steps {
                sh '''
                    pkill gunicorn || true
                    source $VENV_DIR/bin/activate
                    nohup gunicorn -w 4 -b 0.0.0.0:5001 app:app > gunicorn.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment complete. Flask app is live on port 5001."
        }
        failure {
            echo "❌ Deployment failed."
        }
    }
}
