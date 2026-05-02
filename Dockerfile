FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py diagnostics.py config.json ./

EXPOSE 8080

CMD ["python", "app.py"]
