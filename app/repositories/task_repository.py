from sqlalchemy.orm import Session
from app.models.task import Task

class TaskRepository:

    def __init__(self, db: Session):
    
        self.db = db

    def create_task(self, project_id: int, title: str, description: str, deadline: str):
    
        new_task = Task(
            title=title,
            description=description,
            status="pending",
            deadline=deadline,
            project_id=project_id
        )
    
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
    
        return new_task

    def get_task_by_id(self, task_id: int):
    
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_tasks_by_project(self, project_id: int):
    
        return self.db.query(Task).filter(Task.project_id == project_id).all()

    def update_task_status(self, task_id: int, new_status: str):
    
        task = self.get_task_by_id(task_id)
    
        if task:
            task.status = new_status
            self.db.commit()
            self.db.refresh(task)
            return task
    
        return None

    def delete_task(self, task_id: int):
    
        task = self.get_task_by_id(task_id)
    
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
    
        return False
