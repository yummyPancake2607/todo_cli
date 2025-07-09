import sys
import os
import json
from datetime import datetime

tasks_file = 'tasks.json'
def load_task():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
def save_tasks(tasks):
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=4)




args = sys.argv[1:]

if not args:
    print("No input provided")
elif arg[0] == "add":
    if le(args)<2:
        print("Error: Please provide a task description.")
        else:
            description = args[1]
            tasks = load_task()

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new task = {
                "id": len(tasks) +1,
                "description" : description,
                "status":"todo",
                "createdAt": now,
                "updatedAt": now
            }

            tasks.append(new_tasks)
            save_tasks(tasks)
            print(f"task added sucessfully (ID: {new_task['id']})")
        else:
            print(f"unknown command:{args[0]}")