import os
from .base import *

DEBUG = False
SECRET_KEY = ')yk2vl4wzw73%80&l%9%@vaqp^xmgh-ahe&x$te_te8=#nl3%+'
ALLOWED_HOSTS = ['localhost', 'rocketman.silentdesigns.co.nz', '*']

cwd = os.getcwd()
CACHES = {
    'default': {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache",
    }
}

DATABASES = [
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "rocketman",
        "USER": "rocketman",
        "PASSWORD": "arlo678!",
        "HOST": "localhost",
        "PORT": "",
    }
]

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://9d1995ff7a1843be801428badc1e6fea@o1123625.ingest.sentry.io/6161785",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
