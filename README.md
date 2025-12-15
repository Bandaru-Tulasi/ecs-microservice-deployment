🚀 AWS ECS Fargate Microservice Deployment — Docker + ECS + Fargate + ALB

This project demonstrates how to deploy a containerized Python Flask microservice using Docker, Amazon ECR, ECS Fargate, and an Application Load Balancer (ALB).

This setup represents a real-world microservice deployment architecture used in modern cloud-native applications.

🎯 Why This Project Matters

This project demonstrates real-world AWS cloud engineering skills, including:

Building and packaging applications using Docker

Deploying serverless containers using ECS Fargate

Hosting microservices behind a production-grade ALB

Applying least-privilege IAM roles

Configuring VPC networking (subnets, routing, security groups)

Implementing health checks and auto-managed scaling

This architecture is widely used in production across modern cloud-native systems.

🧱 Architecture Overview
          ┌───────────────────────────┐
          │   Application Load        │
          │      Balancer (ALB)       │
          │       Public Access       │
          └───────────────┬──────────┘
                          │
                  ┌───────▼────────┐
                  │   Target Group  │
                  └───────┬────────┘
                          │
                 ┌────────▼───────────┐
                 │   ECS Fargate       │
                 │   Service + Tasks   │
                 │ • Flask App         │
                 │ • Auto Scaling      │
                 └────────┬───────────┘
                          │
          ┌───────────────▼────────────────┐
          │        Amazon ECR Repository    │
          │     Stores Docker Container     │
          └─────────────────────────────────┘

🧰 Technologies Used

Docker

Amazon ECR

Amazon ECS (Fargate)

Application Load Balancer (ALB)

IAM Roles

VPC networking

📁 Project Structure
ecs-microservice-deployment/
│
├── app.py               # Flask application
├── Dockerfile           # Image build instructions
├── requirements.txt     # Python dependencies
└── README.md            # Documentation

🚀 Deployment Steps
1️⃣ Build Docker Image
docker build -t ecs-microservice .

2️⃣ Tag the Image for ECR
docker tag ecs-microservice:latest \
766377908037.dkr.ecr.us-east-1.amazonaws.com/ecs-microservice:latest

3️⃣ Push Image to ECR
docker push \
766377908037.dkr.ecr.us-east-1.amazonaws.com/ecs-microservice:latest

4️⃣ Create ECS Fargate Service

Includes:

Task definition

0.5 vCPU / 1GB RAM

Public ALB

Target group + health checks

Port mapping: Container 8080 → ALB 80

5️⃣ Test the Application

Open your Load Balancer DNS name:

http://<your-load-balancer>.amazonaws.com/


You should see:

Hello from Flask ECS App!

🩺 Health Check Configuration
Setting	Value
Protocol	HTTP
Path	/
Port	traffic-port
Healthy Threshold	2
Unhealthy Threshold	2
Interval	10 seconds
Timeout	5 seconds
