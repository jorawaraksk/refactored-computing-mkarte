FROM python:3.10-slim-bullseye
WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg mediainfo wget

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD bash start.sh
