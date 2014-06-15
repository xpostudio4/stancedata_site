EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS =True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ljimenez@stancedata.com'
EMAIL_HOST_PASSWORD = 'Jesusvictor1'
EMAIL_PORT = 587

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'zinnia',
    'tagging',
)
