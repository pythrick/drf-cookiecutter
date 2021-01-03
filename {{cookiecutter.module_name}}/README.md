# {{cookiecutter.class_name}}
{{cookiecutter.description}}

## Requirements
- Docker
- Docker-compose

## Initial setup
```shell
make init
```

## Run
```shell
make run
```

## Build
```shell
make build
```


## Test
```shell
make test
```

## Create new migrations
```shell
make migrations
```

## Persist migrations
```shell
make migrate
```

## Load fixtures
```shell
make load-fixtures
```

## Custom commands
Start your custom command if the following prefix: `docker-compose run --entrypoint="" web `.
Example:
```shell
docker-compose run --entrypoint="" web python manage.py createsuperuser
```

## Extra commands
There's a chance of something missing here, maybe is a good idea take a look into `Makefile` file.
```shell
cat Makefile
```
Feel free to add new commands in `Makefile` and/or here on `README.md`.
