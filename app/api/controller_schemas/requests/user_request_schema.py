from pydantic import BaseModel

class ProjectCreateRequest(BaseModel):
    name: str
    desc: str


class TaskCreateRequest(BaseModel):
    title: str
    desc: str
    deadline: str


class TaskUpdateRequest(BaseModel):
    status: str