# Django Gateway



Porting the Science Gateway project from Flask to Django.

## Local deployment

```
pip install -r requirements.txt
./reset
python manage.py runserver
```



## Initialisation

The database can be populated using the `reset` shell script. Currently its contents is

```shell
#!/bin/sh

echo "Removing migration history"
rm -rvf db.sqlite3 cases/migrations
rm -rvf db.sqlite3 jobs/migrations

python manage.py makemigrations jobs
python manage.py makemigrations cases
python manage.py migrate

# populate databases with test data
python manage.py populate_jobs
python manage.py populate_cases
```

