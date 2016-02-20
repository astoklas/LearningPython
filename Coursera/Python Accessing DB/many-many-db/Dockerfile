# Pull base image.
FROM ubuntu:14.04
MAINTAINER astoklas

# Ignore APT warnings about not having a TTY
ENV DEBIAN_FRONTEND noninteractive

# install base system running sqlite
RUN \
  apt-get update && \
  apt-get -y install \
  build-essential \
  curl \
  nano \
  sqlite3\
  libsqlite3-dev 

VOLUME ["/data"]

WORKDIR /data

CMD ["bash"]
