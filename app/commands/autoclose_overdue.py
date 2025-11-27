from datetime import datetime
from app.db.session import SessionLocal
from app.repositories.task_repository import TaskRepository

def autoclose_overdue_tasks():
    
    db = SessionLocal()
    task_repo = TaskRepository(db)

    tasks = task_repo.list_all()
    now = datetime.now().date()

    for t in tasks:
        if t.status == "pending" and t.deadline < now:
            t.status = "overdue"
            db.commit()
            print(f"Task {t.id} marked as overdue.")

    db.close()

if __name__ == "__main__":
    autoclose_overdue_tasks()

print("Autoclose executed.")
