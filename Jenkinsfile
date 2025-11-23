pipeline {
    agent any

    environment {
        AWS_REGION      = "us-east-1"
        ECR_REPO        = "744746597411.dkr.ecr.us-east-1.amazonaws.com/url-shortener"
        IMAGE_TAG       = "v1-${env.BUILD_NUMBER}"
        EC2_HOST        = "52.205.232.75"  // Replace with your EC2 public IP
        APP_NAME        = "url-shortener"
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

        stage('Docker Build & Tag') {
            steps {
                sh """
                    docker build -t ${ECR_REPO}:${IMAGE_TAG} .
                    docker tag ${ECR_REPO}:${IMAGE_TAG} ${ECR_REPO}:latest
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

        stage('Push Image to ECR') {
            steps {
                sh """
                    docker push ${ECR_REPO}:${IMAGE_TAG}
                    docker push ${ECR_REPO}:latest
                """
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['EC2_SSH_KEY']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} '
                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO} &&
                        docker pull ${ECR_REPO}:latest &&
                        docker stop ${APP_NAME} || true &&
                        docker rm ${APP_NAME} || true &&
                        docker run -d -p 8000:8000 --name ${APP_NAME} ${ECR_REPO}:latest
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Deployment to EC2 successful: ${EC2_HOST}"
        }
        failure {
            echo "Deployment failed. Check the logs."
        }
    }
}
