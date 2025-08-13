
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

## 📊 Monitoring and Observability

### Health Endpoints

- **Health Check:** `/health` - Returns application status
- **Metrics:** `/metrics` - Application metrics (if enabled)
- **Info:** `/info` - Application information

### Logging

The application uses structured logging with different levels:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Flask environment | `production` |
| `FLASK_DEBUG` | Debug mode | `False` |
| `PORT` | Application port | `5000` |
| `HOST` | Application host | `0.0.0.0` |

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

## 🚨 Troubleshooting

### Common Issues

**Application won't start:**
```bash
# Check Python version
python --version

# Install dependencies
pip install -r requirements.txt

# Check port availability
netstat -an | grep 5000
```

**Docker issues:**
```bash
# Check Docker daemon
docker info

# View container logs
docker logs flask-app

# Debug container
docker exec -it flask-app /bin/sh
```

**Kubernetes issues:**
```bash
# Check cluster connection
kubectl cluster-info

# Check pod status
kubectl describe pod <pod-name>

# Check service endpoints
kubectl get endpoints
```

---

## 🔐 Security Considerations

- **Non-root container:** Application runs as non-privileged user
- **Minimal base image:** Uses Alpine Linux for smaller attack surface
- **No secrets in code:** Use environment variables or Kubernetes secrets
- **HTTPS in production:** Configure reverse proxy with SSL/TLS
- **Regular updates:** Keep dependencies and base images updated

---

## 📈 Scaling and Performance

### Horizontal Scaling

```bash
# Scale with Kubernetes
kubectl scale deployment flask-app --replicas=5

# Auto-scaling with HPA
kubectl autoscale deployment flask-app --cpu-percent=70 --min=2 --max=10
```

### Performance Optimization

- Use **Gunicorn** or **uWSGI** for production
- Implement **caching** for static content
- Configure **load balancing**
- Monitor **resource usage**

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/flask-microservice/issues)
- **Documentation:** [Wiki](https://github.com/yourusername/flask-microservice/wiki)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/flask-microservice/discussions)

---

**Happy Coding!** 🚀✨
