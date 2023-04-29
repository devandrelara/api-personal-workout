from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255))
    exercise_blocks_rest_interval = Column(Integer)  # in seconds, for example

    recurrence_id = Column(Integer, ForeignKey('workout_recurrences.id'))
    recurrence = relationship('WorkoutRecurrence', back_populates='workouts')

    muscles = relationship('WorkoutMuscle', back_populates='workout')
    exercise_blocks = relationship('ExerciseBlock', back_populates='workout')