# -* encoding: utf-8 *-
import django

if django.VERSION < (3, 2):
    default_app_config = 'django_dbconn_retry.DjangoIntegration'

