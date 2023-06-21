FROM python:3.9

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY client_secrets.json /app/client_secrets.json
COPY . .

EXPOSE 4000


CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
