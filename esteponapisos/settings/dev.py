# esteponapisos/settings/development.py
from .base import *

INSTALLED_APPS += [
    #'debug_toolbar',
]

MIDDLEWARE += [
    # ...
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
