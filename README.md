# 🌐 Microservicio de Saludo con Flask

Aplicación web mínima desarrollada con Flask, diseñada para demostrar el ciclo de vida completo de una aplicación en un entorno de desarrollo moderno, incluyendo contenedorización y despliegue automatizado.

Este proyecto es ideal como punto de partida para entender cómo una aplicación simple de Python puede ser empaquetada con Docker y orquestada con Kubernetes, o gestionada a través de un pipeline de CI/CD con Jenkins.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Flask
- **Lenguaje:** Python 3.9+
- **Contenedores:** Docker
- **Orquestación:** Kubernetes
- **CI/CD:** Jenkins

---

## 🚀 Guía de Inicio Rápido

### **Requisitos Previos**

- **Python 3.9+** y **pip** para la ejecución local.
- Opcional: **Docker**, **kubectl** y **Jenkins** para la contenedorización y el despliegue.

### **1. Ejecución Local**

Para probar la aplicación en tu máquina, sigue estos pasos:

1.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
2.  Ejecuta la aplicación:
    ```bash
    python app.py
    ```

La aplicación estará disponible en `http://localhost:5000/` y mostrará el mensaje "Hola desde Flask, soy el Docker en Azure... y estoy funcionando!".

### **2. Contenedorización con Docker**

Crea y ejecuta una imagen de Docker de la aplicación:

1.  Construye la imagen:
    ```bash
    docker build -t flask-app .
    ```
2.  Ejecuta el contenedor, mapeando el puerto 5000:
    ```bash
    docker run -p 5000:5000 flask-app
    ```

### **3. Despliegue en Kubernetes**

Despliega la aplicación en un clúster de Kubernetes:

```bash
kubectl apply -f k8s/flask-app.yaml
