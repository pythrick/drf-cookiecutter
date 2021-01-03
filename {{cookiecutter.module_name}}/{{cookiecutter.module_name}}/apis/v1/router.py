# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views.profile import profile_me_view

router = routers.DefaultRouter()

urlpatterns = [
    path("auth/sign-in/", TokenObtainPairView.as_view(), name="jwt-obtain"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path("profile/me/", profile_me_view),
]

urlpatterns += router.urls
