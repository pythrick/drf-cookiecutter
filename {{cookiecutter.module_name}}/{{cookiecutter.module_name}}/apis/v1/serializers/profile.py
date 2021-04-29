{%- if cookiecutter.rest_framework == "django-rest-framework" -%}
from {{cookiecutter.module_name}}.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "name",
        ]
        read_only_fields = ("email",)
{%- elif cookiecutter.rest_framework == "django-ninja" -%}
from ninja import Schema


class ProfileSchema(Schema):
    email: str
    name: str

{% endif %}