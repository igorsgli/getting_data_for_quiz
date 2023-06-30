FROM python:3.9-slim

WORKDIR /quiz_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /quiz_app/docker/*.sh
