from django.apps import AppConfig as DjangoConfig


class AppConfig(DjangoConfig):
    name = "{{cookiecutter.module_name}}"
    verbose_name = "{{cookiecutter.class_name}}"
