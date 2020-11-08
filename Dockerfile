FROM python:3.8.6-alpine

RUN apk add wkhtmltopdf

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pip install pipenv && \
    pipenv install --system --deploy

COPY . .

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
