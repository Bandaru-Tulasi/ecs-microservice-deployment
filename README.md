🚀 AWS ECS Fargate Microservice Deployment — Docker + ECS + Fargate + ALB

This project demonstrates how to deploy a containerized Python Flask microservice using Docker, Amazon ECR, ECS Fargate, and an Application Load Balancer (ALB).

This setup represents a real-world cloud microservice deployment using fully managed container hosting (Fargate), secure image storage (ECR), and load-balanced traffic distribution (ALB).

🎯 Why This Project Matters

This project demonstrates real-world AWS cloud engineering skills, including:

Building and packaging applications using Docker

Deploying serverless containers using ECS Fargate

Hosting microservices behind a production ALB

Applying least-privilege IAM roles

Understanding VPC networking, subnets & security groups

Implementing health checks and managed scaling

This is the exact architecture used by cloud-native companies to run microservices in production.

🧱 Architecture Overview

          ┌───────────────────────────┐
          │   Application Load        │
          │      Balancer (ALB)       │
          │     (Public Access)       │
          └───────────────┬──────────┘
                          │
                  ┌───────▼────────┐
                  │   Target Group  │
                  └───────┬────────┘
                          │
                 ┌────────▼───────────┐
                 │   ECS Fargate       │
                 │   Service + Tasks   │
                 │ • Runs Flask App    │
                 │ • Auto Scaling      │
                 └────────┬───────────┘
                          │
          ┌───────────────▼────────────────┐
          │        Amazon ECR Repository    │
          │     Stores Docker container     │
          └─────────────────────────────────┘

🧰 Technologies Used

Docker (Containerization)

Amazon ECR (Container registry)

Amazon ECS (Fargate)

Application Load Balancer (ALB)

IAM Roles & Permissions

VPC Networking (Subnets, SGs)

📁 Project Structure

ecs-microservice-deployment/
│
├── app.py               # Flask app (Hello World)
├── Dockerfile           # Build instructions
├── requirements.txt     # Dependencies
└── README.md            # Documentation

🚀 Step-by-Step Deployment

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

0.5 vCPU + 1GB memory

Public ALB + target group

Container port mapping (8080 → 80 ALB)

5️⃣ Test the Application

Open your ALB DNS URL:

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
