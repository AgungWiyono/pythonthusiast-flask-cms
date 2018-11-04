FROM python:3.6-slim
MAINTAINER Agung Wiyono <wiyonoagung1@gmail.com>

RUN apt-get update && apt-get install -qq -y \
build-essential libpq-dev --no-install-recommends

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "main:app"
