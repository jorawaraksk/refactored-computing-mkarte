FROM python:3.10.8-slim-buster
WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg mediainfo wget

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD bash start.sh
