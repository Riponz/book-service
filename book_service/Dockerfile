FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

ENV PYTHONPATH=/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]