# your-daily-diet
Project for beetroot course

## Docker and PostgreSQL 

### Install Docker and PostgreSQL 
https://scriptable.com/postgresql/how-to-install-postgresql-mac-docker/

### Create a PostgreSQL container
`sopurce *.env`
`docker run --name postgres-container -e POSTGRES_PASSWORD=$PSG_PSW -p 5432:5432 -v postgres-data:/Users/cupcake/workspace/your-daily-diet/psg_data -d postgres`

### Stop time PostgreSQL
`docker stop postgres-container `

### Start next time PostgreSQL
`docker start postgres-container `

### DB  
`psql -h 127.0.0.1 -p 5432 --username postgres --password postgres`
>> sql
`create database ydd_db;`

## Django app

### Create a Django app
`django-admin startproject yourDailyDiet`

### Creds
`python manage.py runserver --settings=settings.local`

### Create https certificate
https://timonweb.com/django/https-django-development-server-ssl-certificate/