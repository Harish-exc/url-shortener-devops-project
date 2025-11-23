pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REPO = "744746597411.dkr.ecr.us-east-1.amazonaws.com/url-shortener"
        IMAGE_TAG = "v1-${env.BUILD_NUMBER}"
        CLUSTER_NAME = "url-shortener-eks"
        KUBE_DEPLOYMENT = "url-shortener-deployment"
        KUBE_NAMESPACE = "default"
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

        stage('Update EKS Kubeconfig') {
            steps {
                withAWS(credentials: 'aws-ecr-creds', region: "${AWS_REGION}") {
                    sh """
                        aws eks update-kubeconfig --name ${CLUSTER_NAME} --region ${AWS_REGION}
                    """
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh """
                    kubectl set image deployment/${KUBE_DEPLOYMENT} \
                    ${KUBE_DEPLOYMENT}=${ECR_REPO}:${IMAGE_TAG} \
                    --namespace ${KUBE_NAMESPACE}
                """
            }
        }

    }

    post {
        success {
            echo "Deployment to EKS successful: ${CLUSTER_NAME}"
        }
        failure {
            echo "Deployment failed. Check the logs."
        }
    }
}
