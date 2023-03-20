import os

from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Use the default Django settings module
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover task modules in all registered Django apps
app.autodiscover_tasks()
