from tensorflow.keras.models import load_model
from pathlib import Path

import warnings
warnings.simplefilter("ignore")

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load the model
loaded_model = load_model(f"{BASE_DIR}/classify_model.h5")


if __name__ == '__main__':
    text = input("Enter text: ").strip()
    prediction = loaded_model.predict([text])
    print(f"Prediction: {prediction[0]}")