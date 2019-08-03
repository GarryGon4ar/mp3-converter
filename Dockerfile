FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /youtubedl
WORKDIR /youtubedl
COPY requirements.txt /youtubedl/
RUN pip install -r requirements.txt
COPY . /youtubedl/