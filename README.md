
# Django Authentication Rest API
Working on django authentication with docker features. I used custom django user model with custom user manager.


## Table of content

 - [Packages Installed](#packages)
 - [APIs](#apis)
 - [Docker](#docker)


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