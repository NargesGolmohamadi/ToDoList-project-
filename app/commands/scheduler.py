import schedule
import time
from app.commands.autoclose_overdue import autoclose_overdue_tasks

def job():
    print("Running auto-close task...")
    autoclose_overdue_tasks()

schedule.every(1).minutes.do(job)

print("Scheduler started.")

while True:
    schedule.run_pending()
    time.sleep(1)
