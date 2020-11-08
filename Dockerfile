FROM python:3.8.6-slim-buster

RUN apt-get update -qy \
    && apt-get -qy install --no-install-recommends wget \
    && wget -nv -O /tmp/wkhtmltox.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb \
    && apt-get -qy install /tmp/wkhtmltox.deb

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pip install --no-cache pipenv && \
    pipenv install --system --deploy --clear

COPY . .

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
