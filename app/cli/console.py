import sys
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.project_services import ProjectService
from app.services.task_services import TaskService

def get_db() -> Session:
    db = SessionLocal()

    try:
        return db
    except:
        db.close()


def main_menu():
    print("\n=== TO DO LIST ===")
    print("1. Create Project")
    print("2. List Projects")
    print("3. Open Project")
    print("4. Delete Project")
    print("0. Exit")

def project_menu():
    print("\n--- PROJECT MENU ---")
    print("1. Create Task")
    print("2. List Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("0. Back")

def run():

    db = get_db()

    project_service = ProjectService(db)
    task_service = TaskService(db)

    while True:

        main_menu()
        choice = input("Choose: ")

        if choice == "0":
            print("Goodbye!")
            sys.exit()

        elif choice == "1":

            name = input("Project name: ")
            desc = input("Description: ")
            
            try:
                project = project_service.create_project(name, desc)
                print("project created")
           
            except Exception as e:
                print("Error:", e)

        elif choice == "2":

            projects = project_service.list_projects()
            for p in projects:
                print(f"{p.id} - {p.name}")

        elif choice == "3":

            pid = int(input("Project ID: "))
            project = project_service.get_project(pid)

            while True:

                print(f"\n=== PROJECT: {project.name} ===")
                project_menu()
                ch = input("Choose: ")

                if ch == "0":
                    break

                elif ch == "1":
                    
                    title = input("Task title: ")
                    desc = input("Description: ")
                    deadline = input("Deadline (YYYY-MM-DD): ")
                    task = task_service.create_task(pid, title, desc, deadline)
                    print("Created" )

                elif ch == "2":
                
                    tasks = task_service.list_tasks(pid)
                    for t in tasks:
                        print(f"{t.id} - {t.title} [{t.status}]")

                elif ch == "3":
                
                    tid = int(input("Task ID: "))
                    new_status = input("New status: ")
                    task_service.update_status(tid, new_status)
                    print("Updated.")

                elif ch == "4":
                
                    tid = int(input("Task ID: "))
                    task_service.delete_task(tid)
                    print("Deleted.")

        elif choice == "4":
        
            pid = int(input("Project ID: "))
            project_service.delete_project(pid)
            print("Deleted.")

        else:
            print("Invalid choice")
