from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab    
from django_celery_beat.models import PeriodicTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')

app = Celery('django_celery')
app.conf.enable_utc = False 
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-everyday-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=17,minute=10),  #24 hour format
        # 'args': (2,)  # we can use this in tasks,py with def(request,data):
    }
}

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'request: {self.request!r}')