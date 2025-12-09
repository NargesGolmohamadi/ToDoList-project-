from datetime import datetime
from app.repositories.task_repository import TaskRepository
from app.repositories.project_repository import ProjectRepository
from app.exceptions.service_exceptions import (
    NotFoundError,
    ValidationError
)
from app.exceptions.repository_exceptions import RepositoryError


class TaskService:

    def __init__(self, db_session):
    
        self.task_repo = TaskRepository(db_session)
        self.project_repo = ProjectRepository(db_session)

    def create_task(self, project_id: int, title: str, description: str, deadline: str):

        project = self.project_repo.get_project_by_id(project_id)
    
        if not project:
            raise NotFoundError("Project")

        try:
            datetime.strptime(deadline, "%Y-%m-%d").date()
        
        except:
            raise ValidationError("Invalid deadline format. Use YYYY-MM-DD")

        try:
            return self.task_repo.create_task(project_id, title, description, deadline)
        
        except RepositoryError as e:
            raise e

    def list_tasks(self, project_id: int):
    
        project = self.project_repo.get_project_by_id(project_id)
    
        if not project:
            raise NotFoundError("Project")

        return self.task_repo.get_tasks_by_project(project_id)

    def update_status(self, task_id: int, new_status: str):
    
        task = self.task_repo.get_task_by_id(task_id)
        if not task:
            raise NotFoundError("Task")

        try:
            return self.task_repo.update_task_status(task, new_status)
    
        except RepositoryError as e:
            raise e

    def delete_task(self, task_id: int):
    
        task = self.task_repo.get_task_by_id(task_id)
    
        if not task:
            raise NotFoundError("Task")

        try:
            return self.task_repo.delete_task(task)
        except RepositoryError as e:
            raise e
