from .development import *

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.sqlite3',
    },
}

TEST_OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'test_output')

LOGGING['loggers']['django']['handlers'] = ['file']
LOGGING['loggers']['accounts']['handlers'] = ['file']
LOGGING['loggers']['dwfcommon']['handlers'] = ['file']
LOGGING['loggers']['dwfjob']['handlers'] = ['file']
LOGGING['loggers']['dwfsearch']['handlers'] = ['file']
