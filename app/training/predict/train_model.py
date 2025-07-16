import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

data = {
    "feat1": [10000000, 20000000, 5000000, 12000000, 3000000, 8000000],
    "feat2": [90, 120, 75, 105, 60, 100],
    "feat3": [2015, 2018, 2020, 2012, 2019, 2021],
    "feat4": [75, 60, 45, 80, 30, 90],
    "feat5": [5000, 10000, 2500, 8000, 1200, 11000],
    "feat6": [6.8, 7.5, 5.9, 7.2, 4.8, 8.1],
    "feat7": [0.8, 0.6, 0.3, 0.9, 0.2, 0.95],
    "feat8": [1, 2, 1, 3, 1, 0],  # ejemplo: número de actores famosos
    "target": [1, 1, 0, 1, 0, 1]  # Etiqueta binaria: éxito (1) o fracaso (0)
}

df = pd.DataFrame(data)

# Separar características y etiqueta
X = df.drop("target", axis=1)
y = df["target"]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluar
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy : {accuracy:.2f}")

# Guardar modelo entrenado
model_path = os.path.join("app", "models", "predict_model.pkl")
joblib.dump(model, model_path)
print(f"✅ Model saved in: {model_path}")
