{%- if cookiecutter.rest_framework == "django-rest-framework" -%}
import pytest
from {{cookiecutter.module_name}}.apis.v1.serializers.profile import ProfileSerializer


@pytest.mark.django_db
def test_serialize_profile(user):
    serializer = ProfileSerializer(user)
    assert serializer.data == {
        "name": user.name,
        "email": user.email
    }
{%- elif cookiecutter.rest_framework == "django-ninja" -%}
import pytest
from {{cookiecutter.module_name}}.apis.v1.serializers.profile import ProfileSchema


@pytest.mark.django_db
def test_serialize_profile(user):
    schema = ProfileSchema.from_orm(user)
    assert schema.to_dict() == {
        "name": user.name,
        "email": user.email
    }
{%endif%}