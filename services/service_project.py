import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from models.project import Project
from typing import List

load_dotenv()
import json

class ProjectService:
    def __init__(self):
        self.projects : list[Project] = []
        self.ID = 1
        self.max_projects = int(os.getenv("MAX_NUMBER_OF_PROJECTS", 5))

    def create_project(self, name: str, description: str) -> Project:
        if len(name) > 30:
            raise ValueError("Project name too long.")
        if len(description) > 150:
            raise ValueError("Project description too long.")
        if len(self.projects) >= self.max_projects:
            raise ValueError("Too many projects.")
        if any(p.name == name for p in self.projects):
            raise ValueError("This project already exists.")
        
        project = Project(self.ID, name, description)
        self.projects.append(project)
        self.ID += 1
        return project 

    def list_projects(self) -> List[Project]:
        return sorted(self.projects, key=lambda p: p.id)

    def get_project_by_id(self, project_id: int):
        for p in self.projects:
            if p.id == project_id:
                return p
        return None
    
    def edit_project(self, project_id: int, new_name: str, new_description: str):
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found.")
        if len(new_name) > 30:
            raise ValueError("Project name too long.")
        if len(new_description) > 150:
            raise ValueError("Project description too long.")
        if any(p.name == new_name and p.id != project_id for p in self.projects):
            raise ValueError("This name already exists.")

        project.name = new_name
        project.description = new_description
        return project

    def delete_project(self, project_id: int) -> bool:
        project = self.get_project_by_id(project_id)
        if not project:
            return False
        self.projects.remove(project)
        return True
    


    def save_to_file(self, filename="data.json"):
        data = [
            {
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "tasks": [
                    {
                        "id": t.id,
                        "title": t.title,
                        "description": t.description,
                        "status": t.status,
                        "deadline": t.deadline.strftime("%Y-%m-%d")
                    }
                    for t in p.tasks
                ]
            }
            for p in self.projects
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename="data.json"):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
        self.projects = []
        for p in data:
            project = Project(p["id"], p["name"], p["description"])
            for t in p["tasks"]:
                from models.task import Task
                project.add_task(Task(**t))
            self.projects.append(project)
