FROM python:3.8.6-buster
WORKDIR /jmr
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat
COPY requirements.txt /jmr/
RUN pip install -r requirements.txt

# Copy project
COPY . .

ENTRYPOINT ["/jmr/entrypoint.prod.sh"]

