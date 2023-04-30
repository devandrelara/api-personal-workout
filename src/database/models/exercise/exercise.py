from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255))
    description = Column(String, nullable=True)
    media = Column(String, nullable=True)

    muscles = relationship(
        "Muscle",
        secondary="exercises_muscles",
        back_populates="exercises",
        overlaps="exercise_muscles",
    )
    sets = relationship("Set", secondary="sets_exercises", back_populates="exercises")
