# ruff: noqa: ERA001, E501
"""Base settings to build other settings files upon."""

from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# qvts/
APPS_DIR = BASE_DIR / "qvts"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Australia/Brisbane"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#languages
# from django.utils.translation import gettext_lazy as _
# LANGUAGES = [
#     ('en', _('English')),
#     ('fr-fr', _('French')),
#     ('pt-br', _('Portuguese')),
# ]
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    # "crispy_forms",
    # "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    # "dj_rest_auth",
    # "rest_framework_simplejwt.token_blacklist",
    "webpack_loader",
]

LOCAL_APPS = [
    "qvts.core",
    "qvts.users",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "qvts.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": env.int("PASSWORD_MIN_LENGTH", default=12),
        },
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    {"NAME": "qvts.core.validators.password_validators.NumberValidator"},
    {"NAME": "qvts.core.validators.password_validators.UppercaseValidator"},
    {"NAME": "qvts.core.validators.password_validators.LowercaseValidator"},
    {"NAME": "qvts.core.validators.password_validators.SymbolValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "qvts.users.context_processors.allauth_settings",
            ],
        },
    },
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
# CRISPY_TEMPLATE_PACK = "bootstrap5"
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""ns""", "ns@qvts.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# Force the `admin` sign in process to go through the `django-allauth` workflow
DJANGO_ADMIN_FORCE_ALLAUTH = env.bool("DJANGO_ADMIN_FORCE_ALLAUTH", default=False)

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # default: 3
ACCOUNT_EMAIL_NOTIFICATIONS = True  # default: False
ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False
# ACCOUNT_ADAPTER = "videultra.users.adapters.AccountAdapter"
ACCOUNT_RATE_LIMITS = {
    # Changing the password (for already authenticated users).
    "change_password": "3/m/user",  # default: "5/m/user"
    # Email management related actions, such as add, remove, change primary.
    "manage_email": "5/m/user",  # default: "10/m/user"
    # Requesting a password reset. The email for which the password is to be reset is passed as the key.
    "reset_password": "5/m/ip,5/m/key",  # default: "20/m/ip,5/m/key"
    # Reauthentication (for users already logged in).
    "reauthenticate": "5/m/user",  # default: "10/m/user"
    # Password reset (the view the password reset email links to).
    "reset_password_from_key": "5/m/ip",  # default: "20/m/ip"
    # Signups.
    "signup": "10/m/ip",  # default: "20/m/ip"
    # Logins.
    "login": "15/m/ip",  # default: "30/m/ip"
    # Restricts the allowed number of failed login attempts.
    "login_failed": "5/m/ip,5/5m/key",  # default: "10/m/ip,5/5m/key"
    # request email confirmation mails via the email management view
    "confirm_email": "1/3m/key",  # default: "1/3m/key"
}
ACCOUNT_REAUTHENTICATION_TIMEOUT = 300  # default: 300 (5 minutes)
ACCOUNT_REAUTHENTICATION_REQUIRED = True  # default: False
ACCOUNT_ADAPTER = "qvts.users.adapters.AccountAdapter"
# https://docs.allauth.org/en/latest/account/forms.html
ACCOUNT_FORMS = {"signup": "qvts.users.forms.UserSignupForm"}

# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_ADAPTER = "qvts.users.adapters.SocialAccountAdapter"
SOCIALACCOUNT_FORMS = {"signup": "qvts.users.forms.UserSocialSignupForm"}

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        # "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    # https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    # https://drf-spectacular.readthedocs.io/en/latest/readme.html
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # https://www.django-rest-framework.org/api-guide/throttling/
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",  # only applies to annonymous users
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day", "user": "1000/day"},
}

# drf-spectacular
# https://drf-spectacular.readthedocs.io/en/latest/readme.html
# -------------------------------------------------------------------------------
# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "Queensland Vessel Traffic Service API",
    "DESCRIPTION": "Documentation of API endpoints of Queensland Vessel Traffic Service",
    "VERSION": "1.0.0",
    # "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"],
    # "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SCHEMA_PATH_PREFIX": "/api/",
    "SERVE_INCLUDE_SCHEMA": False,
    # SwaggerUI configuration
    # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    # Self-contained UI (Sidecar)
    "SWAGGER_UI_DIST": "SIDECAR",
    # "SWAGGER_UI_FAVICON_HREF": STATIC_URL + "images/favicons/favicon-32x32.png",
}

# dj-rest-auth
# https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
# ------------------------------------------------------------------------------
# REST_AUTH = {
#     # JWT Authentication in dj_rest_auth.views.LoginView will be used
#     'USE_JWT': True,
#     # The cookie name for access token from JWT Authentication
#     'JWT_AUTH_COOKIE': 'jwt-auth-atoken',
#     # The cookie name for refresh token from JWT Authentication
#     'JWT_AUTH_REFRESH_COOKIE': 'jwt-auth-rtoken',
#     # refresh_token will not be sent if JWT_AUTH_HTTPONLY set to True
#     'JWT_AUTH_HTTPONLY': False,
#     # custom user details serializer
#     "USER_DETAILS_SERIALIZER": 'api.v1.serializers.CustomUserDetailsSerializer',
#     # expiration time will be included in response
#     "JWT_AUTH_RETURN_EXPIRATION": True,
#     "JWT_TOKEN_CLAIMS_SERIALIZER": "api.v1.serializers.TokenObtainPairSerializerDifferentToken",
# }

# django-rest-framework-simplejwt
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10), # default: 5
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7), # default: 1
#     'ROTATE_REFRESH_TOKENS': True,  # default: False
#     'BLACKLIST_AFTER_ROTATION': True,  # default: False
#     'UPDATE_LAST_LOGIN': True,  # default: False
#     'ALGORITHM': 'RS256',  # default: HS256
#     'SIGNING_KEY': env("DJANGO_JWT_SIGNING_KEY"),
#     'VERIFYING_KEY': env("DJANGO_JWT_VERIFYING_KEY"),
#     "USER_ID_FIELD": "id",
#     # "USER_ID_FIELD": "reference_id",
#     "USER_ID_CLAIM": "sub",
#     # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
#     # "AUDIENCE": None,
#     "ISSUER": 'http://localhost',
#     # "ISSUER": 'https://videultra.com.au',
#     "JWK_URL": 'http://localhost:8000/.well-known/jwks',
#     # "JWK_URL": 'http://videultra.com.au/.well-known/jwks.json',
#     "TOKEN_REFRESH_SERIALIZER": "api.v1.serializers.TokenRefreshSerializerDifferentToken",
# }

# django-cors-headers
# -------------------------------------------------------------------------------
# https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000",
# ]

# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "STATS_FILE": BASE_DIR / "webpack-stats.json",
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    },
}

# session
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/topics/http/sessions/#using-cached-sessions
# https://github.com/jazzband/django-redis#configure-as-session-backend
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"  # write-through cache
SESSION_CACHE_ALIAS = "default"

# Other
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#date-input-formats
DATE_INPUT_FORMATS = [
    "%d/%m/%Y",  # '25/10/2024'
    "%Y-%m-%d",  # '2024-10-25'
    "%d %b %Y",  # '25 Oct 2024'
    "%d %B %Y",  # '25 October 2024'
]
