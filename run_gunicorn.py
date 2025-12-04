#!/usr/bin/env python
"""
Launch script for Render deployment.
Fixes the sys.path and launches gunicorn properly.
"""
import os
import sys
from pathlib import Path

# Get the project root
project_root = Path(__file__).resolve().parent
moncv_project = project_root / 'moncv'

# Add moncv to sys.path so Python can import moncv package
sys.path.insert(0, str(moncv_project))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moncv.settings_railway')

# Import gunicorn and run it
from gunicorn.app.wsgiapp import run
sys.argv = [
    'gunicorn',
    'moncv.wsgi:application',
    '--bind', '0.0.0.0:8000',
]
sys.exit(run())
