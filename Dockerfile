FROM python:3.8.6-alpine

RUN apk add wkhtmltopdf

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
