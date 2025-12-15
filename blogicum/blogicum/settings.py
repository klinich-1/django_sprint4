from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings
SECRET_KEY = 'django-insecure-1234567890abcdef'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'pages',
    'django_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogicum.urls'

# Templates directory variable used by tests and project
TEMPLATES_DIR = BASE_DIR / 'templates'
# Also include repository-level templates directory (tests use it)
REPO_TEMPLATES_DIR = BASE_DIR.parent / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, REPO_TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogicum.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

# Ensure login_required redirects to the project's auth urls
LOGIN_URL = '/auth/login/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media (user-uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# File email backend for tests / development
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Use custom CSRF failure view so CsrfViewMiddleware renders our template
CSRF_FAILURE_VIEW = 'blogicum.views.csrf_failure'
