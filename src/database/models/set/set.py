from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Set(Base):
    __tablename__ = 'sets'
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    repetitions = Column(String)  # or duration, depending on the application requirements

    exercises = relationship('ExerciseSet', back_populates='set')