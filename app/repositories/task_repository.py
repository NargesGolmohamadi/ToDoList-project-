from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.task import Task
from app.exceptions.repository_exceptions import RepositoryError

class TaskRepository:

    def __init__(self, db: Session):
    
        self.db = db

    def create_task(self, project_id: int, title: str, description: str, deadline: str):
    
        try:
            task = Task(
                title=title,
                description=description,
                status="pending",
                deadline=deadline,
                project_id=project_id
            )
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
    
            return task
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RepositoryError(str(e))

    def get_task_by_id(self, task_id: int):
    
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_tasks_by_project(self, project_id: int):
    
        return self.db.query(Task).filter(Task.project_id == project_id).all()

    def update_task_status(self, task, new_status):
    
        try:
            task.status = new_status
            self.db.commit()
            self.db.refresh(task)
    
            return task
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RepositoryError(str(e))

    def delete_task(self, task):
    
        try:
            self.db.delete(task)
            self.db.commit()
    
            return True
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RepositoryError(str(e))

    def list_all(self):
        return self.db.query(Task).all()
