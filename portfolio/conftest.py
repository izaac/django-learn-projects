import pytest
import os
import portfolio


@pytest.fixture(scope='session')
def django_db_setup():
    portfolio.settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': os.environ.get('PGSQL_USER', 'izaac'),
        'PASSWORD': os.environ.get('PGSQL_PASSWORD', ''),
        'HOST': os.environ.get('PGSQL_HOST', 'localhost'),
        'PORT': os.environ.get('PGSQL_PORT', '5432'),
    }
