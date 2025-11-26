from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.exceptions.service_exceptions import (
    NotFoundError,
    ValidationError,
    LimitReachedError
)
from app.exceptions.repository_exceptions import RepositoryError
from app.constants import MAX_NUMBER_OF_PROJECTS


class ProjectService:

    def __init__(self, db_session):
    
        self.project_repo = ProjectRepository(db_session)
        self.task_repo = TaskRepository(db_session)

    def create_project(self, name: str, description: str):
    
        if not name.strip():
            raise ValidationError("Project name cannot be empty")

        projects = self.project_repo.get_all_projects()
        if len(projects) >= MAX_NUMBER_OF_PROJECTS:
            raise LimitReachedError("projects")

        try:
            return self.project_repo.create_project(name, description)
    
        except RepositoryError as e:
            raise e

    def list_projects(self):
    
        return self.project_repo.get_all_projects()

    def get_project(self, project_id: int):
    
        project = self.project_repo.get_project_by_id(project_id)
    
        if not project:
            raise NotFoundError("Project")
        return project

    def edit_project(self, project_id: int, new_name: str, new_desc: str):
    
        project = self.get_project(project_id)

        if not new_name.strip():
            raise ValidationError("Project name cannot be empty")

        try:
            return self.project_repo.update_project(project, new_name, new_desc)
    
        except RepositoryError as e:
            raise e

    def delete_project(self, project_id: int):
    
        project = self.get_project(project_id)
    
        try:
            self.project_repo.delete_project(project)
            return True
    
        except RepositoryError as e:
            raise e
