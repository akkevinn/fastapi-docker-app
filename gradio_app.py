from transformers import pipeline
import gradio as gr

# Initialize model
model = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")


def predict(text: str):
    """Endpoint to predict sentiment from text."""
    result = model(text)
    return {result[0]["label"]: result[0]["score"]}


# Create Gradio app
gradio_app = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Label(label="Sentiment"),
    title="Sentiment Analysis",
    description="Type a sentence to analyze its sentiment."
).launch()
