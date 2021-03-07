FROM python:3.8.6-buster
WORKDIR /jmr
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /jmr/
RUN pip install -r requirements.txt
COPY . /jmr/
