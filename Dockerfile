FROM python:3.8.1-slim-buster

# Set workdir
WORKDIR /usr/src/app

COPY . /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv
RUN pipenv install --system --deploy
