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
    'rest_framework',
    
    'structure.accounts.apps.AccountsConfig',
    'structure.codelist.apps.CodelistConfig'
]


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

AUTH_USER_MODEL = "accounts.User"