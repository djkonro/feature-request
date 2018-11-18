FROM python:3.6.7-slim

ADD ./feature_request /feature_request
WORKDIR /feature_request
COPY ./wait-for-it/wait-for-it.sh wait-for-it.sh

RUN pip install -r requirements.txt
