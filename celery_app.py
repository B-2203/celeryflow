from celery import Celery

app = Celery('my_celery_app', broker='redis://localhost:6379/0')

# Optional: configure result backend
# app.conf.result_backend = 'redis://localhost:6379/0'
