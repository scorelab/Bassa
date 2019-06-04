# Pulling ubuntu bionic as base image
FROM alpine:edge

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
VOLUME [ "/data" ]   

# Changing the current directory to data so that the files get downloaded there
WORKDIR /data

# Starting the Aria2c RPC server
CMD ["aria2c", "--enable-rpc", "--rpc-listen-all"]

# Labels for dockerfile information
LABEL multi.org.label-schema.name="Bassa" \
      multi.org.label-schema.description="Bassa provides Automated Download Queue to make the best use of Internet bandwidth" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url="https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref=$VCS_REF \
      multi.org.label-schema.build-date=$BUILD_DATE \
      multi.org.label-schema.vendor="Sustainable Computing Research Group" \
      multi.org.label-schema.version="" \
      multi.org.label-schema.schema-version="1.0"
      

