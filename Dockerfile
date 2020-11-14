FROM python:3.8.6-slim-buster

RUN apt-get update -qy && apt-get -qy install --no-install-recommends pngquant build-essential libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pip install --no-cache pipenv && \
    pipenv install --system --deploy --clear

COPY . .

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
