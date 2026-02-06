FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install poetry==2.2.1

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN --no-root --no-interaction --no-ansi

COPY . .

CMD ["gunicorn", "megano.wsgi:application", "--bind", "0.0.0.0:8001"]