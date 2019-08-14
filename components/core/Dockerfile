# Container as boiler plate
FROM python:3.7-slim as base 

# Setting current work directory to /bassa
WORKDIR /bassa

# Copying API component
COPY . .

# Installing dependencies
RUN apt-get update && \ 
    apt-get install -y --no-install-recommends \ 
    python3-pip \ 
    build-essential \
    default-libmysqlclient-dev \ 
    python3-dev \
    python3-setuptools && \ 
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Installing the python modules
RUN python3 setup.py develop

# -----------------------------

# Container to lint python code
FROM base as linter 

# Setting current work directory to /Bassa
WORKDIR /bassa

# Installing pylint and linting the python code
RUN pip install pylint && pylint -E *.py **/*.py || printf "\n Bassa has got some errors! Continuing the build for now\n\n"

# -----------------------------

# Container for running the Bassa API server
FROM base as production

MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

ARG BUILD_DATE
ARG VCS_REF

# Volume for accessing the downloaded files
VOLUME [ "/downloads" ]

# Setting current work directory to /Bassa
WORKDIR /bassa

# Exposing ports where the server listens 
EXPOSE 5000

# Start the Bassa API server
CMD [ "python3", "Main.py" ]

# Adding data as docker labels
LABEL scorelab.bassa.name="Bassa API development server" \
      scorelab.bassa.description="Dockerfile for Bassa API flask-socketio server" \
      scorelab.bassa.url="https://github.com/scorelab/Bassa/wiki" \
      scorelab.bassa.vcs-url="https://github.com/scorelab/Bassa" \
      scorelab.bassa.vcs-ref=$VCS_REF \
      scorelab.bassa.build-date=$BUILD_DATE \
      scorelab.bassa.vendor="Sustainable Computing Research Group" \
      scorelab.bassa.version="1.0" \
      scorelab.bassa.schema-version="1.0"