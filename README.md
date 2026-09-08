Below is a **modern, professional GitHub-ready `README.md`** for your project. You can copy the entire block directly into `README.md`.

# 🐍 Python Automation Application Using Kubernetes

<div align="center">

### 🚀 Containerized Python Automation & Kubernetes Deployment

A hands-on DevOps project demonstrating how to **build, containerize, deploy, configure, scale, monitor, and self-heal a Python automation application using Docker and Kubernetes.**

<br>

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge\&logo=kubernetes\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)

</div>

---

## 📌 Project Overview

This project demonstrates the complete workflow of deploying a **Python-based system monitoring automation application** inside a Kubernetes cluster.

The application performs basic Linux system monitoring tasks and generates application logs.

The project covers:

* Python automation
* Docker containerization
* Kubernetes Deployment
* Kubernetes Pods
* Kubernetes ReplicaSets
* Kubernetes Services
* Kubernetes ConfigMaps
* Application logging
* Kubernetes troubleshooting
* Horizontal scaling
* Kubernetes self-healing

---

## 🎯 Objective

The primary objective is to understand how a Python automation application can be **containerized with Docker and managed using Kubernetes**.

The project demonstrates how Kubernetes maintains the desired state of an application through Deployments and ReplicaSets while providing service discovery, configuration management, scaling, and self-healing.

---

## ✨ Features

| Feature               | Description                           |
| --------------------- | ------------------------------------- |
| 🕐 System Uptime      | Checks Linux system uptime            |
| 💾 Disk Monitoring    | Checks disk capacity and usage        |
| 🧠 Memory Monitoring  | Checks RAM usage                      |
| ⚙️ Process Monitoring | Lists running processes               |
| 📝 Logging            | Creates application log files         |
| 🐳 Docker             | Packages application into a container |
| ☸️ Kubernetes         | Deploys and manages containers        |
| ⚙️ ConfigMap          | Provides application configuration    |
| 🌐 Service            | Provides stable Kubernetes networking |
| 📈 Scaling            | Runs multiple application replicas    |
| ❤️ Self-Healing       | Recreates deleted Pods automatically  |

---

# 🏗️ Architecture

```text
                       ┌──────────────────────┐
                       │  Python Application  │
                       │      app.py          │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │      Dockerfile      │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  Docker Image v2     │
                       │ python-automation    │
                       └──────────┬───────────┘
                                  │
                                  ▼
                  ┌──────────────────────────────┐
                  │      Kubernetes Cluster      │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                       ┌──────────────────────┐
                       │      Deployment      │
                       │  python-automation   │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │      ReplicaSet      │
                       └──────────┬───────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
                ┌───────┐     ┌───────┐     ┌───────┐
                │ Pod 1 │     │ Pod 2 │     │ Pod 3 │
                └───┬───┘     └───┬───┘     └───┬───┘
                    │             │             │
                    └─────────────┼─────────────┘
                                  ▼
                       ┌──────────────────────┐
                       │ Kubernetes Service   │
                       │ ClusterIP : 8080     │
                       └──────────────────────┘

                 ConfigMap
                     │
                     ▼
              Application Environment
              ├── APP_NAME
              └── ENVIRONMENT
```

---

# 🔄 Application Workflow

```text
Python Source Code
        │
        ▼
requirements.txt
        │
        ▼
Docker Build
        │
        ▼
Docker Image
        │
        ▼
Kubernetes Deployment
        │
        ▼
ReplicaSet
        │
        ▼
Multiple Pods
        │
        ▼
Kubernetes Service
        │
        ▼
Running Application
```

---

# 📂 Project Structure

```text
python-k8s-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    └── configmap.yaml
```

---

# 🛠️ Technologies Used

### Programming

* Python 3.12
* `psutil`

### Containerization

* Docker
* Dockerfile

### Orchestration

* Kubernetes
* kubectl
* Deployment
* ReplicaSet
* Pod
* Service
* ConfigMap

### Operating System

* Linux
* Ubuntu

---

# 📋 Prerequisites

Before running the project, install:

```text
Python 3
Docker
kubectl
Kubernetes Cluster
```

Verify Python:

```bash
python3 --version
```

Verify Docker:

```bash
docker --version
```

Verify Kubernetes:

```bash
kubectl version --client
```

Check the cluster:

```bash
kubectl get nodes
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Navigate into the project:

```bash
cd python-k8s-project
```

---

# 🐍 Task 1 — Run Python Application

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Run:

```bash
python3 app.py
```

The application checks:

```text
System Uptime
Disk Usage
Memory Usage
Running Processes
Log File
```

Check the generated log:

```bash
cat /tmp/python-automation.log
```

---

# 🐳 Task 2 — Build Docker Image

Build the image:

```bash
docker build -t python-automation:v2 .
```

Verify:

```bash
docker images
```

Expected image:

```text
python-automation   v2
```

---

# 🧪 Test Docker Container

Run:

```bash
docker run --rm python-automation:v2
```

Expected output:

```text
============================================================
Application : python-monitor
Environment : development
============================================================

