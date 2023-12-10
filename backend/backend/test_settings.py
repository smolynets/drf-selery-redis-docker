from .settings import *


# DATABASES = {
#     'default': {
#         "ENGINE": "django.db.backends.postgresql",
#         "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
#         "NAME": os.environ.get("POSTGRES_NAME", "postgres"),
#         "USER": os.environ.get("POSTGRES_USER", "test_postgres"),
#         "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "test_postgres"),
#         "PORT": int(os.environ.get("POSTGRES_PORT", "5433")),
#     }
# }

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "test_db",
        "NAME": "test_postgres",
        "USER": "test_postgres",
        "PASSWORD": "test_postgres",
        "PORT": 5432,
    }
}