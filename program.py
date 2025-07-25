from fastapi import FastAPI
from app.Controllers import predict_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartChoiceAI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(predict_router)

