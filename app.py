from fastapi import FastAPI
from transformers import pipeline

# Initialize FastAPI and model
app = FastAPI()
model = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")


@app.post("/predict")
def predict(text: str):
    """Endpoint to predict sentiment from text."""
    return model(text)
