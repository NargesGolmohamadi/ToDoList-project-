from services.project_service import ProjectService
from services.task_service import TaskService

project_service = ProjectService()
task_service = TaskService()


def print_menu():
    print("\n===== TO DO LIST APP =====")
    print("1 Create a new project")
    print("2  Show all projects")
    print("3  Add a task to a project")
    print("4  Show all tasks of a project")
    print("5  Edit a project")
    print("6  Delete a project")
    print("7  Exit")


def create_project():
    name = input("Project name: ")
    desc = input("Project description: ")
    try:
        project = project_service.create_project(name, desc)
        print(f"Project created: {project}")
    except ValueError as e:
        print(f"Error: {e}")


