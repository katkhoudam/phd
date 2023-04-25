# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 16:22:28
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-25 01:55:57
"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

