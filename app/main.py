from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model.detection_model import predict_pipeline


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return {"health_check": "OK"}


@app.post("/predict", response_model=PredictionOut)
def predict(request: Request, payload: TextIn):
    language = predict_pipeline(payload.text)
    return templates.TemplateResponse("index.html", {"request": request, "language": language})


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)