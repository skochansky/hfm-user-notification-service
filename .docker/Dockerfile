FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR usr/src/app

COPY pyproject.toml usr/src/app

COPY poetry.lock usr/src/app

RUN pip3 install poetry

RUN poetry install

COPY . usr/src/app

RUN chmod +x .docker/entrypoint.sh

ENTRYPOINT [".docker/entrypoint.sh"]
