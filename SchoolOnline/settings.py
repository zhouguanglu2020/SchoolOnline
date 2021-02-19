"""
Django settings for SchoolOnline project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cywrk3d5%5gw6ecnr#&!_63d0yhqe#xkb3)x!d&*xd0-06^)%4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Web.apps.WebConfig',
    'Api.apps.ApiConfig',
    'django_hosts',
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'SchoolOnline.urls'
#添加django-host配置
# 客户端的请求通过这个配置被转发到hosts.py文件的host_patterns中匹配
ROOT_HOSTCONF = 'SchoolOnline.hosts'
# 设置一个默认域名，在没有匹配所有请求的域名时，默认请求这个域名
DEFAULT_HOST = 'www'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 不用每次都加载static
            'builtins': [
                'django.templatetags.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'SchoolOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SchoolOnlineDB',
        'USER': 'root', # 账号
        'PASSWORD': 'z19881205', # 密码
        'HOST': '127.0.0.1', # HOST
        'POST': 3306, # 端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
#在每个app里面新建一个static文件夹,将静态文件放到里面,在加载静态文件时,比如要在模板中用到静态文件,django会自动在每个app里面搜索static文件夹。
STATIC_URL = '/static/'
#the dir for command "python manage.py collectstatic",执行完python manage.py collectstatic后，将静态文件复制到STATIC_ROOT指定的目录中
STATIC_ROOT = os.path.join(BASE_DIR, "common_static/")
#让django知道你把一些静态文件放到app以外的公共文件夹中呢,那就需要配置STATICFILES_DIRS了
STATICFILES_DIRS  = [
    os.path.join(BASE_DIR, "static/"),
]


#静态js地址  去这里找 https://www.bootcdn.cn/
JQUERY_ADDR = "https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js"
BOOTSTRAP_ADDR = "https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.5.3/css/bootstrap.min.css"
