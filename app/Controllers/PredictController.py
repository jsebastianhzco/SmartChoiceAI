from fastapi import APIRouter, HTTPException
from app.Entities.MlEntities.PredictionRequest import PredictionRequest
from app.Services.PredictionService import predict_task
import numpy as np


router = APIRouter(prefix="/predict", tags=["Predict"])

@router.post("/")
async def predict(request: PredictionRequest):
    try:
        result = predict_task(request)

        return {"success": True, "data": int(result) if isinstance(result, (np.integer, np.int64)) else result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
