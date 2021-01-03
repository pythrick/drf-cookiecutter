FROM python:{{cookiecutter.python_version}} as backend

ARG DJANGO_ENV

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 \
  DJANGO_ENV=${DJANGO_ENV} \  
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \  
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \  
  POETRY_VERSION={{cookiecutter.poetry_version}} \
  POETRY_VIRTUALENVS_CREATE=false

RUN apt update && apt install -y \
  curl \
  libffi-dev \
  openssl \
  musl-dev \
  && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION"

WORKDIR /pysetup
COPY ./pyproject.toml ./poetry.lock*  /pysetup/
RUN echo $DJANGO_ENV
RUN poetry install $(test "$DJANGO_ENV" = production && echo "--no-dev") --no-interaction --no-ansi

WORKDIR /app
COPY . /app

RUN chmod +x /app/entrypoint/entrypoint.sh
#RUN mv .env.build .env
RUN python /app/manage.py collectstatic --no-input
ENTRYPOINT ["/app/entrypoint/entrypoint.sh"]
