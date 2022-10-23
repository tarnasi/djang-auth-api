
# Django Authentication Rest API
Working on django authentication with docker features. I used custom django user model with custom user manager.


## Table of content

 - [Packages Installed](#packages)
 - [APIs](#apis)
 - [Docker](#docker)
 - [Run Project](#get_start)
 - [LICENSE](#LICENSE)


<h2 id="packages">Packages Installed</h2>

- Django==4.1.2
- django-cors-headers==3.13.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2

<h2 id="apis">APIs</h2>

This api login user with email and password credential and return access token and
refresh token with custom claim (is_admin, is_activate).

```http request
HTTP POST http://localhost:8001/api/v1/login
```

This api get the refresh to generate new access_token.

```http request
HTTP POST http://localhost:8001/api/v1/token/refresh/
```


<h2 id="docker">Docker</h2>

```dockerfile
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /authapp

COPY packages.txt /authapp/packages.txt

RUN pip install --upgrade pip
RUN pip install -r packages.txt

COPY . /authapp
```

```dockerfile
version: "3.10"

services:
    authapp:
        build:
            context: .
            dockerfile: ./Dockerfile
        container_name: authapp
        volumes:
            - .:/authapp
        ports:
            - "8001:8000"
        entrypoint: ['sh', 'run_project.sh']
```

<h2 id="get_start">Get Starting</h2>

First of all need install docker and docker-compose from link below.

[Install Docker Engine](https://docs.docker.com/engine/install/)
****

We are need to change directory to apiauth folder

### Run project with docker
```commandline
cd apiauth
docker-compose up -d
```

-d flag represent to detach to background processor and exist from terminal so we can use for farther action.
Notice: if you want to see the logs of the project you can use below command

```commandline
docker-compose logs -f 
```
-f represent to follow the logs and stay in terminal (live-reload)
****
```http request
live in http://localhost:8001
endpoint api/v1
```

### Run project manually

Install python on your system
[Python Website]()

add new virtualenv in apiauth folder
```commandline
python -m venv .venv
```

active the virtualenv

```commandline
cd apiauth
widnows: .\.venv\Scripts\activate
linux and mac: source .venv/bin/activate
```

install the packages
```commandline
pip install -r packages.txt
```

migrate the Migrations
```commandline
python manage.py migrate
```

run the server
```commandline
python manage.py runserver 0.0.0.0:8001 or any port you like :)
```

<h2 id="LICENSE">LICENSE</h2>

- GNU GENERAL PUBLIC LICENSE