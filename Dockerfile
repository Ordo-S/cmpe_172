FROM python:3.6-alpine

MAINTAINER Keanu Paesler <kepaesler.github.io>

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /backend

WORKDIR /backend

RUN pip3 install -r requirements.txt

RUN python3 backend/manage.py makemigrations


CMD [ "python3", "backend/manage.py", "runserver", "0.0.0.0:8000" ]