FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django/
RUN pip3 install -r requirements.txt
COPY ./django /django/
WORKDIR /usr/local/bin
COPY ./runTests.sh .
RUN chmod +x runTests.sh
RUN mkdir -p /django/django/lmvpinterface/management/commands
WORKDIR /django/django/lmvpinterface/management/commands
RUN curl https://raw.githubusercontent.com/jbinvnt/static-form-gen/master/genforms.py -o genforms.py # This is a hack until staticforms can be made a PyPi package
