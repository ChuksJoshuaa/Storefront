from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

celery = Celery('storefront')
celery.config_from_object('django.conf:settings')

celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
celery.conf.broker_url = "redis://localhost:6379"
celery.conf.beat_schedule = {
    'notify_customers': {
        'task': 'playground.tasks.notify_customers',
        'schedule': 5,
        'args': ['Hello World']
    }
}

# Note we can use crontab to set the day or time when we went task to run. Read it up
# this means every five sceonds our task will run but make sure you open the three terminals when running it,
# 1. celery -A <project> worker -l info -P gevent
# 2. celery -A storefront beat
# 3. python manage.py runserver
# 4. celery -A storefront flower
# then use the local host http://localhost:5555 to check our history


@celery.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
