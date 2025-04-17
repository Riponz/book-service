FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

ENV PYTHONPATH=/

ENV SECRET_KEY="bd3bf469v3b2yv90h84u0hv6309813br2ycb3vy3rvb087rg"
ENV ALGORITHM="HS256"
ENV BOOK_API_URL="https://book-service-7p3c.onrender.com/api/v1/books"


RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]