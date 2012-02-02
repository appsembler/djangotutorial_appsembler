# NOTE: Copy this file into the /mysite directory.

# extra settings specific to deploying with Stackato
import os

# TODO: make 'settings.py' dynamic so that the user can specify a different settings file to use
from settings import *

STACKATO = 'VCAP_SERVICES' in os.environ

if STACKATO:
    # django_stackato makes it easy to set the superuser password
    EXTRA_INSTALLED_APPS = (
        'django_stackato',
        )

    import json
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])

    try:
        postgres = vcap_services['postgresql-8.4'][0]
        cred = postgres['credentials']
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': cred['name'],                      # Or path to database file if using sqlite3.
                'USER': cred['user'],                      # Not used with sqlite3.
                'PASSWORD': cred['password'],                  # Not used with sqlite3.
                'HOST': cred['hostname'],                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': cred['port'],                      # Set to empty string for default. Not used with sqlite3.
                }
            }

    except KeyError:
        pass

    try:
        mysql = vcap_services['mysql-5.1'][0]
        cred = mysql['credentials']
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': cred['name'],                      # Or path to database file if using sqlite3.
                'USER': cred['user'],                      # Not used with sqlite3.
                'PASSWORD': cred['password'],                  # Not used with sqlite3.
                'HOST': cred['hostname'],                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': cred['port'],                      # Set to empty string for default. Not used with sqlite3.
                }
            }

    except KeyError:
        pass

    try:
        redis = vcap_services['redis-2.2'][0]
        cred = redis['credentials']
        CACHES = {
            'default': {
                'BACKEND': 'redis_cache.RedisCache',
                'LOCATION': '%s:%s' % (cred['hostname'], cred['port']),
                'OPTIONS': {
                    'DB': 1,
                    'PASSWORD': cred['pass'],
                    'PARSER_CLASS': 'redis.connection.HiredisParser'
                },
            },
        }

        EXTRA_INSTALLED_APPS += (
            'redis_cache',
            )

    except KeyError:
        pass
        
    # add any extra apps to the INSTALLED_APPS
    try:
        INSTALLED_APPS = tuple(list(INSTALLED_APPS) + list(EXTRA_INSTALLED_APPS))
    except NameError:
        pass