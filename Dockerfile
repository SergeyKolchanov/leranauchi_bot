FROM python:3.8-slim

WORKDIR /usr/local/bot

ADD deps .
ADD src/* .

RUN pip install -r deps

CMD [ "python", "./run.py" ]
