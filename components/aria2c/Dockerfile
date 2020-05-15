FROM alpine:3

# Defining dockerfile maintainer
MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

ARG BUILD_DATE
ARG VCS_REF

# Installing aria2c
RUN apk update && \
	apk add --no-cache --update bash aria2 && \
    rm -rf /var/cache/apk/*

# Exposing port where the RPC server listens
EXPOSE 6800

# Volume for storing the downloaded data
VOLUME [ "/downloads" ]   

# Changing the current directory to data so that the files get downloaded there
WORKDIR /downloads

# Starting the Aria2c RPC server
CMD ["aria2c", "--enable-rpc=true", "--rpc-listen-all", "--no-conf=true", "--disable-ipv6", "--console-log-level=debug"]

# Labels for dockerfile information
LABEL scorelab.bassa.name="Aria2c RPC server" \
      scorelab.bassa.description="Dockerfile for Aria2c RPC server" \
      scorelab.bassa.url="https://github.com/scorelab/Bassa/wiki" \
      scorelab.bassa.vcs-url="https://github.com/scorelab/Bassa" \
      scorelab.bassa.vcs-ref=$VCS_REF \
      scorelab.bassa.build-date=$BUILD_DATE \
      scorelab.bassa.vendor="Sustainable Computing Research Group" \
      scorelab.bassa.version="1.0" \
      scorelab.bassa.schema-version="1.0"
      

