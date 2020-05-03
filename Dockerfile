FROM ubuntu:18.04

RUN apt-get update && apt-get -y install python3.7 python3-pip

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"

WORKDIR /climbing_stats

ADD requirements.txt /climbing_stats

RUN pip3 install -r requirements.txt

COPY . /climbing_stats


CMD ["make", "backend-dev"]