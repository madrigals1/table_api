FROM python:3.8.6-alpine

RUN apk add wkhtmltopdf

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear

COPY . .

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