System Uptime : ...

Disk Usage
...

Memory Usage
...

Running Processes
...

Next monitoring cycle in 60 seconds...
```

The application continuously runs monitoring cycles every 60 seconds.

Stop the container:

```bash
Ctrl + C
```

---

# ☸️ Task 3 — Kubernetes Deployment

Apply the Deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Check Deployment:

```bash
kubectl get deployments
```

Check Pods:

```bash
kubectl get pods
```

Detailed Pod information:

```bash
kubectl get pods -o wide
```

---

# ⚙️ Task 4 — ConfigMap

Apply the ConfigMap:

```bash
kubectl apply -f k8s/configmap.yaml
```

Verify:

```bash
kubectl get configmaps
```

Detailed information:

```bash
kubectl describe configmap python-automation-config
```

The application receives:

```text
APP_NAME=python-monitor
ENVIRONMENT=development
```

Verify inside the Pod:

```bash
kubectl exec <pod-name> -- env | grep -E 'APP_NAME|ENVIRONMENT'
```

Expected:

```text
APP_NAME=python-monitor
ENVIRONMENT=development
```

---

# 🌐 Task 5 — Kubernetes Service

Apply the Service:

```bash
kubectl apply -f k8s/service.yaml
```

Check:

```bash
kubectl get services
```

Describe:

```bash
kubectl describe service python-automation-service
```

Check endpoints:

```bash
kubectl get endpoints python-automation-service
```

### Note

The current application is a background monitoring application and does not expose an HTTP endpoint.

Therefore, the ClusterIP Service is used to demonstrate Kubernetes service configuration and networking rather than browser access.

---

# 📜 Task 6 — Application Logs & Troubleshooting

View application logs:

```bash
kubectl logs <pod-name>
```

Follow logs:

```bash
kubectl logs -f <pod-name>
```

Check previous container logs:

```bash
kubectl logs <pod-name> --previous
```

Describe the Pod:

```bash
kubectl describe pod <pod-name>
```

Check Kubernetes events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Check Deployment:

```bash
kubectl describe deployment python-automation
```

Check ReplicaSets:

```bash
kubectl get replicasets
```

---

# 📈 Task 7 — Kubernetes Scaling

Initially the Deployment runs one replica.

Scale to three:

```bash
kubectl scale deployment python-automation --replicas=3
```

Check Deployment:

```bash
kubectl get deployment
```

Check Pods:

```bash
kubectl get pods -o wide
```

Expected:

```text
python-automation-xxxxx-aaaaa   1/1   Running
python-automation-xxxxx-bbbbb   1/1   Running
python-automation-xxxxx-ccccc   1/1   Running
```

Verify:

```bash
kubectl get deployment python-automation
```

Expected:

```text
READY
3/3
```

---

# ❤️ Task 8 — Kubernetes Self-Healing

List Pods:

```bash
kubectl get pods
```

Select one running Pod and delete it:

```bash
kubectl delete pod <pod-name>
```

Immediately monitor:

```bash
kubectl get pods -w
```

Kubernetes detects that the actual number of Pods is lower than the desired number.

A replacement Pod is automatically created.

Expected final state:

```text
3/3 Pods Running
```

Verify:

```bash
kubectl get deployment python-automation
```

---

# 🔥 Self-Healing Workflow

```text
Desired State
3 Pods
   │
   ▼
┌───────┐ ┌───────┐ ┌───────┐
│ Pod 1 │ │ Pod 2 │ │ Pod 3 │
└───────┘ └───────┘ └───────┘
                       │
                       X
                    Deleted
                       │
                       ▼
              Actual State = 2
                       │
                       ▼
              ReplicaSet detects
                  difference
                       │
                       ▼
                New Pod created
                       │
                       ▼
              Actual State = 3
