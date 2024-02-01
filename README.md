# your-daily-diet
Project for beetroot course

# Steps 

## Prepare and activate environment 
- create virtual env `python -m venv path-to-work-dir/your-daily-diet/venv`
- activate virtual env `source venv/bin/activate`

## Install Docker and PostgreSQL
- install docker 
- lunch docker and login
- Install postgres image [https://scriptable.com/postgresql/how-to-install-postgresql-mac-docker/] 
  - Run `docker pull postgres` 
  - verify with `docker images` 
  - volume `docker volume create postgres-data`
  - verify `docker volume ls`
  - create a PostgreSQL container `docker run --name postgres-container -e POSTGRES_PASSWORD=<password> -p 5432:5432 -v postgres-data:/var/lib/postgresql/data -d postgres`

- install module to get Python to operate with Postgres. `pip install psycopg2-binary` 


## Installs (with requirements.txt)
- `pip install requirements.txt`

## Installs (from scratch)
- Install Django `pip install django`
- Save into requirements each time `pip freeze > requirements.txt`
- ...check postgre install
- `django-admin startproject yourDailyDiet` 
- `cd yourDailyDiet`
- `python manage.py startapp ydd_db`

