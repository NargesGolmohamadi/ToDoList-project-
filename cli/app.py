import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.service_project import ProjectService
from services.service_task import TaskService


class CLIApp:
    def __init__(self):
        self.project_service = ProjectService()
        self.task_service = TaskService()

    def print_menu(self):
        print("\n===== TO DO LIST APP =====")
        print("1. Create a new project")
        print("2. Show all projects")
        print("3. Add a task to a project")
        print("4. Show all tasks of a project")
        print("5. Edit a project")
        print("6. Delete a project")
        print("7. Exit")

    def create_project(self):
        name = input("Project name: ")
        desc = input("Project description: ")
        try:
            project = self.project_service.create_project(name, desc)
            print(f"✅ Project created: {project}")
        except ValueError as e:
            print(f"Error: {e}")

    def show_projects(self):
        projects = self.project_service.list_projects()
        if not projects:
            print("No projects found.")
        else:
            print("\n--- Projects ---")
            for p in projects:
                print(f"{p.id}. {p.name} — {p.description} ({len(p.tasks)} tasks)")

    def add_task(self):
        self.show_projects()
        try:
            pid = int(input("Enter project ID: "))
            project = self.project_service.get_project_by_id(pid)
            if not project:
                print("Project not found.")
                return

            title = input("Task title: ")
            desc = input("Task description: ")
            deadline = input("Task deadline (YYYY-MM-DD): ")

            task = self.task_service.add_task(project, title, desc, deadline=deadline)
            print(f"✅ Task added: {task}")
        except ValueError as e:
            print(f"Error: {e}")

    def show_tasks(self):
        self.show_projects()
        try:
            pid = int(input("Enter project ID: "))
            project = self.project_service.get_project_by_id(pid)
            if not project:
                print("Project not found.")
                return
            if not project.tasks:
                print("No tasks for this project.")
            else:
                print(f"\n--- Tasks in '{project.name}' ---")
                for t in project.tasks:
                    print(f"{t.id}. {t.task_name} — {t.status} — deadline: {t.deadline.date()}")
        except ValueError as e:
            print(f"Error: {e}")

    def edit_project(self):
        self.show_projects()
        try:
            pid = int(input("Enter project ID to edit: "))
            new_name = input("New project name: ")
            new_desc = input("New project description: ")
            updated = self.project_service.edit_project(pid, new_name, new_desc)
            print(f"✅ Project updated: {updated}")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_project(self):
        self.show_projects()
        try:
            pid = int(input("Enter project ID to delete: "))
            if self.project_service.delete_project(pid):
                print("Project deleted.")
            else:
                print("Project not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def run(self):
        while True:
            self.print_menu()
            choice = input("\nSelect an option: ")

            if choice == "1":
                self.create_project()
            elif choice == "2":
                self.show_projects()
            elif choice == "3":
                self.add_task()
            elif choice == "4":
                self.show_tasks()
            elif choice == "5":
                self.edit_project()
            elif choice == "6":
                self.delete_project()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Not an option!")