```

---

# 🔍 Useful Kubernetes Commands

## Cluster

```bash
kubectl get nodes
```

```bash
kubectl cluster-info
```

## Pods

```bash
kubectl get pods
```

```bash
kubectl get pods -o wide
```

```bash
kubectl describe pod <pod-name>
```

```bash
kubectl delete pod <pod-name>
```

## Logs

```bash
kubectl logs <pod-name>
```

```bash
kubectl logs -f <pod-name>
```

```bash
kubectl logs <pod-name> --previous
```

## Deployments

```bash
kubectl get deployments
```

```bash
kubectl describe deployment python-automation
```

```bash
kubectl scale deployment python-automation --replicas=3
```

## ReplicaSets

```bash
kubectl get replicasets
```

## Services

```bash
kubectl get services
```

```bash
kubectl describe service python-automation-service
```

```bash
kubectl get endpoints
```

## ConfigMaps

```bash
kubectl get configmaps
```

```bash
kubectl describe configmap python-automation-config
```

## Events

```bash
kubectl get events --sort-by=.lastTimestamp
```

---

# 🧪 Final Verification

Run:

```bash
kubectl get nodes
```

```bash
kubectl get deployments
```

```bash
kubectl get pods -o wide
```

```bash
kubectl get services
```

```bash
kubectl get configmaps
```

```bash
kubectl get replicasets
```

```bash
kubectl get events --sort-by=.lastTimestamp
```

---

# 📸 Screenshots / Evidence

Add screenshots to your project documentation for:

* Python application execution
* Project directory structure
* Docker image creation
* Docker container execution
* Kubernetes nodes
* Kubernetes Deployment
* Kubernetes Pods
* ConfigMap
* Kubernetes Service
* Application logs
* Three-replica scaling
* Pod deletion
* Automatic replacement Pod

Recommended documentation structure:

```text
screenshots/
│
├── 01-project-structure.png
├── 02-python-application.png
├── 03-docker-build.png
├── 04-docker-image.png
├── 05-docker-container.png
├── 06-kubernetes-nodes.png
├── 07-deployment.png
├── 08-pods.png
├── 09-configmap.png
├── 10-service.png
├── 11-logs.png
├── 12-scaling.png
└── 13-self-healing.png
```

---

# 📊 Kubernetes Resources

| Resource   | Name                        | Purpose                          |
| ---------- | --------------------------- | -------------------------------- |
| Deployment | `python-automation`         | Manages application Pods         |
| ReplicaSet | Generated by Deployment     | Maintains desired replicas       |
| Pod        | `python-automation-*`       | Runs Python container            |
| Service    | `python-automation-service` | Provides stable networking       |
| ConfigMap  | `python-automation-config`  | Stores application configuration |

---

# 🔐 Configuration

The application uses the following environment variables:

```text
APP_NAME=python-monitor
ENVIRONMENT=development
```

These values are managed through Kubernetes ConfigMap.

Sensitive information such as:

```text
Passwords
API Keys
Tokens
Database Credentials
```

should **not** be stored in a ConfigMap. Kubernetes Secrets should be used for sensitive configuration.

---

# 📚 What I Learned

Through this project, I learned:

* How to create a Python automation application
* How to use the `psutil` Python library
* How to create a Dockerfile
* How to build Docker images
* How to test Docker containers
* How to deploy applications using Kubernetes
* How Kubernetes Deployments work
* How ReplicaSets maintain Pod replicas
* How Kubernetes Services work
* How ConfigMaps provide configuration
* How to inspect Kubernetes logs
* How to troubleshoot Pods
* How to inspect Kubernetes events
* How to scale applications
* How Kubernetes performs self-healing
* How Kubernetes maintains the desired state

---

# 🎯 Overall Outcome

The complete DevOps workflow was successfully implemented:

```text
             Python Application
                     │
                     ▼
                Dockerfile
                     │
                     ▼
              Docker Image
                     │
                     ▼
             Kubernetes Cluster
                     │
                     ▼
                Deployment
                     │
                     ▼
                ReplicaSet
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        Pod 1      Pod 2      Pod 3
          │          │          │
          └──────────┼──────────┘
                     ▼
                  Service
                     │
                     ▼
              Python Application
```

The project demonstrates a complete **Python → Docker → Kubernetes** deployment workflow with configuration management, service discovery, logging, scaling, and self-healing.

---

# 🚀 Future Enhancements

Possible improvements include:

* Convert the application into a Flask/FastAPI web application
* Add Kubernetes Ingress
* Add Liveness and Readiness Probes
* Add CPU and Memory resource limits
* Add Horizontal Pod Autoscaler
* Add PersistentVolume for logs
* Add Prometheus monitoring
* Add Grafana dashboards
* Add Docker Hub image publishing
* Add GitHub Actions CI/CD
* Add Kubernetes Secrets
* Add Helm chart
* Add Argo CD GitOps deployment

---

# 👨‍💻 Author

**Venu Gopala Reddy Eppala**

### DevOps / Cloud Engineering Projects

```text
Python • Linux • Docker • Kubernetes • AWS • Terraform
Git • GitHub Actions • Ansible • Jenkins • Prometheus • Grafana
```

---

## ⭐ Project Status

```text
✅ Python Application
✅ Docker Containerization
✅ Kubernetes Deployment
✅ ConfigMap
✅ Kubernetes Service
✅ Logging & Troubleshooting
✅ Scaling
✅ Self-Healing

PROJECT STATUS: COMPLETED
```

---

<div align="center">

### 🐍 Python + 🐳 Docker + ☸️ Kubernetes

**Built as a practical DevOps automation project**

</div>
