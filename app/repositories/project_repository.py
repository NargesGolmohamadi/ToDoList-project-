from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.project import Project
from app.exceptions.repository_exceptions import RepositoryError

class ProjectRepository:

    def __init__(self, db: Session):
    
        self.db = db 

    def create_project(self, name: str, description: str):
        
        try:
            project = Project(name=name, description=description)
            self.db.add(project)
            self.db.commit()
            self.db.refresh(project)
            return project
        
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RepositoryError(str(e))

    def get_project_by_id(self, project_id: int):
    
        return self.db.query(Project).filter(Project.id == project_id).first()

    def get_all_projects(self):
    
        return self.db.query(Project).all()

    def update_project(self, project, new_name, new_desc):
    
        try:
            project.name = new_name
            project.description = new_desc
            self.db.commit()
            self.db.refresh(project)
            return project
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RepositoryError(str(e))

    def delete_project(self, project):
    
        try:
            self.db.delete(project)
            self.db.commit()
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RepositoryError(str(e))
