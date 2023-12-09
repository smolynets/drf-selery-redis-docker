from .settings import *

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "NAME": os.environ.get("POSTGRES_NAME", "postgres"),
        "USER": os.environ.get("POSTGRES_USER", "test_postgrxfdsfes"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "test_postgres"),
        "PORT": int(os.environ.get("POSTGRES_PORT", "5433")),
    }
}