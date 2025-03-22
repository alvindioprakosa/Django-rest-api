"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Tambahkan logging untuk membantu debugging jika terjadi error
logger = logging.getLogger(__name__)

try:
    # Pastikan variabel environment sudah di-set
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE", "mysite.settings"))
    application = get_wsgi_application()
except Exception as e:
    logger.error("WSGI Application Error: %s", e)
    sys.exit(1)
