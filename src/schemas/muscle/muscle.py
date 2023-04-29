from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BaseMuscle(BaseModel):
    name: str
    picture: Optional[str] = None


class CreateMuscle(BaseMuscle):
    pass


class Muscle(BaseMuscle):
    id: UUID

    class Config:
        orm_mode = True
