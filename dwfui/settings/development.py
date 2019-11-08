from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_FROM = 'ssaleheen@swin.edu.au'
EMAIL_HOST = 'mail.swin.edu.au'
EMAIL_PORT = 25

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dwf',
        'USER': 'root',
        'PASSWORD': 'your password',
    },
}

# development version should have blank keys
RECAPTCHA_PUBLIC_KEY = '6LfYRLkUAAAAAGQEz8EcQ8s0uTEaMMbQOxJlGigS'
RECAPTCHA_PRIVATE_KEY = '6LfYRLkUAAAAAOLLXu3bXg5SPfucRDuS1efFrUL2'

RECAPTCHA_REQUIRED_SCORE = 0.85

for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console', 'file']

try:
    from .local import *
except ImportError:
    pass
