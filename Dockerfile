# Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Copy only what we need first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy entrypoint and project code
COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

COPY . .

# (No CMD – we use docker-compose `command:` to choose gunicorn vs celery)
