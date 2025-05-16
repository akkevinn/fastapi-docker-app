# Sentiment Analysis API and Web App

This project provides two implementations for sentiment analysis:
1. A FastAPI-based REST API
2. A Gradio-based web interface

Both implementations use the `distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face's Transformers library to analyze text sentiment.

## Features

- FastAPI endpoint for programmatic sentiment analysis
- Gradio web interface for interactive use
- Docker containerization for easy deployment
- Supports both positive/negative sentiment classification

## Installation

### Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)

### Local Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. Install dependencies:
    ```bash
    pip install torch fastapi transformers uvicorn gradio
    ```

## Usage

### Option 1: FastAPI Server

1. Run the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```

2. Test the API through the interactive web interface:
    - Open `http://localhost:8000/docs` in your browser.
    - Find the `POST /predict` endpoint and click "Try it out".
    - Enter your text in the request body field, for example:
        ```bash
        uvicorn app:app --reload
        ```
    - Click "Execute" to see the sentiment analysis results.

### Option 2: Gradio Web Interface

1. Run the Gradio app:
    ```bash
    python gradio_app.py
    ```

2. Open the provided URL in your browser (typically: `http://localhost:7860`).

## Docker Deployment

Using Docker allows you to run the application without setting up a Python virtual environment or managing dependencies manually.

1. Build the Docker image:
    ```bash
    docker build -t sentiment-analysis .
    ```

2. Run the container:
    ```bash
    docker run -p 8000:8000 sentiment-analysis
    ```
    The FastAPI server will be available at `http://localhost:8000`. This

The FastAPI server will be available at:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## Model Details

The project uses the `distilbert-base-uncased-finetuned-sst-2-english` model, which is a distilled version of BERT fine-tuned for sentiment analysis on the Stanford Sentiment Treebank (SST-2) dataset.

## License
This project is open source under the MIT License.