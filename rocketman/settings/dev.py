from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o3h$b1e*=^==q8wr&yb^1elvq(p6mgk2o#&4g5k-ebazjyvj89'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend',

try:
    from .local import *
except ImportError:
    pass
