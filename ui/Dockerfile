#----------------------- Builder
FROM node:7 as builder

# Setting the current work directory to ui
WORKDIR /ui

# Copying complete ui component in to the container
COPY . .

# Installing node modules and bower modules
RUN apt-get update && \ 
    npm install && \
    npm install --global bower gulp-cli && \
    bower --allow-root install
    
    

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
LABEL scorelab.bassa.name="Bassa Web production server" \
      scorelab.bassa.description="Dockerfile for Bassa Web Nginx server" \
      scorelab.bassa.url="https://github.com/scorelab/Bassa/wiki" \
      scorelab.bassa.vcs-url="https://github.com/scorelab/Bassa" \
      scorelab.bassa.vcs-ref=$VCS_REF \
      scorelab.bassa.build-date=$BUILD_DATE \
      scorelab.bassa.vendor="Sustainable Computing Research Group" \
      scorelab.bassa.version="1.0" \
      scorelab.bassa.schema-version="1.0"
