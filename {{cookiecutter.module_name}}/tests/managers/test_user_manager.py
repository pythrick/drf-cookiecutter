import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user(fake):
    name = fake.name()
    email = fake.email()
    password = fake.password(
        length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    user = User.objects.create_user(name=name, email=email, password=password)

    assert user.name == name, f"The user name should be: {name}."
    assert user.email == email, f"The user email should be: {email}."
    assert user.password is not None, "The password should not be empty."
    assert (
        user.password != password
    ), "The stored password should not be equal to original."
    assert user.check_password(password), "The password should be encripted."


@pytest.mark.django_db
def test_create(fake):
    name = fake.name()
    email = fake.email()
    password = fake.password(
        length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    user = User.objects.create(name=name, email=email, password=password)

    assert user.name == name, f"The user name should be: {name}."
    assert user.email == email, f"The user email should be: {email}."
    assert user.password is not None, "The password should not be empty."
    assert (
        user.password != password
    ), "The stored password should not be equal to original."
    assert user.check_password(password), "The password should be encripted."


@pytest.mark.django_db
def test_create_superuser(fake):
    name = fake.name()
    email = fake.email()
    password = fake.password(
        length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    user = User.objects.create_superuser(name=name, email=email, password=password)

    assert user.is_staff, "The super user shoud be staff."

    assert user.is_active, "The super user shoud be active."

    assert user.is_superuser, "The super user shoud be superuser."
