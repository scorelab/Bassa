FROM ubuntu:18.04 as base

WORKDIR /home/Bassa
COPY . .

RUN apt-get update \
&& apt-get install -y --no-install-recommends python-pip \
&& apt-get install -y --no-install-recommends python-setuptools \
&& pip install pylint && pylint -E .

FROM base

MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

ARG BUILD_DATE
ARG VCS_REF

WORKDIR /home/Bassa
COPY . .

RUN apt-get update \
&& ./setup.sh \
# && python3 setup.py test \ disabing temporary
&& python3 setup.py develop

EXPOSE 5000
CMD [ "./run.sh"]

LABEL multi.org.label-schema.name="Bassa" \
      multi.org.label-schema.description="Bassa provides Automated Download Queue to make the best use of Internet bandwidth" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url="https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref=$VCS_REF \
      multi.org.label-schema.build-date=$BUILD_DATE \
      multi.org.label-schema.vendor="Sustainable Computing Research Group" \
      multi.org.label-schema.version="" \
      multi.org.label-schema.schema-version="1.0"

