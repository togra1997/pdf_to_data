FROM python:slim-bullseye
USER root


RUN apt update 
RUN apt -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
COPY ./requires.txt /

RUN apt -y update && apt -y upgrade && apt -y install libopencv-dev libgtk2.0-dev pkg-config

RUN pip install --upgrade pip && pip install -r requires.txt

# https://qiita.com/tik26/items/a75e03e523926cd2f059

# # RUN poetry new project
# WORKDIR project
# RUN poetry install
# Poetryが仮想環境を生成しないようにする
# RUN poetry config virtualenvs.create false
# WORKDIR /workdir
# VOLUME /var/test