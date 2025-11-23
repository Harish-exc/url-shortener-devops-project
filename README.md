# URL Shortener – DevOps End-to-End Project
![Docker Build](https://img.shields.io/badge/docker-ready-blue)
![CI/CD](https://img.shields.io/badge/ci%2Fcd-jenkins-success)
![Kubernetes](https://img.shields.io/badge/kubernetes-ready-blue)
![Terraform](https://img.shields.io/badge/terraform-iac-purple)
![AWS](https://img.shields.io/badge/aws-cloud-orange)

A production-ready, scalable **URL Shortener** application designed as a full DevOps case study.  
This project covers the complete software delivery lifecycle including:

- Application development (FastAPI)
- Containerization (Docker)
- CI/CD (Jenkins / GitHub Actions)
- Security scanning (Trivy / SonarQube)
- Infrastructure (AWS – EC2 / ECR / S3 / RDS)
- Kubernetes deployment (EKS)
- Observability (Prometheus / Grafana / Node Exporter)

This project is structured and documented following **MAANG-level engineering patterns**.

---

## 🚀 Features

### **Application Features**
- Shorten any URL  
- Retrieve original URL by short ID  
- FastAPI backend  
- SQLite → PostgreSQL (upgrade in later layers)  
- Easy to extend to microservices

### **DevOps Features**
- Dockerized backend  
- CI pipeline: lint → build → test → scan → deploy  
- IaC using Terraform (in later layers)  
- Kubernetes manifests (Deployment, Service, Ingress)  
- Monitoring with Prometheus metrics endpoint  
- Dashboards via Grafana  
- Vulnerability scanning via Trivy  
- Code quality check via SonarQube

---

## 🏛 Architecture Overview

Frontend → FastAPI Backend → Database
│
├── Docker
├── CI/CD (Jenkins)
├── AWS (EC2, ECR, VPC)
└── Kubernetes (EKS)


---

## 🧱 Folder Structure

url-shortener-devops-project/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ └── utils.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md


Additional DevOps directories will be added in later layers:

├── jenkins/
├── k8s/
├── terraform/
├── monitoring/


---

## 🛠 Tech Stack

### **Backend**
- FastAPI  
- Python 3.11  
- SQLite (local)  
- PostgreSQL (production)

### **DevOps Tools**
| Category | Tools |
|---------|-------|
| Version Control | Git, GitHub |
| CI/CD | Jenkins / GitHub Actions |
| Containers | Docker |
| AWS Cloud | EC2, ECR, VPC, IAM, ALB, EKS |
| Deployment | Kubernetes |
| Monitoring | Prometheus, Grafana, Node Exporter |
| Security | Trivy, SonarQube |
| IaC | Terraform |

---

## ⚙️ Local Development

### Install dependencies:
```bash
pip install -r requirements.txt

Run the app:
python -m uvicorn app.main:app --reload

Test health endpoint:
GET http://localhost:8000/health


🐳 Docker Setup
Build image:
docker build -t url-shortener:v1 .

Run container:
docker run -p 8000:8000 url-shortener:v1


🚦 API Endpoints
Health Check
GET /health

Shorten URL
POST /shorten
Body:
{
  "original_url": "https://example.com"
}

Retrieve URL
GET /<short_id>


📈 Future Layers (Roadmap)
Layer 1 — Application ✔ DONE
Layer 2 — Docker (current)
Layer 3 — Jenkins CI/CD
Layer 4 — AWS EC2 Deployment
Layer 5 — Container Registry (ECR)
Layer 6 — Kubernetes (EKS)
Layer 7 — Monitoring & Alerts
Layer 8 — Terraform IaC
Layer 9 — Security (Trivy / SonarQube)
This project grows step-by-step into a complete production system.

🤝 Contributions
PRs, issues, and feature requests are welcome.

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.





