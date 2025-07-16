# 🧠 SmartChoiceAI – ML-Powered Decision Prediction API

**SmartChoiceAI** is a modular and extensible microservice powered by FastAPI and Scikit-learn.  
It predicts binary outcomes like user preferences or decisions (e.g., like a movie, buy a product, complete a course), based on structured input features.

Built for **real-world integration**, **multi-domain use**, and **plug-and-play deployment**.

---

## 🚀 Features

- 🔮 Generic machine learning engine (RandomForestClassifier)
- ⚡ FastAPI microservice architecture
- 🔁 Works with multiple domains (movies, music, products, courses, etc.)
- 📡 Ready to integrate with .NET, JavaScript frontends, mobile apps, and more
- 🧠 Easy to train, update, and customize
- 🧪 Unit-test friendly structure

---

---

## ✨ What Makes SmartChoiceAI Special?

SmartChoiceAI is not just another machine learning experiment. It's a **production-ready, reusable, and scalable solution** designed to be deployed and consumed in real-world applications. Here's what sets it apart:

### ✅ Decoupled & Reusable Architecture
- The ML logic is fully separated from the API layer.
- You can replace, retrain, or extend the model without touching the API endpoints.

### ✅ Multi-Domain Ready
- Although initially designed for movie preferences, the model structure is domain-agnostic.
- You can use the same pipeline to predict interest in products, music, locations, educational content, and more.

### ✅ Fully Scalable & Integration-Ready
- Built with FastAPI, the service is lightweight, async-capable, and **ready to be scaled using Docker, Kubernetes or serverless platforms**.
- Exposed via RESTful endpoints, the API can be consumed by:
  - Frontends (React, Vue, Angular, etc.)
  - Mobile apps (Flutter, React Native, Swift, Kotlin)
  - Other backends (.NET, Java, Python, Node.js, Go, etc.)
  - Automation tools (Zapier, n8n, etc.)
  - Postman or curl (for testing or internal services)

### ✅ Plug & Play in Any Tech Stack
- Because it's language-agnostic at the interface level (via HTTP JSON), **you can integrate it with any stack that supports HTTP requests**.

### ✅ Easy to Maintain & Evolve
- The ML model is trained via a simple script (`train_model.py`) and saved as a serialized file.
- The code is modular, readable, and ready for continuous improvement (e.g., switching to XGBoost, adding SHAP explanations, etc.)

### ✅ Developer-Friendly by Design
- Structured using modern FastAPI best practices
- Typed endpoints with Pydantic validation
- Logs, docs and easy testing out of the box
- Ready to plug into CI/CD or cloud deployment pipelines

---


## 🗂️ Project Structure
<code>
smartchoice-api/
├── app/
│   ├── routers/
│   │   └── prediction.py          ← Endpoint general
│   ├── schemas/
│   │   └── predict_schema.py      ← Entrada flexible
│   ├── services/
│   │   └── task_engine.py         ← Lógica para media + predict
│   ├── models/
│   │   └── predict/
│   │       └── model.pkl          ← Modelo para predicción binaria
│   ├── main.py                    ← App FastAPI
├── train_model.py                 ← Script para entrenar el modelo
├── requirements.txt
└── README.md
</code>
