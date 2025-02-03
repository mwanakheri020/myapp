from urllib import request
from django.apps import AppConfig, apps

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

