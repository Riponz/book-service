FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

ENV PYTHONPATH=/book_service

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . ./user_service

CMD ["uvicorn", "user_service.app.main:app", "--host", "0.0.0.0", "--port", "5000"]