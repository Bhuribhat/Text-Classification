from fastapi import FastAPI
from pydantic import BaseModel
from app.model.detection_model import predict_pipeline


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


app = FastAPI()


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}