FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app

RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
