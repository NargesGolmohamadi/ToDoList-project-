from pydantic import BaseModel
from datetime import date

class ProjectResponse(BaseModel):
    id: int
    name: str
    desc: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    deadline: date
    status: str
    project_id: int

    class Config:
        orm_mode = True
