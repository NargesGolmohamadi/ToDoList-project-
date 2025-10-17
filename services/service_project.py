import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from models.project import Project

load_dotenv()

class ProjectService :

    def __init__(self):
        self.projects = []
        self.ID = 1
        self.max_projects = int(os.getenv("MAX_NUMBER_OF_PROJECTS"))

    def create_project(self, name: str , descripption: str) -> Project :

        if len(name) > 30 :
            raise ValueError("Project name too long.")
        if len(descripption) > 150 :
            raise ValueError("Project descripption too long.")
        if len(self.prjects) > self.max_projects :
            raise ValueError("Too many projects.")
        if any(p.name == name for p in self.projects):
            raise ValueError("This project already exists.")
        
        projcet = Project(self.ID , name , descripption)
        self.projects.append(project)
        self.ID += 1
        return project 
    
    def list_projects(self):
        return self.projects 

    def get_project_by_id(self, project_id: int):
        for p in self.projects:
            if p.id == project_id:
                return p
        return None
    
    def edit_project(self, project_id: int, new_name: str, new_description: str) :

        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found.")
        if len(new_name) > 30 :
            raise ValueError("Project name too long.")
        if len(new_descripption) > 150 :
            raise ValueError("Project descripption too long.")
        if any(p.name == new_name and p.id != project_id for p in self.projects):
            raise ValueError("This name already exists.")

        project.name = new_name
        project.description = new_description
        return project

    def delete_project(self, project_id: int) -> bool :

        project = self.get_project_by_id(project_id)
        if not project:
            return False
        self.projects.remove(project)
        return True

