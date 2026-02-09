FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV BACKEND_URL=http://backend-service:8000

CMD ["python", "app.py"]
