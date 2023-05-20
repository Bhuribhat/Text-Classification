import re
import pickle
from pathlib import Path

import warnings
warnings.simplefilter("ignore")

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Static Classes
classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]


# Load Model
with open(f"{BASE_DIR}/detection_model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]


if __name__ == '__main__':
    text = input("Enter text: ").strip()
    detect = predict_pipeline(text)
    print(f"Prediction: {detect}")