from fastapi import APIRouter
from app.services.project_services import ProjectService
from app.services.task_services import TaskService
from app.api.controller_schemas.requests.user_request_schema import ProjectCreateRequest
from app.api.controller_schemas.requests.user_request_schema import TaskCreateRequest
from app.api.controller_schemas.requests.user_request_schema import TaskUpdateRequest
from typing import List
from fastapi import APIRouter
from app.api.controller_schemas.responses.user_response_schema import TaskResponse

router = APIRouter()


def get_services():
    from app.db.session import SessionLocal
    db = SessionLocal()
    return ProjectService(db), TaskService(db)

@router.post("/")
def create_project(payload: ProjectCreateRequest):
    project_service, _ = get_services()
    return project_service.create_project(payload.name, payload.desc)

@router.get("/")
def list_projects():
    project_service, _ = get_services()
    return project_service.list_projects()

@router.post("/{project_id}/tasks")
def create_task(project_id: int, payload: TaskCreateRequest):
    _, task_service = get_services()
    return task_service.create_task(
        project_id, payload.title, payload.desc, payload.deadline
    )

@router.get("/{project_id}/tasks", response_model=List[TaskResponse])
def list_tasks(project_id: int):
    _, task_service = get_services()
    return task_service.list_tasks(project_id)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskUpdateRequest):
    _, task_service = get_services()
    task_service.update_status(task_id, payload.status)
    return {"message": "updated"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    _, task_service = get_services()
    task_service.delete_task(task_id)
    return {"message": "deleted"}

@router.delete("/{project_id}")
def delete_project(project_id: int):
    project_service, _ = get_services()
    project_service.delete_project(project_id)
    return {"message": "deleted"}
