FROM python:3.9-slim
WORKDIR /app
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
COPY . .
RUN pip install fastapi transformers uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]