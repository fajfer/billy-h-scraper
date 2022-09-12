FROM python:3.9.13-alpine

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY main.py .
CMD ["python3", "main.py"]
