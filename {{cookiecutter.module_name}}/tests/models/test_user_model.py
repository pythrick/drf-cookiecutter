import uuid

import pytest


@pytest.mark.django_db
def test_user_pk(user):
    assert isinstance(
        user.pk, int
    ), f"The {user.__class__.__name__} pk should be an int field."


@pytest.mark.django_db
def test_user_string(user):
    assert str(user) == user.name


@pytest.mark.django_db
def test_user_repr(user):
    assert repr(user) == f"{user.__class__.__name__}<{user}>"


@pytest.mark.django_db
def test_user_external_id(user):
    assert isinstance(
        user.external_id, uuid.UUID
    ), f"The {user.__class__.__name__} pk should be an UUID field."
