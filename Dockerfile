FROM python:3
MAINTAINER SCoRe Lab Community <commuity@scorelab.org>

RUN apt-get update

RUN mkdir -p /home/Bassa
RUN apt-get install git
RUN git clone https://github.com/scorelab/Bassa.git /home/Bassa
RUN chmod 755 /home/Bassa/setup.sh
RUN /home/Bassa/setup.sh
RUN python components/core/setup.py develop

CMD [ "python", "components/core/Main.py" ]

LABEL multi.org.label-schema.name = "Bassa" \
      multi.org.label-schema.description = "Bassa provides Automated Download Queue for Enterprise to take the best use of Internet bandwidth

" \
      multi.org.label-schema.url="https://github.com/scorelab/Bassa/wiki" \
      multi.org.label-schema.vcs-url = "https://github.com/scorelab/Bassa" \
      multi.org.label-schema.vcs-ref = "" \
      multi.org.label-schema.vendor = "Sustainable Computing Research Group" \
      multi.org.label-schema.version = "" \
      multi.org.label-schema.schema-version = "1.0"
