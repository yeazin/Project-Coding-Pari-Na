from .base import *


DEBUG = config('DEBUG')
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '*'
    ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS += [
    'structure.accounts.apps.AccountsConfig',
    'structure.codelist.apps.CodelistConfig'
]


AUTH_USER_MODEL = "accounts.User"