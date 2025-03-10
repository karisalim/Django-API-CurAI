# """
# Django settings for config project.

# Generated by 'django-admin startproject' using Django 5.1.6.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.1/ref/settings/
# """
# from pathlib import Path
# from decouple import config
# from datetime import timedelta

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-hb(m^t+2m0*m+o5#z_em3m7&8*$dczjc8uayykog3t1)03ti1$'
# DEBUG = True

# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
#     'rncib-154-237-254-48.a.free.pinggy.link',

# ]
# # CORS_ALLOWED_ORIGINS = [
# #     "https://example.com",
# #     "https://sub.example.com",
# #     "http://localhost:8080",
# #     "http://127.0.0.1:9000",
# # ]

# # Application definition

# INSTALLED_APPS = [

#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'register_user',
#     'django_filters',
#     'rating',
#     'drf_yasg',
#     "rest_framework.authtoken",
#     "rest_registration",
#     'rest_framework',
#     'rest_framework_simplejwt',
# ]
# AUTH_USER_MODEL = 'register_user.CustomUser'

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
# ]

# ROOT_URLCONF = 'config.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'config.wsgi.application'

# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REST_FRAMEWORK = {

#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'register_user.auth_backend.JWTAuthentication',  # تأكد من إضافة المسار الصحيح إلى فئة `JWTAuthentication`
#         "rest_framework.authentication.SessionAuthentication",
#         # "rest_framework.authentication.TokenAuthentication",
#     ),
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10
# }


# REST_REGISTRATION = {
#     "REGISTER_VERIFICATION_ENABLED": False,
#     "REGISTER_EMAIL_VERIFICATION_ENABLED": True,
#     "RESET_PASSWORD_VERIFICATION_ENABLED": True,
#     'LOGIN_RETRIEVE_TOKEN': True,
#     "REGISTER_EMAIL_VERIFICATION_URL": "http://127.0.0.1:8000/verify-email/",
#     "RESET_PASSWORD_VERIFICATION_URL": "http://127.0.0.1:8000/reset-password/",
#     "VERIFICATION_FROM_EMAIL": "ks0894976@gmail.com",
#     'AUTH_TOKEN_MANAGER_CLASS': 'register_user.auth_backend.AuthJWTManager',
#     "USER_LOGIN_FIELDS": ["email"],
#     'REGISTER_AUTHENTICATION_CLASSES': (
#         'register_user.auth_backend.JWTAuthentication',
#     ),
#     "RESET_PASSWORD_VERIFICATION_PERIOD": timedelta(minutes=20),  # مدة صلاحية الرابط
#     "RESET_PASSWORD_VERIFICATION_ONE_TIME_USE": True,  # الرابط صالح لمرة واحدة فقط
#     'REGISTER_SERIALIZER_CLASS': 'register_user.serializers.CustomRegisterUserSerializer',
#     'REGISTER_OUTPUT_SERIALIZER_CLASS': 'register_user.serializers.CustomRegisterUserSerializer',
#     'RESET_PASSWORD_VERIFICATION_EMAIL_TEMPLATES':{
#     'body': 'rest_registration/reset_password/body.txt',
#     'subject': 'rest_registration/reset_password/subject.txt'},
#     "CHANGE_PASSWORD_SERIALIZER_PASSWORD_CONFIRM": True ,
#         "REGISTER_EMAIL_VERIFICATION_EMAIL_TEMPLATES": {
#         "subject": "rest_registration/register_email/subject.txt",
#         "body": "rest_registration/register_email/body.txt",
#     },

# }

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'ks0894976@gmail.com'
# EMAIL_HOST_PASSWORD = 'oiyq qksu gvta obak'  # كلمة مرور التطبيق التي أنشأتها

# from datetime import timedelta
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }
# # CORS_ALLOW_CREDENTIALS = True
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ''
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'rncib-154-237-254-48.a.free.pinggy.link',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'register_user',
    'django_filters',
    'rating',
    'drf_yasg',
    "rest_framework.authtoken",
    "rest_registration",
    'rest_framework',
    'rest_framework_simplejwt',
]

AUTH_USER_MODEL = 'register_user.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # تأكد من إضافة المسار إلى القوالب
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]


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

