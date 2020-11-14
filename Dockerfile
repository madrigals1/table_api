FROM python:3.8.6-slim-buster

RUN apt-get -qy install --no-install-recommends pngquant

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pip install --no-cache pipenv && \
    pipenv install --system --deploy --clear

COPY . .

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
