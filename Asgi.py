"""
ASGI config for amachine_learning_based_classification_ddosattacks
It exposes the ASGI callable as a module-level variable named ``application``.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amachine_learning_based_classification_ddosattacks.settings')
application = get_asgi_application()
