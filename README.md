# 🌤️ Peeps — Weather Checker Web App

A lightweight weather checker web application built with Django that displays real-time weather data for any city in the world. The project demonstrates a complete DevOps workflow — from local development to containerized deployment via CI/CD.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the App](#running-the-app)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Author](#author)

---

## Overview

Peeps allows users to search for any city and instantly see live weather data including temperature, humidity, wind speed, and feels-like temperature. The app automatically displays the **local time of the searched city** and renders a **dynamic animated background** that reflects the current weather condition — with separate animations for day and night.

The primary focus of this project goes beyond the application itself — it demonstrates how a simple Django app can be containerized, tested, and deployed using modern DevOps practices.

---

## Features

- 🔍 Search weather by city name
- 🌡️ Displays temperature, feels like, humidity, and wind speed
- 🕐 Shows the **local time of the searched city** (not your local machine time)
- 🌤️ Dynamic animated backgrounds based on weather condition
- 🌙 Separate day and night animations (clear night, cloudy night, rain night, snow night, mist night)
- 📱 Fully responsive — works on mobile and desktop
- 🐳 Containerized with Docker
- 🔄 Automated CI/CD via GitHub Actions
- ☁️ Deployed to cloud

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | Django Templates, HTML, CSS |
| External API | OpenWeather API |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Deployment | Render / AWS |


## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10+
- pip
- Git
- Docker (for containerization)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/peeps.git
cd peeps
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root of the project:

```
SECRET_KEY=your-django-secret-key
WEATHER_API_KEY=your-openweather-api-key
DEBUG=True
```

### Getting Your API Key

1. Go to [https://openweathermap.org](https://openweathermap.org)
2. Create a free account
3. Navigate to **My API Keys** in your dashboard
4. Copy your key and paste it into `.env`

> ⚠️ New API keys take 10–15 minutes to activate after creation.

### Getting Your Django Secret Key

Your Django secret key was auto-generated when you ran `startproject`. Find it in `settings.py` and move it into your `.env` file. Never commit it to version control.

---

## Running the App

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser and search for any city.

---

## Running Tests

```bash
python manage.py test
```

---

## Docker

### Build the Image

```bash
docker build -t peeps .
```

### Run the Container

```bash
docker run -p 8000:8000 --env-file .env peeps
```

Visit `http://localhost:8000` in your browser.

### Dockerfile Overview

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

## CI/CD Pipeline

The project uses **GitHub Actions** to automate testing, building, and deployment on every push to the `main` branch.

### Pipeline Stages

```
Push to main
     ↓
Checkout code
     ↓
Install dependencies
     ↓
Run Django tests
     ↓
Build Docker image
     ↓
Push image to registry
     ↓
Deploy to cloud platform
```

### Workflow File

Located at `.github/workflows/deploy.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        env:
          SECRET_KEY: ${{ secrets.SECRET_KEY }}
          WEATHER_API_KEY: ${{ secrets.WEATHER_API_KEY }}
        run: |
          python manage.py test

      - name: Build Docker image
        run: docker build -t peeps .

      - name: Deploy to Render
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### GitHub Secrets Required

Add these in your GitHub repository under **Settings → Secrets and variables → Actions**:

| Secret | Description |
|---|---|
| `SECRET_KEY` | Your Django secret key |
| `WEATHER_API_KEY` | Your OpenWeather API key |
| `RENDER_DEPLOY_HOOK` | Your Render deploy webhook URL |

---

## Deployment

### Deploying to Render

1. Push your code to GitHub
2. Go to [https://render.com](https://render.com) and create a free account
3. Click **New → Web Service** and connect your GitHub repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python manage.py runserver 0.0.0.0:8000`
5. Add your environment variables (`SECRET_KEY`, `WEATHER_API_KEY`, `DEBUG=False`) under **Environment**
6. Click **Deploy**

### Deploying to AWS

1. Push your Docker image to **Amazon ECR**
2. Create an **ECS** task definition using the image
3. Deploy to an ECS cluster behind an **Application Load Balancer**
4. Manage environment variables using **AWS Secrets Manager** or **ECS task environment variables**

---

## Author

**Gilks97**
- Portfolio: [g-moseti.vercel.app](https://g-moseti.vercel.app/)
- GitHub: [@Gilks97](https://github.com/Gilks97)

---
