FROM python:3.8-slim-buster

ADD . /model_py
WORKDIR /model_py

RUN pip3 install -r requirements.txt

EXPOSE 4004

CMD ["flask", "run", "--host=0.0.0.0", "--port=4004"]
