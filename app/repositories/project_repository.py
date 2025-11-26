from sqlalchemy.orm import Session
from app.models.project import Project

class ProjectRepository:

    def __init__(self, db: Session):
    
        self.db = db 

    def create_project(self, name: str, description: str):

        new_project = Project(name=name, description=description)
        self.db.add(new_project)
        self.db.commit()
        self.db.refresh(new_project)
        return new_project

    def get_project_by_id(self, project_id: int):
    
        return self.db.query(Project).filter(Project.id == project_id).first()

    def get_all_projects(self):
    
        return self.db.query(Project).all()

    def delete_project(self, project_id: int):
    
        project = self.get_project_by_id(project_id)
        if project:
            self.db.delete(project)
            self.db.commit()
            return True
        return False
