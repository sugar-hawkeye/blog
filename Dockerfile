FROM hub.c.163.com/library/python:3.6-slim

RUN apt-get update && apt-get install -y \
    gcc \
    gettext \
    mysql-client libmysqlclient-dev \
    sqlite3 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV DJANGO_VERSION 1.11.7
RUN pip install mysqlclient django=="$DJANGO_VERSION"

RUN mkdir -p /django_env
ADD /my_web /django_env
RUN pip install -r /django_env/requirements/dev.txt
