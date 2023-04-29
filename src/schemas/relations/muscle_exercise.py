from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CreateRelationMuscleExercise(BaseModel):
    muscle_id: UUID
    exercise_id: UUID


class RelationMuscleExercise(CreateRelationMuscleExercise):
    id: UUID

    class Config:
        orm_mode = True
