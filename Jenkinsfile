pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                script {
                // Clone the code from GitHub
                    echo "Cloning branch: ${branch}"
                    git branch: "main", url: 'https://github.com/Natali-Dubotolkova/Seminar_Lab4.git'
                }
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install Python and create a virtual environment
                sh '''
                // sudo apt-get update
                // sudo apt-get install -y python3 python3-pip
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                // Run the application
                sh '''
                . venv/bin/activate
                python app.py &
                '''
                // Ensure the application started (you can add a check)
                sleep 5 // Wait for the application to start if needed
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests from the app_test.py file
                sh '''
                . venv/bin/activate
                python -m unittest app_test.py
                '''
            }
        }
    }

    post {
        always {
            // Remove the virtual environment after execution
            sh '''
            rm -rf venv
            '''
        }

        success {
            echo 'Tests ran successfully!'
        }

        failure {
            echo 'There were test failures.'
        }
    }
}
