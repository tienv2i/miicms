FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p -v /usr/miicms

WORKDIR /usr/miicms
COPY requirements.txt .

RUN apk update
RUN apk add gcc python3-dev postgresql-dev musl-dev bash vim
RUN apk add jpeg-dev libjpeg zlib-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/bin/bash", "command.sh"]