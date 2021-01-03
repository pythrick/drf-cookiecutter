import pytest
from rest_framework import status


@pytest.mark.django_db
def test_unauthorized_request_on_route_me(api_client):
    response = api_client.get("/api/v1/profile/me/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


@pytest.mark.django_db
def test_authorized_request(api_client_with_credentials):
    response = api_client_with_credentials.get("/api/v1/profile/me/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_authorized_patch_on_route_me(api_client_with_credentials, fake):
    response = api_client_with_credentials.patch(
        "/api/v1/profile/me/", data={"name": fake.name()}
    )
    assert response.status_code == status.HTTP_200_OK
