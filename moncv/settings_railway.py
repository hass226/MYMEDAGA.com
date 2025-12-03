"""
Django settings for moncv project - Production Ready for Railway Deployment
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production-!@#$%^&*()')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Production hosts - modify for your domain
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# CORS Configuration
CORS_ALLOW_ALL_ORIGINS = os.environ.get('CORS_ALLOW_ALL_ORIGINS', 'False') == 'True'
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Configuration CSP (Content Security Policy)
CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = [
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://code.jquery.com",
    "https://cdn.jsdelivr.net",
    "https://www.google.com",
    "https://www.gstatic.com"
]
CSP_STYLE_SRC = [
    "'self'",
    "'unsafe-inline'",
    "https://cdn.jsdelivr.net",
    "https://stackpath.bootstrapcdn.com"
]
CSP_IMG_SRC = ["'self'", "data:", "https:", "http:"]
CSP_FONT_SRC = ["'self'", "https://cdn.jsdelivr.net", "https://fonts.gstatic.com"]
CSP_CONNECT_SRC = ["'self'", "https://www.google.com"]
CSP_FRAME_SRC = ["'self'", "https://www.google.com"]
CSP_INCLUDE_NONCE_IN = ['script-src']

# Désactiver CSP en mode debug pour faciliter le développement
CSP_REPORT_ONLY = DEBUG

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csp',
    'django.contrib.sitemaps',  # Pour le SEO
    'django.contrib.humanize',  # Pour le formatage des nombres
    'stores',
    'payments',  # Application de gestion des paiements
]

# Channels (optionnel - pour Live Commerce avec WebSocket)
try:
    import channels
    INSTALLED_APPS.insert(0, 'channels')
    CHANNELS_AVAILABLE = True
except ImportError:
    CHANNELS_AVAILABLE = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise pour les fichiers statiques
    'csp.middleware.CSPMiddleware',  # Middleware CSP
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Ajout pour i18n
    'stores.middleware.LanguageCurrencyMiddleware',  # Notre middleware personnalisé
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'moncv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'stores.context_processors.seo_context',  # SEO context
                'stores.context_processors.global_language_currency',
            ],
        },
    },
]

WSGI_APPLICATION = 'moncv.wsgi.application'

# Channels configuration (optionnel - pour Live Commerce avec WebSocket)
if CHANNELS_AVAILABLE:
    ASGI_APPLICATION = 'moncv.asgi.application'
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [('127.0.0.1', 6379)],
            },
        },
    }

# Database Configuration for Railway
# Use PostgreSQL if DATABASE_URL is available (Railway), otherwise SQLite
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_health_checks=True,
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) - WhiteNoise Configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise Cache Control
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URLs
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# Site URL (pour les callbacks de paiement)
SITE_URL = os.environ.get('SITE_URL', 'http://localhost:8000')

# Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_SECURITY_POLICY = True
    X_FRAME_OPTIONS = 'DENY'

# Configuration WhatsApp
WHATSAPP_API_KEY = os.environ.get('WHATSAPP_API_KEY', '')
ADMIN_WHATSAPP_NUMBER = '22601256984'

# Configuration des API de paiement (Production Ready)
ORANGE_MONEY_API_KEY = os.environ.get('ORANGE_MONEY_API_KEY', '')
ORANGE_MONEY_API_SECRET = os.environ.get('ORANGE_MONEY_API_SECRET', '')
ORANGE_MONEY_MERCHANT_ID = os.environ.get('ORANGE_MONEY_MERCHANT_ID', '')
ORANGE_MONEY_ENVIRONMENT = os.environ.get('ORANGE_MONEY_ENVIRONMENT', 'sandbox')

MOOV_MONEY_API_KEY = os.environ.get('MOOV_MONEY_API_KEY', '')
MOOV_MONEY_API_SECRET = os.environ.get('MOOV_MONEY_API_SECRET', '')
MOOV_MONEY_MERCHANT_ID = os.environ.get('MOOV_MONEY_MERCHANT_ID', '')
MOOV_MONEY_ENVIRONMENT = os.environ.get('MOOV_MONEY_ENVIRONMENT', 'sandbox')

MTN_MONEY_API_KEY = os.environ.get('MTN_MONEY_API_KEY', '')
MTN_MONEY_API_SECRET = os.environ.get('MTN_MONEY_API_SECRET', '')
MTN_MONEY_ENVIRONMENT = os.environ.get('MTN_MONEY_ENVIRONMENT', 'sandbox')

PAYDUNYA_MASTER_KEY = os.environ.get('PAYDUNYA_MASTER_KEY', '')
PAYDUNYA_PRIVATE_KEY = os.environ.get('PAYDUNYA_PRIVATE_KEY', '')
PAYDUNYA_TOKEN = os.environ.get('PAYDUNYA_TOKEN', '')
PAYDUNYA_MODE = os.environ.get('PAYDUNYA_MODE', 'test')

WAVE_API_KEY = os.environ.get('WAVE_API_KEY', '')
WAVE_API_SECRET = os.environ.get('WAVE_API_SECRET', '')
WAVE_ENVIRONMENT = os.environ.get('WAVE_ENVIRONMENT', 'sandbox')

CINETPAY_API_KEY = os.environ.get('CINETPAY_API_KEY', '')
CINETPAY_SITE_ID = os.environ.get('CINETPAY_SITE_ID', '')
CINETPAY_ENVIRONMENT = os.environ.get('CINETPAY_ENVIRONMENT', 'sandbox')

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY', '')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET', '')

PAYMENT_ENVIRONMENT = os.environ.get('PAYMENT_ENVIRONMENT', 'sandbox')

# Configuration IA
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')

# Configuration des emails (Production Ready)
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@example.com')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'contact@example.com')

# Mobile Money SMS Gateway
SMS_GATEWAY_API_KEY = os.environ.get('SMS_GATEWAY_API_KEY', '')
SMS_GATEWAY_ALLOWED_IPS = ['127.0.0.1']

# Logging pour les transactions
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'payments.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'stores.payment_providers': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'stores.views': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'payments': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
