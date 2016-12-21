"""
Django settings for flex project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@#(^ho8wu)6yvy^%w93^yh#cf^fs21)d&f29)lhz7gox%x%ta'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (

    # http://django-registration-redux.readthedocs.io/en/latest/quickstart.html#quickstart
    # django-registration-redux
    'registration',
    # Why up here? #http://stackoverflow.com/questions/34577607/django-registration-redux-change-password-link

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # userena

    # For django-userena http://django-userena.readthedocs.io/en/latest/installation.html
    # 'userena',
    # 'guardian',
    # 'easy_thumbnails',



    'crispy_forms',

    'django_summernote',

    # My custom apps
    'profiles',
    'events',
)

AUTHENTICATION_BACKENDS = (
    #'userena.backends.UserenaAuthenticationBackend',
    #'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'flex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'flex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")


ADMIN_SITE_HEADER = 'Timberline Flex Site - Administration'

# django-guardian
# ANONYMOUS_USER_ID = -1
# AUTH_PROFILE_MODULE = 'accounts.UserProfile'

# userena
# USERENA_ACTIVATION_REQUIRED = False
# #USERENA_USE_HTTPS = True
# USERENA_DEFAULT_PRIVACY = 'closed'
# USERENA_HIDE_EMAIL = True
# LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
# #LOGIN_URL = '/accounts/signin/'
# #LOGOUT_URL = '/accounts/signout/'

# django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = "/"

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

from django_summernote.settings import static_url
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    # 'width': '100%',
    # 'height': '480',

    # Use proper language setting automatically (default)
    'lang': None,

    # Or, set editor language/locale forcely
    #'lang': 'ko-KR',

    # Customize toolbar buttons
    # 'toolbar': [
    #     ['style', ['style']],
    #     ['style', ['bold', 'italic', 'underline', 'clear']],
    #     ['para', ['ul', 'ol', 'height']],
    #     ['insert', ['link']],
    # ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
    #'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    #'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    #'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

    # Set common css/js media files
    'external_css': (
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css',
    ),
    'external_js': (
        '//code.jquery.com/jquery-1.9.1.min.js',
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js',
    ),
    'internal_css': (
        static_url('django_summernote/summernote.css'),
    ),
    'internal_js': (
        static_url('django_summernote/jquery.ui.widget.js'),
        static_url('django_summernote/jquery.iframe-transport.js'),
        static_url('django_summernote/jquery.fileupload.js'),
        static_url('django_summernote/summernote.min.js'),
    ),

    # You can add custom css/js for SummernoteWidget.
    'css': (
    ),
    'js': (
    ),

    # And also for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    # 'css_for_inplace': (
    # ),
    # 'js_for_inplace': (
    # ),

    # You can disable file upload feature.
    'disable_upload': False,

    # Codemirror as codeview
    'codemirror': {
            # Please visit http://summernote.org/examples/#codemirror-as-codeview
            'theme': 'monokai',
    },

}
