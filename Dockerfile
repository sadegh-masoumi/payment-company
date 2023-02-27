FROM python:3.10

WORKDIR app
COPY ./requirements.txt /app/requirements.txt

RUN "pip install -r requirements.txt"

COPY ./ /app

CMD "python manage.py"
ENTRYPOINT "uvicorn core.asgi:application --bind 0.0.0.0:8000"