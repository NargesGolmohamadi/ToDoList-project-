from pydantic import BaseModel

class ProjectResponse(BaseModel):
    id: int
    name: str
    desc: str


class TaskResponse(BaseModel):
    id: int
    title: str
    desc: str
    status: str
    deadline: str
