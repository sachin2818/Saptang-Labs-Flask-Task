FROM python:3.9-slim

WORKDIR /service

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["waitress-serve", "--port", "5000", "--call", "app.main:create_app"]
