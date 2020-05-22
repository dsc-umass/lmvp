FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/local/bin
COPY ./runTests.sh .
RUN chmod +x runTests.sh
WORKDIR /django
ADD django /django
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN mkdir -p lmvpinterface/management/commands
WORKDIR lmvpinterface/management/commands
RUN curl https://raw.githubusercontent.com/jbinvnt/static-form-gen/master/genforms.py -o genforms.py
# The above is a hack until staticforms can be made a PyPi package
WORKDIR /django
# The above makes it convenient to run manage.py commands after container start
