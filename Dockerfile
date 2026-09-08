FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV APP_NAME=python-monitor
ENV ENVIRONMENT=development

CMD ["python", "app.py"]
