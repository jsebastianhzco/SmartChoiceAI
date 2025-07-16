import joblib
from app.Entities.MlEntities.PredictionRequest import PredictionRequest
from pathlib import Path
import numpy as np

MODEL_PATH = Path("app/Services/AiModels/model.pkl")
model = joblib.load(MODEL_PATH)

def predict_task(request: PredictionRequest):
    task = request.task.lower()
    data_array = np.array(request.data).reshape(1, -1)

    if task == "predict":
        return model.predict(data_array)[0]
    
    elif task == "average":
        return np.mean(request.data)
    
    elif task == "sum":
        return np.sum(request.data)
    
    else:
        raise ValueError(f"Tarea no reconocida: {request.task}")
