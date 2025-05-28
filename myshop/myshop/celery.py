import os
from celery import Celery

#Задать стандартный модуль настроек django дял celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")
app = Celery("myshop")
app.config_from_object("django.conf:settings", namespace="Celery")
app.autodiscover_tasks()