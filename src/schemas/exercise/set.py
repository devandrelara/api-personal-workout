from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from .exercise import Exercise


class BaseSet(BaseModel):
    reps: str
    description: Optional[str] = None


class CreateSet(BaseSet):
    exercises: List[UUID]


class Set(BaseSet):
    id: UUID
    exercises: List[Exercise]

    class Config:
        orm_mode = True
