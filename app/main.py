import os
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.model.detection_model import predict_pipeline
from app.model.classify_model import predict_classify


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


ROOT_DIR = os.getcwd()

app = FastAPI()
app.mount("/static", StaticFiles(directory=f"{ROOT_DIR}/app/static"), name="static")
templates = Jinja2Templates(directory=f"{ROOT_DIR}/app/templates")


@app.get("/")
def home(request: Request):
    return {"health_check": "OK"}


@app.post("/predict", response_model=PredictionOut)
def predict(request: Request, payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}


@app.post("/classify")
async def classify(request: Request, payload: TextIn):
    text = payload.text
    prediction = predict_classify([text])
    return {"prediction": prediction}


@app.route("/detect", methods=["GET", "POST"])
async def detect(request: Request, payload: TextIn = None):
    if request.method == "POST" and payload is not None:
        language = predict_pipeline(payload.text)
        if language != 'English':
            return templates.TemplateResponse(
                "index.html", {"request": request, "language": language, "prediction": "None"}
            )
        else:
            text = payload.text
            prediction = predict_classify([text])
            return templates.TemplateResponse(
                "index.html", {"request": request, "language": language, "prediction": prediction}
            )
    else:
        return templates.TemplateResponse(
            "index.html", 
            {"request": request, "language": "None", "prediction": "None"}, 
            media_type="text/html"
        )


# uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)