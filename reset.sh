#!/bin/sh

echo "Removing files"
rm -rvf db.sqlite3 cases/migrations
rm -rvf db.sqlite3 jobs/migrations

python manage.py makemigrations jobs
python manage.py makemigrations cases
python manage.py migrate

# populate databases with test data
python manage.py populate_jobs
python manage.py populate_cases
