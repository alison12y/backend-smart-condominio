"""
Django settings for config project.
"""

from pathlib import Path
import os
from corsheaders.defaults import default_headers  # 👈 import necesario

# === Paths ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Seguridad / Entorno ===
SECRET_KEY = os.getenv("SECRET_KEY", "solo-para-dev-no-usar-en-prod")
DEBUG = os.getenv("DEBUG", "True") == "True"  # en dev: True
ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost,[::1],smart-condominio-parcial-1-si-2.vercel.app"
).split(",")

# === Apps ===
INSTALLED_APPS = [
    # Terceros
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Tu app
    "core",
]

# === Middleware (orden recomendado) ===
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS primero
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === REST Framework / JWT ===
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

# === CORS / CSRF ===
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://smart-condominio-parcial-1-si-2.vercel.app",
]
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://.*\.vercel\.app$"]

CORS_ALLOW_CREDENTIALS = True

# 👇 incluimos explícitamente los headers necesarios
CORS_ALLOW_HEADERS = list(default_headers) + [
    "content-type",
    "x-csrftoken",
]

CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://smart-condominio-parcial-1-si-2.vercel.app",
]

# === URLs / WSGI ===
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# === Templates ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === Base de datos (PostgreSQL) ===
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "si2",
        "USER": "si2_user",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# === Password validators (en dev los desactivamos) ===
AUTH_PASSWORD_VALIDATORS = []

# === i18n / zona horaria ===
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# === Estáticos ===
STATIC_URL = "static/"

# === Default PK ===
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
