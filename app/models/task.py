
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True) 
    title = Column(String, nullable=False)    
    description = Column(String, nullable=True) 
    status = Column(String, nullable=False)  
    deadline = Column(Date, nullable=False)   

    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="tasks")
