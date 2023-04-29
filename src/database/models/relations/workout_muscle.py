from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class WorkoutMuscle(Base):
    __tablename__ = 'workout_muscles'
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    workout = relationship('Workout', back_populates='muscles')
    muscle_id = Column(Integer, ForeignKey('muscles.id'))
    muscle = relationship('Muscle', back_populates='workouts')