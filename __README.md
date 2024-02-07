# your-daily-diet
Project for beetroot course

# Steps 

## Installs

### Prepare and activate environment 
- create virtual env `python -m venv path-to-work-dir/your-daily-diet/venv`
- activate virtual env `source venv/bin/activate`

### Install Docker and PostgreSQL
- install docker 
- lunch docker and login


- Install postgres image [ https://scriptable.com/postgresql/how-to-install-postgresql-mac-docker/ ] 
  - Run `docker pull postgres` 
  - verify with `docker images` 
  - volume `docker volume create postgres-data`
  - verify `docker volume ls`

- install module to get Python to operate with Postgres. `pip install psycopg2-binary` 


### Installs (with requirements.txt)
- `pip install requirements.txt`

### Installs (from scratch)
- Install Django `pip install django`
- Save into requirements each time `pip freeze > requirements.txt`
- ...check postgre install
- create an app
- `django-admin startproject yourDailyDiet` 
- `cd yourDailyDiet`
- `python manage.py startapp ydd_db`


## Start

- save password and container name in *.env file:
```
PSG_PSW=<psw>
POSTGRES_CONTAINER_NAME=<name>
```

- `source *.env`
- `docker run --name $PSG_CONTAINER_NAME -e POSTGRES_PASSWORD=$PSG_PSW -p 5432:5432 -v postgres-data:$PSG_DATA_DIR -d postgres`
## Start docker
- create a PostgreSQL container `docker run --name <POSTGRES_CONTAINER_NAME> -e POSTGRES_PASSWORD=<PSG_PSW> -p 5432:5432 -v postgres-data:<path_to_db> -d postgres`

## Make migration and migrate db 
- create `python manage.py makemigrations`
- migrate `python manage.py migrate`


