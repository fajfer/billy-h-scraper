FROM python:3.9.13-alpine

WORKDIR /app

RUN pip install python-telegram-bot requests loguru bs4

COPY main.py .
CMD ["python3", "main.py"]
