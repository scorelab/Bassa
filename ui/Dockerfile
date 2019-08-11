#----------------------- Builder
FROM node:8-alpine as builder

# Setting the current work directory to ui
WORKDIR /ui

# Copying complete ui component in to the container
COPY . .

# Installing node modules
RUN apk update && \
    npm install && \
    npm install --global bower gulp-cli

# Building the ui component to obtain static files.
RUN gulp build

#------------------------------ Production
FROM nginx:alpine as production

MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

ARG BUILD_DATE
ARG VCS_REF

# copy static files
COPY --from=builder /ui/dist/ /usr/share/nginx/html

# Expose ports
EXPOSE 80

# Adding metadata as docker labels
LABEL multi.org.label-schema.name="Bassa" \
      multi.org.label-schema.description="Bassa provides Automated Download Queue to make the best use of Internet bandwidth" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url="https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref=$VCS_REF \
      multi.org.label-schema.build-date=$BUILD_DATE \
      multi.org.label-schema.vendor="Sustainable Computing Research Group" \
      multi.org.label-schema.version="" \
      multi.org.label-schema.schema-version="1.0"
