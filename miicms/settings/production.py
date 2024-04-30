from .base import *
from os import getenv

DEBUG = False

ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "").split(",")

try:
    from .local import *
except ImportError:
    pass
