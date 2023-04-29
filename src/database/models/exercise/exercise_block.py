from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
Base = declarative_base()
class ExerciseBlock(Base):
    __tablename__ = 'exercise_blocks'
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    index = Column(Integer)
    rest_interval = Column(Integer)  # in seconds, for example
    description = Column(String)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    workout = relationship('Workout', back_populates='exercise_blocks')

    sets = relationship('ExerciseBlockSet', back_populates='exercise_block')