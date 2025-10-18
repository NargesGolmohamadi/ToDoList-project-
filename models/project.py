import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from models.task import Task

class Project:
    def __init__(self, project_id: int, name: str, description: str):
        self.id = project_id
        self.name = name
        self.description = description
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> bool:
        for t in self.tasks:
            if t.id == task_id:
                self.tasks.remove(t)
                return True
        return False

    def __repr__(self):
        return f"<Project {self.id}: {self.name}>"
