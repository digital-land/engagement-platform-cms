from .base import *

DEBUG = False

SECRET_KEY = "get from environment"

ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
