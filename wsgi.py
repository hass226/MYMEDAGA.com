"""
WSGI config wrapper - just import from moncv/moncv/wsgi.py
This will only be used if running from root. 
When rootDir=moncv is set in Render, this won't be used.
"""

import os
import sys
from pathlib import Path

# Add moncv to path
sys.path.insert(0, str(Path(__file__).parent / 'moncv'))

# Load from the actual wsgi
from moncv.wsgi import application

__all__ = ['application']
