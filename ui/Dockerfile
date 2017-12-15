FROM node

MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

WORKDIR /home/Bassa

COPY . .

RUN apt-get update \
&& npm install -g gulp \
&& npm install -g bower \
&& npm install --unsafe-perm

CMD ["gulp", "serve"]

LABEL multi.org.label-schema.name = "Bassa" \
      multi.org.label-schema.description = "Bassa provides Automated Download Queue to make the best use of Internet bandwidth" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url = "https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref = "" \
      multi.org.label-schema.vendor = "Sustainable Computing Research Group" \
      multi.org.label-schema.version = "" \
      multi.org.label-schema.schema-version = "1.0"
