pipeline {
    agent any

    environment {
        AWS_REGION     = "us-east-1"
        AWS_ACCOUNT_ID = "744746597411"
        REPO_NAME      = "url-shortener"
        ECR_URI        = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        IMAGE_TAG      = "v1-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
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
                    docker build -t ${ECR_URI}/${REPO_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Login to ECR') {
            steps {
                withAWS(credentials: 'aws-ecr-creds', region: "${AWS_REGION}") {
                    sh """
                        aws ecr get-login-password --region ${AWS_REGION} \
                        | docker login --username AWS --password-stdin ${ECR_URI}
                    """
                }
            }
        }

        stage('Push Image') {
            steps {
                sh """
                    docker push ${ECR_URI}/${REPO_NAME}:${IMAGE_TAG}
                """
            }
        }
    }
}
