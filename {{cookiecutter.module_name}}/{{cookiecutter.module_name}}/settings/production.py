import decouple
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from split_settings.tools import include

from .base import config

include("base.py")

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=decouple.Csv())

sentry_sdk.init(
    dsn=config("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    environment=config("SENTRY_ENVIRONMENT"),
    release=config("SENTRY_RELEASE"),
    send_default_pii=True,
)
