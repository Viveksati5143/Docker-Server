FROM python:3.9-slim
# Do try with alphine image
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask
# Add apk update command
EXPOSE 8080

CMD ["python", "app.py"] 
#python3