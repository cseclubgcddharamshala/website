import os
from django.core.wsgi import get_wsgi_application

# Ensure 'core.settings' matches your actual configuration folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()