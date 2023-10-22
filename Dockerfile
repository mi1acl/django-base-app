FROM python:3.12

# Environment Vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/code

COPY Pipfile Pipfile.lock /opt/code/
RUN pip install pipenv && pipenv install --system

COPY . /opt/code/
