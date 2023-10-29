from .base import *
from os import getenv
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-swl0#bcqlxu_3!ejicxe*=b_s)2d(lunu60p49y3qj4h6pb^*1"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "*").split(",")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
