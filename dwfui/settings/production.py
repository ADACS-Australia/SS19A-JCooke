from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CONN_MAX_AGE = 900  # 15 minutes of persistent connection

EMAIL_FROM = ''
EMAIL_HOST = 'mail.swin.edu.au'
EMAIL_PORT = 25

STATIC_ROOT = os.path.join(BASE_DIR, '../static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../accounts/static/'),
    os.path.join(BASE_DIR, '../dwfcommon/static/'),
    os.path.join(BASE_DIR, '../dwfjob/static/'),
    os.path.join(BASE_DIR, '../dwfsearch/static/'),
]

ROOT_SUBDIRECTORY_PATH = 'projects/live/dwf/'

LOGIN_REDIRECT_URL = '/' + ROOT_SUBDIRECTORY_PATH
LOGOUT_REDIRECT_URL = '/' + ROOT_SUBDIRECTORY_PATH
LOGIN_URL = '/' + ROOT_SUBDIRECTORY_PATH + 'accounts/login'

STATIC_URL = '/' + ROOT_SUBDIRECTORY_PATH + 'static/'
SITE_URL = 'https://supercomputing.swin.edu.au'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dwf',
        'USER': 'root',
        'PASSWORD': 'your password',
        'ATOMIC_REQUESTS': True,
    },
}

# POSTGRESQL DB CONNECTION CREDENTIALS #
POSTGRES_USER = 'postgres_username'
POSTGRES_PASSWORD = 'postgres_password'
POSTGRES_HOST_NAME = 'postgres_host_name'
POSTGRES_PORT = 5432
POSTGRES_DB_NAME = 'postgres_db_name'

try:
    from .local import *
except ImportError:
    pass
