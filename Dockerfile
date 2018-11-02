FROM python:3.6-alpine3.6
MAINTAINER Agung Wiyono <wiyonoagung1@gmail.com>

ENV INSTALL_PATH /web_app
run mkdir -p $INSTALL_PATH

workdir $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

gunicorn -b 0.0.0.0:8000 --access-logfile - "web_app.app:create_app()"
