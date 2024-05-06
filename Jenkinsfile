pipeline {
    agent { dockerfile true }

    stages {
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "pytest"
            }
        }
    }
}