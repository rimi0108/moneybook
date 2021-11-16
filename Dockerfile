FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN apt-get -y install vim
RUN mkdir /srv/code

# WORKDIR /srv/code
ADD requirements.txt . 
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . /code
WORKDIR /code

EXPOSE 8000