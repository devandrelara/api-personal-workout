from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from ..muscle import Muscle


class BaseExercise(BaseModel):
    name: str
    description: Optional[str] = None
    media: Optional[str] = None


class CreateExercise(BaseExercise):
    pass


class Exercise(BaseExercise):
    id: UUID
    muscles: List[Muscle]

    class Config:
        orm_mode = True
