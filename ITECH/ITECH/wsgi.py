"""
WSGI config for ITECH project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
project_path = "/home/Sennori/yourproject"
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITECH.settings')

application = get_wsgi_application()
