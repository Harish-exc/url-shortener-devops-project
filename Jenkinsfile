pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REPO = "744746597411.dkr.ecr.us-east-1.amazonaws.com/url-shortener"
        IMAGE_TAG = "v1-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

             stage('Install Dependencies') {
           steps {
                 sh 'python3 -m pip install -r requirements.txt'
                }
           }


        stage('Run Tests') {
            steps {
                echo 'No tests yet — skipping.'
            }
        }

        stage('Docker Build') {
            steps {
                sh """
                docker build -t \$ECR_REPO:\$IMAGE_TAG .
                """
            }
        }

        stage('Login to ECR') {
            steps {
                withAWS(credentials: 'aws-ecr-creds', region: "${AWS_REGION}") {
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} \
                    | docker login --username AWS --password-stdin ${ECR_REPO}
                    """
                }
            }
        }

        stage('Push Image ok') {
            steps {
                sh """
                docker push \$ECR_REPO:\$IMAGE_TAG
                """
            }
        }
    }
}
