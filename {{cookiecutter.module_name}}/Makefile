SHELL := /bin/bash
.PHONY: all test init build run down superuser clean clean-migrations migrations migrate load-fixtures clean-db reset-db 

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: all test init build run down superuser clean clean-migrations migrations migrate load-fixtures clean-db reset-db

test:
	docker-compose run web pytest

init:
	cp .env.template .env
	docker-compose build
	docker-compose run web pre-commit install -t pre-commit
	docker-compose run web pre-commit install -t pre-push

format:
	docker-compose run web isort .
	docker-compose run web black .

build:
	docker-compose build

run:
	docker-compose up

down:
	docker-compose down

lock:
	docker-compose run web poetry lock

superuser:
	docker-compose run web python manage.py createsuperuser

clean:
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;

clean-migrations:
	@find ./who_fixes_api -name '00*_*.py' -exec rm -rf {} \;


migrations:
	docker-compose run web python manage.py makemigrations
	
migrate:
	docker-compose run web python manage.py migrate

load-fixtures:
	docker-compose run web python manage.py loaddata fixtures/development/*.json

clean-db: 
	docker-compose run web python manage.py reset_db --close-sessions --noinput

reset-db: clean-db clean-migrations migrations migrate load-fixtures
