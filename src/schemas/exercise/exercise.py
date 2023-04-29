from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
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
