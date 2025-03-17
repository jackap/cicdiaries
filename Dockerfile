FROM python:3.12

WORKDIR /app
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN curl -O  http://sqlite.org/2016/sqlite-src-3140100.zip 
RUN unzip sqlite-src-3140100.zip
RUN gcc -g -fPIC -shared sqlite-src-3140100/ext/misc/json1.c -o json1.so
COPY /app/requirements.txt .
RUN pip install -r requirements.txt
CMD ["flask" ,"run"]
