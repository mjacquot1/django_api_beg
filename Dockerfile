FROM python:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN if [ ! -d "django_api_one" ]; then django-admin startproject django_api_one; fi
COPY . .
# WORKDIR /app