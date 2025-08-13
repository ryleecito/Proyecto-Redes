
# 🌐 Flask Greeting Microservice

Minimal web application developed with Flask, designed to demonstrate the complete lifecycle of an application in a modern development environment, including containerization and automated deployment.

This project is ideal as a starting point to understand how a simple Python application can be packaged with Docker and orchestrated with Kubernetes, or managed through a CI/CD pipeline with Jenkins.

---

## 🛠️ Technologies Used

- **Backend:** Flask
- **Language:** Python 3.9+
- **Containers:** Docker
- **Orchestration:** Kubernetes
- **CI/CD:** Jenkins

---

## 🚀 Quick Start Guide

### **Prerequisites**

- **Python 3.9+** and **pip** for local execution
- Optional: **Docker**, **kubectl** and **Jenkins** for containerization and deployment

### **1. Local Execution**

To test the application on your machine, follow these steps:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000/` and will display the message "Hello from Flask, I'm the Docker in Azure... and I'm working!".

### **2. Containerization with Docker**

Create and run a Docker image of the application:

1. Build the image:
   ```bash
   docker build -t flask-app .
   ```

2. Run the container, mapping port 5000:
   ```bash
   docker run -p 5000:5000 flask-app
   ```

### **3. Kubernetes Deployment**

Deploy the application to a Kubernetes cluster:

```bash
kubectl apply -f k8s/flask-app.yaml
```

---

## 📁 Project Structure

```
flask-microservice/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker container configuration
├── k8s/
│   └── flask-app.yaml       # Kubernetes deployment manifest
├── Jenkinsfile              # CI/CD pipeline configuration
└── README.md                # This file
```

---

## 🐳 Docker Configuration

The `Dockerfile` is optimized for production with the following features:

- **Multi-stage build** for smaller image size
- **Non-root user** for security
- **Health checks** for container monitoring
- **Production-ready** WSGI server

### Docker Commands Reference

```bash
# Build image
docker build -t flask-app:latest .

# Run container
docker run -d -p 5000:5000 --name flask-app flask-app:latest

# View logs
docker logs flask-app

# Stop container
docker stop flask-app

# Remove container
docker rm flask-app
```

---

## ☸️ Kubernetes Deployment

The Kubernetes configuration includes:

- **Deployment** with replica management
- **Service** for load balancing
- **ConfigMap** for environment variables
- **Health checks** (readiness and liveness probes)

### Kubernetes Commands Reference

```bash
# Deploy application
kubectl apply -f k8s/flask-app.yaml

# Check deployment status
kubectl get deployments

# Check pods
kubectl get pods

# Check services
kubectl get services

# View logs
kubectl logs -f deployment/flask-app

# Scale deployment
kubectl scale deployment flask-app --replicas=3

# Delete deployment
kubectl delete -f k8s/flask-app.yaml
```

---

## 🔄 CI/CD with Jenkins

The project includes a `Jenkinsfile` that defines a complete CI/CD pipeline:

### Pipeline Stages

1. **Checkout:** Clone source code from repository
2. **Build:** Install dependencies and run tests
3. **Docker Build:** Create Docker image
4. **Docker Push:** Push image to registry
5. **Deploy:** Deploy to Kubernetes cluster
6. **Verify:** Run health checks

### Jenkins Setup

1. Install required plugins:
   - Docker Pipeline
   - Kubernetes CLI
   - Pipeline

2. Configure credentials:
   - Docker registry credentials
   - Kubernetes cluster access

3. Create a new Pipeline job pointing to your repository

---

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
pip install pytest requests

# Run tests
python -m pytest tests/

# Test endpoint manually
curl http://localhost:5000/
```

### Container Testing

```bash
# Test container health
docker exec flask-app curl http://localhost:5000/health

# Load testing with curl
for i in {1..100}; do curl http://localhost:5000/; done
```

---


### Production Configuration

```bash
# Set environment variables
export FLASK_ENV=production
export FLASK_DEBUG=False
export PORT=5000

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

---
## 📈 Scaling and Performance

### Horizontal Scaling

```bash
# Scale with Kubernetes
kubectl scale deployment flask-app --replicas=5

# Auto-scaling with HPA
kubectl autoscale deployment flask-app --cpu-percent=70 --min=2 --max=10
```

