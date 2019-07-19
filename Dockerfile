FROM ubuntu:latest
LABEL maintainer="K@M@L"
RUN apt-get update
RUN apt-get install python-pip python3 -y
RUN pip install requests
ADD ./getMacInfo.py /root
USER root
WORKDIR /root
CMD ["/bin/bash"]
