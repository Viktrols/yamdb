FROM python:3.9-alpine

WORKDIR /code
COPY requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
COPY . .

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
