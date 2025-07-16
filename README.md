# 🧠 SmartChoiceAI – README Metadata

## 📛 Project Title
title: "🧠 SmartChoiceAI – ML-Powered Decision Prediction API"

## 🧾 Description
description: >
  SmartChoiceAI is a FastAPI microservice integrated with a Scikit-learn binary classification model.
  It predicts whether a user will take a specific action (e.g., like a movie, buy a product, choose a location),
  based on structured input features. Flexible, fast, and reusable across domains.

## 🚀 Features
features:
  - "⚡ FastAPI microservice architecture"
  - "🔮 ML model based on RandomForestClassifier (easily swappable)"
  - "🔁 Generic prediction engine for multiple domains"
  - "🧠 Lightweight and extensible ML logic"
  - "📡 Built for integration with .NET, JS frontends, mobile apps, etc."
  - "🧪 Easily testable and modifiable structure"

## 🗂️ Project Structure
project_structure: |
  smartchoice-api/
  ├── app/
  │   ├── crud/                  # (Optional business logic)
  │   ├── models/                # (If using ORM or DB)
  │   ├── routers/
  │   │   └── prediction.py      # ML prediction endpoint
  │   ├── schemas/
  │   │   └── predict_schema.py
  │   ├── services/
  │   │   └── ml/
  │   │       ├── model.py       # ML logic for predictions
  │   │       └── train_model.py # Model training script
  │   ├── database.py
  │   └── main.py
  ├── .gitignore
  ├── README.md
  └── requirements.txt

## 🧠 Model Training
training:
  command: "python app/services/ml/train_model.py"
  output: "services/ml/model.pkl"
  note: "Run this script to generate or update the binary classification model."

## ▶️ Running the API
run_api:
  command: "uvicorn app.main:app --reload"
  url: "http://localhost:8000"
  note: "Start the FastAPI server locally."

## 📮 Sample Request
endpoint: "/predict"
method: "POST"
example_payload:
  duracion: 120
  genero_accion: 1
  genero_romance: 0
example_response:
  will_act: true

## 📦 Dependencies
dependencies:
  install_command: "pip install -r requirements.txt"
  core_libs:
    - fastapi
    - uvicorn
    - scikit-learn
    - pandas
    - joblib

## 💡 Use Cases
use_cases:
  - "🎥 Movie preference prediction"
  - "🛒 Product recommendation"
  - "🎵 Music interest prediction"
  - "📍 Tourism or destination suggestion"
  - "📚 Education or course completion likelihood"
  - "🧪 Any binary classification use case"

## 👤 Author
author: "[Your GitHub username or real name]"

## 📄 License
license: "MIT License"
