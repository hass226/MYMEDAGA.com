"""
WSGI config wrapper for Render deployment.
This wrapper navigates to the moncv/ directory before loading Django.
"""

import os
import sys
import django

# Add the moncv directory to the Python path
moncv_dir = os.path.join(os.path.dirname(__file__), 'moncv')
sys.path.insert(0, moncv_dir)

# Change to moncv directory so Django can find apps and settings
os.chdir(moncv_dir)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moncv.settings_railway')

# Setup Django
django.setup()

# Now import and return the actual WSGI application
from moncv.wsgi import application

__all__ = ['application']
