from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    priority: int = 1
    est_days: int = 1
    due_date: Optional[str] = None


class Task(TaskCreate):
    id: int
    created_at: Optional[str] = None
    completed: int = 0


class Config:
    orm_mode = True