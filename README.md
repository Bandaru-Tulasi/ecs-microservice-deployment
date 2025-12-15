🚀 AWS ECS Fargate Microservice Deployment — Docker + ECS + Fargate + ALB

This project demonstrates how to containerize a Python Flask microservice using Docker, push it to Amazon ECR, and deploy it on ECS Fargate behind an Application Load Balancer (ALB).

This is an excellent portfolio project for showcasing AWS Cloud / DevOps / Microservices skills.

---

📌 Architecture Overview

                +-----------------------------+
User (Browser) ---> |  Application Load Balancer |
                +-----------+-----------------+
                            |
                            v
                +-----------------------------+
                |      Target Group           |
                +--------------+--------------+
                               |
                               v
                +-----------------------------+
                |     ECS Fargate Service     |
                |   (Flask Microservice)      |
                +--------------+--------------+
                               |
                               v
                +-----------------------------+
                |     Amazon ECR Repository   |
                | (Stores Docker Image)       |
                +-----------------------------+

                ---

🧰 Technologies Used

Docker (containerization)

Amazon ECR (private container registry)

Amazon ECS Fargate (serverless container hosting)

Application Load Balancer (ALB) (public traffic routing)

IAM Roles & Policies (permissions)

VPC Networking (subnets, ENIs, security groups)

---

🛠️ Project Setup — Step-by-Step

1️⃣ Create a Flask Microservice

app.py:

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask ECS App!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


Create requirements.txt:

flask

---

2️⃣ Create Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]

---

3️⃣ Build & Test Docker Image Locally
docker build -t ecs-microservice .


Run it:

docker run -p 8080:8080 ecs-microservice


Open:

http://127.0.0.1:8080


Expected output:

Hello from Flask ECS App!

---

4️⃣ Push Image to Amazon ECR
Login to ECR:
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ACCOUNT-ID>.dkr.ecr.us-east-1.amazonaws.com

Tag image:
docker tag ecs-microservice:latest <ACCOUNT-ID>.dkr.ecr.us-east-1.amazonaws.com/ecs-microservice:latest

Push:
docker push <ACCOUNT-ID>.dkr.ecr.us-east-1.amazonaws.com/ecs-microservice:latest

---

5️⃣ Create ECS Fargate Service

Settings:

Launch Type: Fargate

Task Size: 0.5 vCPU, 1 GB RAM

Container Port: 8080

Load Balancer: Application Load Balancer

Health Check Path: /

Desired Tasks: 1

---

6️⃣ ALB Target Group Configuration

Protocol: HTTP

Port: 80

Health check path: /

Healthy threshold: 2

Unhealthy threshold: 2

Interval: 10 seconds

Timeout: 5 seconds

---

7️⃣ Test Your Deployment

Open your ALB DNS name:

http://<your-load-balancer>.amazonaws.com


You should see:

Hello from Flask ECS App!

---

🌍 Final Public Endpoint

Your application is reachable via the ALB URL:

http://<your-alb-dns-name>

📄 Files in This Project
app.py               # Flask microservice
Dockerfile           # Build instructions
requirements.txt     # Python dependencies
README.md            # Documentation
