FROM ubuntu:22.04
WORKDIR /root

RUN mkdir -p .pip && mkdir -p server \
    && sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get update -y\
    && apt-get upgrade -y \
    && apt-get install python3 python3-pip zip g++  libtesseract-dev vim make automake autoconf libtool curl -y\
    && apt-get install pkg-config libicu-dev libleptonica-dev libpango1.0-dev libarchive-tools libcairo2-dev -y\
    && curl https://codeload.github.com/tesseract-ocr/tesseract/zip/refs/heads/main -o tesseract-main.zip \
    && unzip tesseract-main.zip && cd tesseract-main && ./autogen.sh && ./configure --prefix=$HOME/tesseract/ \
    && make install && make training && make training-install