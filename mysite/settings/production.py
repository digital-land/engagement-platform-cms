from .base import *
import os

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
