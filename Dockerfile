FROM python:3.10-slim
WORKDIR /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
COPY requirements.txt .
RUN pip install --upgrade --no-cache-dir -r requirements.txt
ENV HOST=0.0.0.0 \
    PORT=8000 \
    WORKERS=4 \
    OUTPUT_MODEL_PATH="/mnt/association_rules.pkl"
EXPOSE ${PORT}
COPY app.py .
