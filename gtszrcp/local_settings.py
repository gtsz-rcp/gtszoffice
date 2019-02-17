import os
import dj_database_url

DEBUG = True

# DATABASES = {
#     'default': dj_database_url.config(default='postgres://vwohytsdejnxak:6d33d5dfca8c5225a952aa08cb933c54b55d5b65c97c8190e245c03dde706b43@ec2-54-243-239-66.compute-1.amazonaws.com:5432/d128oumgo8gonc'),
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gtszoffice',
        'USER': 'joeaney',
        'PASSWORD': 'joeaney',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ORIGIN_ALLOW_ALL = True