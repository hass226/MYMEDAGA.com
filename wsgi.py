"""
WSGI config wrapper for Render deployment.
Handles the nested Django structure by adjusting the Python path.
"""

import os
import sys
import django

# Get the paths
project_root = os.path.dirname(__file__)
django_project_dir = os.path.join(project_root, 'moncv')

# Add the django project directory to sys.path so imports work correctly
sys.path.insert(0, django_project_dir)

# Set up Django settings module (this refers to moncv/moncv/settings_railway.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moncv.settings_railway')

# Setup Django
django.setup()

# Import the WSGI application from the nested moncv/moncv/wsgi.py
from moncv.wsgi import application

__all__ = ['application']
