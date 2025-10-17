
from datetime import datetime


class TaskStatus:
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    STATUSES = {TODO, DOING, DONE}


class Task:

    def __init__(self, task_id: int, task_name: str, description: str, status: str, deadline: str):

        if status not in TaskStatus.STATUSES:
            raise ValueError("Invalid status")

        self.id = task_id
        self.task_name = task_name
        self.description = description
        self.status = status
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")

    def update_status(self, new_status: str):

        if new_status not in TaskStatus.STATUSES:
            raise ValueError("Invalid status")
        
        self.status = new_status

    def __repr__(self):
        return f"<Task{self.id} : '{self.task_name}', status='{self.status}'>"
   