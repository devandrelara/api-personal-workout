from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ExerciseGroup(Base):
    __tablename__ = "exercise_groups"
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    sets = relationship("ExerciseGroupExercise", back_populates="exercise_group")
