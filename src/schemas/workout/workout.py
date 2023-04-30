from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from ..exercise import SetBlock


class BaseWorkout(BaseModel):
    name: str
    recurrence_id: Optional[UUID] = None
    rest_interval: int


class CreateWorkout(BaseWorkout):
    set_blocks: Optional[List[UUID]] = []


class Workout(BaseWorkout):
    id: UUID
    set_blocks: List[SetBlock]

    class Config:
        orm_mode = True
