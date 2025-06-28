# tasks.py
from celery import Celery

# Create Celery app with Redis as broker
app = Celery('my_celery_app', broker='redis://redis:6379/0',backend='redis://redis:6379/0')

# Define a sample task
@app.task
def add(x, y):
    return x + y
