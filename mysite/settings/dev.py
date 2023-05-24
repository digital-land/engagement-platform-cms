from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-cji4yejoi8$*pp*3*f)mdeeb-u8jg%cp!#p(v9cn6*cv=0+^r#"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = INSTALLED_APPS+[
    "debug_toolbar"]

MIDDLEWARE = MIDDLEWARE+[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    
]

INTERNAL_IPS=("127.0.0.1","127.17.0.1")

try:
    from .local import *
except ImportError:
    pass
