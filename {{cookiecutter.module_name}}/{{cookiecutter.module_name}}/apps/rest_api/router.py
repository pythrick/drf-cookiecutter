# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import MeProfileView

router = routers.DefaultRouter()

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("me", MeProfileView.as_view()),
]

urlpatterns += router.urls
