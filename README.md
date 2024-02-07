# your-daily-diet
Project for beetroot course

## Docker and PostgreSQL 

## Install Docker and PostgreSQL 
https://scriptable.com/postgresql/how-to-install-postgresql-mac-docker/

## Create a PostgreSQL container
`sopurce *.env`
`docker run --name postgres-container -e POSTGRES_PASSWORD=$PSG_PSW -p 5432:5432 -v postgres-data:/Users/cupcake/workspace/your-daily-diet/psg_data -d postgres`

## Stop time PostgreSQL
`docker stop postgres-container `

## Start next time PostgreSQL
`docker start postgres-container `

## Django app