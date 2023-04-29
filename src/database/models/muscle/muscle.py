from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class Muscle(Base):
    __tablename__ = "muscles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255), nullable=False)
    picture = Column(String)

    exercises = relationship(
        "Exercise", secondary="exercises_muscles", back_populates="muscles"
    )
    # workouts = relationship('WorkoutMuscle', back_populates='muscle')
