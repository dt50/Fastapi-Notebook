# Fastapi-Notebook


## Quick start

First, you need to download the project from [github](https://github.com/dt50/Fastapi-Notebook) and 
bootstrap your environment.

```shell script
git clone https://github.com/dt50/Fastapi-Notebook
cd Fastapi-Notebook
poetry install
poetry shell
```

In ``app/core/config`` you need to change to your database url. 

Template url - `postgres://username:password@host:port/db`

After then you can up your uvicorn server with command 

```shell script
uvicorn app.main:app --reload
```


## Start with docker

To start with docker you need to run command 

```shell script
git clone https://github.com/dt50/Fastapi-Notebook
cd Fastapi-Notebook
poetry install
poetry export --without-hashes -f requirements.txt | sed 's/-e //' > requirements.txt
docker-compose up --build
```


## Api URLS:

All routes available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


## What's Included?
* [PostgreSQL](http://www.postgresql.org/)
* [pgcrypto](https://www.postgresql.org/docs/8.3/pgcrypto.html)
* [FastAPI](https://github.com/tiangolo/fastapi)
* [asyncpg](https://github.com/MagicStack/asyncpg)
* [aiosql](https://github.com/nackjicholson/aiosql)


## Project structure 
Files related to application are in the app. Application parts are:
```
app
├── api
│   ├── dependencies
│   ├── errors
│   └── routes
├── core
├── db
│   ├── migrations
│   ├── queries
│   └── repositories
└── models
    └── schemas
```