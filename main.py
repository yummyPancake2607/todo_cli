import sys
import os
import json
from datetime import datetime

tasks_file = 'tasks.json'

# Load tasks from the JSON file
def load_task():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Warning: Corrupted tasks.json file. Starting with an empty list.")
            return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=4)

# Function to print task details
def print_task(task):
    print(f"ID: {task['id']}")
    print(f"Description: {task['description']}")
    print(f"Status: {task['status']}")
    print(f"Created At: {task['createdAt']}")
    print(f"Updated At: {task['updatedAt']}")
    print("-" * 30)

# Command-line arguments
args = sys.argv[1:]

if not args:
    print("No input provided. Use --help to see available commands.")

elif args[0] in ["--help", "-h", "help"]:
    print(" Available commands:")
    print("  add <description>              Add a new task")
    print("  list [status]                  List tasks (all, todo, done, in-progress)")
    print("  update <id> <new description>  Update task description")
    print("  delete <id>                    Delete task by ID")
    print("  mark-done <id>                 Mark task as done")
    print("  mark-in-progress <id>          Mark task as in-progress")

elif args[0] == "add":
    if len(args) < 2:
        print("Error: Please provide a task description.")
    else:
        description = args[1].strip()
        if not description:
            print("Error: Task description cannot be empty.")
        else:
            tasks = load_task()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_task = {
                "id": len(tasks) + 1,
                "description": description,
                "status": "todo",
                "createdAt": now,
                "updatedAt": now
            }

            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task added successfully (ID: {new_task['id']})")

elif args[0] == "list":
    tasks = load_task()
    if not tasks:
        print("No tasks found.")
    elif len(args) == 1:
        for task in tasks:
            print_task(task)
    elif len(args) == 2:
        status = args[1].lower()
        valid_statuses = ["todo", "done", "in-progress"]
        if status not in valid_statuses:
            print(f"Error: '{status}' is not a valid status.")
        else:
            filtered = [task for task in tasks if task["status"].lower() == status]
            if not filtered:
                print(f"No tasks with status '{status}'.")
            for task in filtered:
                print_task(task)
    else:
        print("Invalid usage. Try: python task_cli.py list [status]")

elif args[0] == "update":
    if len(args) < 3:
        print("Error: Please provide task ID and new description.")
    else:
        try:
            task_id = int(args[1])
            new_description = " ".join(args[2:]).strip()
            if not new_description:
                print("Error: Description cannot be empty.")
            else:
                tasks = load_task()
                task_found = False

                for task in tasks:
                    if task['id'] == task_id:
                        task['description'] = new_description
                        task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        task_found = True
                        break

                if task_found:
                    save_tasks(tasks)
                    print(f"Task {task_id} updated successfully.")
                else:
                    print(f"Task with ID {task_id} not found.")
        except ValueError:
            print("Error: Task ID should be a number.")

elif args[0] == "delete":
    if len(args) < 2:
        print("Error: Please provide the task ID to delete.")
    else:
        try:
            task_id = int(args[1])
            tasks = load_task()
            original_count = len(tasks)

            tasks = [task for task in tasks if task["id"] != task_id]

            if len(tasks) < original_count:
                save_tasks(tasks)
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"No task found with ID {task_id}.")
        except ValueError:
            print("Error: Task ID must be a number.")

elif args[0] == "mark-done":
    if len(args) < 2:
        print("Error: Please provide the task ID to mark as done.")
    else:
        try:
            task_id = int(args[1])
            tasks = load_task()
            task_found = False

            for task in tasks:
                if task["id"] == task_id:
                    task["status"] = "done"
                    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    task_found = True
                    break

            if task_found:
                save_tasks(tasks)
                print(f"Task {task_id} marked as done.")
            else:
                print(f"No task found with ID {task_id}.")
        except ValueError:
            print("Error: Task ID must be a number.")

elif args[0] == "Make_done":
    if len(args) < 2:
        print("Error: Please provide the task ID to mark as in-progress.")
    else:
        try:
            task_id = int(args[1])
            tasks = load_task()
            task_found = False

            for task in tasks:
                if task["id"] == task_id:
                    task["status"] = "in_process"
                    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    task_found = True
                    break

            if task_found:
                save_tasks(tasks)
                print(f"Task {task_id} marked as in-progress.")
            else:
                print(f"No task found with ID {task_id}.")
        except ValueError:
            print("Error: Task ID must be a number.")

else:
    print(f"Unknown command: {args[0]}. Use --help to see available commands.")