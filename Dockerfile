FROM python:3.8.1-slim-buster

RUN apt-get update && apt-get upgrade
RUN apt-get -y install wkhtmltopdf

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
