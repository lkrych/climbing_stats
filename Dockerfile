FROM ubuntu:18.04

RUN apt-get update && apt-get -y install python3.7 python3-pip

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"

COPY . /climbing_stats

WORKDIR /climbing_stats

RUN pip3 install -r requirements.txt

CMD ["make", "start_dev"]