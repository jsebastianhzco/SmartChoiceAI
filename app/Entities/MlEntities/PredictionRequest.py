from pydantic import BaseModel
from typing import List, Union

class PredictionRequest(BaseModel):
    data: List[Union[int, float]]
    task: str  # Ej: "predict", "average", "sum", etc.
