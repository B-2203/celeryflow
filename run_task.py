# run_task.py

from app.tasks import add

result = add.delay(5, 7)
print("Task submitted:", result)
print("Waiting for result...")
print("Result:", result.get(timeout=10))
