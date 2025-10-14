import os
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
        
        projct = Project(self.ID , name , descripption)
        self.projects.append(project)
        self.ID += 1
        return self.projects 
    
    def list_projects(self):
        return self.projects 
