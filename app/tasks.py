# tasks.py
import os
from celery import Celery

# Use environment variables
broker_url = os.environ.get("CELERY_BROKER_URL")
backend_url = os.environ.get("CELERY_RESULT_BACKEND")

print(f"Broker: {broker_url}", "\n", f"Backend: {backend_url} ")
# Create Celery app with Redis as broker
app = Celery('my_celery_app', broker=broker_url,backend=backend_url)

# Define a sample task
@app.task
def add(x, y):
    return x + y
