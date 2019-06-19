# Container to lint python code
FROM python:3.7-slim as linter 

# Setting current work directory to /home/Bassa
WORKDIR /linter

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


# Installing pylint and linting the python code
RUN pip install pylint && pylint -E . 

# -----------------------------

# Container for running the Bassa API server
FROM python:3.7-slim as production

MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

ARG BUILD_DATE
ARG VCS_REF

# Volume for accessing the downloaded files
VOLUME [ "/downloads" ]

# Setting current work directory to /home/Bassa
WORKDIR /API

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

# Exposing ports where the server listens 
EXPOSE 5000

# Start the Bassa API server
CMD [ "python3", "Main.py" ]

# Adding data as docker labels
LABEL multi.org.label-schema.name="Bassa" \
      multi.org.label-schema.description="Bassa provides Automated Download Queue to make the best use of Internet bandwidth" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url="https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref=$VCS_REF \
      multi.org.label-schema.build-date=$BUILD_DATE \
      multi.org.label-schema.vendor="Sustainable Computing Research Group" \
      multi.org.label-schema.version="" \
      multi.org.label-schema.schema-version="1.0"