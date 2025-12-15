🚀 AWS ECS Fargate Microservice Deployment

This project demonstrates how to containerize a simple Python Flask microservice using Docker and deploy it on AWS ECS Fargate with:

Amazon ECR

Application Load Balancer (ALB)

CloudWatch Logs

VPC networking

IAM Roles

Auto-managed scaling

This is a real-world production-style project that is perfect for your resume and AWS portfolio.

🏗️ Architecture Overview
               +-----------------------------+
               |  Application Load Balancer  |
               |      (Public Access)        |
               +--------------+--------------+
                              |
                              v
                 +-------------------------+
                 |     Target Group        |
                 +-------------------------+
                              |
                              v
               +----------------------------------+
               |       ECS Fargate Service        |
               |  • Runs Dockerized Flask App     |
               |  • Auto-managed Compute          |
               +----------------+-----------------+
                                |
                                v
               +----------------------------------+
               |      Amazon Elastic Container    |
               |             Registry (ECR)        |
               +----------------------------------+


📁 Project Structure
ecs-microservice-deployment/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md

🧪 1. Flask Application (app.py)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask ECS App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

📦 2. Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

📄 3. requirements.txt
flask

🧱 4. Build & Run Locally with Docker
Build the image:
docker build -t ecs-microservice .

Test locally:
docker run -p 8080:8080 ecs-microservice


Visit:

http://localhost:8080

🗄️ 5. Push Docker Image to Amazon ECR
Log in to ECR:
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

Tag the image:
docker tag ecs-microservice:latest <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ecs-microservice:latest

Push the image:
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ecs-microservice:latest

🏗️ 6. Deploy on AWS ECS Fargate
✔ Create ECS Cluster

Name: ecs-microservice-cluster

✔ Create Task Definition (Fargate)

Image: ECR image URI

Port: 8080

CPU / Memory: default

Execution Role: auto-created

✔ Create Application Load Balancer

Listener Port: 80

Target Group Port: 80

✔ Create ECS Service

Platform: Fargate

Load Balancer: Attach ALB

Health check path: /

🌍 7. Access Your Microservice

Once ECS launches successfully, copy the Load Balancer DNS Name:

http://<your-alb-dns-name>/


You should see:

Hello from Flask ECS App!


🎉 Your ECS microservice is now live!
