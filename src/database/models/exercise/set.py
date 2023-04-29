from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class Set(Base):
    __tablename__ = "sets"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    reps = Column(String, nullable=False)
    description = Column(String, nullable=True)
    exercises = relationship(
        "Exercise", secondary="sets_exercises", back_populates="sets"
    )
    # sets = relationship("ExerciseGroupExercise", back_populates="exercise_group")
