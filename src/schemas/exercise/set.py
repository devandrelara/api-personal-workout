from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from .exercise import Exercise


class BaseSet(BaseModel):
    reps: str
    description: Optional[str] = None
    index: Optional[int] = None


class CreateSet(BaseSet):
    exercises: List[UUID]


class Set(BaseSet):
    id: UUID
    exercises: List[Exercise]

    class Config:
        orm_mode = True


class BaseSetBlock(BaseModel):
    description: Optional[str] = None
    rest_interval: int
    index: int


class CreateSetBlock(BaseSetBlock):
    sets: List[UUID]


class SetBlock(BaseSetBlock):
    id: UUID
    sets: List[Set]

    class Config:
        orm_mode = True
