from fastapi import APIRouter
from app.api.controllers import project_controller

api_router = APIRouter()
api_router.include_router(project_controller.router, prefix="/projects")
