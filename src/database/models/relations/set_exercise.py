from uuid import uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class SetExercise(Base):
    __tablename__ = "sets_exercises"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    exercise_id = Column(UUID(as_uuid=True), ForeignKey("exercises.id"))
    set_id = Column(UUID(as_uuid=True), ForeignKey("sets.id"))

    exercise = relationship("Exercise", backref="sets")
    set = relationship("Set", backref="set_exercises")
