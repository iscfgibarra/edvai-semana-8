FROM python:3.8-slim-bullseye

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5000"]