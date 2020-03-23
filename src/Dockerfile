FROM python:3

ADD . /src

RUN apt-get update

RUN apt-get -y install libboost-all-dev
RUN apt-get -y install libgmp-dev
RUN apt-get -y install vim
RUN apt-get -y install tmux 
RUN apt-get install stress

RUN pip install --upgrade pip
RUN pip --version

RUN pip install black
RUN pip install requests

ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /src

CMD bash




