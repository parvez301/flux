# FastAPI + SQLModel + Alembic

## Steps to run the project
```
python3.11 -m venv <venv name>
docker-compose up --build
```

##
```
http://localhost:8004/songs
```

## Postgres Commands which will be handly
```
docker-compose exec db psql --username=postgres --dbname=foo
\dt 
select * from song;
```

## Steps to insert record in db
```
curl -d '{"name":"Midnight Fit", "artist":"Mogwai", "year":"2021"}' -H "Content-Type: application/json" -X POST http://localhost:8004/songs
```

## Steps to create migration file
```
To create a new migration:
1. docker-compose exec web alembic revision --autogenerate -m "<migration name>"

To apply migration
2. Update the upgrade and downgrade functions from the auto generated migration, it migrates 
``

