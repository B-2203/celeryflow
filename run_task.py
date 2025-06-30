# run_task.py

from app.tasks import add

task_inputs = [(1, 2), (3, 4), (5, 6), (7, 8)]

for x, y in task_inputs:

    result = add.delay(x,y)
    print("Task submitted:", result)
    print("Waiting for result...")
    print("Result:", result.get(timeout=10))
