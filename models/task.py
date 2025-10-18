from datetime import datetime

class TaskStatus:
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    STATUSES = {TODO, DOING, DONE}

class Task:
    def __init__(self, task_id: int, title: str, description: str, deadline: str , status: str = TaskStatus.TODO):
        if status not in TaskStatus.STATUSES:
            raise ValueError("Invalid status")
        if not deadline:
            raise ValueError("Deadline is mandatory")

        self.id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")

    def update_status(self, new_status: str):
        if new_status not in TaskStatus.STATUSES:
            raise ValueError("Invalid status")
        self.status = new_status

    def __repr__(self):
        return f"<Task {self.id}: '{self.title}', status='{self.status}'>"
