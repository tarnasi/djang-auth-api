FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /authapp

COPY packages.txt /authapp/packages.txt

RUN pip install --upgrade pip
RUN pip install -r packages.txt

COPY . /authapp