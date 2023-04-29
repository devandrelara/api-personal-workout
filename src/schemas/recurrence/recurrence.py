from uuid import UUID

from pydantic import BaseModel


class BaseRecurrence(BaseModel):
    name: str


class CreateRecurrence(BaseRecurrence):
    pass


class Recurrence(BaseRecurrence):
    id: UUID

    class Config:
        orm_mode = True
