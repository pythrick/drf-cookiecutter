import os

from split_settings.tools import include
from dotenv import load_dotenv


load_dotenv()
DJANGO_ENV = os.environ.get("DJANGO_ENV")
print(DJANGO_ENV)

if not DJANGO_ENV:
    raise ImportError(
        "Couldn't import Django settings. Are you sure DJANGO_ENV "
        "env var is setup in .env?"
    )

if DJANGO_ENV not in ("development", "local", "production", "staging", "testing"):
    raise ImportError(
        "Couldn't import Django settings. The environment variable DJANGO_ENV "
        "should be one of the following options: development, local, production, "
        "staging, testing"
    )

include(f"{DJANGO_ENV}.py")
