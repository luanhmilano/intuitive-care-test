FROM python:3.10-slim

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sleep", "infinity"]