FROM python:3.6.7-slim

ADD ./feature_request /feature_request
WORKDIR /feature_request

RUN pip install -r requirements.txt

CMD ["python", "feature_request.py", "docker"]
