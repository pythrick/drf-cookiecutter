import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from split_settings.tools import include

from .base import INSTALLED_APPS, config

include("base.py")

INSTALLED_APPS += [
    "django_extensions",
]

sentry_sdk.init(
    dsn=config("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    environment=config("SENTRY_ENVIRONMENT"),
    release=config("SENTRY_RELEASE"),
    send_default_pii=True,
)
