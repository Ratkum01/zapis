FROM python:3.12.2-alpine3.19

COPY requirements.txt /temp/requirements.txt
COPY zapis /zapis
WORKDIR /zapis
EXPOSE 8001

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user