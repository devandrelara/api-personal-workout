from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
Base = declarative_base()
class ExerciseSet(Base):
    __tablename__ = 'exercise_sets'
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    exercise = relationship('Exercise', back_populates='sets')
    set_id = Column(Integer, ForeignKey('sets.id'))
    set = relationship('Set', back_populates='exercises')