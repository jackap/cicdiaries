FROM python:3.13-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    sqlite \
    sqlite-dev \
    curl \
    unzip \
    make

RUN curl -O http://sqlite.org/2016/sqlite-src-3140100.zip && \
    unzip sqlite-src-3140100.zip && \
    gcc -g -fPIC -shared sqlite-src-3140100/ext/misc/json1.c -o json1.so && \
    rm -rf sqlite-src-3140100.zip sqlite-src-3140100

COPY requirements.txt .
COPY app/ /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run"]
