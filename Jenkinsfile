pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REPO = "744746597411.dkr.ecr.us-east-1.amazonaws.com/url-shortener"
        IMAGE_TAG = "v1-${env.BUILD_NUMBER}"
        APP_NAME = "url-shortener"
        EC2_HOST = "ubuntu@52.205.232.75"
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

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${ECR_REPO}:${IMAGE_TAG} .
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
                sh "docker push ${ECR_REPO}:${IMAGE_TAG}"
            }
        }

        stage('Deploy on Docker Host') {
            steps {
                sshagent(['ec2-ssh']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_HOST} << 'EOF'

                        # Login to ECR
                        docker login -u AWS -p \$(aws ecr get-login-password --region ${AWS_REGION}) ${ECR_REPO}

                        # Pull latest image
                        docker pull ${ECR_REPO}:${IMAGE_TAG}

                        # Stop old container if exists
                        docker stop ${APP_NAME} || true
                        docker rm ${APP_NAME} || true

                        # Start new container
                        docker run -d -p 80:8000 --name ${APP_NAME} ${ECR_REPO}:${IMAGE_TAG}

EOF
                    """
                }
            }
        }
    }
}
