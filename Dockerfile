FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY pip3Requirements.txt /django/
RUN pip3 install -r pip3Requirements.txt
COPY ./django /django/
