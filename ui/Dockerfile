FROM nginx:alpine

MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

ARG BUILD_DATE
ARG VCS_REF

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY dist /var/www/bassa

LABEL multi.org.label-schema.name="Bassa" \
      multi.org.label-schema.description="Bassa provides Automated Download Queue to make the best use of Internet bandwidth" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url="https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref=$VCS_REF \
      multi.org.label-schema.build-date=$BUILD_DATE \
      multi.org.label-schema.vendor="Sustainable Computing Research Group" \
      multi.org.label-schema.version="" \
      multi.org.label-schema.schema-version="1.0"
