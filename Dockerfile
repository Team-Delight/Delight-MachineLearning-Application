FROM continuumio/anaconda3

WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./flask_app .
