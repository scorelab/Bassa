FROM python:latest
ADD . /code
WORKDIR /code
RUN \
    ./setup.sh \
    cd core 
CMD python setup.py develop