from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from ... import Base
class Muscle(Base):
    __tablename__ = 'muscles'
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255), nullable=False)
    picture = Column(String)

    exercises = relationship('Exercise', secondary='exercises_muscles', back_populates='muscles')
    # workouts = relationship('WorkoutMuscle', back_populates='muscle')