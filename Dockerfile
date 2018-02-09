FROM hub.c.163.com/library/python:3.6

RUN apt-get update && apt-get install -y \
    gcc \
    gettext \
    mysql-client libmysqlclient-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /blog_env
COPY /my_web/ /blog_env
RUN pip install -r /blog_env/requirements/prod.txt
