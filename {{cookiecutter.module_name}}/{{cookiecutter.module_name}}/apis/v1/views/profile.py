{%- if cookiecutter.rest_framework == "django-rest-framework" -%}
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers.profile import ProfileSerializer


@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated])
def profile_me_view(request: Request) -> Response:
    if request.method == "GET":
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PATCH":
        serializer = ProfileSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
{%- elif cookiecutter.rest_framework == "django-ninja" -%}
from ninja import Router
from ninja.security import django_auth
from ..serializers.profile import ProfileSchema


router = Router()


@router.get("/", response=ProfileSchema, auth=django_auth)
def get_profile_me(request):
    return request.auth


{% endif %}