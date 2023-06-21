FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt && rm /requirements.txt

ADD . /db_py
WORKDIR /db_py

EXPOSE 4003

CMD ["flask", "run", "--host=0.0.0.0", "--port=4003"]
