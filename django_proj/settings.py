# -*- coding: utf-8 -*-

#  Copyright (c) 2022 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

"""
    Django settings for the QR-code project.
"""

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    'QRcode',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
]

# templates (django template language) processors
TEMPLATES = [
    {
        'NAME': 'dtl_loader',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',      # permission checking
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_proj.wsgi.application'
ROOT_URLCONF = 'django_proj.urls'
SECRET_KEY = 'dummy'

# end of file
