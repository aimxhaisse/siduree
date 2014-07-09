FROM ubuntu:saucy
MAINTAINER s. rannou <mxs@sbrk.org>

RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y python python-pip libjpeg-dev python-dev libjpeg8-dev libpng3 libfreetype6-dev libjpeg-dev nginx
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
RUN ln -s ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
RUN pip install Flask Flask-SQLAlchemy Flask-WTF Flask-login PIL gunicorn

RUN groupadd siduree
RUN useradd -m siduree -g siduree
USER siduree

ADD . /code
WORKDIR /code
CMD gunicorn -w 5 -b :5000 app:app
