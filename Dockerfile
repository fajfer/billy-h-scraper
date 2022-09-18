FROM python:3.9.13-alpine

WORKDIR /app

RUN pip install bs4 loguru requests

COPY src ./src

CMD ["python3", "src/main_telegram.py"]
