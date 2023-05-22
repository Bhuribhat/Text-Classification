import pandas as pd
from pathlib import Path

from tensorflow import keras
from keras.models import load_model
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer

import warnings
warnings.simplefilter("ignore")


# Constants
MAX_WORDS = 3000
EMBEDDING_DIM = 100
MAX_SEQUENCE_LENGTH = 64

# Tokenizer with cleaned data
df = pd.read_csv("../data/Text_Classification_Update.csv")
tokenizer = Tokenizer(num_words=MAX_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
tokenizer.fit_on_texts(df.message.values)

# Load the model
BASE_DIR = Path(__file__).resolve(strict=True).parent
loaded_model = load_model(f"{BASE_DIR}/classify_model.h5")


def decode(score):
    return "Positive" if score > 0.5 else "Negative"


def predict(posts):
    X = tokenizer.texts_to_sequences(posts)
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
    score = loaded_model.predict(X, verbose=0)
    return decode(score)


if __name__ == '__main__':
    text = input("Enter text: ").strip()
    prediction = predict([text])
    print(f"Prediction: {prediction}")