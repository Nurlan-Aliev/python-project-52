FROM python:3

RUN pip install poetry

COPY . /task_manager

WORKDIR /task_manager

RUN poetry config virtualenvs.create false && poetry shell

RUN poetry install