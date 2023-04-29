from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class BaseRecurrence(BaseModel):
    name: str

class CreateRecurrence(BaseRecurrence):
    pass

class Recurrence(BaseRecurrence):
    id: UUID

    class Config:
        orm_mode = True
