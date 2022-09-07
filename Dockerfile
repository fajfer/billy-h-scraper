FROM python:3.9.13-alpine

WORKDIR /app

RUN python3 -m pip install python-telegram-bot requests loguru bs4

COPY . .
CMD ["python3", "main.py"]
