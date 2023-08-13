"""
WSGI config for amachine_learning_based_classification_ddosattacks
It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amachine_learning_based_classification_ddosattacks.settings')
application = get_wsgi_application()
