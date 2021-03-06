#! /usr/bin/python
"""
WSGI config for mysitelogin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
#root = os.path.dirname(__file__)


new_path = os.path.abspath('/usr/local/python27/lib/python2.7/site-packages')  


sys.path.insert(0, new_path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
