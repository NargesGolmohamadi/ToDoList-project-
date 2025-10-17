import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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

def show_projects():

    projects = project_service.list_projects()
    if not projects:
        print(" No projects found.")
    else:
        for p in projects:
            print(f" {p.id}. {p.name} — {p.description} ({len(p.tasks)} tasks)")


def add_task():

    show_projects()
    try:
        pid = int(input("Enter project ID: "))
        project = project_service.get_project_by_id(pid)
        if not project:
            print("Project not found.")
            return

        title = input("Task title: ")
        desc = input("Task description: ")
        task = task_service.add_task(project, title, desc)
        print(f" Task added: {task}")
    except ValueError as e:
        print(f" Error: {e}")


def show_tasks():
    show_projects()
    try:
        pid = int(input("Enter project ID: "))
        project = project_service.get_project_by_id(pid)
        if not project:
            print(" Project not found.")
            return
        if not project.tasks:
            print(" No tasks for this project.")
        else:
            for t in project.tasks:
                print(f"  {t.id}. {t.title} — status: {t.status}")
    except ValueError as e:
        print(f"Error: {e}")


def edit_project():
    show_projects()
    try:
        pid = int(input("Enter project ID to edit: "))
        new_name = input("New project name: ")
        new_desc = input("New project description: ")
        updated = project_service.edit_project(pid, new_name, new_desc)
        print(f" Project updated: {updated}")
    except ValueError as e:
        print(f" Error: {e}")


def delete_project():
    show_projects()
    try:
        pid = int(input("Enter project ID to delete: "))
        if project_service.delete_project(pid):
            print(" Project deleted.")
        else:
            print(" Project not found.")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    while True:
        print_menu()
        choice = input("\nSelect an option: ")

        if choice == "1":
            create_project()
        elif choice == "2":
            show_projects()
        elif choice == "3":
            add_task()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            edit_project()
        elif choice == "6":
            delete_project()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Not an option!")


if name == "main":
    main()
