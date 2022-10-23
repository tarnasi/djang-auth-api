#!/bin/sh

python -m pip install -r packages.txt &&
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py runserver 0.0.0.0:8000