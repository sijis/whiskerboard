import os, sys
sys.path.append(os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.base'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
