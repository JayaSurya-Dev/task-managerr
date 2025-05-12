# task.py
from datetime import datetime

class Task:
    def __init__(self, id, title, description, due_date, priority="Medium", status="To Do"):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date  # string format: YYYY-MM-DD
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["id"],
            data["title"],
            data["description"],
            data["due_date"],
            data["priority"],
            data["status"]
        )

    def is_overdue(self):
        return datetime.strptime(self.due_date, "%Y-%m-%d") < datetime.today()
