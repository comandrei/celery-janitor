BROKER_URL = ''
CELERY_JANITOR_PREFIX = "celery"
CELERY_JANITOR_LAST_MODIFIED = 3600 * 24 * 14
# Enable overrides from Django/Celery Config

try:
    from celeryconfig import *  # noqa
    from django.settings import *  # noqa
except ImportError:
    pass
