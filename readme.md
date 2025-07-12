## 📋 Task Tracker CLI

A **Command Line Interface (CLI)** tool to help you manage your daily tasks directly from your terminal.

With this tool, you can:

* ✅ Add new tasks
* 📋 List all or specific types of tasks
* ✏️ Update task descriptions
* 🗑️ Delete tasks
* ✅ Mark tasks as done
* 🚧 Mark tasks as in-progress

---

### 📁 File Structure

```bash
.
├── task_cli.py       # Main Python script
└── tasks.json        # JSON file where all tasks are stored (created automatically)
```

---

## ⚙️ How to Use

### ▶️ Run the Script

```bash
python task_cli.py <command> [arguments]
```

> Make sure you have Python installed.
> Run the command from the same directory where `task_cli.py` is saved.

---

### 🛠️ Available Commands

| Command                         | Example                                           | Description                                         |
| ------------------------------- | ------------------------------------------------- | --------------------------------------------------- |
| `add <description>`             | `python task_cli.py add "Buy groceries"`          | Add a new task                                      |
| `list`                          | `python task_cli.py list`                         | Show all tasks                                      |
| `list <status>`                 | `python task_cli.py list done`                    | Show tasks by status: `todo`, `done`, `in-progress` |
| `update <id> <new description>` | `python task_cli.py update 1 "Buy milk and eggs"` | Update a task's description                         |
| `delete <id>`                   | `python task_cli.py delete 1`                     | Delete a task                                       |
| `mark-done <id>`                | `python task_cli.py mark-done 2`                  | Mark a task as `done`                               |
| `mark-in-progress <id>`         | `python task_cli.py mark-in-progress 3`           | Mark a task as `in-progress`                        |
| `--help` or `-h`                | `python task_cli.py --help`                       | Show available commands                             |

---

## 🗂️ Example Usage

### Add a Task

```bash
python task_cli.py add "Finish homework"
```

### List All Tasks

```bash
python task_cli.py list
```

### List Only Completed Tasks

```bash
python task_cli.py list done
```

### Update a Task Description

```bash
python task_cli.py update 1 "Finish math homework"
```

### Delete a Task

```bash
python task_cli.py delete 1
```

### Mark a Task as Done

```bash
python task_cli.py mark-done 2
```

### Mark a Task as In Progress

```bash
python task_cli.py mark-in-progress 3
```

---

## 🧠 How It Works

* All tasks are stored in a file called `tasks.json`.
* Each task has:

  * `id`: A unique number
  * `description`: What the task is
  * `status`: One of `todo`, `done`, or `in-progress`
  * `createdAt`: Timestamp of creation
  * `updatedAt`: Timestamp of last update

---

## 📌 Requirements

* Python 3.x
  (No external libraries needed)

---

## 💡 Features You Can Add Later (Suggestions)

* ✅ Task priorities (high, medium, low)
* ⏰ Due dates
* 🔁 Recurring tasks
* 🔍 Search/filter by keyword
* 🌈 Colored terminal output for better visibility

---

## 🙌 Author

**Lakshit Verma**
Beginner Python Developer 🌱
Made with ❤️ and curiosity
