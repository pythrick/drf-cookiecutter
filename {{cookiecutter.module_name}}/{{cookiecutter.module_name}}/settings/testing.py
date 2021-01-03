from split_settings.tools import include

from .base import INSTALLED_APPS

include("base.py")

INSTALLED_APPS += [
    "django_extensions",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:",}}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
