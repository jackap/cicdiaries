FROM python:3.6

WORKDIR /app
RUN pip install flask
RUN pip install requests
RUN pip install -U flask-cors
CMD ["flask" ,"run"]
