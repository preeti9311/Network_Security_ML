# 🛡️ End-to-End Network Security ML System
[![Live Demo](https://img.shields.io/badge/Render-Live%20Demo-brightgreen)](https://network-security-ml-nm0k.onrender.com/docs)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://github.com/preeti9311/Network_Security_ML/blob/main/Dockerfile)
[![CI/CD Pipeline](https://github.com/preeti9311/Network_Security_ML/actions/workflows/main.yml/badge.svg)](https://github.com/preeti9311/Network_Security_ML/actions)

An industrial-grade End-to-End Machine Learning pipeline that predicts network security threats. Built with **FastAPI**, **Docker**, **MongoDB Atlas**, **MLflow**, and deployed via **GitHub Actions** on **Render**.

---

## 🚀 Key Features

* **Data Ingestion:** Automated data pipeline fetching raw security datasets from **MongoDB Atlas**.
* **ML Pipeline:** Custom preprocessing layers and scikit-learn classification models.
* **Experiment Tracking:** Integrated **MLflow** & **DagsHub** for remote model tracking and artifact logging.
* **FastAPI Backend:** Web interface rendering batch prediction results directly in clean HTML tables.
* **Containerization:** Environment-isolated **Docker** container built for seamless execution.
* **Automated CI/CD:** **GitHub Actions** workflow for automated testing and continuous deployment on **Render**.

---

## 🛠️ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Language** | Python 3.11 |
| **Web Framework** | FastAPI, Starlette, Jinja2, Uvicorn |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy |
| **MLOps & Logging** | MLflow, DagsHub, Custom Logging & Exception Modules |
| **Database** | MongoDB Atlas |
| **DevOps & Cloud** | Docker, GitHub Actions, Render |

---

## 💻 Local Execution Guide

### 1. Clone Repository & Set Environment Variables
Create a `.env` file in the root directory:
```env
MONGO_DB_URL=your_mongodb_connection_string
DAGSHUB_USER_TOKEN=your_dagshub_token
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_password
