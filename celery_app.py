import os

from celery import Celery

app = Celery('my_celery_app', broker=os.environ['CELERY_BROKER_URL'],
             backend=os.environ['CELERY_RESULT_BACKEND'])

# Optional: configure result backend
# app.conf.result_backend = 'redis://localhost:6379/0'
