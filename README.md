# JMR python recruitment task

JMR python recruitment task is a simple URL shortener written in Django

# Instance running on heroku
>https://safe-mesa-73856.herokuapp.com/
---
# or run Locally

### Clone the source 

```sh
git clone https://github.com/scraber/JMR-python-recruitment-task.git
cd JMR-python-recruitment-task
```


## Using Docker
### Make sure you have installed both docker and docker-compose

1. Install [`docker`](https://docs.docker.com/get-docker/).
2. Install [`docker-compose`](https://docs.docker.com/compose/install/).
3. Create .env file for system variables (replace fields within <> with own values)
```
DEBUG=0
SECRET_KEY=<secret_key>
HASHID_SALT=<hash_salt>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=<postgres>
SQL_USER=<user>
SQL_PASSWORD=<password>
SQL_HOST=db
SQL_PORT=<port>
```
4. Create .env.db file for system variables (replace fields within <> with own values)
```
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db_name>
```


Use docker-compose to build 
```sh
docker-compose -f docker-compose.prod.yml up -d --build  
```
Run initial migrations 
```sh
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
Create Django superuser (which you can use for token auth, later on)
```sh
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

### Run tests
```sh
docker-compose -f docker-compose.prod.yml exec web python manage.py test
```
