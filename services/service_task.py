import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.task import Task, TaskStatus
from models.project import Project
from dotenv import load_dotenv

load_dotenv()


class TaskService:
    def __init__(self):
        self.max_tasks = int(os.getenv("MAX_NUMBER_OF_TASKS", 7))
        self.ID = 1

    def add_task(self, project: Project, title: str, description: str, deadline: str, status: str = TaskStatus.TODO) -> Task:
        if len(title) > 30:
            raise ValueError("Task name too long.")
        if len(description) > 150:
            raise ValueError("Task description too long.")
        if len(project.tasks) >= self.max_tasks:
            raise ValueError("Too many tasks.")
        
        task = Task(
            task_id=self.ID,
            title=title,
            description=description,
            status=status,
            deadline=deadline
        )
        project.add_task(task)
        self.ID += 1
        return task


    def delete_task(self, project: Project, task_id: int) -> bool:
        return project.remove_task(task_id)
