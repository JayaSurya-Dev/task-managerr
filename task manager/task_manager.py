# task_manager.py
import json
import os
from task import Task

TASK_FILE = "data/tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]

    def save_tasks(self):
        with open(TASK_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title, description, due_date, priority):
        new_id = len(self.tasks) + 1
        task = Task(new_id, title, description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        for task in self.tasks:
            overdue = " (OVERDUE)" if task.is_overdue() and task.status != "Done" else ""
            print(f"[{task.id}] {task.title} - {task.status} - Due: {task.due_date} - Priority: {task.priority}{overdue}")

    def update_task(self, task_id, field, new_value):
        for task in self.tasks:
            if task.id == task_id:
                if hasattr(task, field):
                    setattr(task, field, new_value)
                    self.save_tasks()
                    return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
