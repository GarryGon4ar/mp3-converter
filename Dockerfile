FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /youtubedl
WORKDIR /youtubedl
ADD requirements.txt /youtubedl/
RUN pip install -r requirements.txt
ADD . /youtubedl/
