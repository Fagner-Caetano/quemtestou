# Dockerfile
FROM python:3.10-slim

WORKDIR /main

COPY main.py .

CMD ["python", "main.py"]