# ✅ إعدادات Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'register_user.auth_backend.JWTAuthentication',  # تأكد أن المسار صحيح
        'rest_framework.authentication.TokenAuthentication',  # إضافة هذه السطر
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # "rest_framework.authentication.SessionAuthentication",

    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


REST_REGISTRATION = {
    "REGISTER_VERIFICATION_ENABLED": True,
    "REGISTER_EMAIL_VERIFICATION_ENABLED": True,
    "RESET_PASSWORD_VERIFICATION_ENABLED": True,
    'LOGIN_RETRIEVE_TOKEN': True,
    
    # 🔹 روابط التحقق
    "REGISTER_EMAIL_VERIFICATION_URL": "http://127.0.0.1:8000/api/auth/verify-email/",
    "REGISTER_VERIFICATION_URL": "http://127.0.0.1:8000/api/auth/verify-registration/",  # أو استخدم الرابط الصحيح لموقعك
    "RESET_PASSWORD_VERIFICATION_URL": "http://127.0.0.1:8000/api/auth/reset-password/",
    # 'VERIFICATION_URL_BUILDER' : 'rest_registration.utils.verification.build_default_verification_url',
    'VERIFICATION_URL_BUILDER': 'rest_registration.utils.verification.build_default_verification_url',

      # أضف هذا الإعداد لتحديد حقل التفعيل
    'USER_VERIFICATION_FLAG_FIELD': 'is_active',

    
    "REGISTER_VERIFICATION_AUTO_LOGIN": False,  # لا يتم تسجيل الدخول تلقائيًا بعد التحقق

    # ✅ **تفعيل الإيميل**
    "REGISTER_EMAIL_VERIFICATION_EMAIL_SENDER": "rest_registration.verification_notifications.send_register_email_verification_email_notification",
    # 🔹 المدة الزمنية للتحقق من البريد
    "REGISTER_EMAIL_VERIFICATION_PERIOD": timedelta(days=7),
    'REGISTER_VERIFICATION_ONE_TIME_USE': True,

    # 🔹 إعدادات البريد الإلكتروني
    "VERIFICATION_FROM_EMAIL": "ks0894976@gmail.com",
    
    # 🔹 إعدادات التوثيق والسيريالايزر
    # 'REGISTER_AUTHENTICATION_CLASSES': (
    #     'register_user.auth_backend.JWTAuthentication',
    # ),
    'REGISTER_SERIALIZER_CLASS': 'register_user.serializers.CustomRegisterUserSerializer',
    'REGISTER_OUTPUT_SERIALIZER_CLASS': 'register_user.serializers.CustomRegisterUserSerializer',
    'REGISTER_EMAIL_SERIALIZER_CLASS': 'rest_registration.api.serializers.DefaultRegisterEmailSerializer',
    
    # 🔹 صلاحية روابط إعادة تعيين كلمة المرور
    "RESET_PASSWORD_VERIFICATION_PERIOD": timedelta(minutes=20),
    "RESET_PASSWORD_VERIFICATION_ONE_TIME_USE": True,
    
    # ✅ **قوالب الإيميلات**
    'RESET_PASSWORD_VERIFICATION_EMAIL_TEMPLATES': {
        'body': 'rest_registration/reset_password/body.txt',
        'subject': 'rest_registration/reset_password/subject.txt'
    },
    # دا وكدا لما المستخدم يعمل verfiy للايميل بعد مسجل
    "REGISTER_VERIFICATION_EMAIL_TEMPLATES": {
        "subject": "rest_registration/register/subject.txt",
        "body": "rest_registration/register/body.txt",
    },
    # دا لما المستتخدم يريد تغيير الايميل وكدا
    "REGISTER_EMAIL_VERIFICATION_EMAIL_TEMPLATES": {
        "subject": "rest_registration/register_email/subject.txt",
        "body": "rest_registration/register_email/body.txt",
    },
    
    'USER_LOGIN_FIELDS': ['email'],
        'USER_LOGIN_FIELDS_UNIQUE_CHECK_ENABLED': True,  # تأكد من أنه فريد


    # 🔹 إعدادات تغيير كلمة المرور
    "CHANGE_PASSWORD_SERIALIZER_PASSWORD_CONFIRM": True,
}

# ✅ **تأكد من إعدادات الإيميل**
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''  # استخدم "App Password"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ✅ إعدادات JWT لتوثيق المستخدم
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
