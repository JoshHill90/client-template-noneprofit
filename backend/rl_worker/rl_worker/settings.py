from pathlib import Path
from systems.kekeper import SettingKeys

key_code = SettingKeys()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = key_code.django_key

DEBUG = key_code.django_debug

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'api_app',
    'corsheaders',
    'logs',
    'user_auth',
    'systems'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'rl_worker.urls'

CORS_ORIGIN_WHITELIST = [
    key_code.db_wl1,
    key_code.db_wl2,
    key_code.db_wl3,
    key_code.db_wl4,
]
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rl_worker.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': key_code.db_engine,
        'NAME': key_code.db_name,
        'USER': key_code.db_user,
        'PASSWORD': key_code.db_key,
        'HOST': key_code.db_host,
        'PORT':key_code.db_port, 
        'OPTIONS': {
            'init_command': "SET sql_mode= 'STRICT_TRANS_TABLES'"
        } 
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
