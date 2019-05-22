FROM python:latest

RUN pip3 install flask

COPY . .

EXPOSE 3000

CMD python3 server.py
