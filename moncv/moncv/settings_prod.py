from .settings_base import *  # noqa
import dj_database_url
import os

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise RuntimeError('SECRET_KEY must be set in environment for production')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'moncv.fr').split(',')

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL')),
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# --- AWS S3 storage configuration (optional) ---
# If the following environment variables are set, media (and optionally static) files
# will be stored on S3 using django-storages.
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', None)  # e.g. 'eu-west-1'
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL', None)  # for custom endpoints

# Use S3 for media files when credentials are provided
if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME:
    # Keep static files served by WhiteNoise by default; use S3 for media only
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # Optional S3 settings
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # Allow overriding region/endpoint
    if AWS_S3_REGION_NAME:
        AWS_S3_REGION_NAME = AWS_S3_REGION_NAME
    if AWS_S3_ENDPOINT_URL:
        AWS_S3_ENDPOINT_URL = AWS_S3_ENDPOINT_URL

    # If you want to serve static files from S3 instead of WhiteNoise,
    # set the environment variable `USE_S3_STATIC=true` in Render.
    if os.getenv('USE_S3_STATIC', 'False').lower() in ('true', '1'):
        STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

